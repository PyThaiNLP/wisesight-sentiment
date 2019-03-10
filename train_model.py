import pandas as pd
import numpy as np
from pythainlp import word_tokenize
from ast import literal_eval
from tqdm import tqdm_notebook
from collections import Counter
import re
import emoji
import string
from fastai.text import *
from fastai.callbacks import CSVLogger, SaveModelCallback
from pythainlp.ulmfit import *

#when training to find hyperparameters
all_df = pd.read_csv('all_df.csv')
train_df, valid_df = train_test_split(all_df, test_size=0.15, random_state=1412)

# #when training with augmented set
# train_df = pd.read_csv('all_aug.csv')
# valid_df = pd.read_csv('valid_df.csv')

#test set
test_df = pd.read_csv('test_df.csv')

model_path = 'wisesight_data/'

#lm data
data_lm = load_data(model_path,'wisesight_lm.pkl')
data_lm.sanity_check()

#classification data
tt = Tokenizer(tok_func = ThaiTokenizer, lang = 'th', pre_rules = pre_rules_th, post_rules=post_rules_th)
processor = [TokenizeProcessor(tokenizer=tt, chunksize=10000, mark_fields=False),
            NumericalizeProcessor(vocab=data_lm.vocab, max_vocab=60000, min_freq=20)]

data_cls = (ItemLists(model_path,train=TextList.from_df(train_df, model_path, cols=['texts'], processor=processor),
                     valid=TextList.from_df(valid_df, model_path, cols=['texts'], processor=processor))
    .label_from_df('category')
    .add_test(TextList.from_df(test_df, model_path, cols=['texts'], processor=processor))
    .databunch(bs=50)
    )
data_cls.sanity_check()
print(len(data_cls.vocab.itos))

#model
config = dict(emb_sz=400, n_hid=1550, n_layers=4, pad_token=1, qrnn=False,
             output_p=0.4, hidden_p=0.2, input_p=0.6, embed_p=0.1, weight_p=0.5)
trn_args = dict(bptt=70, drop_mult=0.7, alpha=2, beta=1, max_len=500)

learn = text_classifier_learner(data_cls, AWD_LSTM, config=config, pretrained=False, **trn_args)
#load pretrained finetuned model
learn.load_encoder('wisesight_enc')

#train unfrozen
learn.freeze_to(-1)
learn.fit_one_cycle(1, 2e-2, moms=(0.8, 0.7))
learn.freeze_to(-2)
learn.fit_one_cycle(1, slice(1e-2 / (2.6 ** 4), 1e-2), moms=(0.8, 0.7))
learn.freeze_to(-3)
learn.fit_one_cycle(1, slice(5e-3 / (2.6 ** 4), 5e-3), moms=(0.8, 0.7))
learn.unfreeze()
learn.fit_one_cycle(10, slice(1e-3 / (2.6 ** 4), 1e-3), moms=(0.8, 0.7),
                   callbacks=[SaveModelCallback(learn, every='improvement', monitor='accuracy', name='bestmodel')])

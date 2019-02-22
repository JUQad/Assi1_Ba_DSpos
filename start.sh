#!/bin/bash

#sudo pip install fastai==0.7.0
#sudo pip install torchtext==0.2.3
#pip3 install fire spacy
#sudo python3 -m spacy download en
rm -rf ./data
mkdir ./data
python3 ./prepareData.py
python3 ./imdb_scripts/create_toks.py ./data
python3 ./imdb_scripts/tok2id.py ./data
python3 ./imdb_scripts/finetune_lm.py data wt103 0 15 --lm-id pretrain_wt103
python3 ./imdb_scripts/train_clas.py data 0 --lm-id pretrain_wt103 --clas-id pretrain_wt103 --cl 15
python3 ./imdb_scripts/eval_clas.py data 0 --lm-id pretrain_wt103 --clas-id pretrain_wt103

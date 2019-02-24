# Assi1_Ba_DSpos
Sentiment Analysis Scenario

Deep Archticture Part: 
tutorial is at 	```https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts```

- for installation you need: 
	sudo pip install fastai==0.7.0
 	sudo pip install torchtext==0.2.3
  pip3 install fire spacy
  
- to make sure spacy loads the english stuff 
```sudo python3 -m spacy download en```
- download the imdb_scripts folder 
```https://github.com/fastai/fastai/tree/master/courses/dl2/imdb_scripts```

- download the pretrained model from ```http://files.fast.ai/models/wt103/```
- prepare our data
 	python3 ./prepareData.py
- prepare data (step 1. in the fastai tutorial)
	python3 ./imdb_scripts/create_toks.py ./data
- prepare tokens (step 2)
	python3 ./imdb_scripts/tok2id.py ./data
- finetune the model (step 3b)
	python3 ./imdb_scripts/finetune_lm.py data wt103 0 25 --lm-id pretrain_wt103
- train the model (step 4)
	python3 ./imdb_scripts/train_clas.py data 0 --lm-id pretrain_wt103 --clas-id pretrain_wt103 --cl 15
- eval the model (step 5)
	python3 ./imdb_scripts/eval_clas.py data 0 --lm-id pretrain_wt103 --clas-id pretrain_wt103
	

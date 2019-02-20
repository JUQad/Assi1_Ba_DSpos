#!/usr/bin/python3

import shutil
import sys
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
import fastai


# config
class Configuration():
	def __init__(self):
        self.cv_folds = 5
conf = Configuration()



xlFile = "sentences_with_sentiment.xlsx"
xl = pd.ExcelFile (xlFile)
sheetName = xl.sheet_names[0]
data = xl.parse(sheetName, header = 0)



# add "key" for stratification
data["Class"] = data["Positive"]*1 + data["Negative"]*2 + data["Neutral"]*3

  
for (idx, row) in data.iterrows():
	s = row["Sentence"]
	if len(s) < 256:
		s = s + ' '*(256-len(s))
		data.at[idx, "Sentence"] = s


# do a simple CV for now, stratified
skf = StratifiedKFold(n_splits = conf.cv_folds, shuffle = True, random_state = 42)
for train_index, val_index in skf.split(data["Sentence"], data["Class"]):
	train = data.iloc[train_index]
	val = data.iloc[val_index]

	# save data
	train = train[["Class", "Sentence"]]
	train = pd.concat([train]*10)
    train.to_csv("./data/train.csv", index = False, header = False)

    val = val[["Class", "Sentence"]]
	val = pd.concat([val]*10)
	val.to_csv("./data/val.csv", index = False, header = False)
	# ONLY ONE LOOP FOR NOW:
	break

len(train)

data["Sentence"].values

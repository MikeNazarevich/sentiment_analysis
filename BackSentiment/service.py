from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np
import re

def get_sentiment(record):
    fullData = pd.read_csv("./data/example.csv")

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(fullData["text"])

    X = tokenizer.texts_to_sequences(fullData['text'].values)
    X = pad_sequences(X)

    json_file = open("./data/topModel.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("./data/topModel.h5")
    loaded_model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

    record = record.lower()
    print(record)
    record = re.sub(r'[^а-яА-ЯёЁ\s.!?,)(]|', '', record)
    record = re.sub(r'[.,!?)(]{1,}', ' ', record)
    record = re.sub(r'[\s]{2,}', ' ', record)
    record = re.sub(r'[\n]', ' ', record)
    record = re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', record)

    record = [record]

    record = tokenizer.texts_to_sequences(record)
    record = pad_sequences(record, maxlen=32, dtype='int32', value=0)
    sentiment = loaded_model.predict(record, batch_size=1, verbose=2)[0]

    if(np.argmax(sentiment) == 0):
       return 'negative'
    elif(np.argmax(sentiment) == 1):
        return 'positive'






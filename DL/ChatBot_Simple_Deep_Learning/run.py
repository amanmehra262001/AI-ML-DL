import json
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open('intent.json') as file:
    data = json.load(file)

def chat():
    # Load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl = pickle.load(enc)

    # parameters
    max_len = 20

    while True:
        print(Fore.CYAN + "Master: " + Style.RESET_ALL, end = "")
        inp = input()

        if inp.lower() == 'quit':
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))

        tag = lbl.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                print(Fore.GREEN + "J.A.R.V.I.S: " + Style.RESET_ALL, np.random.choice(i['responses']))

print(Fore.YELLOW + "Start messaging... Type Quit to stop!" + Style.RESET_ALL)

chat()
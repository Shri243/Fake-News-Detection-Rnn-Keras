import numpy as np
import pandas as pd

# this line is modified in git practice

from tensorflow import keras

model1 = keras.models.load_model("mode1.keras")
model2 = keras.models.load_model("model2.keras")

# i am also adding this line

print(model1.summary())
print(model2.summary())

import pickle 
a = open("tokenizer.pickle","rb")
b = open("tokenizer2.pickle","rb")

tokenizer_1 = pickle.load(a,)
tokenizer_2 = pickle.load(b,)

a.close()
b.close()

#title = input()
#body = input()

def predict_title(sentence,model,max_len,tokenizer):
    sentence_seq = tokenizer.texts_to_sequences(sentence)
    sentence_pad = keras.preprocessing.sequence.pad_sequences(sentence_seq,maxlen=max_len, padding="post", truncating="post")
    prediction = model.predict(sentence_pad)
    if prediction > 0.5:
        predict = 1
    else:
        predict = 0
    return predict

#print(predict_title([title], model1, 200, tokenizer_1))
#print(predict_title([title+body], model2, 500, tokenizer_2))

def click():
    title = tit01.get()
    body = tit02.get("1.0",END)
    print(title)
    print(body)
    a = predict_title([title], model1, 200, tokenizer_1)
    b = predict_title([title+body], model2, 500, tokenizer_2)
    if a == 1 :
        output_1["text"] = " model 1 predicted true "
        output_1['bg'] = 'lawngreen'
    else:
        output_1["text"] = ("model 1 predicted false")
        output_1['bg'] = 'red'
    if b == 1 :
        output_2["text"] = (" model 2 predicted true ")
        output_2['bg'] = 'lawngreen'
    else:
        output_2["text"] = "model 2 predicted false"
        output_2['bg'] = 'red'
    messagebox.showinfo("result","MODEL 1 : \t" + str(bool(a))+"\t"+"\nMODEL 2 : \t" + str(bool(b)))

from tkinter import *        
from tkinter import messagebox
window = Tk()

x = PhotoImage("ph1.jpg")

window['background'] = '#856ff8'

l0 = Label(window, text = "FAKE NEWS DETECTOR",font= 25)
l0.place(x=375,y=18)
l0['bg'] = 'gold'
l1 = Label(window, text = " Head",font=15)
l1.place(x = 25,y=70)
l1['bg'] = 'lawngreen'
l2 = Label(window, text = "Article",font=15)
l2.place(x=25,y=120)
l2['bg'] = 'orange'

tit01 = Entry(window,width = 80 ,font = 30)
tit01.place(x=90,y=70)

tit02 = Text(window,width = 80 ,font = 15)
tit02.place(x=90,y=120)

predict = Button(window,text = "Predict",font = 30,width=20,height=3,command=click)
predict.place(x = 90 , y = 700)
predict['bg'] = 'brown1'
window.geometry("1050x800")
window.title("Fake News Detector")

output_1 = Label(window, text = "enter heading of article in Head",font=15)
output_2 = Label(window, text = "  enter body of article in body  ",font=15)
output_1.place(x = 500,y= 700)
output_2.place(x = 500,y= 750)
output_1['bg'] = 'skyblue'
output_2['bg'] = 'skyblue'
window.mainloop()
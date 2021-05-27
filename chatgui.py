import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import pyttsx3

from tensorflow.keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            #context = i['context']
            #print(context)
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    friend = pyttsx3.init()
    friend.setProperty("rate",160)
    voices = friend.getProperty("voices")
    friend.setProperty("voice", voices[1].id)
    friend.say(res)
    friend.runAndWait()
    return res


#Creating GUI with tkinter
import tkinter
from tkinter import *
import time


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        i = res.split()
        #print(i)
        if 'bot' in i:
            j = res.split('bot')
            ChatLog.insert(END, "Gogo: " + j[0] + '\n\n')
            ChatLog.insert(END, "Gogo: " + j[1] + '\n\n')
        elif 'return' in i:
            j = res.split('return')
            ChatLog.insert(END, "Gogo: " + j[0] + '\n\n')
            ChatLog.insert(END, "Gogo : Write it on the paper and say Done" +  '\n\n')   
        else:
            ChatLog.insert(END, "Gogo: " + res + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("GOGO")
base.geometry("700x600+40+40")
base.resizable(width=FALSE, height=FALSE)
base.configure(bg='#1b2021')

#Create Chat window
ChatLog = Text(base, bd=0, bg="#e1f4f3", height="60", width="200", font="Arial",)
def hello():
    ChatLog.config(state=NORMAL)
    time.sleep(2)
    ChatLog.insert(END, "Gogo: HELLO" + '\n\n')
    
    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

Label(base, text="GOGO ASSISTANT", font=('Poppins bold', 14)).pack(pady=10)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="#e1f4f3",width="29", height="3", font=("Arial", 16))

#Create Button to send message
SendButton = Button(base, font=("Green",12,'bold'), text="Send", width="12", height="3",
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )


#EntryBox.bind("<Return>", send)

#Place all components on the screen
scrollbar.place(x=640,y=40, height=450)
ChatLog.place(bordermode=OUTSIDE, x=40,y=40, height=450, width=600)
SendButton.place(x=510, y=495, height=90)
EntryBox.place(x=40, y=495, height=90, width=500)

Button2 =  Button(base, font=("blue",2,'bold'), text="Start", width="10", height="2",fg='#ffffff', command= hello )
Button2.place(x=10, y=10, height=10)
'''friend = pyttsx3.init()
friend.say("Hello, I am GOGO. How are you!")
friend.runAndWait()'''

base.mainloop()
import json
import tkinter
from random import randint
from random import shuffle
from tkinter import Tk

def antJa():
    Zeiten.append("Futur antérieur")
    randomize()
    anterieurFrage.destroy()
    Ausgeben()

def antNein():
    randomize()
    anterieurFrage.destroy()
    Ausgeben()

def Ausgeben():
    main = tkinter.Tk()
    ausgab1 = tkinter.Label(main, text=Personen[rp])
    ausgab2 = tkinter.Label(main, text=Zeiten[rz])
    ausgab3 = tkinter.Label(main, text=Verbs[rv])
    Zusammen = ausgab1, ausgab2, ausgab3
    ausgab1.pack()
    ausgab2.pack()
    ausgab3.pack()
    
def inClipboard():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txt)
    r.destroy()

def randomize():
    shuffle(Personen)
    shuffle(Zeiten)
    shuffle(Verbs)
    rv = randint(0, len(Verbs)-1)
    rp = randint(0, len(Personen)-1)
    rz = randint(0, len(Zeiten)-1)

in_file= open ("verbs.txt","rt")
Verbs = json.loads(in_file.read())
in_file.close()

Personen = ["1. Person Singular", "2. Person Singular", "3. Person Singular", "1. Person Singular", "2. Person Singular", "3. Person Singular"]
Zeiten = ["Imparfait", "Plus-que-parfait", "Futur simple", "Imparfait", "Présent", "Passé composé", "Passé simple", "Futur composé", "Conditionnel présent", "Conditionell passé", "Subjonctif"]

rv = 0
rp = 0
rz = 0

anterieurFrage = tkinter.Tk()
Frage = tkinter.Label(anterieurFrage, text="Möchtest du das Futur antérieur nutzen?")
Ja = tkinter.Button(anterieurFrage, text="Ja!", command=antJa)
Nein = tkinter.Button(anterieurFrage, text="Nein!", command=antNein)
Frage.pack()
Ja.pack()
Nein.pack()

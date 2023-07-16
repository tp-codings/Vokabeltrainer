import random
import json
import os

try:
    tf = open("Wörterbuch.json", "r")
    myDict = json.load(tf)
except:
    myDict = {'0':1, '1':("gehen", "ir"), '2':("sehen", "ver"), '3':("schreiben", "escribir"), '4': ("wollen", "querer"), '5':("das Haus", "la casa")}


def learn():
    clearWindow()
    print("Lernen ausgewählt\n")
    if len(myDict.keys())>1:

        anzahl = 0
        richtige = 0
        print("zum Abbrechen x wählen\n")
        while True:
            
            randomDictSize = (random.randint(1, (len(myDict.keys())-1)))
            myTuple = myDict[str(randomDictSize)]
            
            lChoice = random.randint(0,1)
    
            eingabe = str(input(f"{myTuple[lChoice]}:  "))
            clearWindow()
            if eingabe == 'x' or eingabe == 'X':
                print(f"Lernen abgebrochen | {richtige}/{anzahl} richtig\n")
                try:
                    verhaeltnis = richtige / anzahl
                except:
                    break
                if verhaeltnis > 0.8:
                    print(":-) - Prima\n\n------------------------------------------------------")
                elif verhaeltnis > 0.5 and verhaeltnis <= 0.8:
                    print(":-( - Das geht besser\n\n------------------------------------------------------")
                else:
                    print("X-( - Mach mal weniger spanisch blau\n\n------------------------------------------------------")
                break
            
            if lChoice == 0 and eingabe == myTuple[1] or lChoice == 1 and eingabe == myTuple[0]:
                print("Richtig\n")
                richtige += 1
                anzahl += 1
            else:
                print("Falsch\n")
                anzahl += 1
    
        
    else:
        print("Wörterbuch ist leer\n")
        

def add():
    newWords = 0
    clearWindow()
    print("Wörter hinzufügen ausgewählt\nzum Abbrechen x wählen\n")
    while True:
        german = str(input("deutsches Wort eingeben:  "))
        if german == 'x' or german == 'X':
            clearWindow()
            print(f"{newWords} hinzugefügt\n\n------------------------------------------------------")
            break
        print("\n")
        spanish = str(input("spanisches Wort eingeben:  "))
        clearWindow()
        print("gespeichert\n")
        if spanish == 'x' or spanish == 'X':
            break

        myDict[str(myDict['0'])] = (german, spanish)
        newWords += 1  
    
def clearWindow():
    os.system('cls')

print("Wilkommen bei Vokabeltrainer Deutsch <-> Spanisch\n------------------------------------------------------\n")

while True:
    
    choice = int(input("Optionen: 1 - Lernen, 2 - Wörter hinzufügen, 3 - schlließen:  "))
    
    print("\n------------------------------------------------------\n")
    
    if choice == 1:
        learn()
    elif choice == 2:
        add()
        myDict['0'] += 1
    elif choice > 2:
        print("Vokabeltrainer geschlossen\n")
        input("Zum Beenden Taste drücken")
        break


tf = open("Wörterbuch.json", "w")
json.dump(myDict, tf)
tf.close()




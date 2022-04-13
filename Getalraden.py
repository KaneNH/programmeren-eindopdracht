# Imports
from tkinter import *
from tkinter import messagebox
from random import randint



# Scherm
root = Tk()
root.geometry("500x500")
root.title("getal raad spel")



# Genereer getal functie
def Genereergetal():
    global Number
    # Generate Number
    Number = randint(1,10)
    
    # Hier word het getal getoont
    messagebox.showinfo("Een getal is gegenereerd!", "Raad het getal!")



# getal raad functie
def GetalraadFunc():
    global Number
    
    # Get Value van de Antwoordentry
    UserResponse = AntwoordEntry.get()
    
    # Convert Value van antwoord naar getal
    UserResponse = int(UserResponse)

    # Check of het ingevoerde getal te laag, te hoog of gelijk is
    if UserResponse > Number:
        ResultLabel.config(text="Fout! Het getal is lager", fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Fout! Het getal is hoger", fg="Red")
    else:
        ResultLabel.config(text=" Je hebt het getal geraden! Het getal was {}".format(Number), fg="Green")
        AntwoordEntry.delete(0, "end")



# Title
Title = Label(root, text="Getal raad spel!", font=("Arial", 30))
Title.pack()



# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=60)



# Getal raad label
GetalraadLabel = Label(MainFrame, text="Raad een getal tussen de 1 en de 10:", font=("Arial", 20))
GetalraadLabel.pack()


# Antwoord Entry
AntwoordEntry = Entry(MainFrame, font=("Arial", 16))
AntwoordEntry.pack(pady=10)



# Genereer getal Button
GenereergetalBtn = Button(MainFrame, text="Genereer getal", width=16, font=("Arial", 16), background="Dodgerblue", command=Genereergetal)
GenereergetalBtn.pack()



# Raad Button
GuessBtn = Button(MainFrame, text="Raad", width=16, font=("Arial", 16), background="#15e650", command=GetalraadFunc)
GuessBtn.pack(pady=5)



# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()



# Mainloop
root.mainloop()
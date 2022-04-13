from tkinter import *
import random
from tkinter import messagebox
from random import randint

# Maak een nieuw window met een titel
window = Tk()
window.title("Menu")

# Functies voor het menu
def show_thing_1():
    frame_thing_2.pack_forget()
    frame_thing_3.pack_forget()
    frame_thing_4.pack_forget()
    frame_thing_1.pack()
    

def show_thing_2():
    frame_thing_1.pack_forget()
    frame_thing_3.pack_forget()
    frame_thing_4.pack_forget()
    frame_thing_2.pack()

def show_thing_3():
    frame_thing_2.pack_forget()
    frame_thing_1.pack_forget()
    frame_thing_4.pack_forget() 
    frame_thing_3.pack()


def show_thing_4():
    frame_thing_2.pack_forget()
    frame_thing_3.pack_forget()
    frame_thing_1.pack_forget()
    frame_thing_4.pack()
# Menu maken
menubar = Menu(window)
window.config(menu=menubar)

# Menu items maken
mainmenu = Menu(menubar)
mainmenu.add_command(label="dobbelen", command=show_thing_1)
mainmenu.add_command(label="getallen raden", command=show_thing_2)          
mainmenu.add_command(label="galgje", command=show_thing_3)     
mainmenu.add_command(label="klok", command=show_thing_4)     
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
# Menu toevoegen aan menubar
menubar.add_cascade(label="klik HIER voor de keuze", menu=mainmenu)

# FRAME VOOR THING 1 Fabian
frame_thing_1 = Frame(borderwidth=10)
label_1 = Label()
l1=Label(frame_thing_1,font=("dobbel",260))
 
def roll():

    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
     
b1=Button(frame_thing_1,text="gooi de dobbelstenen",foreground='blue',command=roll)
b1.place(x=300,y=0)
b1.pack()
label_1.pack()


# FRAME VOOR THING 2 Kane
frame_thing_2 = Frame(borderwidth=10)
label_2 = Label(frame_thing_2,)

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

        # Getal raad label
GetalraadLabel = Label(frame_thing_2, text="Raad een getal tussen de 1 en de 10:", font=("Arial", 20))
GetalraadLabel.pack()


# Antwoord Entry
AntwoordEntry = Entry(frame_thing_2, font=("Arial", 16))
AntwoordEntry.pack(pady=10)



# Genereer getal Button
GenereergetalBtn = Button(frame_thing_2, text="Genereer getal", width=16, font=("Arial", 16), background="Dodgerblue", command=Genereergetal)
GenereergetalBtn.pack()



# Raad Button
GuessBtn = Button(frame_thing_2, text="Raad", width=16, font=("Arial", 16), background="#15e650", command=GetalraadFunc)
GuessBtn.pack(pady=5)



# Result Label
ResultLabel = Label(frame_thing_2, text="", font=("Arial", 16))
ResultLabel.pack()


label_2.pack()


#frame 3 Stef
frame_thing_3 = Frame(borderwidth=10)
label_3 = Label(frame_thing_3, text="galgje", bg="gray", fg="yellow", width=20, height=8)
label_3.pack()
#frame 4 Dylan
frame_thing_4 = Frame(borderwidth=10)
label_4 = Label(frame_thing_4, text="klok", bg="green", fg="yellow", width=20, height=8)
label_4.pack()


# MAIN --------------------------------
# Begin met frame 1
show_thing_1()
# Start the application
window.mainloop()
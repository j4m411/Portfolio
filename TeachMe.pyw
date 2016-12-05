#stringvar_example.py
from tkinter import *
import tkinter.messagebox as mb
import pyperclip


class StringVarDemo:
    def __init__(self, rootWin):

        #A StringVar is a special object that holds strings and
        #can be linked to a GUI element such as an Entry.
        self.sv = StringVar()
      
        #Create a entry and button to put in the root window!
        self.entry = Entry(rootWin, textvariable=self.sv)
        self.entry.pack()
        #Add some text:
        #self.sv.set("Here is some text!")
      

        self.button = Button(rootWin, text="Search", command=self.search)
        self.button.pack()

    def search(self):
        eText = self.sv.get()
        student = eText.title()
        f = open("TS.txt","r")

        teacherEmail = []
        tempTeacher = ""
        try:
            for line in f:
                if "@" in line:
                    tempTeacher = line

                if student in line:
                    teacherEmail.append(tempTeacher)
                    tempTeacher = ""

        except:
            #print("Sorry no match found. Have you got spelling correct ?")
            mb.showinfo("Oops", "No match - correct spelling & form?")

        if teacherEmail == []:
            #print("Sorry no match found. Have you got spelling correct ?")
            mb.showinfo("Oops", "No match - correct spelling & form?")

        else:
            #print(teacherEmail)
            #for i in range(0, len(teacherEmail)):
                #print(teacherEmail[i])

            pyperclip.copy(','.join(teacherEmail))
            mb.showinfo("Success !","Teachers found ! - emails copied to clipboard")

        teacherEmail = []
          
        f.close()
     
     



#Create the main root window, instantiate the object, and run the main loop!
rootWin = Tk()
rootWin.geometry("250x80")
rootWin.title("TeachMe")
app = StringVarDemo( rootWin )
rootWin.mainloop()


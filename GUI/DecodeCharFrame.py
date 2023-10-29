import tkinter as tk

from dataCreation import makePromptMorse
from constants.EncodingChart import EncodingChart

class DecodeCharFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.prompt=''

        self.menuButton=tk.Button(self,text="Menu")
        self.menuButton.grid(row=0,column=0,columnspan=2)

        self.promptLabel=tk.Label(self)
        self.promptLabel.grid(row=1,column=0,columnspan=2)

        self.answerEntry=tk.Entry(self)
        self.answerEntry.grid(row=2,column=0,columnspan=2)

        self.skipButton=tk.Button(self,text="Skip",command=self.setPrompt)
        self.skipButton.grid(row=4,column=0)
        
        self.submitButton=tk.Button(self,text="Submit",command=self.chkAnswer)
        self.submitButton.grid(row=4,column=1)

        self.validationResultLabel=tk.Label(self,text="")
        self.validationResultLabel.grid(row=5,column=0,columnspan=2)

        self.answerEntry.bind("<Return>",self.chkAnswer)
        self.answerEntry.focus_set()
        self.setPrompt()


    def chkAnswer(self,event=None):
        if(EncodingChart[self.answerEntry.get()]==self.prompt):
            self.setPrompt()
        else:
            self.validationResultLabel["text"]="Wrong"
        self.answerEntry.delete(0,tk.END)
    
    def setPrompt(self,event=None):
        self.prompt=makePromptMorse()
        self.promptLabel["text"]=''.join(map(lambda sig:str(sig)+' ',self.prompt))
        self.validationResultLabel["text"]=""
        self.answerEntry.delete(0,tk.END)


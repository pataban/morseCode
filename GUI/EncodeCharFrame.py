import tkinter as tk
from tkinter import ttk
from constants.EncodingChart import EncodingChart
from constants.Signal import Signal
import random
import time
from constants.constants import *
from dataCreation import *
class EncodeCharFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.prompt=''
        self.answer=[]
        self.keyPressTime=None

        self.menuButton=tk.Button(self,text="Menu")
        self.menuButton.grid(row=0,column=0,columnspan=2)

        self.promptLabel=tk.Label(self)
        self.promptLabel.grid(row=1,column=0,columnspan=2)

        self.answerLabel=tk.Label(self,text="")
        self.answerLabel.grid(row=2,column=0,columnspan=2)

        self.dotButton=tk.Button(self,text="Dot", command=self.addDot)
        self.dotButton.grid(row=3,column=0)

        self.dashButton=tk.Button(self,text="Dash", command=self.addDash)
        self.dashButton.grid(row=3,column=1)

        self.skipButton=tk.Button(self,text="Skip",command=self.setPrompt)
        self.skipButton.grid(row=4,column=0)
        
        self.submitButton=tk.Button(self,text="Submit",command=self.chkAnswer)
        self.submitButton.grid(row=4,column=1)

        self.validationResultLabel=tk.Label(self,text="")
        self.validationResultLabel.grid(row=5,column=0,columnspan=2)

        self.bind("<KeyPress>",self.startSignal)
        self.bind("<KeyRelease>",self.endSignal)
        self.bind("<Return>",self.chkAnswer)
        self.bind("<BackSpace>",self.setPrompt)
        self.focus_set()
        self.setPrompt()


    def startSignal(self,event=None):
        if self.keyPressTime is None:
            self.keyPressTime=time.time()

    def endSignal(self,event=None):
        if self.keyPressTime is not None:
            keyHoldTime=time.time()-self.keyPressTime
            if(keyHoldTime<KEY_HOLD_DURATION):
                self.addDot()
            else:
                self.addDash()
            self.keyPressTime=None

    def addDot(self):
        self.answer.append(Signal.DOT)
        self.answerLabel["text"]=self.answerLabel["text"]+ " Dot"

    def addDash(self):
        self.answer.append(Signal.DASH)
        self.answerLabel["text"]=self.answerLabel["text"]+ " Dash"

    def chkAnswer(self,event=None):
        if(self.answer==EncodingChart[self.prompt]):
            self.setPrompt()
        else:
            self.validationResultLabel["text"]="Wrong"
        self.answer=[]
        self.answerLabel["text"]=""

    def setPrompt(self,event=None):
        self.prompt=makePrompt()
        self.promptLabel["text"]=self.prompt
        self.validationResultLabel["text"]=""
        self.answer=[]
        self.answerLabel["text"]=""

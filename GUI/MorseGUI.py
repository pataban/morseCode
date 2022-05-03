import tkinter as tk
from tkinter import ttk
from GUI.EncodeCharFrame import EncodeFrame
from GUI.DecodeCharFrame import DecodeFrame


class MorseGUI(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        master.title("Morse Code")
        self.pack()
        self.menuFrame=None
        self.encodeFrame=None
        self.decodeFrame=None
        self.showMenuFrame()

    def buildMenuFrame(self):
        self.menuFrame=tk.Frame(self)

        encodeButton=tk.Button(self.menuFrame,text="Encode",command=self.showEncodeFrame)
        encodeButton.grid(row=0,column=0)

        decodeButton=tk.Button(self.menuFrame,text="Decode",command=self.showDecodeFrame)
        decodeButton.grid(row=0,column=1)
        

    def buildEncodeFrame(self):
        self.encodeFrame=EncodeFrame(self)
        self.encodeFrame.menuButton["command"]=self.showMenuFrame


    def buildDecodeFrame(self):
        self.decodeFrame=DecodeFrame(self)
        self.decodeFrame.menuButton["command"]=self.showMenuFrame

    def showMenuFrame(self):
        self.hideAllFrames()
        if self.menuFrame is None:
            self.buildMenuFrame()
        self.menuFrame.pack()

    def showEncodeFrame(self):
        self.hideAllFrames()
        if self.encodeFrame is None:
            self.buildEncodeFrame()
        self.encodeFrame.pack()

    def showDecodeFrame(self):
        self.hideAllFrames()
        if self.decodeFrame is None:
            self.buildDecodeFrame()
        self.decodeFrame.pack()

    def hideAllFrames(self):
        if(self.menuFrame!=None):   
            self.menuFrame.pack_forget()
        if(self.encodeFrame!=None):   
            self.encodeFrame.pack_forget()
        if(self.decodeFrame!=None):
            self.decodeFrame.pack_forget()
        self.pack() 
        return

    def clearSessionData(self):
        self.hideAllFrames()
        self.menuFrame=None
        self.encodeFrame=None
        self.decodeFrame=None
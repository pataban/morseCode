import tkinter as tk
from tkinter import ttk
from GUI.EncodeCharFrame import EncodeCharFrame
from GUI.DecodeCharFrame import DecodeCharFrame


class MorseGUI(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        master.title("Morse Code")
        self.pack()
        self.menuFrame=None
        self.chartFrame=None
        self.treeFrame=None
        self.encodeCharFrame=None
        self.decodeCharFrame=None
        self.encodeFrame=None
        self.decodeFrame=None
        self.showMenuFrame()

    def buildMenuFrame(self):
        self.menuFrame=tk.Frame(self)

        chartButton=tk.Button(self.menuFrame,text="Chart",command=self.showChartFrame)
        chartButton.grid(row=0,column=0)

        treeButton=tk.Button(self.menuFrame,text="Tree",command=self.showTreeFrame)
        treeButton.grid(row=0,column=1)

        encodeCharButton=tk.Button(self.menuFrame,text="Encode Char",command=self.showEncodeCharFrame)
        encodeCharButton.grid(row=1,column=0)

        decodeCharButton=tk.Button(self.menuFrame,text="Decode Char",command=self.showDecodeCharFrame)
        decodeCharButton.grid(row=1,column=1)

        encodeButton=tk.Button(self.menuFrame,text="Encode",command=self.showEncodeFrame)
        encodeButton.grid(row=2,column=0)

        decodeButton=tk.Button(self.menuFrame,text="Decode",command=self.showDecodeFrame)
        decodeButton.grid(row=2,column=1)
        
    def buildChartFrame(self):
        pass

    def buildTreeFrame(self):
        pass

    def buildEncodeCharFrame(self):
        self.encodeCharFrame=EncodeCharFrame(self)
        self.encodeCharFrame.menuButton["command"]=self.showMenuFrame

    def buildDecodeCharFrame(self):
        self.decodeCharFrame=DecodeCharFrame(self)
        self.decodeCharFrame.menuButton["command"]=self.showMenuFrame

    def buildEncodeFrame(self):
        pass

    def buildDecodeFrame(self):
        pass

    def showMenuFrame(self):
        self.hideAllFrames()
        if self.menuFrame is None:
            self.buildMenuFrame()
        self.menuFrame.pack()

    def showChartFrame(self):
        pass

    def showTreeFrame(self):
        pass

    def showEncodeCharFrame(self):
        self.hideAllFrames()
        if self.encodeCharFrame is None:
            self.buildEncodeCharFrame()
        self.encodeCharFrame.pack()

    def showDecodeCharFrame(self):
        self.hideAllFrames()
        if self.decodeCharFrame is None:
            self.buildDecodeCharFrame()
        self.decodeCharFrame.pack()

    def showEncodeFrame(self):
        pass

    def showDecodeFrame(self):
        pass

    def hideAllFrames(self):
        if(self.menuFrame!=None):   
            self.menuFrame.pack_forget()
        if(self.chartFrame!=None):   
            self.chartFrame.pack_forget()
        if(self.treeFrame!=None):   
            self.treeFrame.pack_forget()
        if(self.encodeCharFrame!=None):   
            self.encodeCharFrame.pack_forget()
        if(self.decodeCharFrame!=None):
            self.decodeCharFrame.pack_forget()
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
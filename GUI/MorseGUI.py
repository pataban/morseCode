import tkinter as tk
from PIL import ImageTk, Image
from GUI.EncodeCharFrame import EncodeCharFrame
from GUI.DecodeCharFrame import DecodeCharFrame
from static.constants import *


class MorseGUI(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        master.title("Morse Code")
        master.minsize(MENU_SIZE[0], MENU_SIZE[1])
        self.menuFrame = None
        self.chartFrame = None
        self.treeFrame = None
        self.encodeCharFrame = None
        self.decodeCharFrame = None
        self.encodeFrame = None
        self.decodeFrame = None
        self.showMenuFrame()

    def buildMenuFrame(self):
        self.menuFrame = tk.Frame(self)

        chartButton = tk.Button(
            self.menuFrame, text="Chart", command=self.showChartFrame)
        chartButton.grid(row=0, column=0, ipadx=PADDING_DEFAULT,
                         ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        treeButton = tk.Button(self.menuFrame, text="Tree",
                               command=self.showTreeFrame)
        treeButton.grid(row=0, column=1, ipadx=PADDING_DEFAULT,
                        ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        encodeCharButton = tk.Button(
            self.menuFrame, text="Encode Char", command=self.showEncodeCharFrame)
        encodeCharButton.grid(row=1, column=0, ipadx=PADDING_DEFAULT,
                              ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        decodeCharButton = tk.Button(
            self.menuFrame, text="Decode Char", command=self.showDecodeCharFrame)
        decodeCharButton.grid(row=1, column=1, ipadx=PADDING_DEFAULT,
                              ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        encodeButton = tk.Button(
            self.menuFrame, text="Encode", command=self.showEncodeFrame)
        encodeButton.grid(row=2, column=0, ipadx=PADDING_DEFAULT,
                          ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        decodeButton = tk.Button(
            self.menuFrame, text="Decode", command=self.showDecodeFrame)
        decodeButton.grid(row=2, column=1, ipadx=PADDING_DEFAULT,
                          ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

    def buildChartFrame(self):
        chart = ImageTk.PhotoImage(Image.open("grafics/morseChart2.png"))
        self.chartFrame = tk.Button(
            self, image=chart, command=self.showMenuFrame)
        self.chartFrame.image = chart

    def buildTreeFrame(self):
        tree = ImageTk.PhotoImage(Image.open(
            "grafics/morseTree1.png").resize(MORSE_TREE_IMG_SIZE))
        self.treeFrame = tk.Button(
            self, image=tree, command=self.showMenuFrame)
        self.treeFrame.image = tree

    def buildEncodeCharFrame(self):
        self.encodeCharFrame = EncodeCharFrame(self, self.showMenuFrame)

    def buildDecodeCharFrame(self):
        self.decodeCharFrame = DecodeCharFrame(self, self.showMenuFrame)

    def buildEncodeFrame(self):
        self.encodeFrame = tk.Button(self, text="Menu")
        self.encodeFrame["command"] = self.showMenuFrame

    def buildDecodeFrame(self):
        self.decodeFrame = tk.Button(self, text="Menu")
        self.decodeFrame["command"] = self.showMenuFrame

    def showMenuFrame(self):
        self.hideAllFrames()
        if self.menuFrame is None:
            self.buildMenuFrame()
        self.menuFrame.pack()

    def showChartFrame(self):
        self.hideAllFrames()
        if self.chartFrame is None:
            self.buildChartFrame()
        self.chartFrame.pack()

    def showTreeFrame(self):
        self.hideAllFrames()
        if self.treeFrame is None:
            self.buildTreeFrame()
        self.treeFrame.pack()

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
        if self.menuFrame is not None:
            self.menuFrame.pack_forget()
        if self.chartFrame is not None:
            self.chartFrame.pack_forget()
        if self.treeFrame is not None:
            self.treeFrame.pack_forget()
        if self.encodeCharFrame is not None:
            self.encodeCharFrame.pack_forget()
        if self.decodeCharFrame is not None:
            self.decodeCharFrame.pack_forget()
        if self.encodeFrame is not None:
            self.encodeFrame.pack_forget()
        if self.decodeFrame is not None:
            self.decodeFrame.pack_forget()
        self.pack()

    def clearSessionData(self):
        self.hideAllFrames()
        self.menuFrame = None
        self.chartFrame = None
        self.treeFrame = None
        self.encodeCharFrame = None
        self.decodeCharFrame = None
        self.encodeFrame = None
        self.decodeFrame = None

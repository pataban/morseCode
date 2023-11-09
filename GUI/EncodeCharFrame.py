import tkinter as tk
from time import time
from static.EncodingChart import EncodingChart
from static.Signal import Signal
from dataCreation import makePromptText
from static.constants import *


class EncodeCharFrame(tk.Frame):
    def __init__(self, master, closeFrame):
        super().__init__(master)
        self.answer = []
        self.keyPressTime = None

        self.menuButton = tk.Button(self, text="Menu")
        self.menuButton["command"] = closeFrame
        self.menuButton.grid(row=0, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                             ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.promptLabel = tk.Label(self)
        self.promptLabel.grid(row=1, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                              ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.answerLabel = tk.Label(self, text="")
        self.answerLabel.grid(row=2, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                              ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.dotButton = tk.Button(self, text="Dot", command=self.addDot)
        self.dotButton.grid(row=3, column=0, ipadx=PADDING_DEFAULT,
                            ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.dashButton = tk.Button(self, text="Dash", command=self.addDash)
        self.dashButton.grid(row=3, column=1, ipadx=PADDING_DEFAULT,
                             ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.skipButton = tk.Button(self, text="Skip", command=self.setPrompt)
        self.skipButton.grid(row=4, column=0, ipadx=PADDING_DEFAULT,
                             ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.submitButton = tk.Button(
            self, text="Submit", command=self.chkAnswer)
        self.submitButton.grid(row=4, column=1, ipadx=PADDING_DEFAULT,
                               ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.validationResultLabel = tk.Label(self, text="")
        self.validationResultLabel.grid(row=5, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                                        ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.bind("<KeyPress>", self.startSignal)
        self.bind("<KeyRelease>", self.endSignal)
        self.bind("<Return>", self.chkAnswer)
        self.bind("<BackSpace>", self.setPrompt)
        self.bind("<Escape>", lambda e: closeFrame())
        self.focus_set()
        self.setPrompt()

    def startSignal(self, _=None):
        if self.keyPressTime is None:
            self.keyPressTime = time()

    def endSignal(self, _=None):
        if self.keyPressTime is not None:
            keyHoldTime = time()-self.keyPressTime
            if keyHoldTime < DASH_KEY_HOLD_DURATION:
                self.addDot()
            else:
                self.addDash()
            self.keyPressTime = None

    def addDot(self):
        self.answer.append(Signal.DOT)
        self.answerLabel["text"] = self.answerLabel["text"] + " Dot"

    def addDash(self):
        self.answer.append(Signal.DASH)
        self.answerLabel["text"] = self.answerLabel["text"] + " Dash"

    def chkAnswer(self, _=None):
        if self.answer == EncodingChart[self.promptLabel["text"]]:
            self.setPrompt()
        else:
            self.validationResultLabel["text"] = "Wrong"
        self.answer = []
        self.answerLabel["text"] = ""

    def setPrompt(self, _=None):
        self.promptLabel["text"] = makePromptText()
        self.validationResultLabel["text"] = ""
        self.answer = []
        self.answerLabel["text"] = ""

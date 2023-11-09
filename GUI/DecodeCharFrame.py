import tkinter as tk
from dataCreation import makePromptMorse
from static.EncodingChart import EncodingChart
from static.constants import *


class DecodeCharFrame(tk.Frame):
    def __init__(self, master, closeFrame):
        super().__init__(master)
        self.menuButton = tk.Button(self, text="Menu")
        self.menuButton["command"] = closeFrame
        self.menuButton.grid(row=0, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                             ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.promptLabel = tk.Label(self)
        self.promptLabel.grid(row=1, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
                              ipady=PADDING_DEFAULT, padx=PADDING_DEFAULT, pady=PADDING_DEFAULT)

        self.answerEntry = tk.Entry(self)
        self.answerEntry.grid(row=2, column=0, columnspan=2, ipadx=PADDING_DEFAULT,
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

        self.answerEntry.bind("<Return>", self.chkAnswer)
        self.bind("<BackSpace>", self.setPrompt)
        self.answerEntry.bind("<Escape>", lambda e: closeFrame())
        self.answerEntry.focus_set()
        self.setPrompt()

    def chkAnswer(self, _=None):
        if EncodingChart[self.answerEntry.get()] == self.promptLabel["text"]:
            self.setPrompt()
        else:
            self.validationResultLabel["text"] = "Wrong"
        self.answerEntry.delete(0, tk.END)

    def setPrompt(self, _=None):
        self.promptLabel["text"] = "".join(
            map(lambda sig: str(sig)+" ", makePromptMorse()))
        self.validationResultLabel["text"] = ""
        self.answerEntry.delete(0, tk.END)

import tkinter as tk
from tkinter import ttk

class DecodeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.menuButton=tk.Button(self,text="Menu")
        self.menuButton.grid(row=0,column=0)


import tkinter
from tkinter import Frame, Entry
from typing import Any

import customtkinter as ctk

from main.logger import get_logger

logger = get_logger(__name__)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


class App(ctk.CTk):
	def __init__(self):
		ctk.set_appearance_mode('dark')
		ctk.set_default_color_theme("dark-blue")
		super().__init__()
		self.geometry(f"{WINDOW_HEIGHT}x{WINDOW_WIDTH}")
		self.wm_title("CertPrep")
		self.pady = 10
		self.padx = 10

		self.grid_columnconfigure(0, weight=3)
		self.grid_columnconfigure(1, weight=1)
		self.mainframe = LocalFrame(
			self, width=int(WINDOW_WIDTH*0.8), height=WINDOW_HEIGHT
		)
		self.mainframe.grid(column=0, row=0, sticky='NEWS')
		self.first_var = tkinter.StringVar()
		self.first_var.set('First entry')
		self.entry1 = LocalEntry(self.mainframe, textvariable=self.first_var)
		self.entry1.grid()

		self.second_var = tkinter.StringVar()
		self.second_var.set('Second entry')
		self.entry2 = LocalEntry(self.mainframe, textvariable=self.second_var)
		self.entry2.grid()
		print(self.entry2.master)

		self.sideframe = LocalFrame(
			self, width=int(WINDOW_WIDTH*0.2), height=WINDOW_HEIGHT
		)
		self.sideframe.grid(column=1, row=0, sticky='NWES')
		self.third_var = tkinter.StringVar()
		self.third_var.set('Third entry')
		self.entry3 = LocalEntry(self.sideframe, textvariable=self.third_var)
		self.entry3.grid()
		self.fourth_var = tkinter.StringVar()
		self.fourth_var.set('Fourth entry')
		self.entry4 = LocalEntry(self.sideframe, textvariable=self.fourth_var)
		self.entry4.grid()
		for entry in filter(lambda x: x.startswith('entry'), self.__dir__()):
			self.__getattribute__(entry).grid_configure(padx=5, pady=5)
		self.mainloop()


class LocalEntry(ctk.CTkEntry):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.configure(corner_radius=20)


class LocalFrame(ctk.CTkFrame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.configure(fg_color='transparent')
		self.configure(**kwargs)


if __name__ == "__main__":
	gui = App()

# This file will run the flash cards app that I will write

import os
import pickle
import sys
import tkinter as tk

# +----------------------------------------------------------------------------+
# | Save and Load code                                                         |
# +----------------------------------------------------------------------------+

# Windows file separator compatibility
if sys.platform == 'win32':
    filesep = "\\"
else:
    filesep = "/"

sourcedir = os.path.dirname(os.path.abspath(__file__)) + filesep
savedir = sourcedir + "savedfcs" + filesep

if not os.path.exists(savedir):
    os.makedirs(savedir)

###
# Practice Code
###

def save(cardset):
    with open(cardset.name + ".fc", "wb+") as f:
        pickle.dump(cardset, f)

def load(filename):
    with open(filename + ".fc", "rb") as f:
        return pickle.load(f)

###
# End Practice Code
###

# +----------------------------------------------------------------------------+
# | Card and Sets code                                                         |
# +----------------------------------------------------------------------------+

class Flashcard:
    def __init__(self, fronttext, backtext):
        self.frontside = fronttext
        self.backside = backtext
        self.timescorrect = 0

class Cardset:
    def __init__(self, name):
        # 4 categories where category 1 is the least well known and category 4
        # is the most well known cards
        self.name = name
        self.cat1 = []
        self.cat2 = []
        self.cat3 = []
        self.cat4 = []

# +----------------------------------------------------------------------------+
# | GUI code                                                                   |
# +----------------------------------------------------------------------------+

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.e1 = tk.Entry(self)
        self.e1.grid()

        self.saveentry = tk.Button(self, text='Save', command=self.saveset)
        self.saveentry.grid()

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

    def saveset(self):
        cardset = Cardset(self.e1.get())
        save(cardset)

app = Application()
app.master.title('Sample application')
app.master.geometry("600x400")
app.mainloop()

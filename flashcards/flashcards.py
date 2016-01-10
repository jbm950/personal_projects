# This file will run the flash cards app that I will write

import os
import pickle
import sys
import tkinter as tk
import tkinter.filedialog as fdialog

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


TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        self.entry1 = tk.Entry()
        button1 = tk.Button(self, text="Go to Page One",
                            command=self.folderprint)
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        self.entry1.pack()
        button1.pack()
        button2.pack()

    def folderprint(self):
        folder = fdialog.askdirectory(initialdir="./savedfcs",
                                      title="Choose a Directory") + filesep
        formatted = self.entry1.get().lower().replace(" ", "_")

        if formatted != "" and folder != filesep:
            cardset = Cardset(self.entry1.get())

            with open(folder + formatted, "wb+") as f:
                pickle.dump(cardset, f)

        return


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry('800x600')
    app.mainloop()

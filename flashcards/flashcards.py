# This file will run the flash cards app that I will write

import os
import pickle
import sys
import tkinter as tk
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox

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


# +----------------------------------------------------------------------------+
# | Card and Sets code                                                         |
# +----------------------------------------------------------------------------+

class Flashcard:
    def __init__(self, fronttext, backtext, name):
        self.frontside = fronttext
        self.backside = backtext
        self.cardname = name
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
        self.fulllist = [self.cat1, self.cat2, self.cat3, self.cat4]


# +----------------------------------------------------------------------------+
# | GUI code                                                                   |
# +----------------------------------------------------------------------------+


TITLE_FONT = ("Helvetica", 36, "bold")


# Popup window with an edit bar
class popupEditWindow(object):
    def __init__(self, master, label):
        top = self.top = tk.Toplevel(master)
        self.l = tk.Label(top, text=label)
        self.l.pack()
        self.e = tk.Entry(top)
        self.e.pack()
        self.b = tk.Button(top, text='Ok', command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        self.top.destroy()


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.cardset = []
        self.frames = {}
        for F in (StartPage, EditSetsPage, ChooseSetsPage, PracticePage):
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
        frame.update()
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Flash Cards 4 You", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=40)

        button1 = tk.Button(self, text="Edit Sets", command=self.editsets)
        button2 = tk.Button(self, text="Practice",
                            command=lambda:
                            controller.show_frame("ChooseSetsPage"))
        button1.pack()
        button2.pack()

    def editsets(self):
        response = messagebox.askyesnocancel(message="Would you like to create"
                                             " a new set?")
        if response is None:
            return
        elif response is True:
            window = popupEditWindow(self.controller, label="Card Set "
                                     "Name?\nWarning do not create cardsets "
                                     "with the same name")
            self.controller.wait_window(window.top)
            try:
                filename = window.value
            except AttributeError:
                return

            folder = fdialog.askdirectory(initialdir="./savedfcs",
                                          title="Choose a Directory") + filesep
            formatted = filename.lower().replace(" ", "_")

            if formatted != "" and folder != filesep:
                cardset = Cardset(filename)
                filename = folder + formatted

                with open(filename, "wb+") as f:
                    pickle.dump(cardset, f)
            else:
                return

        elif response is False:
            filename = fdialog.askopenfilename(initialdir="./savedfcs",
                                               title="Choose a Cardset")
            if filename == "":
                return
            cardset = pickle.load(open(filename, "rb"))

        self.controller.cardset = [cardset]
        self.controller.filepath = filename
        self.controller.show_frame("EditSetsPage")

    def update(self):
        pass


class EditSetsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        front = tk.Label(self, text="Front", font=TITLE_FONT)
        front.place(relx=0.2, rely=0.25, anchor="center")
        self.fronte = tk.Text(self, relief="sunken", bd=1)
        self.fronte.place(relx=0.2, rely=0.5, relheight=0.38, relwidth=0.38,
                          anchor="center")

        back = tk.Label(self, text="Back", font=TITLE_FONT)
        back.place(relx=0.6, rely=0.25, anchor="center")
        self.backe = tk.Text(self, relief="sunken", bd=1)
        self.backe.place(relx=0.6, rely=0.5, relheight=0.38, relwidth=0.38,
                         anchor="center")

        savebutton = tk.Button(self, text="Save",
                               command=self.savecard)
        savebutton.place(relx=0.17, rely=0.8, anchor="center")

        exitbutton = tk.Button(self, text="Exit", command=self.exitedit)
        exitbutton.place(relx=0.26, rely=0.8, anchor="center")

        newcardbutton = tk.Button(self, text="New Card", command=self.newcard)
        newcardbutton.place(relx=0.37, rely=0.8, anchor="center")

        deletecardbutton = tk.Button(self, text="Delete Card",
                                     command=self.deletecard)
        deletecardbutton.place(relx=0.5, rely=0.8, anchor="center")

        switchcardbutton = tk.Button(self, text="Switch Card",
                                     command=self.switchcard)
        switchcardbutton.place(relx=0.64, rely=0.8, anchor="center")

    def checksaved(self):
        if (self.fronte.get("1.0", "end")[:-1] == self.active_card.frontside and
           self.backe.get("1.0", "end")[:-1] == self.active_card.backside and
           self.cardnamee.get() == self.active_card.cardname):
            pass
        else:
            response = messagebox.askyesno(message="Would you like to save "
                                           "changes to the current card before "
                                           "continuing?")
            if response:
                success = self.savecard()
                return success

    def deletecard(self):
        if messagebox.askyesno(message="Are you sure you wish to delete this "
                               'card? "%s"' % self.active_card.cardname):
            for i in self.cardset.fulllist:
                for j in i:
                    if j.cardname == self.active_card.cardname:
                        i.remove(self.active_card)

            self.active_card = []
            for i in self.cardset.fulllist:
                try:
                    self.active_card = i[0]
                    break
                except IndexError:
                    pass

            if not self.active_card:
                card = Flashcard("", "", "New Card")
                self.active_card = card
                self.cardset.cat1.append(card)

            self.updatefields()
            self.savecard()

    def exitedit(self):
        if self.checksaved() is False:
            return
        self.controller.show_frame("StartPage")

    def newcard(self):
        if self.checksaved() is False:
            return
        exitflag = False
        for i in self.cardset.fulllist:
            for j in i:
                if j.cardname == "New Card":
                    exitflag = True
                    break
            if exitflag:
                break
        else:
            self.active_card = Flashcard("", "", "New Card")
            self.cardset.cat1.append(self.active_card)

        x = 1
        while exitflag:
            iterate = False
            for i in self.cardset.fulllist:
                for j in i:
                    if j.cardname == "New Card " + str(x):
                        iterate = True
                        break
                if iterate:
                    x += 1
                    break
            else:
                exitflag = False
                self.active_card = Flashcard("", "", "New Card " + str(x))
                self.cardset.cat1.append(self.active_card)

        self.updatefields()
        self.savecard()

    def savecard(self):
        for i in self.cardset.fulllist:
            for j in i:
                if j.cardname == self.cardnamee.get() and j != self.active_card:
                    messagebox.showwarning(message='Card named "%s" already '
                                           'exists' % self.cardnamee.get())
                    return False
        self.active_card.cardname = self.cardnamee.get()
        self.active_card.frontside = self.fronte.get("1.0", "end")[:-1]
        self.active_card.backside = self.backe.get("1.0", "end")[:-1]
        self.updatefields()
        self.saveset()

    def saveset(self):
        with open(self.controller.filepath, "wb+") as f:
            pickle.dump(self.cardset, f)

    def switchcard(self):
        if self.checksaved() is False:
            return
        selected_card = self.cardlist.get("active")
        for i in self.cardset.fulllist:
            for j in i:
                if j.cardname == selected_card:
                    self.active_card = j

        self.updatefields()

    def update(self):
        self.cardset = cardset = self.controller.cardset[0]
        title = tk.Label(self, text=cardset.name, font=TITLE_FONT)
        title.place(relx=0.5, rely=0.05, anchor="center")

        self.active_card = []
        for i in cardset.fulllist:
            try:
                self.active_card = i[0]
                break
            except IndexError:
                pass

        if not self.active_card:
            card = Flashcard("", "", "New Card")
            self.active_card = card
            cardset.cat1.append(card)

        cardname = tk.Label(self, text="Card Name", font=TITLE_FONT)
        cardname.place(relx=0.2, rely=0.15, anchor="center")

        self.cardnamee = tk.Entry(self)
        self.cardnamee.place(relx=0.45, rely=0.16, anchor="center")

        self.cardnamee.insert(0, self.active_card.cardname)
        self.fronte.insert("insert", self.active_card.frontside)
        self.backe.insert("insert", self.active_card.backside)

        self.cards = tk.Label(self, text="Cards", font=TITLE_FONT)
        self.cards.place(relx=0.885, rely=0.05, anchor="center")
        scrollbar = tk.Scrollbar(self, orient="vertical")
        self.cardlist = tk.Listbox(self, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.cardlist.yview)
        scrollbar.place(relx=0.985, rely=0.5, relheight=0.8, anchor="center")
        self.cardlist.place(relx=0.885, rely=0.5, relheight=0.8,
                            anchor="center")

        for i in self.cardset.fulllist:
            for j in i:
                self.cardlist.insert("end", j.cardname)

    def updatefields(self):
        self.cardlist.delete(0, "end")
        self.cardnamee.delete(0, "end")
        self.fronte.delete("1.0", "end")
        self.backe.delete("1.0", "end")

        self.cardnamee.insert(0, self.active_card.cardname)
        self.fronte.insert("insert", self.active_card.frontside)
        self.backe.insert("insert", self.active_card.backside)

        for i in self.cardset.fulllist:
            for j in i:
                self.cardlist.insert("end", j.cardname)


class ChooseSetsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose the sets for practice",
                         font=TITLE_FONT)
        label.place(relx=0.5, rely=0.1, anchor="center")

        addbutton = tk.Button(self, text="Add", command=self.addset)
        addbutton.place(relx=0.5, rely=0.4, anchor="center")

        removebutton = tk.Button(self, text="Remove", command=self.removeset)
        removebutton.place(relx=0.5, rely=0.45, anchor="center")

        upfolderbutton = tk.Button(self, text="Up Folder",
                                   command=self.upfolder)
        upfolderbutton.place(relx=0.5, rely=0.5, anchor="center")

        downfolderbutton = tk.Button(self, text="Down Folder",
                                     command=self.downfolder)
        downfolderbutton.place(relx=0.5, rely=0.55, anchor="center")

        startbutton = tk.Button(self, text="Start", command=self.start)
        startbutton.place(relx=0.5, rely=0.6, anchor="center")

        backbutton = tk.Button(self, text="Back", command=self.back)
        backbutton.place(relx=0.5, rely=0.65, anchor="center")

        scrollbar1 = tk.Scrollbar(self, orient="vertical")
        self.openlist = tk.Listbox(self, yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=self.openlist.yview)
        scrollbar1.place(relx=0.36, rely=0.6, relheight=0.7, anchor="center")
        self.openlist.place(relx=0.2, rely=0.6, relheight=0.7, relwidth=0.3,
                            anchor="center")

        openfolder = tk.Label(self, text="Selected Sets", font=("Helvetica",
                                                                24))
        openfolder.place(relx=0.8, rely=0.2, anchor="center")

        scrollbar2 = tk.Scrollbar(self, orient="vertical")
        self.chosenlist = tk.Listbox(self, yscrollcommand=scrollbar2.set)
        scrollbar2.config(command=self.chosenlist.yview)
        scrollbar2.place(relx=0.96, rely=0.6, relheight=0.7, anchor="center")
        self.chosenlist.place(relx=0.8, rely=0.6, relheight=0.7, relwidth=0.3,
                              anchor="center")

    def addset(self):
        index = self.currentfolder.rfind("savedfcs") + len("savedfcs")
        loc = self.currentfolder[index:]
        item = loc + self.openlist.get("active")

        if item in self.chosenlist.get(0, "end"):
            self.errormessage("item present")
            return
        else:
            self.chosenlist.insert("end", item)

    def back(self):
        self.controller.show_frame("StartPage")

    def downfolder(self):
        folder = self.openlist.get("active")
        if os.path.isdir(self.currentfolder + folder):
            self.currentfolder = self.currentfolder + folder
        else:
            self.errormessage("not folder")
            return

        self.updatelist()

    def errormessage(self, code):
        if code == "not folder":
            errmessage = "The selected item is not a folder"
        elif code == "top folder":
            errmessage = "Already at the root folder. Please make sure your " \
                         "files are saved under the savedfcs folder"
        elif code == "item present":
            errmessage = "The selected item is already added"
        elif code == "none selected":
            errmessage = "No items have been selected"

        messagebox.showwarning(message=errmessage)

    def removeset(self):
        self.chosenlist.delete("active")

    def start(self):
        items = self.chosenlist.get(0, "end")
        root = "./savedfcs"
        if not items:
            self.errormessage("none selected")
            return

        for i in items:
            if os.path.isdir(root + i):
                for subdir, dirs, files in os.walk(root + i):
                    for i in files:
                        if not subdir.endswith(filesep):
                            subdir += filesep
                        cardset = pickle.load(open(subdir + i, "rb"))
                        for i in self.controller.cardset:
                            if i.name == cardset.name:
                                break
                        else:
                            self.controller.cardset += [cardset]
            else:
                cardset = pickle.load(open(savedir + i.lower().replace(" ",
                                                                       "_"),
                                           "rb"))
                for i in self.controller.cardset:
                    if i.name == cardset.name:
                        break
                else:
                    self.controller.cardset += [cardset]

        self.controller.show_frame("PracticePage")

    def upfolder(self):
        if self.currentfolder == savedir:
            self.errormessage("top folder")
            return
        index = self.currentfolder.rstrip(filesep).rindex(filesep)
        self.currentfolder = self.currentfolder[:index + 1]
        self.updatelist()

    def update(self):
        self.controller.cardset = []
        self.openlist.delete(0, "end")
        self.chosenlist.delete(0, "end")
        self.currentfolder = savedir

        self.updatelist()

    def updatelist(self):
        self.openlist.delete(0, "end")

        index = self.currentfolder.rstrip(filesep).rindex(filesep)
        clearing = tk.Label(self, text="                          ",
                            font=("Helvetica", 24))
        clearing.place(relx=0.2, rely=0.2, anchor="center")
        openfolder = tk.Label(self, text=self.currentfolder[index + 1:],
                              font=("Helvetica", 24))
        openfolder.place(relx=0.2, rely=0.2, anchor="center")

        for i in os.listdir(self.currentfolder):
            if os.path.isfile(self.currentfolder + i):
                self.openlist.insert("end", i.replace("_", " ").title())
            else:
                self.openlist.insert("end", i + filesep)


class PracticePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def update(self):
        for i in self.controller.cardset:
            print(i.name)


if __name__ == "__main__":
    app = MainApp()
    app.geometry('800x600')
    app.title("Flash Cards 4 You")
    app.mainloop()

# Graphic User Interface

# 1) Way to collect users input on owner of the book
# 2) Way to display the database nicely
# 3) The scan button that prompts barcodeReader to work

from tkinter import *

# in tkinter canvas/window where every graphical element is located in root
from database_holder import SearchData

root = Tk()
# --------------------------------------------------------------------------------------------------


def getSearch():
    search = searchBar.get()
    result = SearchData(search)
    for i in result:
        print(i)


def keydown(e):
    print(getSearch())
# --------------------------------------------------------------------------------------------------


# creates SearchBox widget
descr = Label(root, text='Search ISBN, author or title of the book')
descr.grid(row=0, column=0)
searchBar = Entry(root, width=75)
searchBar.grid(row=10, column=0)

# when Enter is pressed, text from the searchbar is retrieved into search variable
root.bind("<Return>", keydown)
root.mainloop()


# --------------------------------------------------------------------------------------------------
'''
Input: rows from the database
Output: new window with a graphic representation of the database
'''


def displayData(isbn, title, author, year, owner, holder):
    # rows represent how many rows from the table do we want to output on the screen
    root2 = Tk()
    i = 1
    isbn_display = Label(root2, text=isbn, padx=20).grid(row=i, column=0)
    title_display = Label(root2, text=title, padx=20).grid(row=i, column=1)
    author_display = Label(root2, text=author, padx=20).grid(row=i, column=2)
    year_display = Label(root2, text=year, padx=20).grid(row=i, column=3)
    owner_display = Label(root2, text=owner, padx=20).grid(row=i, column=4)
    holder_display = Label(root2, text=holder, padx=20).grid(row=i, column=5)

# --------------------------------------------------------------------------------------------------

# Not Needed for it now


'''
# function that makes button do something
def scanPressed():
    scanLabel = Label(root2, text="When Button is pressed, barcode reading+webscraping should start").pack()

# get owner's name for the database entry
def getOwner():
    owner = entryBox.get()
    return owner
'''

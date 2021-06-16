# Graphic User Interface 
# Searchbar 
# INPUT: user types out the ISBN, author (exact) or title (exact)
# OUTPUT: prints out results from the database 

from tkinter import *

# function located in datbase_holder.py, pulls rows of the database that correspond to search
from database_holder import SearchData

root = Tk()

# --------------------------------------------------------------------------------------------------
'''
Input: rows from the database
Output: new window with a graphic representation of the database
'''


def displayData(result):
    # rows represent one book in the database
    # len(result) represents how many books were found by search function in the database
    root2 = Tk()
    for i in range(len(result)):
        for j in range(len(result[0])):
            Label(root2, text = result[i][j], padx = 20).grid(row=i, column=j)

# --------------------------------------------------------------------------------------------------

def getSearch():
    search = searchBar.get()
    result = SearchData(search)
    root.destroy()
    displayData(result)


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
!!!NOT READY YET!!!
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

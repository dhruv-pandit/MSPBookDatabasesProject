# Graphic User Interface
from tkinter import *

# in tkinter canvas/window where every graphical element is located in root
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
    print(result)

    # search scenario
    if (result == []):
        Label(root2, text="Sorry, there is no such book in the database!", padx=20).pack()

    else:
        if (len(result[0]) > 3):
            header = ('ISBN', 'Title', 'Author', 'Published', 'Owner of the book', 'Current holder')
            result.insert(0, header)

        for i in range(len(result)):
            for j in range(len(result[0])):
                Label(root2, text=result[i][j], padx=20).grid(row=i, column=j)


# --------------------------------------------------------------------------------------------------

def getSearch():
    search = searchBar.get()  # gets the info from the search bar text field
    result = SearchData(search)  # calls the search data function from database_holder
    root.destroy()
    displayData(result)


def keydown(e):
    getSearch()


# --------------------------------------------------------------------------------------------------


# creates SearchBox widget
descr = Label(root, text='Search ISBN, author or title of the book')
descr.grid(row=0, column=0)
searchBar = Entry(root, width=75)
searchBar.grid(row=10, column=0)

# when Enter is pressed, text from the searchbar is retrieved into search variable
root.bind("<Return>", keydown)
root.mainloop()


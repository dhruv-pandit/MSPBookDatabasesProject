import sqlite3

# we need some variable to connect to our database
# following line of code creates a database called library
conn = sqlite3.connect('library.db')

# create a cursor
cursor = conn.cursor()


# create a table
# Available data types for sqlite: NULL, INTEGER, REAL, TEXT, BLOB
create_library_table = """
CREATE TABLE IF NOT EXISTS library (
  isbn TEXT PRIMARY KEY,
  author TEXT,
  title TEXT,
  year INTEGER,
  owner TEXT,
  holder TEXT
  
);
"""


cursor.execute(create_library_table)
# --------------------------------------
# populating function, must be called after web scraper and user fill prompt are done working
# adds only unique entries


def new_book(ISBN, author, title, year, owner):
    sql = '''INSERT OR IGNORE INTO library (isbn, author, title, year, owner, holder) 
                   VALUES (?, ?, ?, ?, ?, ?) '''
    row = (ISBN, author, title, year, owner, owner)
    cursor.execute(sql, row)
    conn.commit()

# --------------------------------------


'''
Input: search variable from GUI
Output: rows of the table containing relevant information
'''


def SearchData(search):
    sql = 'SELECT * FROM library WHERE isbn like ? OR author like ? OR title like ?'
    tuple = (search, search, search)
    cursor.execute(sql, tuple)
    output = cursor.fetchall()
    conn.commit()
    return output


# commit our command
conn.commit();

# close our connection



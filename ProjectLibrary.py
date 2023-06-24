""" 
THIS FILE CONTAINS LIBRARY CLASS AND ITS METHODS .THIS PROGRAM STORES  DATA 
IN 3 TXT FILES 1.LibraryData.txt STORES DATA FOR GENERAL TEXT RECORD ONLY, 
2. lenderData.txt IS USED BY THE PROGRAM TO FECH LENDER'S DATA EVEN IF 
THE PROGRAM IS CLOSED AND USED LATER, 3. BookData.txt IS USED BY THE 
PROGRAM TO FECH BOOK'S DATA EVEN IF THE PROGRAM IS CLOSED AND USED LATER.
"""
import time
import datetime
f = open("LibraryData.txt","a")
p = open("lenderData.txt","a")
p.close
q = open("BookData.txt","a")
q.close
class Library:
    def __init__(self):
        self.booksList= []
        self.lendDict = {}
        self.lendTime = {}
        self.returnTime = {}

# Method to display book in library
    def displayBooks(self):
        print(f"Books available in Library: ")
        for book in self.booksList:
            print(book)

# Method to lend book in library
    def lendBook(self,user,book):
        if book not in self.booksList:
            print(f"No such book {book} is present in Library")
            return 0
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                self.lendTime.update({book:time.time()})
                f.write(f"Book {book} was lended to {self.lendDict[book]} on {datetime.datetime.now()}\n")
                f.flush()
                print("Lender details has been updated")
                return 1
            else:
                print(f"Book is in already in use by {self.lendDict[book]}")
                return 0

# Method to add book in library
    def addBook(self,book):
        if book not in self.booksList :
            self.booksList.append(book)
            print("Book has been added successfully")
            return 1
        else :
            print(f"Book {book} is already present in library")
            return 0

# Method to return book in library 
    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.returnTime.update({book:time.time()})
            f.write(f"Book {book} was returned by {self.lendDict[book]} on {datetime.datetime.now()}\n")
            f.flush()
            self.lendDict.pop(book)
            print(f"Book {book} returned successfully")
            return 1
        else:
            print(f"{book} was not lended")
            return 0

# Method to delete book in library 
    def deleteBook(self,book):
        if book in self.booksList and book not in self.lendDict.keys():
            self.booksList.remove(book)
            print(f"Book {book} is deleted from the Library")
            return 1
        else:
            print(f"No such book {book} is present in Library or the book is currently lended")
            return 0

# Method to check late fine for a book in library 
    def lateFine(self,book):
        a= self.returnTime[book] - self.lendTime[book]
        dueTime = 10   # SET DUE TIME HERE FOR N DAYS DUE TIME SET (N*24*60*60).................
        if a> (dueTime): 
            print(f"Item overdue late fine is rupees {(a//dueTime)+1}")
            f.write(f"Item overdue late fine was rupees {(a//dueTime)+1}\n")
            f.flush()
            return 1
        return 0

# Method to store lender's data for a book in library
    def lenderData(self):
       p = open("lenderData.txt","w")
       for book in self.lendDict.keys():
        p.write(book+"\n")
        p.write(self.lendDict[book]+"\n")
        p.write(str(self.lendTime[book])+"\n")
        p.close
# Method to fech lender's data for a book in library. 
    def fechLenderData(self):
        p = open("lenderData.txt","r")
        l= p.readlines()
        for item in range(0,len(l)):
            if item % 3 == 0:
                a=str(l[item]).strip()
                b=str(l[item+1]).strip()
                self.lendDict.update({a:b})
                self.lendTime.update({a:float(l[item+2])})
        p.close
# Method to close LibraryData.txt .
    def closeLibraryData(self):
        f.close
# Method to store Book data in library
    def BookData(self):
       q = open("BookData.txt","w")
       for book in self.booksList:
        q.write(book+"\n")
        q.close
# Method to fech book data in library. 
    def fechBookData(self):
        q = open("BookData.txt","r")
        l= q.readlines()
        for item in range(0,len(l)):
            l[item]= str(l[item]).strip()
        self.booksList = l
        q.close
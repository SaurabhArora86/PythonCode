class Library:
    book = []
    numBooks = 0
    # def __init__(self):
    #     self.numBooks = 0

    def addBooks(self, bookname):
        Library.book.append(bookname)
        Library.numBooks += 1
        print(Library.book)
        print(Library.numBooks)

    def validateEntries(self):
        if (Library.numBooks != len(Library.book)):
            print("Book mismatched")

    def showInfo(self):
        print(Library.book)


l1 = Library()
print(l1.numBooks)
print(l1.book)
l1.addBooks("Hindi")
l1.validateEntries()
l2 = Library()
l2.addBooks("Sanskrit")
l2.validateEntries()
l2.showInfo()

class Library:
    def __init__(self, listbooks, permenantBooks):
        self.books=listbooks
        self.permenantList=permenantBooks

    def availableBooks(self):
        print("\nList of available books are:\n")
        for book in self.books: 
            print(f"  *{book}")
    
    def borrowBook(self, name):
        if name in self.books:
            self.books.remove(name)
            print(f"\nCongratulations! Book '{name}' is issued by you.")
            return True
        else:
            if name in self.permenantList:
                print(f"The book {name} is yet to be returned and not available at this moment please come later.")
            else:
                print(f"There is no such book as '{name}' in library to issue.")

    def returnBook(self, name):
        if name in self.permenantList:
            self.books.append(name)
            print("\nThe book is successfully returned!\nThenk you for using Library.")
            return True
        else:
            print("\nThis book does not belong to our library.\nPlease make a new entry to give a book to library.")

            
    def newEntry(self, name):
        self.books.append(name)
        self.permenantList.append(name)
        print("Thanks for giving this new book to the library!")

    def password(self, pin):
        with open("D:\Python\Project Library Management System\password.txt", "r") as p:
            if p.read()==pin:
                return True
            
    def changePassword(self, new):
        with open("D:\Python\Project Library Management System\password.txt", "w") as p:
            p.write(new)
        print("\n** PASSWORD SUCCESSFULLY CHANGED PERMANENTLY **")
        


class student:

    def __init__(self, listStudents):
        self.stud=listStudents

    def getList(self):
        print("\nRecord:-\n")
        for s in self.stud:
            print(f"  *{s}")

    def borrowBook(self):
        global name
        name=input("\nEnter a book to be issued:- ")
        name=name.upper()
        global studentName
        studentName=input("\n Enter Your name:- ")
        studentName=studentName.upper()
        return name
    
    def returnBook(self):
        name=input("\nEnter the name of the book to be returned:- ")
        name=name.upper()
        global studentName
        studentName=input("Enter Your Name:- ")
        studentName=studentName.upper()
        return name

    def newEntry(self):
        name=input("\nEnter the book to give to Library:- ")
        name=name.upper()
        return name


    def studentRecordAdd(self):
        self.stud.append(studentName+" : "+name)

    def studentRecordRemove(self):
        self.stud.remove(studentName+" : "+name)



if __name__ == "__main__":
    Central_Library = Library(["BOOK1", "BOOK2", "BOOK3"], ["BOOK1", "BOOK2", "BOOK3"])
    Student=student([])
    while (True):
        print('''\n***** WELCOME TO CENTRAL LIBRARY *****
        Choose a option to continue:
        1. Check Available Books
        2. Borrow A Book
        3. Return A Book
        4. Make A New Entry
        5. Check Student Record
        6. Change Password Permanently
        7. Exit''')
        a=int(input("\nSelect a choice:- "))
        if a==1:
            Central_Library.availableBooks()
        elif a==2:
            check=Central_Library.borrowBook(Student.borrowBook())
            if check==True:
                Student.studentRecordAdd()
        elif a==3:
            check=Central_Library.returnBook(Student.returnBook())
            if check==True:
                Student.studentRecordRemove()
        elif a==4:
            Central_Library.newEntry(Student.newEntry())
        elif a==5:
            pin=input("\n\n** ENTER THE PASSWORD TO PROCEED **\n :- ")
            check=Central_Library.password(pin)
            if check==True:
                Student.getList()
            else:
                print("\n** ACCESS DENIED **")
        elif a==6:
            pin=input("\n\n** ENTER YOUR OLD PASSWORD **\n :-")
            check=Central_Library.password(pin)
            if check==True:
                new=input("Enter Your new Password:- ")
                Central_Library.changePassword(new)
        elif a==7:
            break
        else:
            print("\nEnter A Valid Input")

    print("\n\tTHANK YOU FOR USING CENTRAL LIBRARY\n\t\tHAVE A GREAT DAY!")

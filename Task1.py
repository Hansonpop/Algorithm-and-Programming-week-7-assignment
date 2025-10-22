class Member:
    def __init__(self,name,member_id,borrowed_books):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = borrowed_books
    def borrowed_book(self,Book_name):
        self.__borrowed_books.append(Book_name)
        print(f'You have borrowed another book called \'{Book_name}\'')
    def return_books(self,Book_name):
        self.__borrowed_books.remove(Book_name)
        print(f'You have just removed \'{Book_name}\' from your list of borrowed books')
    def show_info(self):
        print(f'You currently have borrowed {self.__borrowed_books}')
    def setname(self,new_name):
        old = self.name
        print(f'Your name was {old}, your current name is {new_name}')
    def getname(self):
        print(f'Your name is {self.name}')
A1 = Member('Gilbert','2902718912',['Mom'])
A1.show_info()
A1.borrowed_book('Cool')
A1.show_info()
A1.return_books('Cool')
A1.show_info()
A1.getname()
A1.setname('Kenichi')
A1.getname()





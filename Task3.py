class Esports:
    def __init__(self,name):
        self.name = name
    def show_role(self):
        print(f'Game name is {self.name}')

class ML(Esports):
    def __init__(self,name,genre):
        super().__init__(name)
        self.genre = genre
    def show_role(self):
        print(f'YOU LOSE')
    def review(self):
        self.show_role()
        print(f'Game name is {self.name}, The genre is {self.genre}')

class Pubg(Esports):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre
    def show_role(self):
        print(f'YOU Have a problem')
    def review(self):
        self.show_role()
        print(f'Game name is {self.name}, genre is {self.genre}')
MOBA = ML('Mobile Legends', 'MOBA')
# MOBA.review()
pubg = Pubg('Pubg','Fps')
# pubg.review()

Games = [MOBA,pubg]
for x in Games:
    x.show_role()
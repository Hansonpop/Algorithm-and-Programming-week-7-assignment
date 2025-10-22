class student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def add_grade(self,subject,score):
        if 0 <= score <= 100:
            newgrade= {
                'Subject' : subject,
                'Score' : score
            }
            self.grades.append(newgrade)
            return newgrade
        else:
            print('stupid')
    def calc_gpa(self):
        average = sum(g['Score'] for g in self.grades) / len (self.grades)
        return average
    def get_info(self):
        avg = self.calc_gpa()
        print(f'Student name is {self.name}, Average gpa is {self.calc_gpa()}')
Student1 = student('Gilbert',[])
Student1.add_grade('Maths',90)
Student1.add_grade('Biology',88)
Student1.calc_gpa()
Student1.get_info()
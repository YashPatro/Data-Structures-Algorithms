#16/08/25


'''class fruit:
    def __init__(self,name,shape,taste,CoO,color):
        self.name = name
        self.shape = shape
        self.taste = taste
        self.CoO = CoO
        self.color = color
    def printer(self):
        print(f'name: {self.name}, shape: {self.shape}, taste: {self.taste}, CoO: {self.CoO}, color: {self.color}')
        
    
orange = fruit('Orange','sphere','sweet','China/India/Myanmar','orange')
orange.printer()
print(orange.taste)'''
#python inheritence
'''class person():
    def __init__(self,name,age,birthplace):
        self.name = name
        self.age = age
        self.birthplace = birthplace
    def printer(self):
        print(f'{self.name} = name,{self.age} = age,{self.birthplace} = birthplace')

class child(person):
    def __init__(self, name, age, birthplace,salary,designation):
        person.__init__(self,name,age,birthplace)  
        self.salary = salary
        self.designation = designation

    def printer2(self):
        print(f'{self.name} = name,{self.age} = age,{self.salary} = salary')
unemployed = person('Yash','14','London')
employed = child('Yash','14','London','100,000/anum','COO')
unemployed.printer()
employed.printer2()
employed.printer()

'''
#due 23/08/25 homework
class teacher():
    def __init__(self,name,subject,total_classes):
        self.name = name
        self.subject = subject
        self.total_classes = total_classes

    def printer(self):
        print(f'{self.name} = name,{self.subject} = subject,{self.total_classes} = total classes being taught')

class class1(teacher):
    def __init__(self,name,subject,total_classes,name_class,num_students):
        self.name = name
        self.subject = subject
        self.total_classes = total_classes
        self.name_class = name_class
        self.num_student = num_students

    def printer(self):
        print(f'{self.name} = name of teacher,{self.subject} = subject,{self.name_class} = name_class,{self.num_student} = number of students')

mr_patro = teacher('yash','maths',5)
class_10AB = class1('yash','maths',5,'10AB',31)
class_10AB.printer() 

class Emobilislabs:
    def __init__(self, name, capacity, tablecount, currentclass):
        self.labname = name
        self.labcapacity = capacity
        self.labtablecount = tablecount
        self.labcurrentclass = currentclass


class User:
    def __init__(self, name, email, password):
        self.username = name
        self.useremail = email
        self.userpassword = password
    def register(self):
        print('Registered with email', self.useremail, 'and password', self.userpassword)
    def login(self):
        if self.useremail == 'emobilis@gmail.com' and self.userpassword == '123':
            print('login successful')
        else:
            print('wrong email or password')

#create a product class with properties of choice and make sure class has
#both delete and view methods that print statement of your choice called\

class Students:
    def __init__(self, name, age, gender):
        self.studentname = name
        self.studentage = age
        self.studentgender = gender

    def view(self):
        print('Student name:', self.studentname, 'and age', self.studentage, 'student gender', self.studentgender)

    def delete(self):
        print('you can delete')

class Wanafunzi:
    def login(self):
        print('yeah, I can login')

    def register(self):
        print('yeah, I can register')
studi1 = Wanafunzi()
studi1.register()

class Teacher(Wanafunzi):
    pass
teacher1 = Teacher()
teacher1.login()

import pickle
class School(object):
    def __init__(self,Sname,Addr):
        self.Sname = Sname
        self.Addr = Addr
        self.course = []
    def __del__(self):
        pass
    def __str__(self):
        print('I am school')
    def Create_coures(self):
        name,price,time1 = input('请输入课程的名称，价格，周期：')
        course = Course(name,price,time1)
        self.course.append(course)

class Member(object):
    def __init__(self,name):
        self.name = name
    def __del__(self):
        pass

class Student(Member):
    def __init__(self,name,age,Course_obj):
        super(Student,self).__init__(name)
        self.age = age
        self.Course_obj = Course_obj
    def __del__(self):
        pass
    def __str__(self):
        print('I am a student!')

class Course(object):
    def __init__(self,Cname,price,Ctime,CSchool_addr=0):
        self.Cname = Cname
        self.price = price
        self.Ctime = Ctime
        self.CSchool_addr = CSchool_addr

    def __del__(self):
        pass
    def __str__(self):
        print('I am a Course')

class Teacher(object):
    def __init__(self,name,Course_obj):
        super(Teacher,self).__init__(name)
        self.Course_obj = Course_obj
    def __del__(self):
        pass
    def __str__(self):
        print('I am a Teacher!')

#创建北京、上海两个学校
Beijing_School = School('北京分校','北京')
Shanghai_School = School('上海分校','上海')

#常见linux，python，go3个课程，linux/python在北京，go在上海
Linux = Course('Linux',5000,Beijing_School.Addr)
Python = Course('Python', 7000,Beijing_School.Addr)
Go = Course('Go',6000,Shanghai_School.Addr)

#课程包含周期、价格、通过学校创建课程

class student:
    name="sai"
    print(name)
    def __init__(self,n,a,b):
        print("default method")
        self.name=n
        self.age=a
        self.branch=b
        print(self.name)
        print(self.age)
        print(student.name)
        student.name=n
        print(student.name)
    def details(self):
        print("user defined method")
        print(self.age)
    @classmethod
    def namechange(cls,new_name):
        student.name=new_name
        print(student.name)
    
abc=student("kumar",22,"cse") 
abc.details()
abc.namechange("rahul")


#Online Exam Portal – Encapsulation Example
class Onlineexam:
    def __init__(self):
        self.__questions={
            "city of destiny ?" : "vizag" ,
            "who is ap cm?" : "cbn"
        }
        self.__marks=0
        self.__isloggedin=False
        
        
    def login(self,student_id):
        if student_id == "student123":
            self.__isloggedin=True
            print("student login successful")
        else:
            print("invalid id")
    def start_exam(self):
        if self.__isloggedin:
            print("start exam")
            for q in self.__questions:
                print("Q",q)
        else:
            print("please login and start the exam")
    def submit_exam(self,answers):
        if self.__isloggedin:
            for q, correct_ans in self.__questions.items():
                if answers.get(q) == correct_ans:
                    self.__marks += 1
            print(f"Exam submitted! You scored {self.__marks} out of {len(self.__questions)} marks.")
        else:
            print("please login and start the exam")
  
exam = Onlineexam()
exam.login("student123")
exam.start_exam()
answers={
     "city of destiny ?" : "vizag" ,
            "who is ap cm?" : "cbn"
}
exam.submit_exam(answers)












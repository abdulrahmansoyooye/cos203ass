class Course:
    
    def __init__(self,course_title,units,lecturer,courses):
        self.course_title=course_title
        self.units=units
        self.lecturer=lecturer
        self.students=[]
    def enroll(self,student_name):
        if(student_name not in self.students):
            self.students.append(student_name)
    def drop(self,student_name):
        self.students.pop(student_name)
    def class_size(self):
        return len(self.students)
    def __str__(self):
        return "List of Enrolled Students: %s" % (self.students)
maths = Course("Maths",3,"Ade","")
maths.enroll("abdulrahman")
maths.enroll("abdulrahman")
maths.enroll("ade")
print(maths)


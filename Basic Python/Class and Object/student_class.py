class Student:
    def __init__(self, name, Id, department, CGPA, isEnrolled):
        self.name = name
        self.Id = Id
        self.department = department
        self.CGPA = CGPA
        self.isEnrolled = isEnrolled
    
    def is_honour_roll(self): #Class function
        if self.CGPA >= 3.5:
            return True
        else:
            return False
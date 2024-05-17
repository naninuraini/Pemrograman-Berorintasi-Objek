class Student:
    def __init__(self, name, npm):
        self.name = name
        self.npm = npm
        self.courses = []
        self.total_sks = 0 

    def take_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.enroll_student(self)
            self.total_sks += course.sks  
            print(f"{self.name} berhasil mengambil mata kuliah {course.name}:")
            print(f"\tDosen: {course.instructor}")
            print(f"\tSKS: {course.sks}")
            print(f"\tJadwal: {course.schedule}")
            print(f"\tTotal SKS sekarang: {self.total_sks}\n")
        else:
            print(f"{self.name} sudah mengambil mata kuliah {course.name}\n")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)
            self.total_sks -= course.sks 
            print(f"{self.name} berhasil menghapus mata kuliah {course.name}:")
            print(f"\tTotal SKS sekarang: {self.total_sks}\n")
        else:
            print(f"{self.name} tidak mengambil mata kuliah {course.name}\n")


class Course:
    def __init__(self, name, instructor, sks, schedule):
        self.name = name
        self.instructor = instructor
        self.sks = sks
        self.schedule = schedule
        self.students = []

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

if __name__== "__main__":
    Della = Student("Della Agustin", "2215061116")
    Nani = Student("Nani Nuraini", "2215061032")
    Syefara = Student("Syefara Raissa", "2215061012")
    Cia = Student("Siti Fatiha", "2215061084")

    PBO_course = Course("Pemrograman Berorinetasi Objek", "Puput", 4, "Jumat 13.30-10.00")
    AI_course = Course("Kecerdasan Buatan", "Yessi", 3, "Senin 14.40.00-17.10")

    Nani.take_course(PBO_course)
    Della.take_course(PBO_course)
    Della.take_course(AI_course)

    print(f"Total SKS {Nani.name}: {Nani.total_sks}")
    print(f"Total SKS {Della.name}: {Della.total_sks}")
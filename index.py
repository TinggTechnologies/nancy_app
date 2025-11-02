from abc import ABC, abstractmethod  # For abstraction


# ---------- ABSTRACTION ----------
class Student(ABC):
    def __init__(self, name, matric_no):
        self.name = name
        self.matric_no = matric_no

    @abstractmethod
    def calculate_result(self):
        pass


# ---------- ENCAPSULATION ----------
class Undergraduate(Student):
    def __init__(self, name, matric_no, scores):
        super().__init__(name, matric_no)
        self.__scores = scores  # Private variable (encapsulation)

    def calculate_result(self):
        avg = sum(self.__scores) / len(self.__scores)
        return f"Undergraduate {self.name} ({self.matric_no}) - Average: {avg:.2f}"


# ---------- INHERITANCE ----------
class Postgraduate(Student):
    def __init__(self, name, matric_no, scores, thesis_score):
        super().__init__(name, matric_no)
        self.__scores = scores
        self.__thesis_score = thesis_score

    # ---------- POLYMORPHISM ----------
    def calculate_result(self):
        avg = (sum(self.__scores) / len(self.__scores) + self.__thesis_score) / 2
        return f"Postgraduate {self.name} ({self.matric_no}) - Final Score: {avg:.2f}"


# ---------- MAIN PROGRAM ----------
def main():
    student1 = Undergraduate("Alani Afeez", "ECO230211071", [70, 65, 80, 75])
    student2 = Postgraduate("Blessing Ade", "ECO230211101", [60, 55, 65], 70)

    students = [student1, student2]

    print("===== STUDENT RESULT SUMMARY =====")
    for s in students:
        print(s.calculate_result())


if __name__ == "__main__":
    main()

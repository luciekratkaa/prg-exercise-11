class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        if self.get_by_index(index) >= 90:
            znamka = "A"
        elif 90 > self.get_by_index(index) >= 80:
            znamka = "B"
        elif 80 > self.get_by_index(index) >= 70:
            znamka = "C"
        elif 70 > self.get_by_index(index) >= 60:
            znamka = "D"
        elif 60 > self.get_by_index(index) >= 50:
            znamka = "E"
        else:
            znamka = "F"
        return znamka

    def find(self, index):
        idx = []
        for i in range(len(self.scores)):
            if self.scores[i] == index:
                idx.append(i)
        return idx

    def get_sorted(self):
        scores = list(self.scores)
        for num in range(len(scores)):
            for n in range(0, len(scores) - num - 1):
                if scores[n] > scores[n + 1]:
                    scores[n], scores[n + 1] = scores[n + 1], scores[n]
        return scores

if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())          # 9
    for student in range(results.count()):
        print(f"Student {student}: {results.get_grade(student)} - {results.get_grade(student)}")
    print(results.get_by_index(2))  # 91
    print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
from datetime import datetime
class Worker:
    def __init__(self, Number, Name, Age, Salary):
        self.number = Number
        self.age = datetime.now().year - Age
        self.name = Name
        self.salary = Salary
def srzar(workers):
    sumSalary = 0
    for y in workers:
        sumSalary += y.salary
    return sumSalary / workers.__len__()
def srzaDo30(workers):
    sumSalary = 0
    counter = 0
    for y in workers:
        if y.age < 30:
            counter += 1
            sumSalary += y.salary
    try:
        return sumSalary / counter
    except:
        return 0
        print("Nie ma ludzi młodsze 30 lat")
def srzaOd30(workers):
    sumSalary = 0
    counter = 0
    for y in workers:
        if y.age >= 30:
            counter += 1
            sumSalary += y.salary
    return sumSalary / counter
def porownaj(mlodszy, starsi):
    if mlodszy > starsi:
        return "Wynagrodzenie młodych ludzi jest większe(30)"
    else:
        return "Pensja osób starszych jest większa(30)"

def main():
    dict = [[1, "Adam", 1983, 1500],
            [2, "Anna", 1981, 1700],
            [3, "Blazej", 1990, 1800],
            [4, "Beata", 1992, 1600],
            [5, "Czesław", 1980, 2000],
            [6, "Cecylia", 1983, 2100],
            [7, "Daniel", 1976, 1900]]
    people = []
    for y in dict:
        people.append(Worker(y[0], y[1], y[2], y[3]))
    print(srzar(people))
    print((porownaj(srzaDo30(people), srzaOd30(people))))
main()
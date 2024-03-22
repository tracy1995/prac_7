import csv

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

    def __lt__(self, other):
        return self.year < other.year

def load_guitars():
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                name, year, cost = line
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("No previous data found. Starting with an empty list.")
    return guitars

def save_guitars(guitars):
    with open('guitars.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


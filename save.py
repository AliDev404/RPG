import csv

class SaveLoader:
    def __init__(self):
        self.filename = "save.csv"
        self.saves = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                self.saves = [row for row in reader]
        except FileNotFoundError:
            self.saves = []  

    def save(self, name, level):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, level])
        print(f"Saved {name}, {level}")

        self.saves.append({'name': name, 'level': level})

    def load(self, name):
        for row in self.saves:
            if row['name'] == name:
                print(f"{name} {row['level']}")
                return
        print(f"Name '{name}' not found in the file.")

    def show_all_save(self):
        if not self.saves:
            print("No saves found.")
            return
        for row in self.saves:
            print(f"{row['name']} {row['level']}")






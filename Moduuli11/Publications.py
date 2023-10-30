class Publication:
    def __init__(self, name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        Publication.__init__(self, name)

    def print_info(self):
        print(f"Sarjakuvan tiedot:\nNimi: {self.name}\nPäätoimittaja: {self.editor}")

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        Publication.__init__(self, name)

    def print_info(self):
        print(f"Kirjan tiedot:\n"
              f"Nimi: {self.name}\n"
              f"Kirjailija: {self.author}\n"
              f"Sivumäärä: {self.pages}")

def main():
    sarjis = Magazine("Aku Ankka", "Aki Hyyppä")
    kirja = Book("Hytti n:o 6", "Rosa Liksom", 200)
    sarjis.print_info()
    print("--------")
    kirja.print_info()

main()

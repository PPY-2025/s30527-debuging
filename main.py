# Zad 1

def factorial(n):
    if n == 0:
        return 1 #silnia nigdy nie zwraca 0, nawet jak jest 0! to wynik jest 1
    return n * factorial(n - 1)

# testy
assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(5) == 120

# Zad 2

def get_grades():
    return [5, 4, "3", 2, 1]        # "3" jest stringiem wiec sprawdzamy czy ocena nie jest stringiem aby policzyc srednia

def calculate_average(grades):
    numeric_grades = []
    for g in grades:
        try:
            numeric_grades.append(int(g))
        except ValueError:
            print(f"Nieprawidłowa ocena: {g}, pomijam.")
    if numeric_grades:
        return sum(numeric_grades) / len(numeric_grades)
    return 0


def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

show_result()

# Zad 3

#Metoda take_damage otrzymuje float (damage = 15.0) i aktualizuje hp,
# ale hp może się stać floatem, co nie pasuje do oczekiwanego typu danych (int).

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = int(hp)

    def take_damage(self, amount):
        self.hp = max(0, int(self.hp - amount))

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        damage = int(self.strength * 1.5)
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)  # Powinien wypisać "Not enough mana!"
    print("End:", w.hp, m.hp)

# Testy (asercje)
    assert m.hp == 45  # 60 - 15 od wojownika
    assert w.hp == 25  # 3 ataki po 25 -> 75 obrażeń
    assert m.mana == 0  # 2 ataki = 20 many

simulate_battle()
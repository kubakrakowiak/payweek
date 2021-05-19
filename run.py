import names
import random
import readkeys
import os


class Game:
    def __init__(self):
        self.time = 100
        self.threat = 50

    def add_time(self, time):
        self.time += time

    def add_threat(self, threat):
        self.threat += threat


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class Player(Person):
    def __init__(self, name, lastname, cls):
        super().__init__(name, lastname)
        self.cls = cls


class Guard(Person):
    def __init__(self):
        super().__init__(names.get_first_name(gender='male'), names.get_last_name())
        self.power = random.randint(1, 60)
        self.isDead = False

    def introduce(self):
        return self.name + " " + self.lastname

    def shooting(self):
        self.power += -20
        if self.power <= 0:
            self.isDead = True

    def is_dead(self):
        return self.isDead


class Lock:
    def __init__(self):
        self.difficulty = random.randint(1, 100)


class Gun:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def ammo_check(self):
        return self.ammo

    def add_ammo(self, value):
        self.ammo += value

class View:
    Part = Game()
    SpawnedGuard = []
    SpawnedGuard.append(Guard())
    SpawnedGuard.append(Guard())
    SpawnedGuard.append(Guard())
    SpawnedGuard.append(Guard())
    Weapon = Gun('Default', 0)
    desc = [
        "Jesteś agentem 123 i musisz ukraść superbroń z bazy złej organizacji, to jana misja dlatego nie możesz dać się zauważyć.",
        "Widzisz pokój kontrolny z kamerami.",
        "Widzisz strażnika " + SpawnedGuard[0].introduce() + " w pokoju z kamerami.",
        "Na końcu korytarza widzisz stalowe zamknięte drzwi",
        "Widzisz dwóch rozmawiających ze sobą strażników  " + SpawnedGuard[1].introduce() + " i " + SpawnedGuard[2].introduce(),
        "Zauważa cię cywilny pracownik (" + SpawnedGuard[3].introduce() + ").",
        "Widzisz zbrojownię co robisz?",
        "Wchodzisz do dużego magazynu. Po drugiej stronie pomieszczenia widzisz przełącznik przeciwpożarowy.",
        "Przed twoimi oczami pojawia się się wielki sejf z zamkiem elektronicznym.",
        "Znajdujesz w sejfie tajną broń zabierasz ją i uciekasz włazem"
    ]
    picks = [
        ["Wejdź do budynku przez wentylację. (zabiera 5 czasu daje 5% wykrycia)", 1, 2, -5, 5, 0], #desc, stage, destination, time, guards
        ["Wejdź do budynku przez okno. ( zabiera 10 czasu daje 10% wykrycia)", 1, 2, 0, 0, 0],
        ["Wejdź frontowymi drzwiami. ( zabiera 1 czasu daje 100% wykrycia)", 1, 2, -1, 100, 0],
        ["Wyłącz kamery. (zabiera 10 czasu odejmuje 15% wykrycia)", 2, 3, -10, 15, 0],
        ["Idź dalej korytarzem. (zabiera 1 czasu)", 2, 4, -1, 0, 0],
        ["Strzelasz do strażnika.(zabiera 1 czasu, zabiera 1 pocisk)", 3, 4, -1, 0, 1],
        ["Ogłuszasz strażnika.(zabiera 5 czasu)", 3, 4, -5, 0, 0],
        ["Otwierasz zamek wytrychem.(zabiera 5 czasu)", 4, 5, -5, 0, 0],
        ["Strzelasz do zamka. (zabiera 1 czasu, zwiększa wykrycie o 3%, zabiera 1 ammo)", 4, 5, -1, 3, 0],
        ["Przekradasz się obok nich. (zabiera 5 czasu)", 5, 6, -5, 0, 0],
        ["Strzelasz do nich. (zabiera 1 czasu, zabiera 2 ammo)", 5, 6, -1, 0, 2],
        ["Bijesz się z nimi. (zabiera 2 czasu, podnosi wykrycie o 10%)", 5, 6, -2, 10, 0],
        ["Uciekasz przed nimi. (tracisz 1 czasu, wykrycie wzrasta)", 6, 7, -1, 10, 0],
        ["Obezwładniasz cywila. (tracisz 5 czasu)", 6, 7, -5, 0, 0],
        ["Przeszukujesz ją w poszukiwaniu amunicji. (dodaje x naboi, tracisz 5 czasu)", 7, 8, -5, 0, 0],
        ["Idziesz dalej korytarzem. (tracisz 1 czasu)", 7, 8, -2, 0, 0],
        ["Strzelsz w przełącznik odwracając uwagę strażników. (odejmuje 5 czasu, odejmuje 10 wykrycia, odejmuje 1 "
         "amunicji)", 8, 9, -5, -10, 0],
        ["Przełączasz czujnik  ręcznie. (odejmuje 10 czasu, odejmuje 10 wykrycia)", 8, 9, -10, -10, 0],
        ["Ignorujesz czujnik. (odejmuje 1 czasu)", 8, 9, -1, 0, 0],
        ["Hakujesz drzwi. (zabiera 5 czasu daje 5 wykrycia)", 9, 10, -5, 5, 0],
        ["Szukasz karty dostępu. (zabiera 10 czasu, daje 2 wykrycia)", 9, 10, -10, 2, 0],
        ["Uciekasz korytarzem w lewo.", 10, 11, 0, 0, 0],
        ["Uciekasz korytarzem w prawo.", 10, 11, 0, 0, 0]
    ]

    def welcome(self):
        clearConsole()
        print(text_wrapper("|", "|", "-"))
        print(
            text_wrapper("| Jesteś tajnym agentem, który musi wykraść niebezpieczną broń złej organizacji.", "|", " "))
        print(text_wrapper(
            "| Zadanie nie należy do najprostrzych, musisz wykazać się sprytem i dobrze zarządzać dostępnymi zasobami.",
            "|", " "))
        print(text_wrapper("| Każdy wybór ma znaczenie! ", "|", " "))
        print(text_wrapper("|", "|", "-"))
        print("")
        print(text_wrapper("|", "|", "-"))
        print(text_wrapper("| Wybieraj mądrze.", "|", " "))
        print(text_wrapper("|", "|", "-"))
        print("")
        print(text_wrapper("|", "|", "-"))
        print(text_wrapper("| Wciśnij spacje.", "|", " "))
        print(text_wrapper("|", "|", "-"))
        print("")
        ch = readkeys.getch()
        if ch == " ":
            self.weapon_pick()

    def start(self):
        clearConsole()
        print("")
        print("|------------|")
        print("| [1] Start  |")
        print("| [2] Zasady |")
        print("| [0] Wyjdź  |")
        print("|------------|")
        print("")

        ch = readkeys.getch()
        if ch == "1":
            self.welcome()
        elif ch == "2":
            self.rules()
        elif ch == "0":
            return

    def rules(self):
        clearConsole()
        print("")
        print(
            "|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(
            "| Zasady gry:                                                                                                                                                                 |")
        print(
            "| Trzy statystyki:                                                                                                                                                            |")
        print(
            "| -Czas- jeśli spadnie do zera gra się kończy, jedne czynności zabierają więcej inne mniej czasu                                                                              |")
        print(
            "| -Wykrycie- jeśli wyniesie 100% gra się kończy, jedne czynności dodają inne odejmują wykrycie                                                                                |")
        print(
            "| -Amunicja- mamy tylko parę sztuk, zużywają ją tylko pojedyncze czynności                                                                                                    |")
        print(
            "|                                                                                                                                                                             |")
        print(
            "|                                                                                                                                                                             |")
        print(
            "| Fabuła: jesteś tajnym agentem który musi wykraść niebezpieczną broń złej organizacji. Musisz wykazać się sprytem i sprytnie zarządzać dostępnymi zasobami by ci się udało.  |")
        print(
            "|                                                                                                                                                                             |")
        print(
            "| Opis krok po kroku                                                                                                                                                          |")
        print(
            "| *liczby są przykładowe                                                                                                                                                      |")
        print(
            "| **czas na początku =100, wkrycie 50%, amunicja 5                                                                                                                            |")
        print(
            "|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("")

    def action_pick(self, stage):
        clearConsole()
        print(text_wrapper("|", "|", "-"))
        print(text_wrapper("|    John Wick", "Stage: " + str(stage) + "         |", " "))
        print(text_wrapper("|", "Ammo: " + str(self.Weapon.ammo) + "         |", " "))
        print(text_wrapper("|", "Time: " + str(self.Part.time) + "         |", " "))
        print(text_wrapper("|", "Threat: " + str(self.Part.threat) + "         |", " "))
        print(text_wrapper("|", "|", "-"))
        print(self.desc[stage - 1])
        i = 0
        tab = []
        for p in self.picks:
            if p[1] == stage:
                tab.append([])
                tab[i].append(p[2])
                tab[i].append(p[3])
                tab[i].append(p[4])
                tab[i].append(p[5])
                i += 1
                print(str(i) + ". " + p[0])

        ch = readkeys.getch()

        if stage == 10:
            self.gameover_win()
        else:
            for t in range(1, len(tab) + 1):
                if ch == str(t):
                    self.Part.add_time(tab[t - 1][1])
                    self.Part.add_threat(tab[t - 1][2])
                    if self.Part.time <= 0 or self.Part.threat >= 100:
                        self.gameover_lost(stage)
                    else:
                        self.action_pick(tab[t - 1][0])

    def gameover_lost(self, stage):
        clearConsole()
        print(text_wrapper("|", "|", "-"))
        print(" Zostałeś złapany!")
        print(" Twój wynik to: ", stage)
        print(text_wrapper("|", "|", "-"))

    def gameover_win(self):
        clearConsole()
        print("")
        print(" Gratulacje!")
        print(" Udało Ci się wykraść niebezpieczną broń.")
        print(" Twój wynik to: amunicja - ", self.Weapon.ammo_check(), "", "|", "", "wykrycie - ", self.Part.threat, "", "|", "", "",
              "czas - ", self.Part.time)

    def weapon_pick(self):
        clearConsole()
        print("")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print(
            "| Wybierz Broń                                                                                            |\n")
        print(
            "| 1. Plainsrider Bow                                                                                      |")
        print(
            "| 2. USP Compact Tactical                                                                                 |")
        print(
            "| 3. Vulcan Minigun                                                                                       |")
        print(
            "| Wybieraj mądrze.                                                                                        |")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print("")
        ch = readkeys.getch()
        if ch == "1":
            self.Weapon = Gun('Plainsrider Bow', 3)
            self.Part.add_threat(-20)
            self.class_pick()
        elif ch == "2":
            self.Weapon = Gun('USP Compact Tactical', 10)
            self.Part.add_threat(0)
            self.class_pick()

        elif ch == "3":
            self.Weapon = Gun('Vulcan Minigun', 20)
            self.Part.add_threat(25)
            self.class_pick()

    def class_pick(self):
        clearConsole()
        print("")
        print(text_wrapper("|", "| ", "-"))
        print(text_wrapper("| Wybierz Klasę", "| ", " "))
        print(text_wrapper("| Wybieraj mądrze.", "| ", " "))
        print(text_wrapper("| 1. Ghost.", "| ", " "))
        print(text_wrapper("| 2. Anarchist.", "| ", " "))
        print(text_wrapper("| 3. Gambler.", "| ", " "))
        print(text_wrapper("|", "|", "-"))
        print("")
        ch = readkeys.getch()
        if ch == "1":
            self.Character = Player("John", "Wick", 0)
            self.action_pick(1)
        elif ch == "2":
            self.Character = Player("John", "Wick", 1)
            self.action_pick(1)
        elif ch == "3":
            self.Character = Player("John", "Wick", 2)
            self.action_pick(1)


def clearConsole():
    os.system('cls')


def text_wrapper(left, right, fill_char):
    try:
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = os.get_terminal_size(1)
    return str(left) + str(fill_char) * (columns - len(left) - len(right)) + str(right)


def main():
    print('elo')
    Screen = View()
    Screen.start()

    input()


if __name__ == "__main__":
    main()

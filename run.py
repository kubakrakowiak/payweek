import names
import random
import readkeys
import os




class Game:
    def __init__(self):
        self.time = 1000
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
    def __init__(self, name, lastname):
        super().__init__(name, lastname)
        self.power = random.randint(1, 60)


class Lock:
    def __init__(self):
        self.difficulty = random.randint(1, 100)


class Gun:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo


class View:
    def clearConsole(self):
        os.system('cls')

    def welcome(self):
        self.clearConsole()
        print("")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print(
            "| Jesteś tajnym agentem, który musi wykraść niebezpieczną broń złej organizacji.                          |")
        print(
            "| Zadanie nie należy do najprostrzych, musisz wykazać się sprytem i dobrze zarządzać dostępnymi zasobami. |")
        print(
            "| Każdy wybór ma znaczenie!                                                                               |")
        print(
            "| Wybieraj mądrze.                                                                                        |")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print("")
        ch = readkeys.getch()
        if ch == " ":
            self.weapon_pick()

    def start(self):
        self.clearConsole()
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

    def rules(self):
        self.clearConsole()
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

    def action_pick(self, desc, picks, stage):
        self.clearConsole()
        print(desc[stage-1])
        for p in picks:
            if p[1] == stage:
                print(p[0])


    def gameover_lost(self, stage):
        self.clearConsole()
        print("")
        print(" Zostałeś złapany!")
        print(" Twój wynik to: ", stage)

    def gameover_win(self, ammo, time, threat):
        self.clearConsole()
        print("")
        print(" Gratulacje!")
        print(" Udało Ci się wykraść niebezpieczną broń.")
        print(" Twój wynik to: amunicja - ", ammo, "", "|", "", "wykrycie - ", threat, "", "|", "", "", "czas - ", time)

    def weapon_pick(self):
        self.clearConsole()
        print("")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print(
            "| Wybierz Broń                                                                                            |")
        print(
            "| Wybieraj mądrze.                                                                                        |")
        print(
            "|---------------------------------------------------------------------------------------------------------|")
        print("")


def main():
    print('elo')
    Screen = View()
    desc = ["Opis1", "Opis2"]
    desc[1]
    picks = [
        ["Wejdż do budynku przez wentylację(zabiera 5 czasu daje 5% wykrycia)", 1, 2, -5, 5, 0],
        ["Wejdź do budynku przez okno( zabiera 10 czas daje 10% wykrycia)", 1, 2, 0, 0, 0],
        ["Wejdz frontowymi drzwiami( zabiera 1 czasu daje 100% wykrycia)", 1, 2, -1, 100, 0],
        ["dsadsada(zabiera 5 czasu daje 5% wykrycia)", 2, 3, -5, 5, 0],
        ["Wdasdaso( zabiera 10 czas daje 10% wykrycia)", 2, 3, 0, 0, 0],
        ["Wdasdasd( zabiera 1 czasu daje 100% wykrycia)", 2, 3, -1, 100, 0]
    ]
    Screen.action_pick(desc, picks, 2)

    input()


if __name__ == "__main__":
    main()

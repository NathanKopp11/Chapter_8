class Critter(object):
    def __init__(self,name,hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappniess <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    def talk(self):
        print("I'm", self.name, "and I feel",self.mood,"now.\n")
        self.__pass_time()

    def eat(self,food = 4):
        food = int(input("How much food(1-4): "))
        if 1 <= food <= 4:
            print("Brruppp. Thank you.")
            self.hunger -= food
        else:
            print("Invalid food choice.")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        fun = int(input("How long do you want to play(1-4): "))
        if 1 <= fun <= 4:
            print("Wheee!")
            self.boredom -= fun
        else:
            print("Invalid time choice.")
        if self.boredom < 0:
            self.boredom = 0
            self.__pass_time()
    def __str__():
        print("Hunger:" , self.hunger)
        print("Boredem: ", self.boredom)
        print("Happiness: ", (self.hunger + self.boredom))
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappniess <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
        print("Mood: ", m)
# main program loop
def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
              ("""
Critter Caretaker

+0 - Quit
+1 - Listen to your critter
+2 - Feed your critter
+3 - Play with your critter
+A - See your stats together
""")
        choice = input("Choice: ")
        print()
        if choice == "0":
            print("Good-bye")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        elif choice == "A":
                crit.__str__()
        else:
            print("\nSorry, but",choice,"isn't a valid choice.")
main()
input("\n\nPress <Enter> to exit....")

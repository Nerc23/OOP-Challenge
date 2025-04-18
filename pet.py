#---assignment done by Nercia Motsepe and Abraham Opilo from from Group109--
class Pet: #Python is like Java, just with a few more steps 
    def __init__(self, name):
        self.name = name #name of my pet
        self.hunger = 2  #an integer representing hunger level(0=full, 10 = very hungry) | changed value from 5 to 2
        self.energy = 9  #an integer, enegry level (0 = tired, 10 = fully rested) | changed value from 5 to 2
        self.happiness = 5 # level 0 to 10
        self.tricks= [] #teaches pet new tricks and stores in a list | somewhere somehow add method to print learnt tricks| BONUS
        
        #Methods: 
        #eat() reduces hunger by 3 points never below 0
        # And increases happiness by 1
    def eat(self):
        self.hunger = max(0, self.hunger -3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating.")

        #Methods:
        #sleep() increases energy by 5 points but never above 10
    def sleep(self):
        self.energy = min(10, self.energy + 5) 
        print(f"{self.name} is sleeping. ZZzzz...")

        #Methods:
        #play() descreases energy by 2
        # Increases happiness by 2
        # Increases hunger by 1 
    def play(self):
        self.energy = max(0, self.energy -2)
        self.happiness = min(10, self.happiness +2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} is playing.")

        #Methods:
        #get_status() prints current state of pet
    def get_status(self):
        print(f"\n--- {self.name}'s Status ----")
        print(f"Energy {self.energy}/10")
        print(f"Happiness {self.happiness}/10")
        print(f"Hunger {self.hunger}/10")
        if self.tricks:
            print(f"Total tricks learnt: {', '.join(self.tricks)}") #checks 'if' the conditions are met or 'else' a message is sent out. 
        else:
            print("Zero tricks learnt!!") #Can't teach old dogs new tricks...Dog, Cat, Bird whatever
            print("---------------------\n")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick) #attribute that coonects trick to train
            print(f"{self.name} learned a new trick: {trick}!")

        else: 
            print(f"{self.name} already knows the trick: {trick}.")

    
    def show_tricks(self):
        if self.tricks:
            print(f"\n-- {self.name}'s Tricks ---")
            for trick in self.tricks: 
                print(f"- {trick}")
            print(f"--------------------\n")
        else:
            print("{self.name} has not learned any new tricks.")
        


#🏁 Submission
#Deadline: [18/04/2025]

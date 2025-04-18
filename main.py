#---assignment done by Nercia Motsepe and Abraham Opilo from from Group109--
from pet import Pet

if __name__ == "__main__": #in main.py we test functionality
    my_pet = Pet("Danger the Dog 🐩") #add other instances of pets to show diversity | all my_pets variables: dog, cat, hamster, bird and monkey to minimize confusion.
    
    my_pet.get_status() #Check status

    my_pet.eat()
    my_pet.get_status() #Check status

    my_pet.play()
    my_pet.get_status() #Check status

    my_pet.sleep()
    my_pet.get_status() #Check status

    #Learning tricks in training
    my_pet.train("Sit")
    my_pet.train("Stay")
    my_pet.train("Come")
    my_pet.train("Heel")
    my_pet.train("High Five")
    my_pet.train("Fetch")
    my_pet.train("Spin")
    my_pet.train("Play Dead")
    my_pet.train("Bark")
    my_pet.train("Sit") # Try to teach trick that has already been taught
    my_pet.show_tricks()

    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status() #Last status check

    #-----------------------------------
    my_pet1 = Pet("Claire the Cat🐈") # Input the Name
    my_pet1.get_status() #Check status

    my_pet1.eat()
    my_pet1.get_status() #Check status

    my_pet1.play()
    my_pet1.get_status() #Check status

    my_pet1.sleep()
    my_pet1.get_status() #Check status

     #Learning tricks in training
    my_pet1.train("Sit")
    my_pet1.train("Stay")
    my_pet1.train("Come")
    my_pet1.train("High Five")
    my_pet1.train("Fetch")
    my_pet1.train("Spin")
    my_pet1.train("Jump")
    my_pet1.show_tricks()

    my_pet1.eat()
    my_pet1.play()
    my_pet1.sleep()
    my_pet1.get_status() #Last status check

    #---------------------
    #When confused, do it the long way
    my_pet2 = Pet("Henry the Hamster🐹") # Input the Name
    my_pet2.get_status() #Check status

    my_pet2.eat()
    my_pet2.get_status() #Check status

    my_pet2.play()
    my_pet2.get_status() #Check status

    my_pet2.sleep()
    my_pet2.get_status() #Check status

     #Learning tricks in training
    my_pet2.train("Sit")
    my_pet2.train("Stay")
    my_pet2.train("Come")
    my_pet2.train("Fetch")
    my_pet2.train("Spin")
    my_pet2.train("Kiss")
    my_pet2.train("Stand")
    my_pet2.show_tricks()

    my_pet2.eat()
    my_pet2.play()
    my_pet2.sleep()
    my_pet2.get_status() #Last status check

    #-----------------------------------
    my_pet3 = Pet("Birdie the Bird🦜") # Input the Name
    my_pet3.get_status() #Check status

    my_pet3.eat()
    my_pet3.get_status() #Check status

    my_pet3.play()
    my_pet3.get_status() #Check status

    my_pet3.sleep()
    my_pet3.get_status() #Check status

     #Learning tricks in training
    my_pet3.train("Sit")
    my_pet3.train("Fly")
    my_pet3.train("Come")
    my_pet3.train("Nod")
    my_pet3.train("Wave")
    my_pet3.train("Spin")
    my_pet3.train("Spin") #Repeat
    my_pet3.show_tricks()

    my_pet3.eat()
    my_pet3.play()
    my_pet3.sleep()
    my_pet3.get_status() #Last status check

    #-----------------------------------
    my_pet4 = Pet("Lucy the Monkey🐒") # Input the Name
    my_pet4.get_status() #Check status

    my_pet4.eat()
    my_pet4.get_status() #Check status

    my_pet4.play()
    my_pet4.get_status() #Check status

    my_pet4.sleep()
    my_pet4.get_status() #Check status

     #No learning tricks in training
    my_pet4.show_tricks()

    my_pet4.eat()
    my_pet4.play()
    my_pet4.sleep()
    my_pet4.get_status() #Last status check
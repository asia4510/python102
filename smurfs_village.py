class Village:

    population = 0
    n_houses = 0
   
    def __init__(self, name):
        self.name = name
       
    def check_status(self):
        if Village.population <= Village.n_houses:
            print("The village is in a good shape.")
        else:
            print("The village is overcrowded. Consider building more houses.")

    def get_size(self):
        return f"The Village has {self.n_buildings} buildings and {self.population} habitants"


    def raise_alarm(self):
        smurf_without_hide = Village.population / Village.n_houses
        if smurf_without_hide > 0:
            smurfs_eaten = Village.population % Village.n_houses 
            Village.population = Village.population - smurfs_eaten
            return smurfs_eaten
        print(f"Gargamel has eaten {smurfs_eaten} Smurfs")
    
       
class Building:

    def __init__(self, location, owner):
        self.location = location
        self.owner = owner

    def __str__(self):
        return f"Owner: {self.owner} Location: {self.location}"
    
class House(Building):
        Village.n_houses = Village.n_houses + 1

    
class Pantry(Building):

    total_jam = 0 
    berries_picked = 0

    def check_supply(self):
        return f"You have total of {Pantry.berries_picked} berries and {Pantry.total_jam} jars of jam"
            
       
class Dumpster(Building):
    fill = 100
    
    def __init__(self, fill):
        self.fill = fill
    
    def empty(self):
        self.fill = 0
        
    def check(self):
        bin_check = capacity - fill 
        if bin_check <= 100:
            return "Dumpster is not full"
        else:
            return "It's getting stinky... is time to empty the Dumpster"
    
class Habitant:
    energy = 0
    
   
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name} and I am a resident of a {Village.name}!"

    def sleep(self):
        self.energy = self.energy + 20
        return self.energy

    def eat(self):
        if Kitchen.total_jam == 0:
            print("No jam left. Go over the kitchen and cook some!")
        else:
            self.energy = self.energy + 25
            Pantry.total_jam = Pantry.total_jam - 1

class Smurf(Habitant):
    experience = 0
    
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height
        self.talent = None
        Village.population = Village.population + 1

    def __str__(self):
        return f"Name:{self.name} Age:{self.age} Height:{self.height} inches Experience:{self.experience}"
        
    def check_talent(self):
        if self.talent is None:
            print(f"{self.name} has no talent yet.")

    def give_talent(self, assign_talent):
        if self.experience < 300:
            return "You need more experience before assigning a talent"
        else:
            self.talent = assign_talent
    
    def pick_berries(self, amount):
        self.amount = amount
        Pantry.berries_picked = Pantry.berries_picked + amount
        self.experience = self.experience + (amount * 0.5)

    def cook(self):
        if Pantry.berries_picked < 20:
            print("Note enough berries. Please check the village supplies.")
            pass
        else:
            jam = Pantry.berries_picked // 20
            trash = Pantry.berries_picked % 20
            Dumpster.fill = Dumpster.fill + trash
            Pantry.total_jam = Pantry.total_jam + jam
            Pantry.berries_picked = 0
            print (f"You have created a {jam} jars of jam!")
            
        
class Stork(Habitant):
    def travel(self):
        if self.energy < 20:
            print (f"{self.name} is exhausted and needs more energy")
        else:
            destination = input("Where are we travelling to?: ")
            self.energy = self.energy - 20
            print (f"{self.name} is on the way to {destination}")
            

class Bird(Habitant):
    def send_message(self, recipient, sender):
        message = input("What's the message?: ")
        return f"Message to: {recipient} From: {sender} \n {message}"



    

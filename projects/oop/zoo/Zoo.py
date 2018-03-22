# This is a zoo


class Animal:
	population = 0
	animals = []

	def __init__(self, name):
		self.name = name
		self.animals.append(name)
		Animal.population += 1
		
	def get_animal_name(self):
		return self.name

	def print_animal_name(self):
		print "\nAnimal Name: " + self.get_animal_name()

	@classmethod
	def how_many(cls):
		print cls.animals
		if len(cls.animals) == 1:
			print "You have 1 animal in your zoo!\n" 
		elif len(cls.animals) == 0:
			print "You have no animals in your zoo!\n"
		else:
			print "You have %d animals in your zoo!\n" % cls.population

	@classmethod
	def animal_die(cls):
		animal = raw_input("Which animal?: ")
		cls.animals.remove(animal)
		Animal.how_many()

	def print_description(self):
		print self.description 


class Mammal(Animal):

	def print_description(self):
		self.description = "Mammals have mammary glands and fur."
		print self.description

class Bird(Animal):

	def print_description(self):
		self.description = "Birds have feathers and (usually) wings."
		print self.description

class Fish(Animal):
	
	def print_description(self):
		self.description = "Fish live underwater and have fins & gills."
		print self.description

# Function to check if animal type is valid
def check_animal():
	checking = True

	while checking:
		animal = raw_input("Type (Mammal, Bird, Fish): ").lower()

		if animal == 'mammal':
			animal_name = raw_input("Name: ")
			animal_name = Mammal(animal_name)
			animal_name.print_animal_name()
			animal_name.print_description()
			Animal.how_many()
			checking = False

		elif animal == 'bird':
			animal_name = raw_input("Name: ")
			animal_name = Bird(animal_name)
			animal_name.print_animal_name()
			animal_name.print_description()
			Animal.how_many()
			checking = False

		elif animal == 'fish':
			animal_name = raw_input("Name: ")
			animal_name = Fish(animal_name)
			animal_name.print_animal_name()
			animal_name.print_description()
			Animal.how_many()
			checking = False

		else:
			print "Please input valid animal type (Mammal, Bird, Fish)."

def animal_death():
	death = True
	while death:
		try:
			Animal.animal_die()
			death = False

		except ValueError:
			print "Animal not in zoo." 
			death = False


# main function
def zoo():
	print "Welcome to my Zoo program. You can add/update animals to help keep track of your zoo!"
	running = True

	while running:
		action = raw_input("Add/remove animal? (X to exit): ").lower()

		if action == 'add': 
			check_animal()

		elif action == 'remove':
			animal_death()
		
		elif action == 'x':
			running = False	

		else:
			print "Please follow instructions. "

zoo()
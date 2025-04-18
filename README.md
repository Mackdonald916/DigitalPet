# 🐾 Digital Pet (Python OOP Challenge)

This project demonstrates a **digital pet** using Python's Object-Oriented Programming (OOP) concepts. You can interact with your pet—feed it, let it sleep, play with it, and even teach it tricks!

---

## 🧠 How It Works

The project consists of two main files:
- `pet.py` – contains the `Pet` class that defines how the pet behaves.
- `main.py` – a script where we create a pet object and interact with it.

---

## 🐕‍🦺 `pet.py` Explained

### ✅ Class Definition

class Pet:
This defines a blueprint for our pet. Every pet object created from this class will have the same structure.

🧱 The Constructor: __init__
python
Copy
Edit
def __init__(self, name):
    self.name = name
    self.hunger = 5
    self.energy = 5
    self.happiness = 5
    self.tricks = []
This special method runs automatically when we create a new pet. It sets:

name: the pet's name

hunger: starts at 5 (0 = full, 10 = very hungry)

energy: starts at 5 (0 = tired, 10 = fully rested)

happiness: starts at 5 (0 = sad, 10 = very happy)

tricks: an empty list for storing learned tricks

🍗 eat() Method
python
Copy
Edit
def eat(self):
    self.hunger = max(0, self.hunger - 3)
    self.happiness = min(10, self.happiness + 1)
Reduces hunger by 3, but not below 0.

Increases happiness by 1, but not above 10.

😴 sleep() Method
python
Copy
Edit
def sleep(self):
    self.energy = min(10, self.energy + 5)
Increases energy by 5, but not more than 10.

🎮 play() Method
python
Copy
Edit
def play(self):
    if self.energy >= 2:
        self.energy -= 2
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
Can only play if the pet has at least 2 energy.

Decreases energy by 2.

Increases happiness by 2.

Increases hunger by 1.

📊 get_status() Method
python
Copy
Edit
def get_status(self):
    print(f"{self.name}'s Status:")
    print(f"  Hunger: {self.hunger}/10")
    print(f"  Energy: {self.energy}/10")
    print(f"  Happiness: {self.happiness}/10")
Prints the current values of hunger, energy, and happiness.

🎓 train(trick) Method
python
Copy
Edit
def train(self, trick):
    self.tricks.append(trick)
Adds a new trick (passed as a string) to the pet's tricks list.

🧠 show_tricks() Method
python
Copy
Edit
def show_tricks(self):
    print(", ".join(self.tricks))
Prints all tricks the pet has learned. If none, it says so.

📜 main.py Explained
This is the script that runs the simulation.

🐶 Create a Pet
python
Copy
Edit
my_pet = Pet("Buddy")
Creates a new Pet object called Buddy.

🕹️ Interact with the Pet
python
Copy
Edit
my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
Shows the pet’s initial status

Feeds the pet

Lets it rest

Plays with it

🎯 Teach Tricks
python
Copy
Edit
my_pet.train("roll over")
my_pet.train("sit")
Teaches the pet some tricks

🪞 Show Tricks and Status Again
python
Copy
Edit
my_pet.show_tricks()
my_pet.get_status()
Shows all learned tricks

Displays updated status after interactions



🚀 Try It Yourself!
Run the project and watch your pet come to life! Want to expand it?

Add moods or health tracking

Add time-based hunger or sleep decay

Save/load pet state to/from a file



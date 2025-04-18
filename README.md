
# 🐶 Digital Pet – Python OOP Challenge

Welcome to the **Digital Pet** project! This is a fun and interactive way to learn the basics of Object-Oriented Programming (OOP) in Python. You’ll create your own virtual pet that can eat, sleep, play, and even learn tricks! This mini-project is perfect for beginners who want to build something engaging while practicing classes, methods, and object management in Python.

---

## 🧠 Objective

Create a class called `Pet` that simulates a digital pet with attributes and behaviors. The pet should have its own hunger, energy, and happiness levels, and the user should be able to interact with it using defined methods.

---

## ⚙️ Attributes

Your pet will have the following attributes:

- `name`: the name of your pet (string)
- `hunger`: an integer (0 = full, 10 = very hungry)
- `energy`: an integer (0 = tired, 10 = fully rested)
- `happiness`: an integer (0 = sad, 10 = very happy)
- `tricks`: a list that stores learned tricks (initially empty)

---

## 🔧 Methods

- `eat()`:  
  Reduces `hunger` by 3 points (not below 0) and increases `happiness` by 1 (up to 10).

- `sleep()`:  
  Increases `energy` by 5 points (not above 10).

- `play()`:  
  Decreases `energy` by 2, increases `happiness` by 2 (up to 10), and increases `hunger` by 1 (up to 10). If `energy` is too low, the pet won't play.

- `get_status()`:  
  Prints the current state of the pet — hunger, energy, and happiness.

---

## 🎯 Bonus Features

- `train(trick)`:  
  Teaches the pet a new trick (adds the trick to the `tricks` list).

- `show_tricks()`:  
  Displays all tricks that the pet has learned.

---

## ▶️ How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/digital-pet.git
   cd digital-pet
Run the program


python main.py
Interact with your pet

The pet will eat, sleep, play, learn tricks, and show its current status.

💻 Sample Output
Buddy's Status:
  Hunger: 5/10
  Energy: 5/10
  Happiness: 5/10

Buddy eats happily!
Buddy takes a nap. 😴
Buddy plays joyfully! 🐾
Buddy has learned a new trick: roll over! 🎓
Buddy has learned a new trick: sit! 🎓

Buddy's Tricks: roll over, sit

Buddy's Status:
  Hunger: 3/10
  Energy: 8/10
  Happiness: 8/10
📌 Tip
Feel free to extend the project:

Add pet moods (e.g., excited, bored)

Introduce time-based hunger/energy loss

Use file storage to save pet progress

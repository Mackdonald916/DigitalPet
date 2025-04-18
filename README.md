# 🐶 Digital Pet - Python OOP Challenge

Welcome to the **Digital Pet** project! This Python mini-project is a fun way to practice Object-Oriented Programming (OOP) concepts such as classes, objects, attributes, and methods. In this challenge, you'll interact with your own virtual pet and teach it new tricks! 🎉

## 🧠 Objective

Create a virtual pet using Python's OOP features. The pet can eat, sleep, play, and even learn tricks!

---

## 📁 Project Structure

digital-pet/ ├── pet.py # Pet class definition ├── main.py # Main script to interact with the pet └── README.md # Project documentation

markdown
Copy
Edit

---

## 🔧 Features

### `Pet` Class

- **Attributes**
  - `name`: Name of your pet.
  - `hunger`: Hunger level (0 = full, 10 = very hungry).
  - `energy`: Energy level (0 = tired, 10 = fully rested).
  - `happiness`: Happiness level (0 = sad, 10 = very happy).
  - `tricks`: A list to store learned tricks.

- **Methods**
  - `eat()`: Reduces hunger by 3 (not below 0), increases happiness by 1.
  - `sleep()`: Increases energy by 5 (not above 10).
  - `play()`: Reduces energy by 2, increases happiness by 2, and increases hunger by 1.
  - `get_status()`: Displays current pet status.
  - `train(trick)`: Teaches the pet a new trick and stores it.
  - `show_tricks()`: Displays a list of all learned tricks.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/digital-pet.git
   cd digital-pet
Run the program:

bash
Copy
Edit
python main.py
🖼️ Sample Output
yaml
Copy
Edit
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
🎯 Bonus Ideas
Want to level up the game?

Add pet moods (e.g. bored, excited).

Save pet data to a file for persistence.

Add a GUI using Tkinter or Pygame!

👨‍💻 Author
This project was built as part of the Python OOP Challenge.

Happy coding! 🐾✨

yaml
Copy
Edit

---

Let me know if you want it customized with your GitHub username or repo link, or if you’d like a badge section or screenshot included!

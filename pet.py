class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap. 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays joyfully! 🐾")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10\n")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}! 🎓")

    def show_tricks(self):
        print(f"{self.name}'s Tricks: {', '.join(self.tricks) if self.tricks else 'No tricks learned yet.'}")

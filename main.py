import random

class DiceRoller:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

if __name__ == "__main__":
    # Create a six-sided die
    six_sided_die = DiceRoller()

    # Roll the die
    result = six_sided_die.roll()

    print(f"You rolled a {result} on the six-sided die.")

    assert result > 0 
    assert result <=6 

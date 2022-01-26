import random

class Card:
    """ The responsibility of Card is to keep track of the current and last care and determine if the current
    card is higer or lower than the last card and calculate the points for it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
    def __int__(self):

        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self (Card): An instance of a card.
        """
        self.first_card = 0
        self.next_card = 0
        self.points= 0
    
    def choose_card(self):
# 3) Create the choose_card(self) method. Use the following method comment.
        """Generates a new random value and calculates the points.
        
        Args:
            self (Card): An instance of choosing the next card.
        """
        self.first_card = random.randint(1,13)
        print(f"The card is: {self.first_card} ")
        guess = input("Higher or lower: [h/l] ")
        self.next_card = random.randint (1,13)
        print(f"Next card was: {self.next_card}")

        if guess == "h" and self.first_card < self.next_card:
            self.points = 100
        elif guess == "l" and self.first_card > self.next_card:
            self.points = 100
        elif guess == "h" or guess == "l" and self.first_card == self.next_card:
            self.points = 0
        else:
            self.points = -75
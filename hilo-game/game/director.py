from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[cards]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        if self.total_score > 0:
            play_again = input("Play again? [y/n] ")
            print()
            self.is_playing = (play_again == "y")
        elif self.total_score <= 0:
            quit()
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        card = Card()
        card.choose_card() 
        self.total_score += card.points

    def do_outputs(self):
        """Display the score and check if the game is still being played. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)
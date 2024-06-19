import unittest
from game import game, play_game

class TestGame(unittest.TestCase):
    def test_game(self):
        # Test when user wins
        result, _ = game("rock", "no", "scissors")
        self.assertEqual(result, "You win!")

        # Test when user loses
        result, _ = game("rock", "no", "paper")
        self.assertEqual(result, "You lose!")

        # Test when it's a tie
        result, _ = game("rock", "no", "rock")
        self.assertEqual(result, "It's a tie!")

    def test_play_again(self):
        # Test when user wants to play again
        _, play_again = game("rock", "yes", "rock")
        self.assertEqual(play_again, "yes")

        # Test when user doesn't want to play again
        _, play_again = game("rock", "no", "rock")
        self.assertEqual(play_again, "no")

# Note: Testing the play_game function is tricky because it involves user input and print statements.
# You might want to refactor your code to make it more testable. For example, you could separate the logic for getting user input from the game logic.

if __name__ == '__main__':
    unittest.main()
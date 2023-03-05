from questions import *
import random
import logging
from typing import List

logging.basicConfig(level=logging.INFO)


#sukursime žaidimų klasę, kad galėtume valdyti patį žaidimą. Ši klasė turės metodus, kaip pradėti žaidimą, užduoti klausimus ir sekti vartotojo rezultatą.
#///// English
'''#Then we'll create a game class to handle the game itself. This class 
will have methods to start the game, ask questions, and track the user's score.'''


class Game:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)

    def start(self) -> None:
        logging.info("Welcome to Trivia Challenge!")
        logging.info(f"You will be asked a series of {self.total_questions} questions.")
        logging.info("Answer each question by entering the letter (A, B, or C) corresponding to the correct answer.")
        input("Press enter to begin...")

        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            if self.ask_question(i, question):
                logging.info("Correct!")
                self.score += 1
            else:
                logging.info(f"Sorry, the correct answer was {question.correct_answer}.")
        
        logging.info(f"\nGame over! You scored {self.score} out of {self.total_questions}.")

    def ask_question(self, number, question) -> bool:
        logging.info(f"\nQuestion {number + 1}: {question.prompt}")
        for option, answer in question.answers.items():
            logging.info(f"{option}. {answer}")

        user_answer = input("Your answer: ").upper()
        try:
            return question.check_answer(user_answer)
        except ValueError:
            logging.info(f"\n'{user_answer}' is not a valid option! Try again")
            return self.ask_question(number, question)


# Galiausiai sukuriam pagrindinę žaidimo pradžios funkciją, sukurdami Žaidimo objektą su klausimais iš klausimų modulio.
#////English
'''Finally, we create the main game launch function by creating 
a Game object with questions from the questions module.'''


from game_start import Game

def main() ->None:
    game = Game(questions)

    while True:
        game.start()

        logging.info("Nice try! Enter 'Y' to play again. Enter any other value to exit")
        play_again_answer = input("Play again: ").upper()
        # logging.info(play_again_answer, [play_again_answer != 'Y'])

        if play_again_answer != "Y":
            break

if __name__ == '__main__':
    main()


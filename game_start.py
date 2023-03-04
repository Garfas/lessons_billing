# sukursime klausimų klasę, kuri atspindės kiekvieną žaidimo klausimą. 
# Kiekvienas klausimas turės raginimą ir galimų atsakymų rinkinį, 
# o vienas iš jų bus teisingas.




# Tada sukursime modulį, vadinamą klausimais, kad išsaugotume 
# klausims, kurie bus naudojami žaidime, sąrašą.

from questions import *

#Tada sukursime žaidimų klasę, kad galėtume valdyti patį žaidimą. Ši klasė turės metodus, kaip pradėti žaidimą, užduoti klausimus ir sekti vartotojo rezultatą.
import random
import logging
from typing import List

logging.basicConfig(level=logging.INFO)

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

# Galiausiai galime sukurti pagrindinę žaidimo pradžios funkciją, sukurdami Žaidimo objektą su klausimais iš klausimų modulio.

from game_start import Game

def main():
    game = Game(questions)
    game.start()

if __name__ == '__main__':
    main()

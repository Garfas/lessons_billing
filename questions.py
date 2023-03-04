from typing import List

class Question:
    def __init__(self, prompt, answers, correct_answer) -> None:
        self.prompt = prompt
        self.answers = answers
        self.correct_answer = correct_answer

class GameQuestion(Question):
    def check_answer(self, user_answer) -> bool:
        if user_answer not in self.answers:
            raise ValueError('Invalid option!')
        return user_answer == self.correct_answer

questions = [
    GameQuestion("What is the current capital of Japan?", {"A": "Tokyo", "B": "Asuka", "C": "Kuni-kyo"}, "A"),
    GameQuestion("What is the largest continent?", {"A": "Africa", "B": "Asia", "C": "Europe"}, "B"),
    GameQuestion("What is the highest mountain in the world?", {"A": "Mount Everest", "B": "Mount Kilimanjaro", "C": "Mount McKinley"}, "A"),
    GameQuestion("In 1945, the Atomic bomb was dropped on Hiroshima, what was the name of the bomb?", {"A": "Big Boy", "B": "Little Boy", "C": "Untitled"}, "B"),
    GameQuestion("What is the currency of Japan?", {"A": "Yen", "B": "Won", "C": "Dollar"}, "A"),
    GameQuestion("Who is the founder of Apple?", {"A": "Bill Gates", "B": "Steve Jobs", "C": "Mark Zuckerberg"}, "B"),
    GameQuestion("Waht is the first man to fly to the moon?", {"A": "Buzz Aldrin", "B": "Yuri Alekseyevich Gagarin", "C": "Neill Amstrong"}, "C"),
    GameQuestion("In what year did the first man land on the moon?", {"A": "1969", "B": "1961 ", "C": "1989"}, "A"),
    GameQuestion("Who became the first astronaut to fly to the space and orbited the earth?", {"A": "John Gleen", "B": "Peter Ilyich Tchaikovsky", "C": "Yuri Alekseyevich Gagarin"}, "C"),
    GameQuestion("The area of the largest desert in the world is 14,000,000 km².Which desert is this?", {"A": "Arctic Desert", "B": "Antarctic Desrt", "C": "Sahara Desert"}, "B"),
    GameQuestion("Who became the first king of Lithuania?",{"A": "Mindaugas", "B": "Vytautas", "C": "Gediminas"}, "A" ),
    GameQuestion("In which year was the name of Lithuania first mentioned in written sources?",{"A": "1109 ", "B": "1007", "C": "1009"}, "C"),
    GameQuestion("In which year did Lithuania become an independent state?", {"A": "1918", "B": "1954", "C": "1991"},"A"),
    GameQuestion("The first president of Lithuania?", {"A": "Kazys Grinius", "B": "Antanas Smetona", "C": "Algirdas Mykolas Brazauskas"}, "B"),
    GameQuestion("What is special about the year 2022 in the world?", {"A": "Russia invades Ukraine", "B": "The coronavirus spreads", "C": "Olympic competitions were held"}, "A"),
    GameQuestion("What singer was called the King of Rock and Roll", {"A": "Michael Jackson", "B": "No one was titled", "C": "Elvis Presley"}, "C"),
    GameQuestion("Frenchwoman Jeanne Louise Calment was born in 1875. She is the longest-lived person in the world. How old did she live?", {"A": "120 years", "B": "121 years", "C": "122 years"}, "C"),
    GameQuestion("The highest grossing film in the world", {"A": "Titanic", "B": "Avatar", "C": "Avengers: Endgame"}, "B"),
    GameQuestion("According to the Online Historical Encyclopaedia of Programming Languages, people have created about... ?", {"A": "2351 languages ", "B": "8945 languages", "C": "987 languages"}, "B"),
]
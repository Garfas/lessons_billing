# sukursime klausimų klasę, kuri parodys kiekvieną žaidimo klausimą. 
# Kiekvienas klausimas turės raginimą ir galimų atsakymų pasirinkimą, 
# bet, tik vienas iš jų bus teisingas.
#//// English
''' we'll create a question class to represent each question in the game.
# Each question will have a prompt and a set of possible answers,
# and one of them will be correct.'''


from typing import List

class Question:
    def __init__(self, prompt, answers, correct_answer) -> None:
        self.prompt = prompt
        self.answers = answers
        self.correct_answer = correct_answer

# sukursime modulį, vadinamą klausimais, kad išsaugotume 
# klausimus, kurie bus naudojami žaidimo, sąraše.
#///// English
''' Then we'll create a module called questions to store it
# of questions to be used in the game list.'''

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
    GameQuestion("What singer was called the King of Rock and Roll?", {"A": "Michael Jackson", "B": "No one was titled", "C": "Elvis Presley"}, "C"),
    GameQuestion("Frenchwoman Jeanne Louise Calment was born in 1875. She is the longest-lived person in the world. How old did she live?", {"A": "120 years", "B": "121 years", "C": "122 years"}, "C"),
    GameQuestion("The highest grossing film in the world?", {"A": "Titanic", "B": "Avatar", "C": "Avengers: Endgame"}, "B"),
    GameQuestion("According to the Online Historical Encyclopaedia of Programming Languages, people have created about... ?", {"A": "2351 languages ", "B": "8945 languages", "C": "987 languages"}, "B"),
    GameQuestion("What year did the I world war take place?", {"A": "1814", "B": "1914", "C": "2014"}, "B"),
    GameQuestion("What year did the II world war take place?", {"A": "1901", "B": "1914", "C": "1939"}, "C"),
    GameQuestion("In which year did the I World War end?", {"A": "1918", "B": "1914", "C": "1945"}, "A"),
    GameQuestion("In which year did the II World War end?", {"A": "1939", "B": "1940", "C": "1945"}, "C"),
    GameQuestion("What year was the Ford T car created??", {"A": "1905", "B": "1927", "C": "1932"}, "B"),
    GameQuestion("The first Ford brand car is?", {"A": "Model T", "B": "Model A", "C": "Model C"}, "A"),
    GameQuestion("A city in Japan is named after a car company?", {"A": "Mazda", "B": "Toyota", "C": "Nissan"}, "B"),
    GameQuestion("What was the name of the Japanese city Toyota in the past?", {"A": "Koromo", "B": "Aichi", "C": "Nagoya"}, "A"),
    GameQuestion("What is the largest animal in the world?", {"A": "Colossal Squid", "B": "African Elephant", "C": "Blue Whale"}, "C"),
    GameQuestion("What is the festest land animal in the world?", {"A": "Pronghorn", "B": "Cheetah", "C": "Springbok"}, "B"),
    GameQuestion("Which country produced the largest Bobblehead figure", {"A": "Russia", "B": "America", "C": "United Kingdom"}, "B"),
    GameQuestion("Who created the Python programming language?", {"A": "Tim Berner", "B": "James Gosling", "C": "Guido van Rossum"}, "C"),
    GameQuestion("In which country was the largest pizza baked in 1990?", {"A": "Africa", "B": "USA", "C": "Italy"}, "A"),
    GameQuestion("In 1990, the largest pizza was baked in Africa. What diameter was it?", {"A": "37.3888 meters", "B": "36.5999 meters", "C": "38.6888 meters"}, "A"),
    GameQuestion("The world's deepest lake is?", {"A": "Michigan", "B": "Baikal", "C": "Tanganyika"}, "B"),
    GameQuestion("In Greek mythology, he was half man, half bull, who lived in a labyrinth. Who is he?", {"A": "Pegasus", "B": "Minotaur", "C": "Satire"}, "B"),
    GameQuestion("God created man and woman, but he...invention. Now any moron can do the same.Which he didn't do?", {"A": "Did not patent his invention", "B": "He created woman", "C": "He did everything well"}, "A"),
    GameQuestion("God created a man, but he said I can do better. Then he created a woman and said.What did he say?", {"A": "That's all it takes", "B": "She will do her makeup", "C": "A man is better than a woman"}, "B"),
    GameQuestion("Monica Lewinsky was known to the whole world because?", {"A": "She works in the White House", "B": "She became the first lady", "C": "She had an affair with the president"}, "C"),
    GameQuestion("Who was the First President of the United States of America?", {"A": "George Washington", "B": "Thomas Jefferson", "C": "John Adams"}, "A"),
    GameQuestion("A person who likes to walk without shoes, married his half-sister and a recognized genius?", {"A": "Thomas Alva Edison", "B": "Nikola Tesla", "C": "Albert Einstein"}, "C"),
    GameQuestion("Which company created Santa Claus in 1931, St. Nicholas' interpretations in the modern world.?", {"A": "Pepsi", "B": "James Gosling", "C": "Coca-Cola"}, "C"),
]
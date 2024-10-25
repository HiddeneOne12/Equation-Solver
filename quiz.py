import random

questionsAndAnswers = [
    {"question":"Who is protagonist of first assassins creed from 2008? ","answer":  "Altair"},
    {"question":"How many games are released in Assassins Creed Franchise? ","answer": "13"},
    {"question":"Who make his own luck? ","answer": "Shay Patrick Cormac"},
    {"question":"Who said this line \"IN A WORLD WITHOUT GOLD WE MIGHT HAVE BEEN HEROS\"? ","answer": "Black Beard"},
    {"question":"Who is most famous assassin in assassins creed? ","answer": "Ezio Aditore"},
    {"question":"Who killed tommy angelo in Mafia and Mafia 2? ","answer": "Vito Scaletta"},
    {"question":"Which ending is considered canon in Grand Theft Auto 4? ","answer": "Revenge"},
    {"question":"What is home country of Niko Bellic from Grand Theft Auto 4?","answer": "Russia"},
    {"question":"Who is Mason portray himself as in Call of Duty Black Ops? ","answer": "Victor Resnov"},
    {"question":"Which race does Cirri belong to in Witchers 3? ","answer": "Human and Elf"},
    {"question":"Which historic period does Assassins Creed Unity take place in? ","answer":"French Revolution"},
    {"question":"Nemesis system was introduced in which game ? ","answer":"Shadow of Morder and Shadow of War"},
    {"question":"Which game take place in alternate timeline in which nazis have won world war 2? ","answer": "Wolfestein"},
    {"question":"What is profession of Alan Wake?","answer": "Writer"},
    {"question":"Ghost of Tsushima was developed by which company? ","answer":"Sucker Punch"},
    {"question":"What is name of other atreus name in God of War 2018? ","answer":"Loki"},
    {"question":"Agent Casey also played as which character in Alan Wake 2? ","answer":"Max Pyne"},
    {"question":"Who is antagonist in far cry 4? ","answer":"Pagan Min"},
    {"question":"Which pirate treasure Nathan Drake trying to find in Uncharted 4? ","answer": "Henry Avery"},
    {"question":"Wei shan is playing as what in Sleeping dogs? ","answer":"Double Agent"},
]
amountWon = 0
pointsScored = 0
maxQuestions = 10


def displayQuestion(pointsScored,amountWon):
    try:
        while pointsScored < maxQuestions:       
            random_index = random.randint(0, len(questionsAndAnswers) - 1)
            print(questionsAndAnswers[random_index]['question'])
            answer = input('Please Enter Your Answer : ')
            if(answer.lower() == questionsAndAnswers[random_index]['answer'].lower()):
                amountWon += 100
                pointsScored += 1
                print(f"Correct! you have scored {pointsScored}0")
                questionsAndAnswers.pop(random_index)
            elif(answer != questionsAndAnswers[random_index]['answer']):
                print(f"Oops Wrong Answer! you have scored {pointsScored}0 points and won ${amountWon}")
                break  
        if(pointsScored == maxQuestions):
         print(f"Congratulations Dude You have won the quiz and won ${amountWon} amount of cash enjoy!")        
    except ValueError:
      print('Oops! Something Went Wrong Nigga Screw You!')   
    

displayQuestion(pointsScored,amountWon)    


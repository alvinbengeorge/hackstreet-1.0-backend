from pprint import pprint
import nltk
nltk.download('stopwords')
from Questgen import main

answer = main.AnswerPredictor()
payload3 = {
    "input_text" : '''Sachin Ramesh Tendulkar is a former international cricketer from 
              India and a former captain of the Indian national team. He is widely regarded 
              as one of the greatest batsmen in the history of cricket. He is the highest
               run scorer of all time in International cricket.''',
    "input_question" : "Who is Sachin tendulkar ? "
    
}
output = answer.predict_answer(payload3)

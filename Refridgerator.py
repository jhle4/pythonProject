from datetime import datetime, date
from word2number import w2n

class FoodItem:
    """
    Food item that has attributes that will help with logging how much of an item there is and its current expiration.

    Attributes:
        Current Date : Based on entered, or based on system time.
        Expiration Date : Based on web-scraping, or entered
        Amount : amount with varying units in oz, gram, ml, and item count.
        Mocronutrients : shows grams of carbs, protein, and fat in item.

    Methods:
        number_converter : changes words to numbers
    """


    def __init__(self, cdate=date.today(), edate=None, amount=None, macro=None):
        self._current_date = cdate
        if edate is None:
            self._expiration_date = None
        else:
            self._expiration_date = edate
        self._amount = amount
        macro = 

    def number_finalizer(self, input_words):
        if type(input_words) is str:
            return w2n.word_to_num(input_words)
        elif type(input_words) is int:
            return w2n.word_to_num(input_words)
        return input_words




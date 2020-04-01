from random_word import RandomWords
import numpy as np 
from nltk.corpus import stopwords

if __name__ == '__main__':
    stops = set(stopwords.words('english'))
    err = 'Entered word not valid. Please re-run script.'
    r = RandomWords()
    werds = r.get_random_words(limit = 25)
    werds[12] = 'FREE'
    for i, w in enumerate(werds):
        if w in stops:
            y = raw_input('Enter a word: ')
            if len(y) > 5 and y not in stops:
                werds[i] = y
            else:
                werds = err
    if werds != err:
        werds = np.array(werds).reshape(5,5)
    print(werds)
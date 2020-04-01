from werds import werds
import numpy as np 

if __name__ == '__main__':
    card = np.random.choice(set(werds), size=[5,5], replace=False)
    card[2,2] = 'FREE'
    print(card)
    
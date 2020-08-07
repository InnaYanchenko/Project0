#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
def game_core_binsearch(number):
    #Составим функцию бинарного поиска. 
    #Каждый раз будем делить список поплам и сравнивать
    #загаданное число с серединой списка. Неподходящую часть отбрасываем,
    #а оставшуюся снова делим пополам и т.д., пока не дойдем до нужного числа.
    list=[]
    for i in range(1,101):
        list.append(i)
    low=0
    high=len(list)-1  #Define left(low) ahd right(high) edges of our list
    mid=len(list)//2  #then define middle (mid)
    count = 1
    while list[mid] != number and low<=high:
        count+=1
        if number > list[mid]: 
            low=mid+1
        else:
            high=mid-1
        mid=(low+high)//2
    else:
        return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_binsearch(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_binsearch)


# In[ ]:





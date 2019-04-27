import matplotlib.pyplot as plt
import pandas as pd
from time import time
get_ipython().run_line_magic('matplotlib', 'inline')

def check_speed(function_,limit):
    '''
    args:
        function_(function): to be tested
    return:
        performance(list)
    '''
    performance = []
    n=0
    while n <= limit:
        # worst case (max) where item not found
        t0 = time()*1000 # miliseconds
        y = function_(n)
        print(y)
        t1 = time()*1000 # miliseconds
        t_delta = (t1-t0)
        n +=1
        performance.append((n,t_delta))
    return performance

def plotPerformance(performance,algoName,title):
    try:
        bs = pd.DataFrame(performance)
        bs.columns=['input_size','mseconds']
        fig, ax = plt.subplots()
        _=ax.set_title(title)
        _=ax.plot(bs.input_size,bs['mseconds'],label=algoName,color='blue')
        _=ax.legend()
        _=ax.grid()
        _=ax.set_xlabel('input size')
        _=ax.set_ylabel('mili seconds')
        return True
    except Exception as e:
        print(e)
        return False
  
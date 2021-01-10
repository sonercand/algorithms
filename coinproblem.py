'''
Calculates minimum number of coins needed to make the change
''' 
def min_coins(coins,V):
    '''
    args:
        coins list : list of coins
        V int : Value to make from these coins
    return:
        minimum number of coins
    '''
    min_ = [0 for k in range(V+1)] # array of values -> min number of coins
    
    for k in range(V+1): # loop through values up to V and store min coin required to reach that value
        if k>0:
            minimum = float("inf")
            for coin in coins:
                
                if coin<=k:
                    minimum = min(minimum, 1 + min_[k-coin] ) 
        else: 
            minimum = 0 
         
        min_[k] = minimum
    return min_[k]


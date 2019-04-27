#### Fibonacci Numbers

naive algorithm: Calculates fibonacci numbers fibonacci sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    Function naiveAlgorithm(n):
        if n<=1:
          return n
        else:
          return naiveAlgorithm(n-1) + naiveAlgorithm(n-2)
     
    List Algorithm:
      create an empty list
      fibonacciNumbers = []
      if n = 0:
         f0 = 0 
         append f0 to list
      if n = 1: 
         f1 = 1
         append f1 to list
      for k to n given that n>1:
         fk = fk-1 + f-2
         append fk to list

      return fibonacciNumbers[n]

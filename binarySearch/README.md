# Binary Array Search
Reduces computation complexity (O(n) to O(log n))


                
                 
    search (A,t)
      low = 0
      high = n-1
      while low<= high do
          mid = (low+high)/2
          if t = A[mid] then
              return true
          elseif t<A[mid] then
              high = mid-1
          else 
              low = mid+1
       return false
    end

> This is search for a value in a  sorted list.

Start searching for the value within a list from the middle. 
If search element(t) is equal to the middle element then return middle element. 
If not, then the value is either on the left or on the right. If t is larger than the mid value
then it is on the right, so update low to mid +1 otherwise update high value.
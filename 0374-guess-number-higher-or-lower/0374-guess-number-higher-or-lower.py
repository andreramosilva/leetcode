# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n ==1:
             return 1
        if guess(n) == 0: 
            return n

        first, last = 1, n
        mid = 0 

        while first < last:
            mid = first + ( last - first) //2
            temp = guess(mid)

            if temp == 0:
                return mid
            elif temp == -1:
                last = mid
            else:
                first = mid
        return 0 
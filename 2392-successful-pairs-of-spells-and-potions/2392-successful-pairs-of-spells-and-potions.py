import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = [0] * len(spells)
        #spells.sort()
        potions.sort()
        min_pot = math.floor(math.sqrt(success)) , 0

        for i in range(len(spells)):
            
            min_pot = math.floor(success / spells[i])
            left, right  = 0 , len(potions)
            while left < right:
                mid =  left + ( right - left ) //2
                if spells[i] * potions[mid] >= success:
                    right = mid
                else:
                    left = mid+1
            # for j in range(min_pot, len(potions)):
            #     if spells[i] * potions[j] >= success:
            #         result[i]+=len(potions) -j
            #     else:
            #         break
            result[i] = len(potions)-left
        return result 
        

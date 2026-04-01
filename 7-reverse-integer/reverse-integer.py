class Solution:
    def reverse(self, x: int) -> int:
        new=0
        count=0

        if x<0:
            count= count+1
            x=-x
        while x>0:
            rem = x%10
            new = new*10 + rem
            x=x//10
        
        if count==1:
            new=-new
        if new < -2**31 or new > 2**31 - 1:
            return 0
        return new

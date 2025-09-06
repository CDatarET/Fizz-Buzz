class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1, n+1):
            if(i % 3 == 0 and i % 5 == 0):
                ret.append("FizzBuzz")
                continue
            if(i % 3 == 0):
                ret.append("Fizz")
                continue
            if(i % 5 == 0):
                ret.append("Buzz")
                continue
            ret.append(str(i))
        return(ret)

class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        h1 = self.findHeight(first=red,second=blue)
        h2 = self.findHeight(first=blue,second=red)
        return max(h1,h2)

    def findHeight(self,first,second):
            isFirst = False
            i = 1
            length = 0
            while True:
                if isFirst:
                    if first < i or first == 0 :
                        return length
                    else:
                        first -=  i
                        isFirst = False
                else:
                    if second < i or second == 0:
                        return length
                    else:
                        second -= i
                        isFirst = True
                length+=1      
                i += 1
            return length

    
        
> Function that reverses a string, input is an array of characters s
> must do this by modifying the input array in-place with O(1) extra memory

```
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reversed = ''
        # for i in s:
            # reversed = i + reversed
        s.reverse()
```

> Find 1st unique character in a string
> 
```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        indx = -1
        
        for i in s:
            #print(i)
            if s.count(i) == 1:
               # print(i)
                indx = s.index(i)
               # print(indx)
                return indx
       # print(-1)   
        return indx
```
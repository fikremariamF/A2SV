class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 0
        mylist = []
        l,r = 0 ,0
        while r < len(chars):
            if chars[l] == chars[r]:
                counter += 1
                r += 1
            else:
                mylist.append(chars[l])
                if counter > 1:
                    counter = str(counter)
                    for val in counter:
                        mylist.append(val)
                counter = 0
                l = r
        mylist.append(chars[l])
        if counter > 1:
            counter = str(counter)
            for val in counter:
                mylist.append(val)
        chars[:] = list(mylist)
        print(chars)
        return len(mylist)

        
def oddString(self, words: List[str]) -> str:
        def func(str):
            alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            i = 0
            arr = []
            while i < len(str) and i+1 < len(str):
                a = str[i]
                b = str[i+1]
                arr.append(alpa.index(b) - alpa.index(a))
                i += 1
            return arr
        
        difference = []
        for i in words:
            diff = func(i)
            difference.append(diff)
        k = 0
        while k < len(difference) and k+1 < len(difference):
            if difference[k] == difference[k+1]:
                k += 1
            else:
                index = k+1
                break
        if index == 1 and difference[len(words) - 1] == difference[1]:
            index = 0

        return words[index]
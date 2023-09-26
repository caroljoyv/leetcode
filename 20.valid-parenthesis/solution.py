s = "]"

def find(s):
    dict = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack =[]
    for i in s:
        if i =='(' or i=='{' or i =='[':
            stack.append(i)
        elif i == ')' or i == '}' or i == ']':
            if stack:
                ele = stack.pop()
            else: 
                return False
            if dict[i] != ele:
                print("inside for loop")
                return False
            
    if stack:
        return False
    else:
        return True







print(find(s))
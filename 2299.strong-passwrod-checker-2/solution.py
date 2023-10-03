def has_upper(str):
    return any(char.isupper() for char in str)

def has_lower(str):
    return any(char.islower() for char in str)

def has_digit(str):
    return any(char.isdigit() for char in str)

def has_special(str):
    spe = '!@#$%^&*()'
    return any(char in spe for char in str)

def no_adj(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return False
        
    return True
def main():
    str = "12Caroloe!"
    all = has_upper(str) and has_lower(str) and has_digit(str) and has_special(str)
    other = no_adj(str)
    print(all)
    print()
    print(other)



if __name__ == "__main__":
    main()
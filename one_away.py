str1 = "pale"
str2 = "pals"

str3 = "black"
str4 = "white"

def one_away(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_1 = str_1.lower()
    str_2 = str_2.replace(" ", "")
    str_2 = str_2.lower()
    dict = {}
    for char in str_1:
        if char not in dict.values():
            dict[char] = 1
        else: 
            dict[char] += 1
    for char in str_2:
        if char not in dict.values():
            dict[char] = 1
        else:
            dict[char] -= 1
    count = 0
    for k, v in dict.values():
        if v == 1:
            count += 1
    if count < 1:
        return False
    return True

def one_away2(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_1 = str_1.lower()
    str_2 = str_2.replace(" ", "")
    str_2 = str_2.lower()
    dict = {}
    

print(one_away(str1, str2))
print(one_away(str3, str4))


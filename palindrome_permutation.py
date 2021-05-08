is_palin = "tacocat"
not_palin = "john"

def palin_perm(palin):
    dict = {}
    palin = palin.replace(" ", "")
    palin = palin.lower()
    for l in palin:
        if l not in dict:
            dict[l] = 1
        else: 
            dict[l] += 1
    odd_count = 0
    for k, v in dict.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

print(palin_perm(is_palin))
print(palin_perm(not_palin))

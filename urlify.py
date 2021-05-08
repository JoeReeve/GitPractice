sentance = "My name is John"

def urlify(reg_str):
    reg_str = reg_str.replace(" ", "%20")
    return reg_str

print(urlify(sentance))
from num2words import num2words
# 40c6 * 5c1

def calculate_factorial():
    numfact = 40 * 39 * 38 * 37 * 36 * 35
    numfacc = 6 * 5 * 4 * 3 * 2 * 1
    dreamfact = 5
    dreamfacc = 1
    result = (numfact / numfacc) * (dreamfact / dreamfacc)
    return int(result)

def convert_to_words():
    words = num2words(calculate_factorial()) 
    return words

print(convert_to_words(),calculate_factorial()) 
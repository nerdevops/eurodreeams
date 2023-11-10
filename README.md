# EuroDreams function 40c6 * 5c1 
> This code represent in numbers what's the chance of winning the Eurodreams.

    ![EuroDreams](/img/eurodreams.png)

```python 
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
    words = num2words(calculate_factorial())  # Call the function here
    return words

print(convert_to_words(),calculate_factorial())  # Call the function here
```

1. To run first install the lib
```console
pip install num2words
pip install requirements.txt
```
2. Run the .py file
```console
python3.8 eurodreams.py 
nineteen million, one hundred and ninety-one thousand, nine hundred, 19191900
```
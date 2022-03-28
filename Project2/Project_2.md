# Project 2 #

Create a library that has a function called **product** that will read a file called **numbers.txt**, multiply the numbers and return their product.

There will be three numbers.

Example file:
```
2
4
3
```
Correct Output
```
24
```

## BONUS ##
Create your function so that if there is an unknown quantity of numbers in the file it will still return the correct product.

The program I will use to check your answer is

```Python
from greenProj2 import products

print(product('numbers.txt'))

print(product('numbers2.txt'))
```

### Included Files ###


| File      | Output |
| --- | :----: |
| **numbers.txt**    | **31671**       |
| **numbers2.txt**   | **3277260**        |

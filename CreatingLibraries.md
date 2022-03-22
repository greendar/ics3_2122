# Creating Libraries

We can create a library of functions and classes by putting them in a .py file in the same folder as our program. These can be accessed in several ways.

If our library was named **myLibrary.py** and contained the function
```python
def addTwo(a, b):
  return a + b
```
then it can be accessed by using the code

```python
import myLibrary
```
Notice that the **.py** is not used. To use the function **addTwo** it is called as follows
```python
x = myLibrary.addTwo(3, 4)
```
The above is the safest way to call **addTwo** but it can be called in other ways.

The name of the library can be shortened and then this shortened form can be used to call the function.
```python
import myLibrary as m

x = m.addTwo(3, 4)
```

If no other functions called **addTwo** are being used then it can be imported in either of the following ways
```python
from myLibrary import addTwo
```
or
```python
from myLibrary import *
```
Both of the above allows the user to call **addTwo** directly by name but the user needs to be sure that there is not another **addTwo** function in the scope to avoid *Name Clashing*.
```python
x = addTwo(3, 4)
```

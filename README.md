# Grade 11 Computer Science
*{Code Examples are given in Python}*

## Data Types

- **String** an array of bytes that contains unicode characters

- **Integer** a whole number, positive or negative, without decimals
- **Float** a real number written with a decimal point dividing the integer and fractional parts
- **Boolean** has only two possible values, True or False

## Computer Science Concepts

### New Variable

*Name:* What do we call the thing?

*Type:* What type of data does it contain?

*InitVal:* What is its starting Value

`Algorithm`    Create a variable called **Name** of type **Type** that starts with the value **InitVal**



**Code**
```Python
name = InitVal
```

### Input

*Variable:* Where the answer from the user will be stored.

*Message:* Question being asked of the user.

`Algorithm`    Ask the user **Message** and store the answer in **Variable**


**Code**
```Python
variable = input('Message')
```



### Output
*Message:*  Text to write to uses.

`Algorithm`    Output the text  **Message**

*Code*
```Python
print("Hello World!")
```


### While Loop
*Sentry:*  Variable that will control the loop.


*Initialization Code:*  Code that initializes the sentry.

*Condition:*  Loop repeats if condition is true.

*Change Code:* Code to change sentry so condition can be triggered.

`Algorithm`    Initialize **Sentry** with **Initialization Code** then continue loop as long as **Condition** is true. Inside loop change sentry with **Change Code**.

*Code*
```Python
initializationCode
while(condition):
  changeCode
```
*Example*
```Python
count = 0
while count < 10:
  print(count)
  count += 1
```
## Loops
- **FOR Loop**
- **WHILE Loop**

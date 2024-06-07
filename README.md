### Thursday 6th June 2024 - Python Lesson
python3 activity.py - execute

#### Control Flow
Order in which a program executes code.

print("Hello, welcome to programming.")

a = 10
b = 5
result = a + b

print(f"The result of adding {a} and {b} is {result}")

print("Thank you")


#### Sequential Control Flow
Execution of code statements one after another, in the order they appear in the program.

#### Conditional control flow / Control Flow
Execution of code statements based on some input.

If ("if" is a condition) 

If tomorrow is Saturday
    set the alarm for 7
If tomorrow is Tuesday
    set alarm for 6

#### Boolean Data Types

There are two values - TRUE and FALSE
Works similarly to binary in that there are two options - TRUE or FALSE
Boolean values are used to control the flow of the program.

I_Am_Happy = True

print(I_Am_Happy)

#### Comparison Operators / Relational Operators

Decide the relationship between the operands. Result of comparison is a boolean value (TRUE or FALSE).

x = 5
y = 7
z = 9

print(x > y)

x = 5
y = 7
z = 9

print(x != y) - Not equal to


Rewriting with Boolean logic:

If (condition) tomorrow == Saturday
    set the alarm for 7
If tomorrow == Tuesday
    set alarm for 6

#### If, elif (else/if), else
Simplest form of AI

"If" checks the condition
When true, intended blocks are executed
When false, intended blocks are skipped

elif uses less memory

Statement

today = "Tuesday"

if today == "Monday":
    print("Set an alarm for 5 AM.")
elif today == "Tuesday":
    print("Set an alarm for 6 AM.")
elif today == "Wednesday":
    print("Set alarm for 7 AM.")

Statement

If, elif, else statement:

temperature = 38  <-- the condition

if temperature > 35: 
    print("It's hot outside.")
elif temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is mild.") <-- What is printed when the other conditions aren't met.

#### pass

temperature = 38

if temperature > 35:
   pass ## This lets the program continue on to the next statement. Something needs to go after the condition in an if statement.
elif temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is mild.")

#### Boolean Operators

AND, OR, NOT. Operands needs to be boolean as well.

When AND is used, all conditions must be met for it to be true. If any conditions are false, result is false.

OR means that one of the conditions must be met for the result to be true

NOT means that the condition can't be met to reach a True result

a = True
b = False

result = a or b
print(result)



age = 20
has_permission = True

if age >= 18:
    if has_permission:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("Access denied.")
## Syntax must be indented as above or doesn't work ##

age = 20
has_permission = True

if age >= 18:
    if has_permission: ## - this is a nested if statement
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("Access denied.")
## Syntax must be indented as above or doesn't work ##

## A simpler version ##

if age >=18 and has_permission:
    print("Access granted.")
else:
    print("Access denied.")

#### Ternary operator
Condenses series of code into one line statements.

age = 20
has_permission = True


print("Access granted.") if age >=18 and has_permission else print("Access denied.")

#### Example 

temperature = 30

if temperature > 30:
    message = "It's hot outside."
else:
    message = "It's not hot outside."
print(message)

## convert to ternary operator ##

message = "It's hot outside." if temperature > 30 else "It's not hot outside."

print(message)

#### Match Case

day_number = 3

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"

print(day_name)

#### Activity 

Write a python script
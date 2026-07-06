# Python Decorators — Complete Notes

## 1. What is a Decorator?

A decorator is a function that takes another function, adds some extra behavior to it, and returns a new function — **without modifying the original function's code**.

Think of it as wrapping a gift.

```python
Original Function
        │
        ▼
+----------------+
|   Decorator    |
+----------------+
        │
        ▼
Enhanced Function
```

The original function remains the same, but it gains additional functionality.

---

## 2. Why Do We Need Decorators?

Suppose you have many functions:

```python
login()
logout()
register()
delete_account()
```

Before each function runs, you want to:

- Check if the user is logged in
- Log the function call
- Measure execution time

Without decorators, you'd repeat the same code in every function.

**Decorators let you write that code once and reuse it.**

---

## 3. Functions Are First-Class Objects

Before understanding decorators, you need to know that functions are objects in Python.

```python
def greet():
    print("Hello")
```

You can assign it to another variable:

```python
say_hello = greet

say_hello()
```

**Output:**

```
Hello
```

Notice:

- We didn't copy the function.
- Both variables point to the same function object.

```
greet  ───────────┐
                   │
                   ▼
           Function Object
                   ▲
                   │
say_hello ─────────┘
```

---

## 4. Functions Can Be Passed as Arguments

```python
def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)
```

**Output:**

```
Hello
```

Notice: we passed the function itself, not the result.

✅ Correct:

```python
execute(greet)
```

❌ Wrong:

```python
execute(greet())
```

Because `greet()` executes immediately.

---

## 5. Functions Can Return Functions

```python
def outer():

    def inner():
        print("Hello")

    return inner
```

Now:

```python
func = outer()

func()
```

**Output:**

```
Hello
```

Visual:

```
outer()
   ↓
returns
   ↓
inner
   ↓
func()
   ↓
Hello
```

This ability is what makes decorators possible.

---

## 6. Building Our First Decorator

```python
def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper
```

### Line-by-Line Breakdown

**`def decorator(func):`**
The decorator receives another function as an argument.

**`def wrapper():`**
This is a new function that will wrap the original function.

**`print("Before function")`**
Runs before the original function.

**`func()`**
Executes the function that was passed in.

**`print("After function")`**
Runs after the original function.

**`return wrapper`**
Instead of returning the original function, return the enhanced one.

---

## 7. Using the Decorator Manually

```python
def say_hello():
    print("Hello!")

say_hello = decorator(say_hello)

say_hello()
```

Predict the output before reading.

**Output:**

```
Before function
Hello!
After function
```

What happened?

```
say_hello
   ↓
decorator()
   ↓
wrapper()
   ↓
Before
   ↓
Original Function
   ↓
After
```

---

## 8. The `@` Syntax

Writing

```python
say_hello = decorator(say_hello)
```

every time is tedious. Python provides a shortcut:

```python
@decorator
def say_hello():
    print("Hello!")
```

This is exactly equivalent to:

```python
def say_hello():
    print("Hello!")

say_hello = decorator(say_hello)
```

**Nothing magical happens. The `@` syntax is just syntactic sugar.**

---

## 9. Dry Run

```python
@decorator
def greet():
    print("Welcome")
```

Python internally does:

```
Create greet()
   ↓
Pass greet to decorator
   ↓
Decorator returns wrapper
   ↓
Replace greet with wrapper
```

When you call:

```python
greet()
```

Python actually executes:

```
wrapper()
   ↓
Before
   ↓
Original greet()
   ↓
After
```

**Output:**

```
Before function
Welcome
After function
```

---

## 10. Real Example: Timing a Function

```python
import time

def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print(f"Execution Time: {end - start:.6f} seconds")

    return wrapper
```

Use it:

```python
@timer
def task():
    for _ in range(1000000):
        pass

task()
```

The decorator measures how long `task()` takes.

---

## 11. Decorators with Arguments

Suppose your function has parameters:

```python
def greet(name):
    print(f"Hello {name}")
```

Our previous wrapper won't work because it accepts no arguments. Instead:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper
```

Now:

```python
@decorator
def greet(name):
    print(f"Hello {name}")

greet("Alice")
```

**Output:**

```
Before
Hello Alice
After
```

- `*args` collects positional arguments.
- `**kwargs` collects keyword arguments.

This makes the decorator work with almost any function.

---

## 12. Built-in Decorators

You've already used these.

### `@property`

```python
@property
def brand(self):
    return self.__brand
```

Converts a method into a property.

### `@staticmethod`

```python
@staticmethod
def generalDesc():
    return "Cars are vehicles"
```

No `self`. No `cls`.

### `@classmethod`

```python
@classmethod
def totalCars(cls):
    return cls.count
```

Receives the class instead of the object.

# Python Notes

## 1. Data Types in Python

### Basic Data Types

| Data Type | Description | Example |
|----------|------------|--------|
| `int` | Integer numbers | `x = 10` |
| `float` | Decimal numbers | `y = 3.14` |
| `str` | Text/String | `name = "xyz"` |
| `bool` | True/False | `is_valid = True` |

### Collection Data Types

| Data Type | Description | Example |
|----------|------------|--------|
| `list` | Ordered, mutable | `a = [1, 2, 3]` |
| `tuple` | Ordered, immutable | `b = (1, 2, 3)` |
| `set` | Unordered, unique values | `c = {1, 2, 3}` |
| `dict` | Key-value pairs | `d = {"name": "xyz", "age": 10}` |

### ✅ Example

```python
a = 10
b = 3.5
name = "cpckiit"
bool_value = True

new_list = [1, 2, 3]
new_tuple = (4, 5, 6)
new_set = {1, 2, 3}
new_dict = {"name": "xyz", "age": 10}
```

---

## 2. Loops in Python

### for loop

```python
count = 10
for i in range(count):
    print(i)
```

### while loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Loop Control

```python
new_list=[2,4,6,10,5,14]
for i in list:
    if i % 2 == 0:
        print(i)
        continue
    if i % 2 !=0
        break
```

---

## 3. Functions in Python

### Basic Function

```python
def no_parameter():
    print("function will work without parameter")

no_parameter()
```

### Function with Parameters

```python
def add(a, b):
    return a + b

print(add(3, 4))
```

### Default Argument

```python
def add(a=4, b=3):
    return a + b

print(add(10, 15))
print(add())
```

## 4. File Handling in Python

### Read File

```python
with open("file.txt", "r") as file:
    print(file.read())
```

### Write File

```python
with open("file.txt", "w") as file:
    file.write("python notes")
```

### Append File

```python
with open("file.txt", "a") as file:
    file.write("python notes new line")
```

---


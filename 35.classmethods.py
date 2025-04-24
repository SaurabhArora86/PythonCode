'''
In Python, both class methods and static methods are used to define methods that are not bound to instances of the class, but there are key differences between them:

### 1. **Class Method**
- A class method is bound to the class and not the instance.
- It takes a reference to the class itself as its first argument, which is conventionally named `cls`.
- It can access and modify class-level variables and properties but cannot access instance-specific properties unless they are passed explicitly.
- Defined using the `@classmethod` decorator.

**Syntax:**
```python
class MyClass:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        print(cls.class_variable)
```

**Usage:**
```python
MyClass.class_method()  # Output: Hello
```

### 2. **Static Method**
- A static method does not take any reference to the class or instance as its first argument.
- It behaves like a regular function that belongs to the class's namespace.
- It cannot access or modify class or instance variables directly.
- Defined using the `@staticmethod` decorator.

**Syntax:**
```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")
```

**Usage:**
```python
MyClass.static_method()  # Output: This is a static method
```

### Key Differences:
| Feature             | **Class Method**                                | **Static Method**                               |
|---------------------|-------------------------------------------------|-------------------------------------------------|
| **First argument**   | Takes `cls` (reference to the class)            | No special first argument                       |
| **Access to class** | Can access class variables and modify them      | Cannot access class or instance variables       |
| **Use case**         | Used when you need to modify or access class-level data or perform class-specific operations | Used when you want to have a method within a class but don't need to access the class or instance |
'''


class Company:
    companyName = "Apple"

    def show(self):
        print(f"Company name is {self.companyName} and My name is {self.name}")

# class methods are added with decorator name @classmethod
    @classmethod
    def changeCompany(cls, change):
        cls.companyName = change


e1 = Company()
e1.name = "Saurabh"
e1.show()
e1.changeCompany("Adidas")
print(e1.companyName)
print(Company.companyName)
print("******")
Company.changeCompany("Google")
e1.show()
print(Company.companyName)

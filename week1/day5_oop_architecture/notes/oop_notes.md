## What is OOP?

OOP is a programming style where we create objects that contain:
Data → variables
Behavior → functions

OOP helps in:
- code reusability
- clean structure
- modular development
- easy maintenance

# Core Concepts of OOP

## 1. Class

A class is a blueprint/template for creating objects.

Example:

```python
class Student:
    pass

## 2. Object

An object is a real instance of a class.

Example:

```python
s1 = Student()

## 3. Constructor

A constructor initializes object data automatically.

Syntax:

def __init__(self):

Example:

class Student:
    def __init__(self, name):
        self.name = name

## 4. Methods

Functions inside a class are called methods.

Example:

def display(self):
    print(self.name)

## OOP Principles

Principle	             Meaning
Encapsulation     -  	Hiding data
Abstraction	      -      Showing only important details
Inheritance       -  	Reusing code from another class
Polymorphism	  -      One thing behaving in multiple ways
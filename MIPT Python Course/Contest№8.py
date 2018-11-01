"""MIPT Python Course Contest 8"""
import sys
print('Exercise 1. Factorial')


def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)


print(fac(10))

print('Exercise 2. Recursion depth')


def endless_recursion():
    endless_recursion()

try:
    endless_recursion()
except:
    print("Stack Overflow", sys.getrecursionlimit())


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print('Exercise 3. Fibonacci numbers')


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(7))

print('Exercise 4. Kochs Curve ')

import turtle
turtle.speed('fastest')

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def Koch_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    Koch_Curve(l, n - 1)
    turtle.left(60)
    Koch_Curve(l, n - 1)
    turtle.right(120)
    Koch_Curve(l, n - 1)
    turtle.left(60)
    Koch_Curve(l, n - 1)

Koch_Curve(400, 4)
turtle.reset()

print('Exercise 5. Kochs Snowflake')
turtle.speed('fastest')
Koch_Curve(400, 4)
turtle.right(120)
Koch_Curve(400, 4)
turtle.right(120)
Koch_Curve(400, 4)
turtle.reset()

print('Exercise 6. Minkovskys Curve')
turtle.speed('fastest')

def Minko_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 8
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.left(90)
    Minko_Curve(l, n - 1)
    turtle.right(90)
    Minko_Curve(l, n - 1)

Minko_Curve(3000, 3)
turtle.reset()

print('Exercise 7. Levys Curve')

turtle.speed('fastest')
def Levys_Curve(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 2
    Levys_Curve(l, n-1)
    turtle.right(90)
    Levys_Curve(l, n-1)
    turtle.left(90)
Levys_Curve(2000, 8)
turtle.reset()

print('Exercise 8. Dragons Curve')

print('Exercise 8. Dragons Curve')

import turtle

def Drago_Turn(n):
    turtle.right(45*n)

def Drago_Curve(l, n):

    if n == 0:
        turtle.forward(l)
        return
    Drago_Curve(l, n - 1)
    if n % 2 == 0:
        turtle.right(90)
    else:
        turtle.left(90)
    Drago_Curve(l, n - 1)

Drago_Turn(1)
Drago_Curve(100, 1)
turtle.reset()

print('Exercise 9. Cantor set')


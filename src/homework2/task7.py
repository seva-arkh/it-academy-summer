import math
import os
import random
import re
import sys

# You are given an unordered array consisting of consecutive integers
#[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements.
#You need to find the minimum number of swaps required to sort the array
#in ascending order.
def minimumSwaps(arr):
    length = len(arr)
    swaps = 0
    for i in range (length):
        min = 10
        for el in arr[i:]:
            if el < min:
                min = el
        if arr[i] != min:
            ind = arr.index(min)
            arr[i], arr[ind] = arr[ind], arr[i]
            swaps +=1
    print(arr)
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()


#Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
#to small details like topography. During his last hike he took exactly  steps.
#For every step he took, he noted if it was an uphill, U, or a downhill, D step.
#Gary's hikes start and end at sea level and each step up or down represents a
#unit change in altitude. We define the following terms:
#A mountain is a sequence of consecutive steps above sea level, starting with a
#step up from sea level and ending with a step down to sea level.
#A valley is a sequence of consecutive steps below sea level, starting with a
#step down from sea level and ending with a step up to sea level.

def countingValleys(n, s):
    k = 0
    v = 0
    for i in range(n):
        if s[i] == "U":
            k +=1
        else:
            k -=1
        if k == 0 and s[i] == "U":
            v +=1
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


#Alice and Bob each created one problem for HackerRank. A reviewer rates the two
#challenges, awarding points on a scale from 1 to 100 for three categories:
#problem clarity, originality, and difficulty.
#We define the rating for Alice's challenge to be the triplet a=(a[0],a[1],a[2]),
#and the rating for Bob's challenge to be the triplet b=(b[0],b[1],b[2]).
#Your task is to find their comparison points by comparing a[0] with b[0], a[1]
#with b[1], a[2] and  with b[2].
#If a[i]>b[i], then Alice is awarded  point.
#If a[i]<b[i], then Bob is awarded  point.
#If a[i]=b[i], then neither person receives a point.
#Comparison points is the total points a person earned.


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    p1, p2 = 0, 0
    l = len(a)
    for i in range(l):
        if a[i] > b[i]:
            p1 += 1
        elif b[i] > a[i]:
            p2 += 1
    return [p1, p2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#This is the first part of this kata series. Second part is here.

# We want to create a simple interpreter of assembler which will
# support the following instructions:
#
# mov x y - copies y (either a constant value or the content of
# a register) into register x
# inc x - increases the content of the register x by one
# dec x - decreases the content of the register x by one
# jnz x y - jumps to an instruction y steps away (positive means forward,
# negative means backward, y can be a register or a constant), but only if x
# (a constant or a register) is not zero
# Register names are alphabetical (letters only). Constants are always integers
# (positive or negative).
#
# Note: the jnz instruction moves relative to itself. For example, an offset of
# -1 would continue at the previous instruction, while an offset of 2 would skip
# over the next instruction.
#
# The function will take an input list with the sequence of the program
# instructions and will execute them. The program ends when there are no more
# instructions to execute, then it returns a dictionary with the contents of the
# registers.
#
# Also, every inc/dec/jnz on a register will always be preceeded by a mov on the
# register first, so you don't need to worry about uninitialized registers.



def jnz(prog, a, f):
    num = '-0123456789'
    while f[a]:
        for el in prog:
            p = el.split()
            if p[0] == 'mov':
                if p[2][0] in num:
                    f[p[1]] = int(p[2])
                else:
                    f[p[1]] = f[p[2]]


            elif p[0] == 'dec':
                f[p[1]] -= 1


            elif p[0] == 'inc':
                f[p[1]] += 1


            elif p[0] == 'jnz':
                ind = prog.index(el)
                if p[2][0] == '-':
                    jnz(prog[ind + int(p[2]):ind], p[1], f)
                elif p[1][0] in num:
                    if int(p[1]):
                        for n in range(1, int(p[2])):
                            try:
                                prog.pop(ind + n)
                            except:
                                break
                else:
                    if f[p[1]]:
                        for n in range(1, int(p[2])):
                            try:
                                prog.pop(ind + n)
                            except:
                                break


def simple_assembler(program):

  num = '-0123456789'
  f = {}
  for el in program:
    p = el.split()
    if p[0] == 'mov':
        if p[2][0] in num:
            f[p[1]] = int(p[2])
        else:
            f[p[1]] = f[p[2]]


    elif p[0] == 'dec':
        f[p[1]] -= 1


    elif p[0] == 'inc':
        f[p[1]] += 1


    elif p[0] == 'jnz':
        ind = program.index(el)
        if p[2][0] == '-':
            jnz(program[ind + int(p[2]):ind], p[1], f)
        elif p[1][0] in num:
            if int(p[1]):
                for n in range(1, int(p[2])):
                    try:
                        program.pop(ind + n)
                    except:
                        break
        else:
            if f[p[1]]:
                for n in range(1, int(p[2])):
                    try:
                        program.pop(ind + n)
                    except:
                        break


  return f

# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function
# represents the right operand
# Divison should be integer division. For example, this should return 2,
# not 2.666666...:

def op(a,b,c):
    f = 0
    if b=='+':
        f= a+c
    elif b=='-':
        f= a-c
    elif b=='*':
        f= a*c
    elif b=='//':
        f= a//c
    return f


def zero(*args): #your code here
    c = 0
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def one(*args): #your code here
    c = 1
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def two(*args): #your code here
    c = 2
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def three(*args): #your code here
    c = 3
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def four(*args): #your code here
    c = 4
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def five(*args): #your code here
    c = 5
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def six(*args): #your code here
    c = 6
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def seven(*args): #your code here
    c = 7
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def eight(*args): #your code here
    c = 8
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c
def nine(*args): #your code here
    c = 9
    if len(args):
        c = op(c, args[0][0], args[0][1])
    return c

def plus(a): #your code here
    return '+', a
def minus(a): #your code here
    return '-', a
def times(a): #your code here
    return '*', a
def divided_by(a): #your code here
    return '//', a

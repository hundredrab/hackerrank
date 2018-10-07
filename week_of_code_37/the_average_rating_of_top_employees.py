#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    ans = 0
    c = 0
    for i in rating:
        if i>=90:
            ans+=i
            c+=1
    
    print("%.2f" % (ans/c))
        

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)

# reverse an array starting with the element after index m 

from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    arr[m+1:] = arr[m+1:][::-1] # set m+1 index till end of array to its reverse
    return arr
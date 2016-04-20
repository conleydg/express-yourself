import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import re

def binary(value):
    return re.match(r'0|1+', value)

def binary_even(value):
    return re.search(r'0$', value)

def hex(value):
    return re.match(r'^[\dA-F]+$', value)

def word(value):
    return re.match(r'^[\w-]+[a-z]+$', value, re.IGNORECASE)

def words(value, count=20):
    space_seperated = re.findall(r'[\S]+', value, re.IGNORECASE)
    words_list = re.findall(r'[\w-]+[a-z]+', value, re.IGNORECASE)
    if count == 20:
        if len(words_list) > 0 and len(words_list) == len(space_seperated):
            return True
        else:
            return False
    else:
        if count == len(words_list):
            return True
        else:
            return False

def phone_number(value):
    number = re.findall(r'[\d]', value)
    if len(number) == 10:
        return True

def money(value):
    return re.match(r'\$[\d]+(\,\d\d\d)*\.?(\d\d)?$', value)

def zipcode(value):
    return re.match(r'[\d]{5}(-\d\d\d\d)?$', value)

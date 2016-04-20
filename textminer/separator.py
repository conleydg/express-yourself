import re


def words(string):
    word_string = re.findall(r'[\w-]+[a-z]+', string, re.IGNORECASE)
    if len(word_string) == 0:
        return None
    return word_string


def phone_number(string):
    if re.match(r'^[\D]?[\d]{3}[\D]?[\D]?[\d]{3}[\D]?[\d]{4}?$', string):
        is_nums = re.findall(r'\d', string)
        is_nums.insert(6, '-')
        just_numbers = ''.join(is_nums)
        area_code = just_numbers[0:3]
        number = just_numbers[3:11]
        return({"area_code": (area_code), "number": (number)})
    else:
        return None

phone_number("(919) 555-1212")


def money(value):
    is_money = re.match(r'\$[\d]+(\,\d\d\d)*\.?(\d\d)?$', value)
    if is_money:
        is_money = is_money.group()
        currency = is_money[0]
        amount = is_money[1:]
        amount = re.findall(r'[\d.]', amount)
        amount = ''.join(amount)
        amount = (float(amount))
        return({"currency": currency, "amount": amount})
    else:
        return None


def zipcode(value):
    is_zip = re.match(r'[\d]{5}(-\d\d\d\d)?$', value)
    if is_zip:
        is_zip = is_zip.group()
        zipc = is_zip[0:5]
        plus4 = is_zip[6:]
        if len(plus4) == 0:
            plus4 = None
        return({"zip": zipc, "plus4": plus4})
    else:
        return None

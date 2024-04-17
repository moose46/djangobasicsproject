from django import template
from num2words import num2words

register = template.Library()


def first_five_upper(value):
    return value[:5].upper()


def first_n_upper(value, n):
    return value[:n].upper()


def length_limit(value, limit):
    if len(value) > limit:
        return value[0:limit] + "...."
    else:
        return value


def rating(value):
    if float(value) >= 4:
        return f"{value}[Excellent]"
    elif float(value) >= 3:
        return f"{value}[Very Good]"
    elif float(value) >= 1.5:
        return f"{value}[Average]"
    else:
        return f"{value}[Poor]"


def convertnumbertowords(value):
    return num2words(value)


register.filter("firstfiveupper", filter_func=first_five_upper)
register.filter("firstnupper", filter_func=first_n_upper)
register.filter("lengthlimit", filter_func=length_limit)
register.filter("rating", filter_func=rating)
register.filter("convertnumbertowords", filter_func=convertnumbertowords)

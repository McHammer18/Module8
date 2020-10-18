"""
Morgan Christensen

Module 8- program that finds a persons half birthday after they sumbit a date

10/17/20
"""


from datetime import datetime, timedelta


def half_birthday(datetime):
    half = datetime + timedelta(days=90)
    return half


if __name__ == '__main__':
    print("Your half birthday is {}.".format(half_birthday()))

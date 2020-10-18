"""
Morgan Christensen

Module 8- program that goes through a dictionary to see if the entry exitsts
and gives back a message

10/17/20
"""


def switch_average(entry):
    my_dict = {'A': 'You Entered an A!',
               'B': 'You Entered an B!',
               'C': 'You Entered an C!',
               'D': 'You Entered an D!',
               'F': 'You Entered an F!'}

    result = my_dict.get(entry, "This is not a valid Grade!")
    return result


if __name__ == '__main__':
    print(switch_average('A'))
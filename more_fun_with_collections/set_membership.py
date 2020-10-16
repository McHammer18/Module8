"""
Morgan Christensen

Module 8 - sets

10/16/20
"""

def in_set(set, int):
    return(int in set)


if __name__ == '__main__':
    my_set = {1, 4, 3, 6, 8, 1, 3, 9}
    print(in_set(my_set, 6))
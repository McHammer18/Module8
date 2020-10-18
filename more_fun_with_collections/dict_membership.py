"""
Morgan Christensen

Module 8 - dictionaries
program checks a dictionary for the key value given

10/16/20
"""
MIN = 0
MAX = 100

def in_dict(dict, key):
    return(key in dict)


def get_test_scores():
    scores_dict = dict()
    try:
        num_score = int(input("How many scores will you be entering? "))
        if MIN > num_score:
            raise ValueError
    except ValueError:
        raise ValueError


    for num in range(num_score):
        flag = False
        while not flag:
            try:
                score = float(input("Test Score {}: ".format(num + 1)))
                if MIN <= score <= MAX:
                    scores_dict.update({str(num + 1): score})
                    flag = True
                else:
                    raise ValueError
            except ValueError:
                print("Enter a valid score between {} and {}".format(MIN, MAX))

    return scores_dict


def average_scores(scores_dict):
    total = 0
    for key in scores_dict:
        total += scores_dict[key]
    average = total/len(scores_dict)
    return average

if __name__ == '__main__':
    try:
        my_scores = get_test_scores()
        print(my_scores)
        print(average_scores(my_scores))
    except ValueError:
        print("Enter an integer")
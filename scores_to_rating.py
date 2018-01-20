def convert_to_numeric(score):
    """
    Covert score to a numerical type.
    """
    converted_score = float(score)
    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    sum = #add them together and take away the max and min
    return sum

def score_to_rating_string(score):
    """
    Convert the average score, which should be between 0 and 5,
    into a string rating.
    """
    rating =
    return rating

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the middle three of the five
    scores and assigning this average to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    # STEP 4 trun average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

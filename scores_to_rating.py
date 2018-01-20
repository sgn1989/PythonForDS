def scores_to_rating(score1, score2, score3, score4, score5):
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

    # STEP 2 find middle three scores
    #how am I going to do this?

    # STEP 3 take average of middle three scores
    average_score = # (sum of the middle scores)/3

    # STEP 4 trun average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

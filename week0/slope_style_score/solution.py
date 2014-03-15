# returns a score formed in the following way:
# remove a min and a max score from 'scores',
# take the average from the rest
def slope_style_score(scores):
    score = scores
    score.remove(min(score))
    score.remove(max(score))
    score = int(sum(score) / len(score) * 100)

    return score / 100
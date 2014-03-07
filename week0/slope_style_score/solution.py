# returns a score formed in the following way:
# remove a min and a max score from 'scores',
# take the average from the rest
def slope_style_score(scores):
	score = scores
	score.remove(min(score))
	score.remove(max(score))
	score = int(sum(score) / len(score) * 100)

	return score / 100

def main():
	print(slope_style_score([94, 95, 95, 95, 90]))
	print(slope_style_score([60, 70, 80, 90, 100]))
	print(slope_style_score([96, 95.5, 93, 89, 92]))

if __name__ == '__main__':
	main()
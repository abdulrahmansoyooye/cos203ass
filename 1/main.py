from grade_utils import score_to_grade
from grade_utils import is_valid_score
input_count=0
total_scores = []
while input_count < 5:
   score = int(input(f"Enter your score {input_count + 1}: " ))
   total_scores.append(score)
   input_count = input_count + 1

for score in total_scores:
   if(is_valid_score(score) is True):
    print(score_to_grade(score))
   else:
     print("Enter a score between (0-100)")
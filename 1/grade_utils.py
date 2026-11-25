def score_to_grade(score):
   
    if(score >70):
        return "A"
    elif(score >60):
        return "B"
    elif(score > 50):
        return "C"
    elif(score >40):
        return "D"
    else:
        return "F"
def is_valid_score(score):
     if(score > 100 or score < 0):
        return False
     else:
         return True
     
def grade_to_point(grade):
    
    if(grade == "A"):
        return 5
    elif(grade == "B"):
        return 4
    elif(grade == "C"):
        return 3
    elif(grade == "D"):
        return 2
    elif(grade == "F"):
        return 0
    else:
        return "Invalid grade"
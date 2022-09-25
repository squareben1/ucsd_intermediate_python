
def check_password(string):
    score = 0
    if len(string) >= 8:
        score += 1
    
    return score
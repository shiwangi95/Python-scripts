def print_details(name,age,scorecard):
    print("Name is: {} \nAge is: {} \nScorecard: {}".format(name,age,scorecard))

def result(scorecard):
    if min(scorecard) >= 33:
        return "Pass"
    return "Fail"
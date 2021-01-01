def check(D,Table, NoL):
    if NoL == "L":
        if Table in D:
            return True 
    return False

def adder(D,Table,N):
    Sum = D[Table]["S"] + N
    # Checker
    if Sum > D[Table]["R"]:
        return False
    return Sum

def subtracter(D,Table,N):
    Sum = D[Table]["S"] - N
    # Checker
    return Sum

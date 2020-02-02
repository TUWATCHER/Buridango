def tickets(people):
    cash = 0
    for i in people:
        if i == 25:
            cash += 25
            continue
        else:
            cash = cash - i
            if cash >= 0:
                continue
            else:
                return "NO"



    return "YES"


stack = [25,50,25,50,25,25,25,100,100]

print(tickets(stack))
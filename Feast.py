def feast(beast, dish):
    # your code here
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False

beast = "brown bear"
dish = "bear claw"

print(feast(beast, dish))

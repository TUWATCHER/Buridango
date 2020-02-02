import heapq

def how_much_i_love_you(nb_petals):
    lovemeter = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]

    if nb_petals < 6:
        return lovemeter[nb_petals - 1]
    elif nb_petals == 6:
        return lovemeter[5]
    else:
        return lovemeter[nb_petals % 6 - 1]

print(how_much_i_love_you(30))

print(3 % 6)
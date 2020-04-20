import random, string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def randomemail():
    return randomword(8) + '@' + randomword(5) + '.' + randomword(3)

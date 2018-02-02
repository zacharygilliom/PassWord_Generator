import random


strength = input("Would you like the password to be strong or weak?\n")


def get_random_number():
    c = random.randrange(1000000, 9999999)
    str(c)
    return c


def get_random_symbol():
    str_list = []
    for x in range(0, 5):
        d = random.choice('!@#$%^&*')
        str_list.append(d)
        h = ''.join(str_list)
    return h


def shuffle_characters(x, y, w):
    z = str(x) + str(y) + str(w)
    a = list(z)
    random.shuffle(a)
    result = ''.join(a)
    return result


def get_random_letters():
    words = ['cat', 'dog', 'penny', 'beef', 'gate', 'washer', 'elephant']
    rand_word = random.choice(words)
    return rand_word


if strength.lower() == "strong":
    e = get_random_number()
    f = get_random_symbol()
    h = get_random_letters()
    g = shuffle_characters(e, f, h)
    print("Your new password is " + g)


if strength.lower() == "weak":
    e = get_random_number()
    h = get_random_letters()
    g = str(e) + str(h)
    print("Your new password is " + g)

def prime(num):
    num_find = False
    if num <= 1:
        return False
    i = 2
    while not num_find:
        if i >= num:
            num_find = True
            return True
        elif num % i == 0:
            return False
        else:
            i += 1

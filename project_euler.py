def is_a_multiple(num_to_test):
    for divisor in range(1, 21):
        if num_to_test % divisor != 0:
            return False
    return True

is_found = False
num_to_test = 0

while not is_found:
    num_to_test += 1
    is_found = is_a_multiple(num_to_test)

print(num_to_test)

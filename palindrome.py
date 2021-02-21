import time

def is_palindrome(input_number):
    """ This method checks if the given number is a palindrome or not """
    input_number_in_str = str(input_number)
    midpoint_position = (len(input_number_in_str) / 2) - 1
    for position in range(0, len(input_number_in_str)):
        if input_number_in_str[position] != input_number_in_str[-(position+1)]:
            return False
        if position >= midpoint_position:
            break
    return True

if __name__ == "__main__":
    start_time = time.time()
    high_result = max([num_1 * num_2 for num_1 in range(999, 100, -1)
                                     for num_2 in range(999, 100, -1)
                                     if is_palindrome(num_1 * num_2)])
    print(high_result)
    print("--- %s seconds ---" % (time.time() - start_time))

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

def get_reversed_number(input_number):
    "This method returns a reversed equivalent of a given number"
    input_number_in_str = str(input_number)
    return int(input_number_in_str[::-1])

if __name__ == "__main__":
    start_time = time.time()
    input_number = 47358
    reversed_input_number = get_reversed_number(input_number)
    output_number = input_number + reversed_input_number

    while not is_palindrome(output_number):
        input_number = output_number
        reversed_input_number = get_reversed_number(input_number)
        output_number = input_number + reversed_input_number

    print(output_number)
    print("--- %s seconds ---" % (time.time() - start_time))

#! /usr/bin/env python3

def getTime(input_string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    time = 0

    for current_char in input_string:
        # Find the position of the character relative to the 
        # current alphabet arrangement
        cw_position = alphabet.find(current_char)

        # Re-arrange the alphabet with the current character on position 0
        rearranged_alphabet = (alphabet[cw_position:] 
                               + alphabet[:cw_position])
        
        # String containing the counter clockwise arrangement of the alphabet
        reversed_alphabet = alphabet[0] + alphabet[-1:-26:-1]
        ccw_position = reversed_alphabet.find(current_char)

        # Update the alphabet for the next iteration
        alphabet = rearranged_alphabet

        # Get the shortest time
        time += min(cw_position, ccw_position)

    return time

if __name__ == "__main__":
    print("Total Time:", getTime('DOMINIQUEIANAQUINO'))

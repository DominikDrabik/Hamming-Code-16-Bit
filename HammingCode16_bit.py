from enum import Enum


class Parity(Enum):
    EVEN_PARITY = 0
    UNEVEN_PARITY = 1

def HammingCode_16Bit(parity, Code):

    if(len(str(Code)) != 16):
        return "Wrong Input"

    Code_string = str(Code)
    pos_of_1 = [1,2,4,5,7,9,11,12,14,16]
    pos_of_2 = [1,3,4,6,7,10,11,13,14]
    pos_of_4 = [2,3,4,8,9,10,11,15,16]
    pos_of_8 = [5,6,7,8,9,10,11]
    pos_of_16 = [12,13,14,15,16]

    #Get the sum of each Bit for the parity bits
    parity_bit_1 = sum([int(Code_string[i - 1]) for i in pos_of_1]) % 2
    parity_bit_2 = sum([int(Code_string[i - 1]) for i in pos_of_2]) % 2
    parity_bit_4 = sum([int(Code_string[i - 1]) for i in pos_of_4]) % 2
    parity_bit_8 = sum([int(Code_string[i - 1]) for i in pos_of_8]) % 2
    parity_bit_16 = sum([int(Code_string[i - 1]) for i in pos_of_16]) % 2

    if(parity == Parity.UNEVEN_PARITY):
        bit_1 = "0" if parity_bit_1 else "1"
        bit_2 = "0" if parity_bit_2 else "1"
        bit_4 = "0" if parity_bit_4 else "1"
        bit_8 = "0" if parity_bit_8 else "1"
        bit_16 = "0" if parity_bit_16 else "1"
    elif(parity == Parity.EVEN_PARITY):
        bit_1 = "1" if parity_bit_1 else "0"
        bit_2 = "1" if parity_bit_2 else "0"
        bit_4 = "1" if parity_bit_4 else "0"
        bit_8 = "1" if parity_bit_8 else "0"
        bit_16 = "1" if parity_bit_16 else "0"

    print(bit_1 + bit_2 + Code_string[0] + bit_4 + Code_string[1:4] + bit_8 + Code_string[4:11] + bit_16 + Code_string[11:])
    return bit_1 + bit_2 + Code_string[0] + bit_4 + Code_string[1:4] + bit_8 + Code_string[4:11] + bit_16 + Code_string[11:]


HammingCode_16Bit(Parity.UNEVEN_PARITY ,"0111100100011010")
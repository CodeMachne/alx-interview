#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list of int): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the significant bits of a byte
    mask_1_byte = 0b10000000  # 1st bit is set to 0: 0xxxxxxx
    mask_2_bytes = 0b11100000  # 2nd and 3rd bits are 10: 110xxxxx
    mask_3_bytes = 0b11110000  # 3rd and 4th bits are 10: 1110xxxx
    mask_4_bytes = 0b11111000  # 4th and 5th bits are 10: 11110xxx
    mask_cont_byte = 0b11000000  # Continuation byte: 10xxxxxx

    for byte in data:
        if byte > 255:  # Validate that all data values are 1 byte (8 bits)
            return False

        if num_bytes == 0:
            # Determine how many bytes in the character
            if byte & mask_1_byte == 0b00000000:
                continue  # 1-byte character
            elif byte & mask_2_bytes == 0b11000000:
                num_bytes = 1  # 2-byte character
            elif byte & mask_3_bytes == 0b11100000:
                num_bytes = 2  # 3-byte character
            elif byte & mask_4_bytes == 0b11110000:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid starting byte
        else:
            # Validate continuation byte
            if byte & mask_cont_byte != 0b10000000:
                return False
            num_bytes -= 1

    # If num_bytes is not zero, there are incomplete characters
    return num_bytes == 0


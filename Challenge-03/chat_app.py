import sys

def encode(key, message):
    """Encodes a message using the given key, with improved error handling and clarity.

    Args:
        key: A list of strings representing the encoding key.
        message: The string to encode (UTF-8).

    Returns:
        The encoded string, or "Error" if encoding is not possible.
    """

    encoded = ""
    for char in message:
        found = False
        for i, group in enumerate(key):
            if char.lower() in group:
                index = group.index(char.lower()) + 1  # Adjust for 1-based indexing
                encoded += str(i + 1) * index
                if char.isupper():
                    encoded = "0" + encoded  # Add indicator for uppercase
                found = True
                break
        if not found:
            return "Error"  # Character not found in key
        encoded += "0"  # Add delimiter after each character
    return encoded

def decode(key, encoded):
    """Decodes an encoded message using the given key, with enhanced error handling.

    Args:
        key: A list of strings representing the encoding key.
        encoded: The encoded string to decode.

    Returns:
        The decoded string (UTF-8), or "Error" if decoding is not possible.
    """

    decoded = ""
    i = 0
    while i < len(encoded):
        digit = int(encoded[i])
        if digit == 0:
            i += 1  # Skip delimiter
            continue
        group = key[digit - 1]  # Adjust for 0-based indexing

        # Improved error handling for out-of-bounds indices:
        try:
            index = int(encoded[i + 1 : i + 1 + digit]) - 1  # Adjust for 1-based indexing
            char = group[index]
        except (ValueError, IndexError):
            return "Error"  # Invalid encoding

        if i + 1 + digit < len(encoded) and encoded[i + 1 + digit] == "0":  # Check for uppercase
            char = char.upper()
        decoded += char
        i += digit + 2  # Move to the next character
    return decoded.encode("utf-8").decode("utf-8")  # Ensure UTF-8 decoding

# Read input from file (using command-line argument)
if len(sys.argv) != 2:
    print("Usage: python chat_app.py input.txt")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as file:
    key = file.readline().strip().split(",")
    operation = int(file.readline().strip())
    message = file.readline().strip().encode("utf-8").decode("utf-8")  # Ensure UTF-8 encoding

# Perform encoding or decoding
if operation == 1:
    result = encode(key, message)
elif operation == 2:
    result = decode(key, message)
else:
    print("Invalid operation")
    sys.exit(1)

print(result)

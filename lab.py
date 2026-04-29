# 1. Calculate the length of a string
def calculate_string_length(input_string):
    """Calculate and return the length of a string."""
    return len(input_string)

# 2. Count the number of characters in a string (same as above)
def count_characters(input_string):
    """Count and return the number of characters in a string."""
    return len(input_string)

# 3. Replace all occurrences of first character (except first occurrence) with '$'
def replace_characters(input_string):
    """Replace all occurrences of first character with '$', except the first occurrence."""
    if not input_string:
        return input_string
    
    first_char = input_string[0]
    result = first_char  # Keep first character as is
    
    # Replace all subsequent occurrences of first_char with '$'
    for char in input_string[1:]:
        if char == first_char:
            result += '$'
        else:
            result += char
    
    return result

# 4. Combine two strings with space and swap first two characters of each
def combine_and_swap(str1, str2):
    """Combine two strings with space
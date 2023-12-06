def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    result = 0

    for i in range(len(roman_str)):
        current_value = roman_dict[romn_str[i]]
        next_val = roman_dict[romn_str[i + 1]] if i + 1 < len(romn_str) else 0

        if current_value < next_val:
            result -= current_value
        else:
            result += current_value

    return result

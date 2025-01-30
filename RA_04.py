def to_lowercase(input_string):
    result = ""
    for char in input_string:
        if 'A' <= char <= 'Z':  # Check if the character is an uppercase letter
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # Keep the character as it is
    return result

print(to_lowercase("GWJGWg"))

def are_twins(txt1: str, txt2: str) -> bool:
    lower: bool
    numbers1: bool
    if to_lowercase(txt1[0:3]) == to_lowercase(txt2[0:3]):
        lower = True
    else:
        lower = False
    if (int(txt1[3:]) - int(txt2[3:])) == -1 or (int(txt1[3:]) - int(txt2[3:])) == 1:
        numbers1 = True
    else:
        numbers1 = False
    
    if numbers1 and lower:
        return True
    else:
        return False

print(are_twins('tyw589', 'TYw590'))
    
    
    
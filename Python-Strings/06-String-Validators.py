if __name__ == '__main__':
    s = input()
    
    has_alphanumeric = any(char.isalnum() for char in s)
    has_alphabetical = any(char.isalpha() for char in s)
    has_digits = any(char.isdigit() for char in s)
    has_lowercase = any(char.islower() for char in s)
    has_uppercase = any(char.isupper() for char in s)
    
    

    if has_alphanumeric:
        print("True")
    else:
        print("False")

    if has_alphabetical:
        print("True")
    else:
        print("False")

    if has_digits:
        print("True")
    else:
        print("False")

    if has_lowercase:
        print("True")
    else:
        print("False")
        
    if has_uppercase:
        print("True")
    else:
        print("False")
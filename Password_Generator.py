def generate_password(length):

    if length < 1:
        return "Error: Password length must be minimun 1."
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyx"
    digits = "0123456789"
    punctuation = "!@#$%^&*<>?,./;':=-_()|\"[]{}"
    character_pool = uppercase_letters + lowercase_letters + digits + punctuation

    password = ""
    for _ in range(length):
        random_index = int((id(password) * _) % len(character_pool))
        password += character_pool[random_index]
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
print(f"Your password is: {password}")
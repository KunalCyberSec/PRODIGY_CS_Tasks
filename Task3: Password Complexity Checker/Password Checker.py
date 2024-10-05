import re

# Function to check password strength
def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))  # Special characters include non-alphanumeric symbols
    
    # Scoring system
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback based on the score
    if strength_score == 5:
        return "Strong password! Your password meets all security criteria."
    elif strength_score == 4:
        return "Good password, but it could be stronger by adding special characters or making it longer."
    elif strength_score == 3:
        return "Medium strength password. Consider adding uppercase letters, numbers, or special characters."
    elif strength_score == 2:
        return "Weak password. Try adding a mix of uppercase, lowercase, numbers, and special characters."
    else:
        return "Very weak password. Make sure your password is at least 8 characters long, and includes uppercase, lowercase, numbers, and special characters."

# Main function to interact with the user
def password_strength_tool():
    print("Password Strength Assessment Tool")
    password = input("Enter your password: ")
    
    # Assess the strength of the password
    feedback = assess_password_strength(password)
    
    # Provide feedback to the user
    print("Password Strength:", feedback)

# Run the Password Strength Tool
password_strength_tool()

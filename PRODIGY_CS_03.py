import re

def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate the strength based on the criteria met
    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Provide feedback based on the strength
    if strength == 5:
        feedback = "Very Strong"
    elif strength == 4:
        feedback = "Strong"
    elif strength == 3:
        feedback = "Moderate"
    elif strength == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    return feedback, {
        'Length': length_criteria,
        'Uppercase': uppercase_criteria,
        'Lowercase': lowercase_criteria,
        'Numbers': number_criteria,
        'Special Characters': special_criteria
    }

def main():
    password = input("Enter a password to check its strength: ")
    feedback, criteria_results = check_password_strength(password)
    
    print(f"Password Strength: {feedback}")
    print("Criteria met:")
    for criteria, met in criteria_results.items():
        print(f"{criteria}: {'Yes' if met else 'No'}")

if __name__ == "__main__":
    main()

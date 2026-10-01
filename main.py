
import string
import getpass

def analyze_password(password):

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score == 3:
        strength = "MEDIUM"
    elif score == 4:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, feedback


# Main program
print("=" * 40)
print("     PASSWORD STRENGTH ANALYZER")
print("=" * 40)

password = getpass.getpass("Enter your password: ")

score, strength, feedback = analyze_password(password)

print("\nPassword Strength:", strength)
print("Security Score:", score, "/ 5")

if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("\nYour password meets all basic checks!")

print("\nThank you for using Password Analyzer!")
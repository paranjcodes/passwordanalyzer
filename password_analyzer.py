import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0
    strength_criteria = []

    # Check length of the password
    if len(password) >= 12:
        strength_score += 1
        strength_criteria.append("✔️ Sufficient length (>=12 characters)")
    else:
        strength_criteria.append("❌ Too short (<12 characters)")

    # Check for lowercase characters
    if re.search(r'[a-z]', password):
        strength_score += 1
        strength_criteria.append("✔️ Contains lowercase letters")
    else:
        strength_criteria.append("❌ No lowercase letters")

    # Check for uppercase characters
    if re.search(r'[A-Z]', password):
        strength_score += 1
        strength_criteria.append("✔️ Contains uppercase letters")
    else:
        strength_criteria.append("❌ No uppercase letters")

    # Check for digits
    if re.search(r'\d', password):
        strength_score += 1
        strength_criteria.append("✔️ Contains digits")
    else:
        strength_criteria.append("❌ No digits")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
        strength_criteria.append("✔️ Contains special characters")
    else:
        strength_criteria.append("❌ No special characters")

    # Check for common password patterns
    common_patterns = ['password', '12345', 'qwerty', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        strength_criteria.append("❌ Contains common patterns")
    else:
        strength_score += 1
        strength_criteria.append("✔️ No common patterns")

    # Calculate overall strength
    if strength_score == 6:
        strength = "Very Strong"
    elif strength_score >= 4:
        strength = "Strong"
    elif strength_score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, strength_criteria

def main():
    print("\n--- Password Strength Analyzer ---\n")
    password = input("Enter a password to analyze: ")
    strength, criteria = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("\nAnalysis:")
    for criterion in criteria:
        print(f" - {criterion}")

if __name__ == "__main__":
    main()


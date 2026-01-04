def check_password(password):
    issues = []

    if len(password) < 12:
        issues.append("Password is shorter than 12 characters.")

    if password.lower() == password or password.upper() == password:
        issues.append("Password should mix upper and lower case letters.")

    if not any(char.isdigit() for char in password):
        issues.append("Password should include at least one number.")

    if not any(char in "!@#$%^&*()" for char in password):
        issues.append("Password should include a special character.")

    if issues:
        print("Password needs improvement:")
        for issue in issues:
            print("-", issue)
    else:
        print("Password looks strong.")

if __name__ == "__main__":
    user_password = input("Enter a password to check: ").strip()

    if not user_password:
        print("No password entered. Please try again.")
    else:
        check_password(user_password)

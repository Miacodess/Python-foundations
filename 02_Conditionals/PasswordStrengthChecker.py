"""An exercise to check if some predetermined rules for a passord's length and characters involved
are strictly adhered to"""

# Initialize password length
MIN_LEN = 8
COMMON_PWDS = {"password", "12345678", "qwerty123", "letmein", "iloveyou"}


# define functions for checking
def pwd_checker_strength(password: str) -> str:
    """Make rules for return value; WEAK, MEDIUM or STRONG"""
    if " " in password:
        return "INVALID"
    if password.lower() in COMMON_PWDS:
        return "WEAK"
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_symbol = True

    # For rule base, we award score for each rule followed
    pwd_score = 0
    if len(password) >= MIN_LEN:
        pwd_score = +1
    if has_upper:
        pwd_score += 1
    if has_lower:
        pwd_score += 1
    if has_digit:
        pwd_score += 1
    if has_symbol:
        pwd_score += 1

    if pwd_score == 5:
        return "STRONG"
    elif pwd_score >= 3:
        return "MEDIUM"
    else:
        return "WEAK"


def get_missing_rules(password: str) -> list[str]:
    missing = []
    if len(password) < MIN_LENGTH:
        missing.append(f"at least {MIN_LENGTH} characters")
    if not any(char.isupper() for char in password):
        missing.append("an uppercase letter")
    if not any(char.islower() for char in password):
        missing.append("a lowercase letter")
    if not any(char.isdigit() for char in password):
        missing.append("a digit")
    if not any(not char.isalnum() for char in password):
        missing.append("a symbol")
    return missing


def main() -> None:
    password = input("Enter a password to check: ")
    print(f"Strength: {pwd_checker_strength(password)}")


if __name__ == "__main__":
    main()
missing = get_missing_rules(password)
if missing:
    print("Missing: " + ", ".join(missing))
else:
    print("All rules met!")

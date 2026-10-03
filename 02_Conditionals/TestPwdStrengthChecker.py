from PasswordStrengthChecker import pwd_checker_strength


def test_password_with_space_is_invalid():
    assert pwd_checker_strength("Abcd ef1!") == "INVALID"


def test_common_password_is_weak():
    assert pwd_checker_strength("Password") == "WEAK"


def test_empty_password_is_weak():
    assert pwd_checker_strength("") == "WEAK"


def test_short_lowercase_is_weak():
    assert pwd_checker_strength("abc") == "WEAK"


def test_missing_symbol_is_medium():
    assert pwd_checker_strength("Abcdefg1") == "MEDIUM"


def test_all_rules_met_is_strong():
    assert pwd_checker_strength("Abcdef1!") == "STRONG"


def test_length_boundary():
    assert pwd_checker_strength("Abcde1!") == "MEDIUM"
    assert pwd_checker_strength("Abcdef1!") == "STRONG"

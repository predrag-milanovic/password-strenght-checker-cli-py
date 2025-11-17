import re
import argparse
import getpass
import sys

def check_password_strength(password):
    """
    Returns (score:int, details:dict) where score is 0..6
    Criteria:
      - length: 0 (len<8), 1 (8-11), 2 (>=12)
      - lowercase, uppercase, digit, special: 1 point each
    """
    score = 0
    details = {
        'length': 0,
        'lower': False,
        'upper': False,
        'digit': False,
        'special': False
    }

    if len(password) >= 12:
        details['length'] = 2
        score += 2
    elif len(password) >= 8:
        details['length'] = 1
        score += 1

    if re.search(r'[a-z]', password):
        details['lower'] = True
        score += 1
    if re.search(r'[A-Z]', password):
        details['upper'] = True
        score += 1
    if re.search(r'\d', password):
        details['digit'] = True
        score += 1
    # cover a wide set of common special characters
    if re.search(r'[^\w\s]', password):
        details['special'] = True
        score += 1

    return score, details

def categorize_score(score):
    if score >= 6:
        return 'Very Strong'
    if score == 5:
        return 'Strong'
    if score == 4:
        return 'Medium'
    if score == 3:
        return 'Weak'
    return 'Very Weak'

def feedback(details):
    tips = []
    if details['length'] < 1:
        tips.append('Make the password at least 8 characters long (12+ is better).')
    elif details['length'] == 1:
        tips.append('Consider increasing length to 12+ characters for extra strength.')
    if not details['lower']:
        tips.append('Add lowercase letters.')
    if not details['upper']:
        tips.append('Add uppercase letters.')
    if not details['digit']:
        tips.append('Include digits (0-9).')
    if not details['special']:
        tips.append('Include special characters (e.g. !@#$%^&*).')
    return tips

def main():
    parser = argparse.ArgumentParser(description='Password Strength Checker')
    parser.add_argument('-p', '--password', help='Password to check (avoid using on a shared terminal)')
    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        try:
            password = getpass.getpass('Enter a password: ')
        except (KeyboardInterrupt, EOFError):
            sys.exit('\nAborted.')

    score, details = check_password_strength(password)
    category = categorize_score(score)

    print(f'Password strength: {category}  (score: {score}/6)')
    for tip in feedback(details):
        print('- ' + tip)

if __name__ == '__main__':
    main()
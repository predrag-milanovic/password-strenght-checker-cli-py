import importlib.util
from pathlib import Path


# Load the script by file path (filename contains hyphens so import by path)
module_path = Path(__file__).resolve().parent.parent / 'password-strenght-checker.py'
spec = importlib.util.spec_from_file_location('pwmod', module_path)
pwmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pwmod)


def test_very_strong():
    score, details = pwmod.check_password_strength('Aa1!Aa1!Aa1!')
    assert score >= 5
    assert pwmod.categorize_score(score) in ('Very Strong', 'Strong')


def test_very_weak():
    score, details = pwmod.check_password_strength('abc')
    assert score <= 1
    assert pwmod.categorize_score(score) == 'Very Weak'


def test_medium_expected():
    # 'Abcdef12' -> length >=8 (1), lower (1), upper (1), digit (1) => score 4 -> Medium
    score, details = pwmod.check_password_strength('Abcdef12')
    assert score == 4
    assert pwmod.categorize_score(score) == 'Medium'


def test_feedback_contains_length_tip():
    _, details = pwmod.check_password_strength('abc')
    tips = pwmod.feedback(details)
    assert any('at least 8' in t for t in tips)

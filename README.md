# Password strength checker

A small command-line tool that evaluates password strength using simple heuristics
(length, lowercase, uppercase, digits, special characters) and provides basic
feedback and a categorical rating (Very Weak → Very Strong).

## Quick start

- Run interactively (prompts for a password):

```bash
python password-strenght-checker.py
```

- Or provide the password on the command line (avoid on shared terminals):

```bash
python password-strenght-checker.py -p 'My$ecureP4ssw0rd'
```

## CLI flags

- `-p, --password` : supply the password to evaluate (optional — otherwise the
	tool will prompt securely using `getpass`).

## Running automated tests

This project uses `pytest`. A small test suite is included under `tests/`.

If you use the included virtual environment, run:

```bash
/home/pmubu/password-strenght-checker/.venv/bin/python -m pytest -q
```

Or, with your system Python (after installing pytest):

```bash
python -m pip install --user pytest
python -m pytest -q
```

## Development notes

- The main script file is named `password-strenght-checker.py` (contains a
	hyphen). Tests import it by path to avoid Python module name issues. If you
	prefer importing as a module, consider renaming the file to
	`password_strength_checker.py` and updating the tests accordingly.

## Optional Enhancements

- After evaluating the password, give the user suggestions on how to make it
	stronger, such as adding more characters, including special symbols, or
	avoiding common words.

## Contributing

Contributions are welcome. Please fork the repository and open a pull request
against the `main` branch. Ensure tests pass and add tests for new behavior.

## License

See the [LICENSE](LICENSE) file for details.
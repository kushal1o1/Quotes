# Project Standards for Django

## Code Style
- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python code.
- Use meaningful variable and function names.

## Project Structure
- Organize apps by functionality.
- Use `settings.py` for configuration and environment-specific settings.
- Keep templates and static files organized within their respective app directories.

## Version Control
- Use Git for version control.
- Write clear and concise commit messages.(usually feat,TODO,refactor,fix)

## Testing
- Write unit tests for all critical functionality.
- Use Django's built-in testing framework.
- Ensure tests pass before merging code.

## Security
- Use environment variables for sensitive data (e.g., database credentials, secret keys).
- Regularly update dependencies to patch vulnerabilities.
- Enable Django's built-in security features (e.g., CSRF protection, XSS prevention).

## Documentation
- Document all APIs and endpoints.
- Maintain a `README.md` with setup instructions.
- Use comments to explain complex code logic.


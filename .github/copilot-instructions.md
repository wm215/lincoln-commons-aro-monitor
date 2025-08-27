# Lincoln Commons ARO Monitor

Lincoln Commons ARO Monitor is a Python web scraper designed to monitor Lincoln Commons apartments for ARO (Affordable Rental Opportunity) one-bedroom availability and send notifications when units become available.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Development Setup
- **Python Environment**: Use Python 3.12+ (available: Python 3.12.3)
- **Create virtual environment**: `python3 -m venv venv` -- takes ~3 seconds
- **Activate virtual environment**: `source venv/bin/activate`
- **Install dependencies**: `pip install -r requirements.txt` -- **Network-dependent timing**
  - **In development environment**: May timeout due to network limitations
  - **In GitHub Actions**: Typically completes in 10-30 seconds
  - **NEVER CANCEL**: Set timeout to 120+ seconds for pip installs
- **Alternative for testing**: Use system Python packages when network is limited

### Build and Test Commands
- **NEVER CANCEL**: Package installation may take 60-120 seconds due to network limitations
- **Install all dependencies**: `pip install -r requirements.txt` -- **NEVER CANCEL, may take 2+ minutes**
- **Run tests**: `pytest` -- takes ~2 seconds when tests exist
- **Run linting**: `flake8 .` -- takes ~1 second
- **Format code**: `black .` -- takes ~1 second
- **Alternative validation when network limited**: Use system packages or skip package installation steps

### Project Structure (Expected)
```
lincoln-commons-aro-monitor/
├── .github/
│   ├── workflows/
│   │   └── monitor.yml          # GitHub Actions for scheduled monitoring
│   └── copilot-instructions.md  # This file
├── src/
│   ├── __init__.py
│   ├── scraper.py               # Main scraping logic
│   ├── notifier.py              # Email/notification logic
│   └── config.py                # Configuration management
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   └── test_notifier.py
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
├── .flake8                      # Flake8 configuration
├── pyproject.toml               # Black and other tool configuration
└── README.md                    # Project documentation
```

## Validation and Testing

### Manual Validation Requirements
- **Always test web scraping functionality** after making changes to scraper logic
- **Test apartment availability detection** by running the scraper against known test data
- **Validate notification system** by sending test emails when making notification changes
- **Check GitHub Actions workflow** runs successfully after modifying automation

### Validation Scenarios
**CRITICAL**: Always run these validation scenarios after making changes:

1. **Basic Environment Test** (when network is limited):
   ```bash
   source venv/bin/activate
   python3 -c "print('✓ Python environment works')"
   which python  # Should show venv path when activated
   ```

2. **Basic Scraping Test** (requires network or system packages):
   ```bash
   source venv/bin/activate
   python -c "import requests; import bs4; print('✓ Scraping packages work')"
   ```

3. **Scraper Functionality Test** (when scraper.py exists):
   ```bash
   source venv/bin/activate
   python src/scraper.py --test-mode
   ```

3. **Full Integration Test**:
   ```bash
   source venv/bin/activate
   python src/scraper.py --dry-run  # Should detect apartments without sending notifications
   ```

### Test Data and Mock Scenarios
- **Use `--test-mode`** flag for testing without making real HTTP requests
- **Use `--dry-run`** flag for testing full pipeline without sending notifications
- **Mock apartment listings** should include both available and unavailable units
- **Test email notifications** with a test email address before production use

## Development Workflow

### Adding New Features
1. **Always start with tests**: Create test cases in `tests/` directory first
2. **Follow TDD approach**: Write failing tests, then implement functionality
3. **Run linting early**: `flake8 .` before committing
4. **Format code**: `black .` before committing
5. **Test integration**: Run full validation scenarios

### Code Style and Standards
- **Use Black formatting**: `black .` (line length: 88 characters)
- **Follow Flake8 rules**: `flake8 .` (with default configuration)
- **Type hints recommended**: Use type annotations for functions and methods
- **Docstrings required**: All functions should have docstrings
- **Error handling**: Always handle network errors and parsing exceptions

### GitHub Actions and Automation
- **Scheduled monitoring**: GitHub Actions runs scraper on schedule (typically hourly)
- **Secrets management**: Use GitHub Secrets for email credentials and apartment site credentials
- **Workflow triggers**: Push to main branch triggers validation workflow
- **NEVER CANCEL**: GitHub Actions typically complete in 2-3 minutes

## Environment and Dependencies

### Required Environment Variables
- `EMAIL_FROM`: Sender email address for notifications
- `EMAIL_TO`: Recipient email address for notifications  
- `EMAIL_PASSWORD`: Application password for sender email
- `SMTP_SERVER`: SMTP server (e.g., smtp.gmail.com)
- `SMTP_PORT`: SMTP port (e.g., 587)

### Network Requirements
- **Internet access required**: For scraping apartment websites
- **SMTP access needed**: For sending email notifications
- **Rate limiting awareness**: Implement delays between requests to avoid blocking

### Common Issues and Solutions
- **Network timeouts**: Use `timeout=10` in requests calls
- **HTML parsing errors**: Always check if elements exist before accessing
- **Email delivery issues**: Verify SMTP settings and use application passwords
- **GitHub Actions failures**: Check secrets are properly configured

## Key Files and Locations

### Frequently Accessed Files
- **`src/scraper.py`**: Main scraping logic - modify when changing apartment detection
- **`src/notifier.py`**: Email notification logic - modify when changing notification format
- **`.github/workflows/monitor.yml`**: Automation schedule - modify when changing monitoring frequency
- **`requirements.txt`**: Dependencies - modify when adding new packages

### Configuration Files
- **`.flake8`**: Linting configuration
- **`pyproject.toml`**: Black formatter and other tool configuration
- **`.gitignore`**: Excludes `venv/`, `__pycache__/`, `.env`, `*.log`

## Troubleshooting

### Common Commands for Debugging
- **Check virtual environment**: `which python` (should show venv path)
- **List installed packages**: `pip freeze`
- **Test imports**: `python -c "import requests; import bs4; print('OK')"`
- **Check network connectivity**: Limited in development environment
- **View logs**: Check GitHub Actions logs for scheduled run results

### Performance Notes
- **Virtual environment creation**: ~3 seconds
- **Dependency installation**: **NEVER CANCEL - Can take 60-120 seconds** due to network limitations
- **Linting and formatting**: <2 seconds combined (when tools are available)
- **Test execution**: <5 seconds for typical test suite
- **Full scraper run**: 10-30 seconds depending on apartment site response time

### Network and Environment Limitations
- **Limited internet access** in development environment causes pip timeouts
- **GitHub Actions environment** has full network access for reliable builds
- **Use longer timeouts**: Always set 120+ second timeouts for pip operations
- **Alternative testing**: Use system Python packages when network is restricted

### Before Committing Changes
**ALWAYS run this validation checklist**:

**When network allows (GitHub Actions environment)**:
```bash
source venv/bin/activate
pip install -r requirements.txt       # NEVER CANCEL - up to 120 seconds
black .                               # Format code
flake8 .                             # Check linting  
pytest                               # Run tests
python src/scraper.py --dry-run      # Test scraper functionality
```

**When network is limited (development environment)**:
```bash
source venv/bin/activate
python3 -m py_compile src/*.py       # Basic syntax validation
python tests/test_scraper.py         # Run tests manually  
python src/scraper.py               # Test basic functionality
```

All commands should complete successfully before pushing changes.

## Network Limitations
- **Limited internet access** in development environment
- **Use mock data** for testing when network access is restricted
- **Test with real data** only when necessary and with proper error handling
- **GitHub Actions environment** has full network access for production runs
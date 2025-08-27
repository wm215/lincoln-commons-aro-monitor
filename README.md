# Lincoln Commons ARO Monitor

> **🤖 Copilot-Optimized Repository**: This project is specifically configured for optimal GitHub Copilot development experience. See the [Development with GitHub Copilot](#development-with-github-copilot) section for detailed guidance.

A Python-based monitoring system for tracking ARO (Affordable Rental Opportunity) one-bedroom apartment availability at Lincoln Commons Apartments.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Quick Start for Developers](#quick-start-for-developers)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Development with GitHub Copilot](#development-with-github-copilot)
- [Troubleshooting with Copilot](#troubleshooting-with-copilot)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project automatically monitors the Lincoln Commons apartment website (https://www.lincolncommonapartments.com/floorplans) for available ARO one-bedroom units and sends notifications when units become available.

## Features

- **Automated Scraping**: Periodically checks the Lincoln Commons website for ARO unit availability
- **Notification System**: Sends email or SMS notifications when units become available
- **Scheduled Monitoring**: Runs automatically every hour using GitHub Actions
- **Configurable**: Easy to set up with environment variables for notification preferences

## Setup

### Prerequisites

- Python 3.8 or higher
- Valid email account for notifications (Gmail recommended)
- Optional: Twilio account for SMS notifications

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/wm215/lincoln-commons-aro-monitor.git
   cd lincoln-commons-aro-monitor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   ```bash
   # Email settings
   export EMAIL_ADDRESS="your-email@gmail.com"
   export EMAIL_PASSWORD="your-app-password"
   export NOTIFICATION_EMAIL="recipient@email.com"
   
   # Optional: SMS settings (requires Twilio)
   export TWILIO_ACCOUNT_SID="your-twilio-sid"
   export TWILIO_AUTH_TOKEN="your-twilio-token"
   export TWILIO_PHONE_NUMBER="your-twilio-number"
   export NOTIFICATION_PHONE="recipient-phone-number"
   ```

### Usage

#### Manual Run

```bash
python src/scraper.py
```

#### Automated Monitoring

The scraper runs automatically every hour via GitHub Actions. No manual intervention required once set up.

## Quick Start for Developers

### Local Development with GitHub Copilot

For the best development experience with GitHub Copilot:

```bash
# Quick setup for Copilot-enabled development
git clone https://github.com/wm215/lincoln-commons-aro-monitor.git
cd lincoln-commons-aro-monitor

# Install dependencies (Copilot can help resolve any issues)
pip install -r requirements.txt

# Create local environment file
cp .env.example .env  # Edit with your credentials

# Test the scraper locally
python src/scraper.py
```

**Pro tip**: Use Copilot chat to ask: *"How do I set up email notifications for testing?"* or *"Help me understand the apartment parsing logic"*

## Project Structure

```
lincoln-commons-aro-monitor/
├── src/
│   └── scraper.py          # Main scraping and notification logic
├── .github/
│   └── workflows/
│       └── monitor.yml     # GitHub Actions workflow
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Configuration

### Email Notifications

The system uses SMTP to send email notifications. For Gmail:

1. Enable 2-factor authentication
2. Generate an app password
3. Use the app password as `EMAIL_PASSWORD`

### SMS Notifications (Optional)

To enable SMS notifications:

1. Create a Twilio account
2. Get your Account SID and Auth Token
3. Purchase a Twilio phone number
4. Configure the Twilio environment variables

## Development with GitHub Copilot

This repository is optimized for development with GitHub Copilot. Follow these guidelines to maximize productivity and code quality when contributing to the Lincoln Commons ARO Monitor.

### Setting Up Your Development Environment

1. **Install GitHub Copilot**: Ensure you have GitHub Copilot enabled in your IDE (VS Code, JetBrains, Vim, etc.)

2. **Clone and setup**:
   ```bash
   git clone https://github.com/wm215/lincoln-commons-aro-monitor.git
   cd lincoln-commons-aro-monitor
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** for local development:
   ```bash
   # Copy and customize these variables
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   NOTIFICATION_EMAIL=recipient@email.com
   # Optional Twilio settings...
   ```

### How Copilot Can Assist You

#### 1. **Web Scraping Enhancements**
Copilot excels at helping with BeautifulSoup selectors and parsing logic. Try these prompts:

```python
# Copilot can help you find elements more efficiently
# Type: "Parse apartment data from HTML div with class 'floor-plan'"
def parse_apartment_data(soup):
    # Copilot will suggest something like:
    apartments = soup.find_all('div', class_='floor-plan')
    return [{'name': apt.find('h3').text, 'price': apt.find('.price').text} for apt in apartments]
```

#### 2. **Notification System Extensions**
Ask Copilot to help implement new notification methods:

```python
# Type: "Add Slack webhook notification method"
def send_slack_notification(self, units: List[Dict]) -> bool:
    # Copilot will generate webhook implementation
    pass

# Type: "Add Discord webhook for apartment notifications"
def send_discord_notification(self, units: List[Dict]) -> bool:
    # Copilot will suggest Discord API integration
    pass
```

#### 3. **Error Handling and Resilience**
Copilot is excellent at suggesting robust error handling:

```python
# Type: "Add retry logic with exponential backoff for web requests"
def fetch_with_retry(self, url: str, max_retries: int = 3) -> Optional[str]:
    # Copilot will suggest retry implementation with exponential backoff
    pass
```

#### 4. **Data Processing and Filtering**
Let Copilot help with apartment filtering logic:

```python
# Type: "Filter apartments by price range and availability date"
def filter_apartments(self, apartments: List[Dict], max_price: int, earliest_date: str) -> List[Dict]:
    # Copilot will suggest filtering logic
    pass
```

### Copilot-Optimized Development Workflows

#### **Feature Development Pattern**
1. **Write descriptive comments first** - Copilot works best with clear intent:
   ```python
   # Check if the apartment listing contains ARO units and extract pricing information
   # Look for elements with class 'aro-unit' and parse the monthly rent
   def extract_aro_pricing(self, listing_html: str) -> List[Dict]:
   ```

2. **Use type hints** - Copilot provides better suggestions with strong typing:
   ```python
   from typing import List, Dict, Optional, Union
   
   def process_listings(self, listings: List[Dict[str, Union[str, int]]]) -> Optional[List[Dict]]:
   ```

3. **Break down complex functions** - Copilot excels with focused, single-purpose functions:
   ```python
   # Instead of one large monitoring function, break it down:
   def fetch_listings(self) -> str: pass
   def parse_aro_units(self, html: str) -> List[Dict]: pass
   def filter_available_units(self, units: List[Dict]) -> List[Dict]: pass
   def send_notifications(self, units: List[Dict]) -> bool: pass
   ```

#### **Testing with Copilot**
Copilot can generate comprehensive tests for your monitoring functions:

```python
# Type: "Create unit tests for LincolnCommonsMonitor class"
import unittest
from unittest.mock import Mock, patch

class TestLincolnCommonsMonitor(unittest.TestCase):
    # Copilot will suggest test methods for each function
    pass
```

#### **Configuration Management**
Ask Copilot to help with environment configuration:

```python
# Type: "Create configuration class with validation for email and SMS settings"
class MonitorConfig:
    # Copilot will suggest validation and default handling
    pass
```

### Best Practices for This Repository

1. **Commenting for Copilot**: Write descriptive comments about web scraping intent:
   ```python
   # Navigate to the floor plans page and extract all one-bedroom ARO units
   # Look for availability status and pricing information
   ```

2. **Naming Conventions**: Use descriptive function names that help Copilot understand context:
   ```python
   # Good: extract_available_aro_units()
   # Better: extract_available_one_bedroom_aro_units_with_pricing()
   ```

3. **Domain-Specific Prompts**: Use apartment/real-estate terminology in comments:
   ```python
   # Parse lease terms, security deposits, and move-in availability dates
   # Extract square footage, floor level, and unit amenities
   ```

### Common Copilot Prompts for This Project

- `"Add logging for web scraping failures with retry count"`
- `"Create apartment data model with validation"`
- `"Implement rate limiting for website requests"`
- `"Add email template for different notification types"`
- `"Create utility function to compare apartment availability changes"`
- `"Add configuration validation for required environment variables"`

### Example Copilot Workflows

#### Adding a New Notification Channel
```python
# 1. Start with a descriptive comment - Copilot will understand the context
# Add support for Microsoft Teams webhook notifications for apartment availability

class TeamsNotifier:
    def __init__(self, webhook_url: str):
        # Copilot will suggest initialization code
        pass
    
    def send_notification(self, units: List[Dict]) -> bool:
        # Copilot will generate Teams-specific webhook payload
        pass
```

#### Enhancing Data Parsing
```python
# 2. Ask Copilot to improve existing parsing logic
# Parse additional apartment details including floor number, balcony, and pet policy
def parse_detailed_apartment_info(self, unit_element) -> Dict[str, Any]:
    # Copilot will suggest comprehensive parsing based on the comment
    details = {}
    # Let Copilot complete the parsing logic...
    return details
```

#### Creating Tests
```python
# 3. Generate comprehensive tests
# Create unit tests for apartment availability checking with mock HTML responses
class TestApartmentParsing(unittest.TestCase):
    def setUp(self):
        # Copilot will create realistic test setup
        pass
    
    def test_parse_available_units(self):
        # Copilot will generate test cases with mock data
        pass
```

### Extending the Monitor

When adding new features, let Copilot guide you through the architecture:

1. **New apartment sites**: `"Create generic scraper interface for multiple apartment websites"`
2. **Data persistence**: `"Add SQLite database to track apartment availability history"`
3. **Advanced filtering**: `"Implement apartment filtering by amenities, pet policy, and lease terms"`
4. **Scheduling**: `"Create configurable monitoring schedule with different frequencies"`

## Troubleshooting with Copilot

Use Copilot to help debug common issues:

### Network Issues
```python
# Ask Copilot: "Add network error handling with retry logic for apartment website requests"
def fetch_with_resilience(self, url: str) -> Optional[str]:
    # Copilot will suggest timeout handling, user agent rotation, etc.
    pass
```

### Parsing Issues
```python
# Ask Copilot: "Debug why apartment parsing is not finding ARO units"
def debug_apartment_parsing(self, html_content: str) -> Dict[str, Any]:
    # Copilot will suggest logging and debugging strategies
    pass
```

### Email/SMS Failures
```python
# Ask Copilot: "Add comprehensive error handling for notification failures"
def robust_notification_sender(self, units: List[Dict]) -> Dict[str, bool]:
    # Copilot will suggest fallback mechanisms and error reporting
    pass
```

## Contributing

### Development Workflow

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Set up development environment** (see Copilot setup above)
4. **Write descriptive commits** that help Copilot understand your changes
5. **Use Copilot for code review** - ask it to review your changes for potential issues
6. **Submit a pull request** with clear description of changes

### Code Quality Standards

- **Type hints**: Use type annotations for all function signatures
- **Docstrings**: Include docstrings for all classes and public methods
- **Error handling**: Implement proper exception handling for web requests
- **Logging**: Use structured logging with appropriate levels
- **Testing**: Add tests for new functionality (let Copilot help generate them)

### Pull Request Guidelines

- Include examples of how Copilot helped in your development process
- Document any new configuration options or environment variables
- Update README if you add new features or change setup requirements
- Test notifications with dummy data before submitting

## License

This project is for personal use only. Please respect the terms of service of the Lincoln Commons website.

## Disclaimer

This tool is intended for personal use to monitor apartment availability. Please use responsibly and in accordance with the website's terms of service.

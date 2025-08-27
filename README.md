# Lincoln Commons ARO Monitor

A Python-based monitoring system for tracking ARO (Affordable Rental Opportunity) one-bedroom apartment availability at Lincoln Commons Apartments.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Development with GitHub Copilot](#development-with-github-copilot)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Best Practices for Copilot Development](#best-practices-for-copilot-development)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Quick Start with GitHub Copilot

If you're using GitHub Copilot, follow these steps for the optimal development experience:

1. **Clone and Setup**:
   ```bash
   git clone https://github.com/wm215/lincoln-commons-aro-monitor.git
   cd lincoln-commons-aro-monitor
   pip install -r requirements.txt
   # Optional: Install development tools for better Copilot suggestions
   pip install pytest black flake8 mypy
   ```

2. **Open in VS Code** with GitHub Copilot extension enabled

3. **Explore the codebase** by reading comments and docstrings - Copilot learns from existing patterns

4. **Start coding** with descriptive comments to get relevant suggestions:
   ```python
   # Add new apartment complex monitoring for [site name]
   # Implement price change alerts with email templates
   # Create apartment availability dashboard with Flask
   ```

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

This repository is optimized for use with GitHub Copilot coding agent. Here's how to maximize productivity when contributing to this project.

### Setting Up Your Development Environment

1. **IDE Setup**: Use VS Code with the GitHub Copilot extension for the best experience
2. **Python Environment**: Ensure you have Python 3.8+ and pip installed
3. **Dependencies**: Install all dependencies including optional ones for full Copilot suggestions:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-mock  # For testing support
   pip install black flake8        # For code formatting suggestions
   ```

### How GitHub Copilot Can Help

GitHub Copilot is particularly useful for this project in the following areas:

#### 1. Web Scraping Enhancements
- **CSS Selector Generation**: When modifying `src/scraper.py`, Copilot can suggest CSS selectors for different apartment listing formats
- **Error Handling**: Copilot can suggest robust error handling patterns for network requests and HTML parsing
- **Rate Limiting**: Get suggestions for implementing respectful scraping delays and retry mechanisms

Example Copilot prompts to try:
```python
# Type this comment and let Copilot suggest the implementation:
# Parse apartment listings with rent prices and availability status
```

#### 2. Notification System Improvements
- **Email Templates**: Copilot can help create rich HTML email templates
- **Multi-channel Notifications**: Get suggestions for Discord, Slack, or other notification platforms
- **Notification Scheduling**: Improve notification logic with smart filtering and deduplication

Example:
```python
# Add this comment for Copilot suggestions:
# Send notification only if unit price is below threshold and hasn't been seen before
```

#### 3. Configuration Management
- **Environment Variables**: Copilot can suggest configuration validation and default value patterns
- **Config File Support**: Get suggestions for YAML or JSON configuration file support
- **Secret Management**: Improve security with better credential handling patterns

#### 4. Testing and Reliability
- **Unit Tests**: Copilot excels at generating test cases for scraping logic
- **Mock Data**: Generate realistic apartment listing data for testing
- **Integration Tests**: Create tests for email/SMS notification systems

Example test generation:
```python
# Comment: "Test that apartment scraper handles missing price information gracefully"
# Let Copilot generate the test function
```

#### 5. Data Processing and Analysis
- **Data Structures**: Improve apartment data models with dataclasses or Pydantic
- **Analytics**: Add features like price tracking, availability trends, or notification effectiveness
- **Data Export**: Generate CSV/JSON export functionality for apartment history

### Copilot-Friendly Code Patterns

When working on this project, use these patterns to get better Copilot suggestions:

1. **Descriptive Comments**: Write clear intention comments before complex logic
   ```python
   # Extract apartment name, price, and availability from listing card
   def parse_apartment_card(card_element):
       # Copilot will suggest implementation
   ```

2. **Type Hints**: Use comprehensive type annotations
   ```python
   from typing import List, Dict, Optional, Union
   
   def send_notification(units: List[Dict[str, Union[str, float]]]) -> bool:
       # Copilot provides better suggestions with type context
   ```

3. **Docstrings**: Include detailed docstrings for better context
   ```python
   def monitor_apartments():
       """
       Main monitoring function that:
       1. Fetches apartment listings from Lincoln Commons
       2. Filters for ARO one-bedroom units
       3. Sends notifications for new availability
       4. Logs results for debugging
       """
       # Copilot understands the full context
   ```

### Development Workflow with Copilot

1. **Feature Development**:
   - Start with a clear comment describing what you want to build
   - Let Copilot suggest the implementation structure
   - Refine and customize the suggestions for this specific project

2. **Code Review**:
   - Use Copilot to suggest improvements to existing code
   - Ask for alternative implementations of complex logic
   - Get suggestions for edge case handling

3. **Documentation**:
   - Copilot can help generate comprehensive docstrings
   - Create usage examples and API documentation
   - Generate troubleshooting guides

### Common Copilot Workflows for This Project

#### Adding New Apartment Sites
```python
# Comment: "Create scraper class for [apartment complex name] similar to LincolnCommonsMonitor"
# Copilot will suggest the class structure with appropriate methods
```

#### Enhancing Email Notifications
```python
# Comment: "Create HTML email template with apartment photos and interactive map links"
# Copilot will suggest HTML template and email composition logic
```

#### Adding Price Alerts
```python
# Comment: "Add price threshold filtering to only notify when rent is below maximum budget"
# Copilot will suggest configuration and filtering logic
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes (leverage Copilot suggestions as described above)
4. Ensure your code follows the patterns that work well with Copilot
5. Submit a pull request with clear descriptions for future Copilot context

## Best Practices for Copilot Development

Follow these practices to get the most out of GitHub Copilot when working on this repository:

### Code Organization Best Practices

1. **Modular Functions**: Break complex scraping logic into smaller, well-named functions
   ```python
   # Instead of one large monitor() function, create specific functions:
   def fetch_apartment_listings() -> List[Dict]:
   def filter_aro_units(listings: List[Dict]) -> List[Dict]:
   def check_for_new_availability(current_units: List[Dict]) -> List[Dict]:
   ```

2. **Clear Variable Names**: Use descriptive names that help Copilot understand context
   ```python
   # Good: Copilot understands the data structure
   aro_one_bedroom_units = filter_units_by_type(all_units, "ARO", "1BR")
   
   # Less helpful for Copilot
   units = filter_units(data, "ARO", "1BR")
   ```

3. **Configuration Patterns**: Use standard patterns that Copilot recognizes
   ```python
   # Copilot knows this pattern and can suggest environment variable handling
   @dataclass
   class NotificationConfig:
       email_address: str = os.getenv('EMAIL_ADDRESS', '')
       email_password: str = os.getenv('EMAIL_PASSWORD', '')
       notification_email: str = os.getenv('NOTIFICATION_EMAIL', '')
   ```

### Project-Specific Copilot Tips

#### Web Scraping Improvements
- Use standard CSS selector patterns that Copilot recognizes
- Implement retry logic using well-known libraries like `tenacity`
- Follow BeautifulSoup best practices for robust parsing

#### Notification Enhancements
- Implement template-based notifications for easier customization
- Add rate limiting to prevent spam (Copilot can suggest `ratelimit` library usage)
- Create notification queues for reliable delivery

#### Error Handling and Logging
- Use structured logging with consistent message formats
- Implement comprehensive exception handling for network operations
- Add health check endpoints for monitoring system status

### Copilot Code Generation Examples

Here are some specific prompts that work well with this project:

```python
# Generate apartment data model
# Create a dataclass for apartment listing with price, availability, and unit type

# Implement smart notification filtering  
# Only send notification if apartment hasn't been seen in last 24 hours and price changed

# Add apartment comparison functionality
# Compare current listings with previous run and identify newly available units

# Create backup notification channels
# If email fails, send SMS notification as fallback using Twilio

# Implement apartment favorites system
# Allow users to mark preferred unit types and get priority notifications
```

### Testing with Copilot

Since this project doesn't currently have tests, Copilot can help you add them:

```python
# Generate unit tests for apartment scraper with mock HTTP responses
# Create integration tests for email notification system
# Add property-based tests for data parsing edge cases
```

Copilot excels at generating test data and mock responses for web scraping projects.

## License

This project is for personal use only. Please respect the terms of service of the Lincoln Commons website.

## Disclaimer

This tool is intended for personal use to monitor apartment availability. Please use responsibly and in accordance with the website's terms of service.

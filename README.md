# Lincoln Commons ARO Monitor

A Python-based monitoring system for tracking ARO (Affordable Rental Opportunity) one-bedroom apartment availability at Lincoln Commons Apartments.

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for personal use only. Please respect the terms of service of the Lincoln Commons website.

## Disclaimer

This tool is intended for personal use to monitor apartment availability. Please use responsibly and in accordance with the website's terms of service.

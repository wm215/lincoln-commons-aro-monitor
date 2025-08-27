#!/usr/bin/env python3
"""
Lincoln Commons ARO Monitor
Scrapes the Lincoln Commons website for ARO one-bedroom availability
and sends notifications when units become available.
"""

import os
import sys
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup

# Optional Twilio for SMS
try:
    from twilio.rest import Client
    TWILIO_AVAILABLE = True
except ImportError:
    TWILIO_AVAILABLE = False
    print("Twilio not installed. SMS notifications disabled.")

# Optional dotenv for environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('aro_monitor.log', mode='a')
    ]
)
logger = logging.getLogger(__name__)

class LincolnCommonsMonitor:
    """Monitor Lincoln Commons website for ARO unit availability."""
    
    def __init__(self):
        self.base_url = "https://www.lincolncommonapartments.com/floorplans"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Email configuration
        self.email_address = os.getenv('EMAIL_ADDRESS')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.notification_email = os.getenv('NOTIFICATION_EMAIL')
        
        # SMS configuration (optional)
        self.twilio_client = None
        if TWILIO_AVAILABLE:
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            self.twilio_phone = os.getenv('TWILIO_PHONE_NUMBER')
            self.notification_phone = os.getenv('NOTIFICATION_PHONE')
            
            if account_sid and auth_token:
                self.twilio_client = Client(account_sid, auth_token)

    def fetch_floorplans(self) -> Optional[str]:
        """Fetch the floorplans page content."""
        try:
            logger.info(f"Fetching floorplans from {self.base_url}")
            response = self.session.get(self.base_url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching floorplans: {e}")
            return None

    def parse_aro_units(self, html_content: str) -> List[Dict]:
        """Parse HTML content to find ARO one-bedroom units."""
        soup = BeautifulSoup(html_content, 'html.parser')
        aro_units = []
        
        try:
            # Look for apartment listings
            # This is a placeholder - actual selectors would need to be determined
            # by inspecting the Lincoln Commons website structure
            
            # Common patterns for apartment listing sites:
            listings = soup.find_all(['div', 'article', 'section'], 
                                   class_=lambda x: x and any(term in x.lower() for term in 
                                                            ['apartment', 'unit', 'floorplan', 'listing']))
            
            for listing in listings:
                # Look for ARO and one-bedroom indicators
                text_content = listing.get_text().lower()
                
                if 'aro' in text_content and ('1 bed' in text_content or 'one bed' in text_content):
                    # Extract unit details
                    unit_info = {
                        'type': 'ARO One-Bedroom',
                        'available': 'available' in text_content or 'now' in text_content,
                        'text': listing.get_text().strip()[:200],  # First 200 chars
                        'timestamp': datetime.now().isoformat()
                    }
                    aro_units.append(unit_info)
                    
            logger.info(f"Found {len(aro_units)} ARO one-bedroom units")
            return aro_units
            
        except Exception as e:
            logger.error(f"Error parsing ARO units: {e}")
            return []

    def send_email_notification(self, units: List[Dict]) -> bool:
        """Send email notification about available units."""
        if not all([self.email_address, self.email_password, self.notification_email]):
            logger.warning("Email configuration incomplete. Skipping email notification.")
            return False
            
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = self.notification_email
            msg['Subject'] = f"🏠 ARO Units Available at Lincoln Commons - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            
            body = f"""
Good news! ARO one-bedroom units are available at Lincoln Commons:

{chr(10).join([f"• {unit['type']}: {unit['text'][:100]}..." for unit in units])}

Check the website: {self.base_url}

Time checked: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This is an automated message from Lincoln Commons ARO Monitor.
            """.strip()
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to Gmail SMTP
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.send_message(msg)
            server.quit()
            
            logger.info(f"Email notification sent to {self.notification_email}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email notification: {e}")
            return False

    def send_sms_notification(self, units: List[Dict]) -> bool:
        """Send SMS notification about available units."""
        if not self.twilio_client or not self.twilio_phone or not self.notification_phone:
            logger.warning("SMS configuration incomplete. Skipping SMS notification.")
            return False
            
        try:
            message_body = f"🏠 ARO units available at Lincoln Commons! {len(units)} unit(s) found. Check: {self.base_url}"
            
            message = self.twilio_client.messages.create(
                body=message_body,
                from_=self.twilio_phone,
                to=self.notification_phone
            )
            
            logger.info(f"SMS notification sent to {self.notification_phone}. SID: {message.sid}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending SMS notification: {e}")
            return False

    def monitor(self) -> bool:
        """Main monitoring function."""
        logger.info("Starting Lincoln Commons ARO monitoring check")
        
        # Fetch page content
        html_content = self.fetch_floorplans()
        if not html_content:
            return False
            
        # Parse for ARO units
        aro_units = self.parse_aro_units(html_content)
        
        # Check for available units
        available_units = [unit for unit in aro_units if unit.get('available', False)]
        
        if available_units:
            logger.info(f"🎉 Found {len(available_units)} available ARO one-bedroom units!")
            
            # Send notifications
            email_sent = self.send_email_notification(available_units)
            sms_sent = self.send_sms_notification(available_units)
            
            if email_sent or sms_sent:
                logger.info("Notifications sent successfully")
            else:
                logger.warning("Failed to send notifications")
                
            return True
        else:
            logger.info("No available ARO one-bedroom units found")
            return False


def main():
    """Main entry point."""
    logger.info("=== Lincoln Commons ARO Monitor Started ===")
    
    monitor = LincolnCommonsMonitor()
    
    try:
        success = monitor.monitor()
        logger.info(f"Monitoring completed. Success: {success}")
        
    except KeyboardInterrupt:
        logger.info("Monitoring interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error during monitoring: {e}")
        sys.exit(1)
    
    logger.info("=== Lincoln Commons ARO Monitor Finished ===")


if __name__ == "__main__":
    main()
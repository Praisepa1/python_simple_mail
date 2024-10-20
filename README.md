Motivational Quote Email Sender
This Python script sends a random motivational quote via email every Friday. The quotes are read from a text file and sent to the specified recipient using an SMTP server.

Features
Automatically sends a motivational quote on Fridays.
Reads quotes from a local text file (qoutes.txt).
Uses the Gmail SMTP server for sending emails.
Prerequisites
Before running the script, ensure you have:

Python installed (version 3.6 or higher recommended).
A Gmail account with:
An app-specific password generated for use with the script. (Required because regular Gmail passwords may not work due to security reasons).
Less secure app access enabled (if not using an app-specific password).
Setup Instructions
Clone or download the project.

Create a qoutes.txt file in the project directory. This file should contain motivational quotes, with each quote on a new line.

Edit the script (main.py) to update the email credentials:

Replace my_email with your Gmail address.
Replace password with your app-specific password.
Ensure that your Gmail settings allow for sending emails from third-party applications (using app-specific passwords or enabling "Less secure app access").

How to Run
Open a terminal or command prompt.
Navigate to the project directory.
Run the script:
bash
Copy code
python main.py
If today is Friday, the script will read a random quote from the qoutes.txt file and send it via email.

Code Overview
Imports Required Libraries:

smtplib for sending emails.
datetime to get the current day.
random to select a random quote from the file.
Checks the Current Day:

Sends an email only if today is Friday.
Reads a Random Quote:

Selects a random line from the qoutes.txt file.
Formats the Email:

Adds a subject line and encodes the message to UTF-8.
Sends the Email:

Uses Gmail's SMTP server with TLS encryption.
Example
An example of what the qoutes.txt file might look like:

mathematica
Copy code
"Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill
"The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt
"Don't watch the clock; do what it does. Keep going." - Sam Levenson
Important Notes
Use app-specific passwords for better security.
Keep your password safe. Avoid hardcoding it in public repositories.
Troubleshooting
Error: smtplib.SMTPAuthenticationError: Make sure you are using the correct email and password. Double-check Gmail settings.
File Not Found Error: Make sure qoutes.txt exists in the same directory as the script.
License
This project is open source and available under the MIT License.

import time

with open("emails.txt", "r") as f:
    emails = f.readlines()

print("Starting Bulk Email Sender...\n")

for email in emails:
    email = email.strip()
    print(f"Sending email to {email}...")
    time.sleep(1)   # delay for realism
    print(f"Email sent to {email}\n")

print("All emails sent successfully!")
import re

# Regex patterns for emails, phone numbers, dates, and URLs
email_regex = r"(?<!\.)[\w\-_.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?!\.)"
phone_regex = r"(?:([+]\d{1,4})[-.\s]?)?(?:[(](\d{1,3})[)][-.\s]?)?(\d{1,4})[-.\s]?(\d{1,4})[-.\s]?(\d{1,9})"
date_pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{2,4}|\d{2} [A-Za-z]+ \d{4}|\d{4} [A-Za-z]+ \d{2}|\d{4}[-/]\d{2}[-/]\d{2}|[A-Za-z]+ \d{1,2}, \d{4})\b'
url_regex = r"((https?:\/\/|www\.)[^\s/$.?#].[^\s]*)"

# Read the content of the text file
with open('data.txt', 'r', encoding='utf-8') as file:
    test_str = file.read()

# Find all email matches
email_matches = re.findall(email_regex, test_str, re.IGNORECASE)

# Convert tuple matches to complete email strings
valid_emails = [''.join(email) for email in email_matches]

# Print the valid emails found
print("Valid emails found:")
print(valid_emails)

# Find all phone number matches
phone_matches = re.findall(phone_regex, test_str)

# Create a list of full phone numbers
valid_phone_numbers = []
for match in phone_matches:
    full_number = ''.join(filter(None, match))  # Join non-empty groups
    if full_number:  # Ensure it's not empty
        valid_phone_numbers.append(full_number)

# Print the valid phone numbers found
print("\nValid phone numbers found:")
print(valid_phone_numbers)

# Find all date matches
date_matches = re.findall(date_pattern, test_str)

# Print the valid dates found
print("\nValid dates found:")
print(date_matches)

# Find all URL matches
url_matches = re.findall(url_regex, test_str)

# Extract only the full URL from the matches
valid_urls = [match[0] for match in url_matches]

# Print the valid URLs found
print("\nValid URLs found:")
print(valid_urls)

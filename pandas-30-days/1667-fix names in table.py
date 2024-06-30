
# 1667 Fix Names in a Table

import re
import pandas as pd
# Define the regex pattern
pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'

# Test strings
test_emails = [
    "john_doe@leetcode.com",
    "jane.doe123@leetcode.com",
    "a-very.long-email_address@leetcode.com",
    "invalid-email@leetcode.net",  # Invalid domain
    "1stuser@leetcode.com",        # Invalid prefix
    "user@invalid.com"             # Invalid domain
]

# Validate emails
valid_emails = [email for email in test_emails if re.match(pattern, email)]

print("Valid emails:", valid_emails)

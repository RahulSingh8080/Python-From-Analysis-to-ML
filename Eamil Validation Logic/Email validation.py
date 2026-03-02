    # Email must not be empty 
    # Email must contain a '.' and '@'
    # Email must contain exactly one '@' symbol
    # Email must end with '.com', '.org', or '.net.
    # Email must not be longer than 254 characters
    # Email must start and with a letter or digit
import pandas as pd

# Load CSV
df = pd.read_csv("C:/Users/thaku/OneDrive/Data Scienstist Journey 2026 - To be closed/Phase I (Mar-26 to May-26)/Python/Daily Test Cases/emails.csv")

def validate_email(email):

    # Check if null
    if pd.isna(email):
        return "Email cannot be empty"
    
    # Clean string
    email = str(email).strip()

    if email == "":
        return "Email cannot be empty"
    
    elif not ('.' in email and '@' in email):
        return "Must contain . and @"
    
    elif email.count('@') != 1:
        return "Must contain exactly one @"
    
    elif not email.endswith(('.com', '.org', '.net')):
        return "Must end with .com/.org/.net"
    
    elif len(email) > 254:
        return "Too long (max 254 chars)"
    
    elif not (email[0].isalnum() and email[-1].isalnum()):
        return "Must start & end with letter/digit"
    
    else:
        return "Valid"


# Apply validation to entire column
df["email_status"] = df["email"].apply(validate_email)

# Save output
df.to_csv("validated_emails.csv", index=False)

print("Validation completed successfully.")
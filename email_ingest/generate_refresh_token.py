import os
import google.oauth2.credentials
import google_auth_oauthlib.flow

# This is the scope for reading emails.
# If your application needs to send emails, you might need to change this to
# 'https://www.googleapis.com/auth/gmail.modify'
SCOPES = ['https://mail.google.com/']
CLIENT_SECRETS_FILE = 'credentials.json'

def get_refresh_token():
    """
    Generates a refresh token for the Gmail API by running a local server
    and opening a browser window for user authorization.
    """
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    
    # This will open a browser window for you to authorize the application.
    # After you grant permission, the local server will receive the
    # authorization code and exchange it for a refresh token.
    creds = flow.run_local_server(port=0)

    # The refresh token is part of the credentials object.
    refresh_token = creds.refresh_token
    print("\n✅ Your GMAIL_REFRESH_TOKEN is:\n")
    print(refresh_token)
    print("\nCopy this token and add it to your .env file.")

if __name__ == '__main__':
    # Make sure you have your credentials.json file in the same directory
    # as this script when you run it.
    if not os.path.exists(CLIENT_SECRETS_FILE):
        print(f"Error: '{CLIENT_SECRETS_FILE}' not found in the current directory.")
        print("Please download your OAuth 2.0 client secrets from the Google")
        print("Cloud Console and save the file as 'credentials.json' here.")
    else:
        get_refresh_token() 
from __future__ import print_function
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from config import Config

class master_prompt:
    # Define the Google Docs API scope
    SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

    @staticmethod
    def main():
        print("Starting Google Docs auth flow...")
        creds = None

        # Load existing credentials if available
        if os.path.exists('token.json'):
            print("Found existing token.json")
            creds = Credentials.from_authorized_user_file('token.json', master_prompt.SCOPES)

        # If no valid credentials, start the OAuth browser flow
        if not creds or not creds.valid:
            print("No valid credentials, starting flow...")
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing expired credentials...")
                creds.refresh(Request())
            else:
                print("Running local server for OAuth...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', master_prompt.SCOPES)
                creds = flow.run_local_server(port=0)  # opens browser automatically

            # Save credentials
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
                print("✅ Saved new credentials to token.json")

        print("Building Google Docs service...")
        service = build('docs', 'v1', credentials=creds)

        # Retrieve your document
        print("Fetching document content...")
        DOCUMENT_ID = Config.FLOWCHART_AGENT_MODEL_SPEC
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        # Extract text
        text = ""
        for content in document.get('body', {}).get('content', []):
            if 'paragraph' in content:
                for element in content['paragraph'].get('elements', []):
                    if 'textRun' in element:
                        text += element['textRun']['content']

        print("✅ Document text retrieved successfully.\n")
        return text


if __name__ == "__main__":
    text = master_prompt.main()
    print("Document content:\n")
    print(text)




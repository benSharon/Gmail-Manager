# Gmail API Python CLI Application

## Overview
This is a Python application designed to interact with the Gmail API for various email management tasks. It provides a command-line interface (CLI) to send emails, retrieve email message IDs, and delete emails in bulk. The project uses OAuth2 for authentication and authorization with the Gmail API.

## Features
- **Send Emails:** Send an email by specifying the sender, recipient, subject, and message body.
- **Retrieve Email Message IDs:** Retrieve email message IDs based on a search query.
- **Delete Emails:** Delete emails in bulk based on a search query.

## Files and Structure
The project is structured into four main Python files:

- **`authenticator.py`:**
  - Handles authentication with the Gmail API.
  - Defines the permission scopes needed for the application.
  - Manages the OAuth flow and token storage.

- **`handler.py`:**
  - Contains utility functions to interact with the Gmail API.
  - Functions to create, send, retrieve, and delete email messages.

- **`flow.py`:**
  - Defines the user interaction flows for sending, deleting, and retrieving email messages.
  - Guides the user through the necessary steps for each operation.

- **`main.py`:**
  - The main entry point of the application.
  - Manages the main menu and user interactions.
  - Calls the appropriate functions from `flow.py` based on user input.

## Setup and Installation

1. Install the required dependencies:

   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```
2. Set up Google API credentials:
Follow the instructions [here](https://developers.google.com/gmail/api/quickstart/python#step_1_turn_on_the_api_name)

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Follow the on-screen prompts**:
    - **Main Menu**:
        1. Send message.
        2. Delete message(s).
        3. Get message ID(s) and count.
        4. Exit.

    - **Send Message**:
        - Enter sender email.
        - Enter destination email.
        - Enter subject.
        - Enter message text.

    - **Delete Message(s)**:
        - Enter query (e.g., `from:example@gmail.com` or `subject: <string text>`).
        - Confirm deletion.

    - **Get Message ID(s) and Count**:
        - Enter query (e.g., `from:example@gmail.com` or `subject: <string text>`).

## Notes

- The application saves the user's access and refresh tokens in a `token.json` file for future use.
- If the scopes are modified, delete the `token.json` file and re-authenticate.
- The Gmail API has usage limits and quotas. Ensure your usage complies with Google's policies.

## If token is expired/invalid:
- When running the app, if you get an error saying 'token invalid/expired', delete the token.json file and re-run the app.
- It will then open a new tab in the browser (choose your email):
![image](https://github.com/user-attachments/assets/f069f2ad-c2e9-44f4-bb21-2892a6d29493)
- Click 'continue'.
![image](https://github.com/user-attachments/assets/af1f3e47-5f47-4140-8219-7630eb35c063)
- Click 'continue', again.
![image](https://github.com/user-attachments/assets/8c293d2f-794d-4701-bc9a-710c32c2924d)
- And finally, you should get a black page with the following notification:
![image](https://github.com/user-attachments/assets/81020ba9-d404-436f-b087-2a7ca936044b)

Now you are ready to use the app.

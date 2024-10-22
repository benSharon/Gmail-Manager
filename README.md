# Gmail API Python CLI Application (with argparse)

This project provides a command-line tool for managing Gmail messages, including sending emails, retrieving message IDs, deleting messages in bulk and getting the content of a message ID using the Gmail API.

## Features

- **Send Email**: Send an email by specifying the sender, recipient, subject, and message text.
- **Get Message IDs**: Retrieve the IDs of emails that match a specific query.
- **Delete Messages**: Delete emails in bulk based on a specific query.
- **Get content of Message ID**: Retrieve the content of a message ID.

## Setup

### Prerequisites

- Python 3.6 or higher (preferably latest version).
- Google API credentials and token files.

### Installation

1. Set up your Google API credentials:
   - Follow the steps in [this guide](https://developers.google.com/gmail/api/quickstart/python) to create a `credentials.json` file.
   - Place the `credentials.json` file in the root directory of this project.

2. Run the application using the following command (go to **If token is expired/invalid** section for authentication steps):

```sh
python gmail_cli.py --token /path/to/your/token.json
```

## Usage

### Command-Line Arguments

| Argument                                   | Description                                                                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `-t, --token`                              | Path to your `.json` token file (required).                                                                                                     |
| `-q, --query`                              | Query for retrieving or deleting emails. Example: `'from: someone@example.com'` (functions with both `--get-message-ids` and `delete-messages`) |
| `--get-message-ids`                        | Retrieve the message IDs of emails that match the query.                                                                                        |
| `--delete-messages`                        | Delete emails that match the query.                                                                                                             |
| `--send-message`                           | Send an email. Requires `[SENDER]`, `[DESTINATION]`, `[SUBJECT]`, and `[MESSAGE]` as arguments.                                                 |
| `--get-message-id-content`, `--message-id` | Get the content of an email (`--get-message-id-content`) by providing its `message-id`.                                                         |

`python gmail_cli.py --help` displays the following:
```
usage: python gmail_cli.py [-h] -t TOKEN ([-q QUERY] [--get-message-ids | --delete-messages]) [--send-message [SENDER] [DESTINATION] [SUBJECT] [MESSAGE]]

options:
  -h, --help            show this help message and exit

Token - REQUIRED:
  -t TOKEN, --token TOKEN
                        Enter the path to your .json token file

Query-based operations:
  -q QUERY, --query QUERY
                        Enter query (ex: 'from: <email/name>' or 'subject: <subject string>')
  --get-message-ids     Get message IDs that match the query
  --delete-messages     Deletes message(s)

Send Email:
  --send-message [SENDER] [DESTINATION] [SUBJECT] [MESSAGE]
                        Send an email. Requires sender email, destination email, subject, and message text
                        
Message Content:
  --get-message-id-content
                        Retrieve the content of a message-id
  --message-id MESSAGE_ID
                        Message-id of that mail we want to read

Example of usage:
    python gmail_cli.py --token token.json --get-message-ids --query "from:John"
    python gmail_cli.py --token token.json --get-message-ids --query "subject:Order"
    python gmail_cli.py --token token.json --delete-messages --query "from:John"
    python gmail_cli.py --token token.json --send-message sender@hotmail.com receiver@gmail.com "Example Subject" "This is the message box."
    python gmail_cli.py --token token.json --get-message-id-content --message-id <MESSAGE-ID>
```

### Examples

1. **Send an email**:

```
python gmail_cli.py --token /path/to/your/token.json --send-message your-email@gmail.com recipient-email@gmail.com "Subject" "Message text"
```

2. **Get message IDs**:

```
python gmail_cli.py --token /path/to/your/token.json --get-message-ids --query "from:someone@example.com"
```

3. **Delete messages**:

```python
python gmail_cli.py --token /path/to/your/token.json --delete-messages --query "subject:Important"
```

4. **Get message ID content**:
```
python gmail_cli.py --token /path/to/your/token.json --get-message-id-content --message-id <MESSAGE ID>
```

## Notes

- The Gmail API scopes defined in `authenticator.py` grant full access to your Gmail account, including the ability to delete emails (for more scopes, go to [Apps Script API](https://developers.google.com/identity/protocols/oauth2/scopes)). Be careful when using the `--delete-messages` option.
- The `token.json` file is automatically created after the first authentication and stores your access and refresh tokens. Keep this file secure.

## Acknowledgments

- [Google's Python Quickstart for Gmail API](https://developers.google.com/gmail/api/quickstart/python)
- [Python Code Examples for Gmail API](https://thepythoncode.com/article/use-gmail-api-in-python)
- [Gmail-deleter](https://github.com/marin117/Gmail-deleter/blob/master/src/gmail_deleter.py)


## If token is expired/invalid:
- When running the app, if you get an error saying 'token invalid/expired', delete the token.json file and re-run the app:
```
python gmail_cli.py --token <credentials.json>
```
- It will then open a new tab in the browser (choose your email):
  ![image](https://github.com/user-attachments/assets/3dc1d748-05bb-43c0-b053-1c9db43d8e7b)
- Click 'continue'.
  ![image](https://github.com/user-attachments/assets/9c89bf1f-8024-42d1-88bc-51f7954a87ce)
- Click 'continue', again.
  ![image](https://github.com/user-attachments/assets/28e30826-2e8e-4105-adfe-7b2f583000a4)
- And finally, you should get a black page with the following notification:
  ![image](https://github.com/user-attachments/assets/95e8bb18-ffce-4ec0-afe0-3ba192297f6b)


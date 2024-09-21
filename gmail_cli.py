# refer to:
# https://github.com/marin117/Gmail-deleter/blob/master/src/gmail_deleter.py
# https://thepythoncode.com/article/use-gmail-api-in-python#google_vignette

import argparse

from gmail_manager.authenticator import authenticate
from gmail_manager.flow import (
    send_message_flow,
    get_message_ids_flow,
    delete_message_flow,
    get_message_content_flow
)

EPILOG = """
Example of usage:
    python gmail_cli.py --token token.json --get-message-ids --query "from:John"
    python gmail_cli.py --token token.json --get-message-ids --query "subject:Order"
    python gmail_cli.py --token token.json --delete-messages --query "from:John"
    python gmail_cli.py --token token.json --send-message sender@hotmail.com receiver@gmail.com "Example Subject" "This is the message box."
"""


def main():
    prog = "python gmail_cli.py"
    parser = argparse.ArgumentParser(
        prog=prog,
        formatter_class=argparse.RawTextHelpFormatter,
        usage=f"{prog} [-h] -t TOKEN ([-q QUERY] [--get-message-ids | --delete-messages]) "
        f"[--send-message [SENDER] [DESTINATION] [SUBJECT] [MESSAGE]]",
        description="Command-line tool for managing Gmail messages, "
        "including sending emails, retrieving message IDs, "
        "and deleting messages in bulk using the Gmail API.",
        epilog=EPILOG,
    )

    # Token (required)
    token_group = parser.add_argument_group("Token (REQUIRED)")
    token_group.add_argument(
        "-t",
        "--token",
        help="Enter the path to your .json token file",
        type=str,
        required=True,
    )

    # Group for query-related arguments
    query_group = parser.add_argument_group("Query-based operations")

    # Query (not required by default)
    query_group.add_argument(
        "-q",
        "--query",
        type=str,
        help="Enter query (ex: 'from: <email/name>' or 'subject: <subject string>')\n",
    )

    query_group = query_group.add_mutually_exclusive_group()

    # Get message IDs (in query group)
    query_group.add_argument(
        "--get-message-ids",
        action="store_true",
        help="Get message IDs that match the query",
    )
    # Delete message(s) (in query group)
    query_group.add_argument(
        "--delete-messages", action="store_true", help="Deletes message(s)"
    )

    send_group = parser.add_argument_group("Send Email")
    # Send message
    send_group.add_argument(
        "--send-message",
        help="Send an email. Requires sender email, destination email, subject, and message text",
        nargs=4,
        metavar=("[SENDER]", "[DESTINATION]", "[SUBJECT]", "[MESSAGE]"),
    )

    message_content = parser.add_argument_group("Message Content")
    message_content.add_argument(
        "--get-message-id-content",
        type=str,
        help="Retrieve the content of a message-id"
    )

    args = parser.parse_args()

    service_api = authenticate()

    if (args.get_message_ids or args.delete_messages) and not args.query:
        parser.error("--query is required with --get-message-ids or --delete-messages")

    if args.delete_messages:
        delete_message_flow(service_api, args.query)

    elif args.get_message_ids:
        get_message_ids_flow(service_api, args.query)

    elif args.send_message:
        send_message_flow(service_api, *args.send_message)

    elif args.get_message_id_content:
        get_message_content_flow(service_api, args.get_message_id_content)


if __name__ == "__main__":
    main()

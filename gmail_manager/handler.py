import base64

from email.mime.text import MIMEText
from googleapiclient.errors import HttpError


def create_message(sender, destination, subject, message_text):
    message = MIMEText(message_text)
    message["to"] = destination
    message["from"] = sender
    message["subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}


def send_message(service, message):
    try:
        sent_message = (
            service.users().messages().send(userId="me", body=message).execute()
        )
        print(f'\nMessage ID: {sent_message["id"]}')
    except HttpError as error:
        print(f"\nAn error occurred: {error}")


def get_message_ids(service, query):
    result = service.users().messages().list(userId="me", q=query).execute()
    messages_ids = []

    if "messages" in result:
        messages_ids.extend(result["messages"])

    while "nextPageToken" in result:
        page_token = result["nextPageToken"]
        result = (
            service.users()
            .messages()
            .list(userId="me", q=query, pageToken=page_token)
            .execute()
        )

        if "messages" in result:
            messages_ids.extend(result["messages"])

    return messages_ids


def get_message_content(service, message_id):
    # Get the message
    message = (
        service.users()
        .messages()
        .get(userId="me", id=message_id, format="full")
        .execute()
    )

    # Extract headers
    headers = message["payload"]["headers"]
    subject = next(header["value"] for header in headers if header["name"] == "Subject" or header["name"] == "subject")
    from_email = next(header["value"] for header in headers if header["name"] == "From" or header["name"] == "from")

    # Extract the body of the message
    decoded_body = ""

    # check if message has parts
    if "parts" in message["payload"]:
        parts = message["payload"]["parts"]
        for part in parts:
            if part["mimeType"] == "text/plain":
                body_data = part["body"]["data"]
                decoded_body = base64.urlsafe_b64decode(body_data).decode("utf-8")
                break
            else:
                decoded_body = "No body content found"
    else:
        # if not parts, handle a simple message
        body_data = message["payload"]["body"]["data"]
        decoded_body = base64.urlsafe_b64decode(body_data).decode("utf-8")

    # Display content
    print(f"\nFrom: {from_email}\n")
    print(f"Subject: {subject}\n")
    print(f"Body: {decoded_body}\n")


def delete_messages(service, messages: list):
    # This method deletes a bulk of messages
    # To delete a single message:
    # service.users().messages().delete(userId='me', id=msg['id'])
    return (
        service.users()
        .messages()
        .batchDelete(userId="me", body={"ids": [msg["id"] for msg in messages]})
        .execute()
    )

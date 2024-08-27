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
        print(f'Message Id: {sent_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")


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

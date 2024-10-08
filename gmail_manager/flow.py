import time
import os

from gmail_manager.handler import (
    create_message,
    send_message,
    get_message_ids,
    delete_messages,
    get_message_content,
)


def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


def send_message_flow(service_api, sender, destination, subject, message_text):
    message_to_send = create_message(sender, destination, subject, message_text)
    send_message(service_api, message_to_send)
    time.sleep(1)
    print("\nMessage sent.\n")
    return


def get_message_ids_flow(service_api, query):
    messages = get_message_ids(service_api, query=query)
    if not messages:
        print("\nNo message-ids have been found.\n")
        return
    else:
        print()
        for message in messages:
            print(f"id: {message["id"]}")
        print(
            f'\nNumber of message{'s' if len(messages) > 1 else ''}: {len(messages)}\n'
        )
        return


def get_message_content_flow(service_api, message_id):
    if not message_id:
        print("\nMessage-id not found.\n")
    else:
        get_message_content(service_api, message_id)


def delete_message_flow(service_api, query):
    messages = get_message_ids(service_api, query=query)
    print()
    for message in messages:
        print(f"id: {message["id"]}")
    print(f'\nNumber of message{'s' if len(messages) > 1 else ''}: {len(messages)}\n')

    if len(messages) > 1000:
        print(f'\nNumber of message{'s' if len(messages) > 1 else ''}: {len(messages)}\n')
        messages = messages[:1000]
        print("\nReduced number of message-ids to 1000\n")

    if not messages:
        print("\nNo message-ids have been retrieved.\n")
        return

    delete_choice = input("\nAre you sure you want to delete (yes/no): ")

    wrong_input = True
    while wrong_input:  # Keep prompting till input is either 'yes' or 'no'
        if delete_choice == "yes":
            print(f'Deleting message{'s' if len(messages) > 1 else ''}...')
            delete_messages(service_api, messages)
            time.sleep(3)
            print(f'\nMessage{'s' if len(messages) > 1 else ''} deleted.\n')
            return
        if delete_choice == "no":
            print("\nAborted deletion...\n")
            return
        else:
            delete_choice = input("Wrong input. Answer should be 'yes' or 'no': ")

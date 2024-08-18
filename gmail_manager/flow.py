import time
import os

from gmail_manager.handler import (create_message,
                                   send_message,
                                   get_message_ids,
                                   delete_messages)


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def send_message_flow(service_api, sender, destination, subject, message_text):
    message_to_send = create_message(sender, destination, subject, message_text)
    send_message(service_api, message_to_send)
    time.sleep(1)
    print("Message sent.")
    return


def get_message_ids_flow(service_api, query):
    messages = get_message_ids(service_api, query=query)
    if not messages:
        print('No message-ids have been retrieved.')
        return
    else:
        print(messages)
        print(f'Number of message{'s' if len(messages) > 1 else ''}: {len(messages)}')
        return


def delete_message_flow(service_api, query):
    messages = get_message_ids(service_api, query=query)
    print(messages)
    print(f'Number of message{'s' if len(messages) > 1 else ''}: {len(messages)}')

    if len(messages) > 1000:
        print(f'Number of message{'s' if len(messages) > 1 else ''}: {len(messages)}')
        messages = messages[:1000]
        print('Reduced number of message-ids to 1000')

    if not messages:
        print('No message-ids have been retrieved.')
        return

    delete_choice = input('Are you sure you want to delete (yes/no): ')

    wrong_input = True
    while wrong_input:  # Keep prompting till input is either 'yes' or 'no'
        if delete_choice == 'yes':
            print(f'Deleting message{'s' if len(messages) > 1 else ''}...')
            delete_messages(service_api, messages)
            time.sleep(3)
            print(f'Message{'s' if len(messages) > 1 else ''} deleted.')
            return
        elif delete_choice == 'no':
            print('Aborted deletion...')
            return
        else:
            delete_choice = input('Wrong input. Answer should be \'yes\' or \'no\': ')

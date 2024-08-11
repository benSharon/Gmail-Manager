import time
import os
from handler import (create_message,
                     send_message,
                     get_message_ids,
                     delete_messages)


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def flow_section(flow_task):
    def decorator(func):
        def wrapper(*args, **kwargs):
            clean_screen()
            print(f'{flow_task}:')
            print('=' * len(flow_task))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@flow_section('SEND_MESSAGE')
def send_message_flow(service_api):
    sender = input('Enter sender email: ')
    destination = input('Enter destination email: ')
    subject = input('Enter subject: ')
    message_text = input('Enter message text: ')
    message_to_send = create_message(sender, destination, subject, message_text)
    send_message(service_api, message_to_send)
    time.sleep(1)
    print("Message sent.")
    input('Press \'Enter\' to get back to the main menu...')
    return


@flow_section('DELETE_MESSAGE')
def delete_message_flow(service_api):
    query = input('Enter query (ex: \'from: <email/name>\' or \'subject: <subject string>\') \n'
                  'or type \'back\' to go back to main menu: ')

    while query != 'back':
        messages = get_message_ids(service_api, query=query)
        print(messages)
        print(f'Number of messages: {len(messages)}')

        if not messages:
            print('No message-ids have been retrieved.')
            input('Press \'Enter\' to get back to the main menu...')
            return
        # batchDelete maximum is 1000 message-ids

        if len(messages) > 1000:
            messages = messages[:1000]
            print('Reducing number of message-ids to 1000')
        delete_choice = input('Are you sure you want to delete (yes or no): ')

        if delete_choice == 'no':
            print("Deletion aborted...")
            input('Press \'Enter\' to get back to the main menu...')
            return

        if delete_choice == 'yes':
            print('Deleting messages...')
            delete_messages(service_api, messages)
            time.sleep(3)
            print('Messages deleted.')
            input('Press \'Enter\' to get back to the main menu...')
            return

        else:
            print('Aborted message delete.')
            input('Press \'Enter\' to get back to the main menu...')
            return


@flow_section('GET_MESSAGE_IDs')
def get_message_ids_flow(service_api):
    query = input('Enter query (ex: \'from: <email/name>\' or \'subject: <subject string>\') \n'
                  'or type \'back\' to go back to main menu: ')
    while query != 'back':
        messages = get_message_ids(service_api, query=query)
        if not messages:
            print('No message-ids have been retrieved.')
            input('Press \'Enter\' to get back to the main menu...')
            return

        else:
            print(messages)
            print(f'Number of messages: {len(messages)}')
            input('Press \'Enter\' to get back to the main menu...')
            return

# refer to:
# https://github.com/marin117/Gmail-deleter/blob/master/src/gmail_deleter.py
# https://thepythoncode.com/article/use-gmail-api-in-python#google_vignette

import sys
import time

from authenticator import authenticate
from flow import (clean_screen,
                  send_message_flow,
                  get_message_ids_flow,
                  delete_message_flow)


def main():
    service_api = authenticate()

    MAIN_MENU = """
1. Send message.
2. Delete message(s).
3. Get message ID(s) and count.
4. Exit.
"""

    # choice = ''
    while True:
        clean_screen()
        print(MAIN_MENU)
        choice = input('Choose a number: ')

        if choice.strip() == "":
            continue

        elif choice == '1':
            send_message_flow(service_api)

        elif choice == '2':
            delete_message_flow(service_api)

        elif choice == '3':
            get_message_ids_flow(service_api)

        elif choice == '4':
            print("Exiting...")
            time.sleep(1)
            sys.exit()


if __name__ == "__main__":
    main()

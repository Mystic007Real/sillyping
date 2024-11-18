import os
import subprocess
import time
import sys

# Function to print the text with color
def print_with_color(text, color_code):
    color_codes = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'bright_black': '\033[90m',
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'bright_white': '\033[97m'
    }
    # Print the text with the desired color
    print(f"{color_codes.get(color_code, color_codes['reset'])}{text}{color_codes['reset']}")

# Function to ping an IP address
def ping(ip):
    try:
        # Run the ping command and capture the output
        result = subprocess.run(
            ['ping', '-n', '1', '-l', '65500', ip],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        # Check if the output contains "TTL=" indicating success
        if "TTL=" in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error during pinging: {e}")
        return False

# Main function to continuously ping with different colors
def pinger():
    print_with_color("██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗", 'magenta')
    print_with_color("██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝", 'magenta')
    print_with_color("██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗", 'magenta')
    print_with_color("██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║", 'magenta')
    print_with_color("╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝", 'magenta')
    
    ip = input("Enter Target IP: ")
    
    colors = ['green', 'yellow', 'cyan', 'bright_green', 'white']
    
    while True:
        for color in colors:
            print_with_color(f"Pinging {ip}...", color)
            if ping(ip):
                print_with_color(f"Response from {ip}: Online", color)
            else:
                print_with_color(f"Response from {ip}: Offline", color)
            
            # Wait a short time before the next ping
            time.sleep(2)

if __name__ == "__main__":
    pinger()

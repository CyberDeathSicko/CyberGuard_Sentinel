import subprocess
import platform
from datetime import datetime

# Function to display System Enumeration options
def system_enumeration_options():
    print("System Enumeration Section")
    print("1. Basic System Information")
    print("2. Network Information")
    print("3. Running Processes")
    print("4. Installed Software")
    print("5. Users and Groups")
    print("6. System Uptime")
    print("7. Disk Usage")
    print("0. Exit")

# Function to perform System Enumeration
def perform_system_enumeration():
    while True:
        system_enumeration_options()
        try:
            se_choice = int(input("Enter your choice (0-7): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if se_choice == 0:
            print("Exiting System Enumeration. Goodbye!")
            break
        elif se_choice == 1:
            basic_system_information()
        elif se_choice == 2:
            network_information()
        elif se_choice == 3:
            running_processes()
        elif se_choice == 4:
            installed_software()
        elif se_choice == 5:
            users_and_groups()
        elif se_choice == 6:
            system_uptime()
        elif se_choice == 7:
            disk_usage()
        else:
            print("Invalid choice. Please try again.")

# Function to get Basic System Information
def basic_system_information():
    print("Getting Basic System Information...")
    try:
        print("System: ", platform.system())
        print("Node: ", platform.node())
        print("Release: ", platform.release())
        print("Version: ", platform.version())
        print("Processor: ", platform.processor())
    except Exception as e:
        print("Error fetching basic system information:", str(e))

# Function to get Network Information
def network_information():
    print("Getting Network Information...")
    try:
        subprocess.run(['ipconfig', '/all'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving network information:", str(e))

# Function to list Running Processes
def running_processes():
    print("Listing Running Processes...")
    try:
        subprocess.run(['tasklist'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving running processes:", str(e))

# Function to list Installed Software
def installed_software():
    print("Listing Installed Software...")
    try:
        subprocess.run(['Get-WmiObject', '-Query', '"SELECT * FROM Win32_Product"', '|', 'Format-Table', 'Name, Version'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error listing installed software:", str(e))

# Function to list Users and Groups
def users_and_groups():
    print("Listing Users and Groups...")
    try:
        subprocess.run(['net', 'user'], check=True)
        print("Groups:")
        subprocess.run(['net', 'localgroup'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error listing users and groups:", str(e))

# Function to display System Uptime
def system_uptime():
    print("System Uptime:")
    try:
        import psutil
        uptime = psutil.boot_time()
        print("Uptime: ", datetime.now() - datetime.fromtimestamp(uptime))
    except Exception as e:
        print("Error fetching system uptime:", str(e))

# Function to display Disk Usage
def disk_usage():
    print("Disk Usage:")
    try:
        subprocess.run(['Get-Volume', '|', 'Format-Table', 'DriveLetter, FileSystemLabel, Size, SizeRemaining'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving disk usage information:", str(e))

# Call the main function to start System Enumeration
perform_system_enumeration()

import subprocess

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
        se_choice = input("Enter your choice (0-7): ")

        if se_choice == '0':
            print("Exiting System Enumeration. Goodbye!")
            break
        elif se_choice == '1':
            basic_system_information()
        elif se_choice == '2':
            network_information()
        elif se_choice == '3':
            running_processes()
        elif se_choice == '4':
            installed_software()
        elif se_choice == '5':
            users_and_groups()
        elif se_choice == '6':
            system_uptime()
        elif se_choice == '7':
            disk_usage()
        else:
            print("Invalid choice. Please try again.")

# Function to get Basic System Information
def basic_system_information():
    print("Getting Basic System Information...")
    print("Hostname:", subprocess.getoutput('hostname'))
    print("OS Version:", subprocess.getoutput('systeminfo | grep "OS Version" | awk -F: "{print $2}"'))
    print("System Manufacturer:", subprocess.getoutput('systeminfo | grep "System Manufacturer" | awk -F: "{print $2}"'))
    print("System Model:", subprocess.getoutput('systeminfo | grep "System Model" | awk -F: "{print $2}"'))
    print("Processor:", subprocess.getoutput('systeminfo | grep "Processor" | awk -F: "{print $2}"'))
    print("Memory:", subprocess.getoutput('systeminfo | grep "Total Physical Memory" | awk -F: "{print $2}"'))

# Function to get Network Information
def network_information():
    print("Getting Network Information...")
    subprocess.run(['ipconfig', '/all'], shell=True)

# Function to list Running Processes
def running_processes():
    print("Listing Running Processes...")
    subprocess.run(['tasklist'], shell=True)

# Function to list Installed Software
def installed_software():
    print("Listing Installed Software...")
    subprocess.run(['Get-WmiObject', '-Query', '"SELECT * FROM Win32_Product"', '|', 'Format-Table', 'Name, Version'], shell=True)

# Function to list Users and Groups
def users_and_groups():
    print("Listing Users and Groups...")
    subprocess.run(['net', 'user'], shell=True)
    print("Groups:")
    subprocess.run(['net', 'localgroup'], shell=True)

# Function to display System Uptime
def system_uptime():
    print("System Uptime:")
    print(subprocess.getoutput('systeminfo | grep "System Up Time"'))

# Function to display Disk Usage
def disk_usage():
    print("Disk Usage:")
    subprocess.run(['Get-Volume', '|', 'Format-Table', 'DriveLetter, FileSystemLabel, Size, SizeRemaining'], shell=True)

# Call the main function to start System Enumeration
perform_system_enumeration()

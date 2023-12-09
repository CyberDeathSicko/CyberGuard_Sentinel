import subprocess
import os

def system_enumeration_options():
    print("System Enumeration Section")
    print("1. Basic System Information")
    print("2. Network Information")
    print("3. Running Processes")
    print("4. Installed Software")
    print("5. Users and Groups")
    print("6. System Uptime")
    print("7. Disk Usage")
    print("8. Hardware Information")
    print("9. Firewall Configuration")
    print("10. Open Network Connections")
    print("11. System Logs")
    print("12. Printers and Scanners")
    print("13. USB Devices")
    print("14. List Scheduled Tasks")
    print("15. Security Policies")
    print("0. Exit")

def hardware_information():
    print("Getting Hardware Information...")
    try:
        subprocess.run(['systeminfo'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving hardware information:", str(e))

def firewall_configuration():
    print("Firewall Configuration:")
    try:
        subprocess.run(['netsh', 'advfirewall', 'show', 'allprofiles'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving firewall configuration:", str(e))

def open_network_connections():
    print("Open Network Connections:")
    try:
        subprocess.run(['netstat', '-an'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving open network connections:", str(e))

def system_logs():
    print("System Logs:")
    try:
        subprocess.run(['Get-EventLog', '-LogName', 'System', '-Newest', '10'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving system logs:", str(e))

def printers_and_scanners():
    print("Printers and Scanners:")
    try:
        subprocess.run(['Get-Printer'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving printers and scanners information:", str(e))

def usb_devices():
    print("USB Devices:")
    try:
        subprocess.run(['Get-PnpDevice', '-Class', 'USB'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving USB devices information:", str(e))

def list_scheduled_tasks():
    print("Scheduled Tasks:")
    try:
        subprocess.run(['schtasks'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error listing scheduled tasks:", str(e))

def security_policies():
    print("Security Policies:")
    try:
        subprocess.run(['secedit', '/export', '/cfg', 'security_policies.txt'], check=True)
        with open('security_policies.txt', 'r') as file:
            print(file.read())
    except subprocess.CalledProcessError as e:
        print("Error retrieving security policies information:", str(e))
    finally:
        try:
            os.remove('security_policies.txt')
        except FileNotFoundError:
            pass

def hardware_information():
    print("Getting Hardware Information...")
    try:
        subprocess.run(['systeminfo'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error retrieving hardware information:", str(e))

def list_scheduled_tasks():
    print("Scheduled Tasks:")
    try:
        subprocess.run(['schtasks'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error listing scheduled tasks:", str(e))

def security_policies():
    print("Security Policies:")
    try:
        subprocess.run(['secedit', '/export', '/cfg', 'security_policies.txt'], check=True)
        with open('security_policies.txt', 'r') as file:
            print(file.read())
    except subprocess.CalledProcessError as e:
        print("Error retrieving security policies information:", str(e))
    finally:
        try:
            os.remove('security_policies.txt')
        except FileNotFoundError:
            pass

def perform_system_enumeration():
    while True:
        system_enumeration_options()
        try:
            se_choice = int(input("Enter your choice (0-15): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if se_choice == 0:
            print("Exiting System Enumeration. Goodbye!")
            break
        elif se_choice == 1:
            hardware_information()
        elif se_choice == 2:
            firewall_configuration()
        elif se_choice == 3:
            open_network_connections()
        elif se_choice == 4:
            system_logs()
        elif se_choice == 5:
            printers_and_scanners()
        elif se_choice == 6:
            usb_devices()
        elif se_choice == 7:
            list_scheduled_tasks()
        elif se_choice == 8:
            security_policies()
        else:
            print("Invalid choice. Please try again.")

# Call perform_system_enumeration to start the program
perform_system_enumeration()

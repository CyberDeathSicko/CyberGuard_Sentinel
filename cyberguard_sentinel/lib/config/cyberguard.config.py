# Import necessary libraries
import ipaddress
import logging

from lib.ad_exploitation import *
from lib.osint import *
from lib.privilege_escalation import *
from lib.system_enumeration import *
from lib.uac_bypass import *
from lib.vulnerability_scan import *

# Configuration
TARGET_IP = "192.168.1.1"
TARGET_PORT = "22"
TARGET_PROTOCOL = "ssh"

# Set up logging
logging.basicConfig(filename='sentinel.log', level=logging.INFO)

# Function to perform OSINT
def perform_osint_menu():
    osint_options()
    osint_choice = input("Enter your OSINT choice (0-3): ")
    perform_osint(osint_choice)

# Function to perform vulnerability scan
def perform_vulnerability_scan_menu():
    vulnerability_scan_options()

# Function to perform active directory exploitation
def perform_ad_exploitation_menu():
    perform_active_directory_exploitation(TARGET_IP)

# Function to perform privilege escalation
def perform_privilege_escalation_menu():
    privilege_escalation_options()
    pe_choice = input("Enter your privilege escalation choice (0-2): ")
    privilege_escalation_actions(pe_choice)

# Function to perform system enumeration
def perform_system_enumeration_menu():
    system_enumeration_options()
    se_choice = input("Enter your system enumeration choice (0-3): ")
    system_enumeration_actions(se_choice)

# Function to perform UAC bypass
def perform_uac_bypass_menu():
    uac_bypass_options()
    uac_choice = input("Enter your UAC bypass choice (0-2): ")
    uac_bypass_actions(uac_choice)

# Function to display the main menu
def main_menu():
    print("+-----------------------------------------+")
    print("|       CyberGuard Sentinel                 |")
    print("+-----------------------------------------+")
    print("1. OSINT")
    print("2. Vulnerability Scan")
    print("3. Active Directory Exploitable")
    print("4. Update Vulnerability Database")
    print("5. Privilege Escalation")
    print("6. System Enumeration")
    print("7. UAC Bypass (Windows)")
    print("8. Exit")
    print("-------------------------------------------")

# Perform an interactive menu
while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        perform_osint_menu()
    elif choice == '2':
        perform_vulnerability_scan_menu()
    elif choice == '3':
        perform_ad_exploitation_menu()
    elif choice == '4':
        update_vulnerability_database()
    elif choice == '5':
        perform_privilege_escalation_menu()
    elif choice == '6':
        perform_system_enumeration_menu()
    elif choice == '7':
        perform_uac_bypass_menu()
    elif choice == '8':
        exit(0)
    else:
        print("Invalid choice. Please try again.")

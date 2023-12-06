#!/bin/bash

# Configuration
TARGET_IP="192.168.1.1"
TARGET_PORT="22"
TARGET_PROTOCOL="ssh"

# Include libraries
source lib/ad_exploitation.sh
source lib/osint.sh
source lib/privilege_escalation.sh
source lib/system_enumeration.sh
source lib/uac_bypass.sh
source lib/vulnerability_scan.sh

# Function to display the main menu
function main_menu() {
    echo "+-----------------------------------------+"
    echo "|       CyberGuard Sentinel                 |"
    echo "+-----------------------------------------+"
    echo "1. OSINT"
    echo "2. Vulnerability Scan"
    echo "3. Active Directory Exploitable"
    echo "4. Update Vulnerability Database"
    echo "5. Privilege Escalation"
    echo "6. System Enumeration"
    echo "7. UAC Bypass (Windows)"
    echo "8. Exit"
    echo "-------------------------------------------"
    read -p "Enter your choice: " choice
    case $choice in
        1) osint_options
           read -p "Enter your OSINT choice (0-3): " osint_choice
           perform_osint $osint_choice;;
        2) vulnerability_scan_options;;
        3) perform_active_directory_exploitation $TARGET_IP;;
        4) update_vulnerability_database;;
        5) source lib/privilege_escalation.sh
           privilege_escalation_options
           read -p "Enter your privilege escalation choice (0-2): " pe_choice
           privilege_escalation_actions $pe_choice;;
        6) source lib/system_enumeration.sh
           system_enumeration_options
           read -p "Enter your system enumeration choice (0-3): " se_choice
           system_enumeration_actions $se_choice;;
        7) source lib/uac_bypass.sh
           uac_bypass_options
           read -p "Enter your UAC bypass choice (0-2): " uac_choice
           uac_bypass_actions $uac_choice;;
        8) exit 0;;
        *) echo "Invalid choice. Please try again.";;
    esac
}

# Perform an interactive menu
while true; do
    main_menu
done

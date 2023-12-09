#!/bin/bash

# Function to display System Enumeration options
function system_enumeration_options() {
    echo "System Enumeration Section"
    echo "1. Basic System Information"
    echo "2. Network Information"
    echo "3. Running Processes"
    echo "4. Installed Software"
    echo "5. Users and Groups"
    echo "6. System Uptime"
    echo "7. Disk Usage"
    echo "0. Exit"
}

# Function to perform System Enumeration
function perform_system_enumeration() {
    while true; do
        system_enumeration_options
        read -p "Enter your choice (0-7): " se_choice

        case $se_choice in
            0)
                echo "Exiting System Enumeration. Goodbye!"
                exit;;
            1) basic_system_information;;
            2) network_information;;
            3) running_processes;;
            4) installed_software;;
            5) users_and_groups;;
            6) system_uptime;;
            7) disk_usage;;
            *)
                echo "Invalid choice. Please try again."
                ;;
        esac
    done
}

# Function to get Basic System Information
function basic_system_information() {
    echo "Getting Basic System Information..."
    echo "Hostname: $(hostname)"
    echo "OS Version: $(systeminfo | grep 'OS Version' | awk -F: '{print $2}')"
    echo "System Manufacturer: $(systeminfo | grep 'System Manufacturer' | awk -F: '{print $2}')"
    echo "System Model: $(systeminfo | grep 'System Model' | awk -F: '{print $2}')"
    echo "Processor: $(systeminfo | grep 'Processor' | awk -F: '{print $2}')"
    echo "Memory: $(systeminfo | grep 'Total Physical Memory' | awk -F: '{print $2}')"
}

# Function to get Network Information
function network_information() {
    echo "Getting Network Information..."
    ipconfig /all
}

# Function to list Running Processes
function running_processes() {
    echo "Listing Running Processes..."
    tasklist | head -n 10
}

# Function to list Installed Software
function installed_software() {
    echo "Listing Installed Software..."
    Get-WmiObject -Query "SELECT * FROM Win32_Product" | Format-Table Name, Version
}

# Function to list Users and Groups
function users_and_groups() {
    echo "Listing Users and Groups..."
    net user
    echo "Groups:"
    net localgroup
}

# Function to display System Uptime
function system_uptime() {
    echo "System Uptime:"
    systeminfo | grep 'System Up Time'
}

# Function to display Disk Usage
function disk_usage() {
    echo "Disk Usage:"
    Get-Volume | Format-Table DriveLetter, FileSystemLabel, Size, SizeRemaining
}

# Call the main function to start System Enumeration
perform_system_enumeration

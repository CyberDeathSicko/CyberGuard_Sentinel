#!/bin/bash

# Function to display initial reconnaissance options
function initial_recon_options() {
    echo "===== Initial Reconnaissance with Information Gathering ====="
    echo "1. Email OSINT (theHarvester)"
    echo "2. Domain OSINT (Recon-ng)"
    echo "3. SpiderFoot OSINT"
    echo "0. Exit"
}

# Function to perform initial reconnaissance
function perform_initial_recon() {
    local recon_choice=$1

    case $recon_choice in
        1) perform_email_osint;;
        2) perform_domain_osint;;
        3) perform_spiderfoot_osint;;
        0) echo "Exiting the script. Goodbye!"; exit;;
        *) echo "Invalid choice. Please enter a valid option (0-3).";;
    esac
}

# Function to perform Email OSINT using theHarvester
function perform_email_osint() {
    echo "===== Performing Email OSINT using theHarvester ====="

    # Basic theHarvester command
    theharvester -d example.com -l 100 -b all -v -f basic_results.html

    # Additional OSINT tools
    # Add more OSINT tools and commands here

    echo "Email OSINT using theHarvester completed."
}

# Function to perform Domain OSINT using Recon-ng
function perform_domain_osint() {
    echo "===== Performing Domain OSINT using Recon-ng ====="

    # Advanced Recon-ng commands
    recon-ng --no-check -m recon/domains-hosts/google_site_web -c "show options; set SOURCE example.com; run"
    # Add more advanced commands as needed

    echo "Domain OSINT using Recon-ng completed."
}

# Function to perform SpiderFoot OSINT
function perform_spiderfoot_osint() {
    echo "===== Performing OSINT using SpiderFoot ====="

    # Advanced SpiderFoot commands for domain
    spiderfoot -d example.com -o advanced_domain_results.html
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for phones, email, IP address, and social media profiles
    spiderfoot -p +1234567890 -e user@example.com -i 192.168.0.1 -s facebook.com/user -o advanced_results.html
    # Add more advanced commands as needed

    echo "SpiderFoot OSINT completed."
}

# Main menu
while true; do
    clear
    initial_recon_options
    read -p "Enter your choice (0-3): " choice
    perform_initial_recon $choice
    read -p "Press enter to continue..."
done

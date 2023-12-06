#!/bin/bash

# Function to display initial reconnaissance options
function initial_recon_options() {
    echo "Initial Reconnaissance with Information Gathering"
    echo "1. Email OSINT (theHarvester)"
    echo "2. Domain OSINT (Recon-ng)"
    echo "3. SpiderFoot OSINT"
    echo "0. Return to Main Menu"
}

# Function to perform initial reconnaissance
function perform_initial_recon() {
    local recon_choice=$1

    case $recon_choice in
        1) perform_email_osint;;
        2) perform_domain_osint;;
        3) perform_spiderfoot_osint;;
        0) return;;
        *) echo "Invalid choice. Please try again.";;
    esac
}

function perform_email_osint() {
    echo "Performing Email OSINT using theHarvester..."

    # Basic theHarvester command
    echo "Basic theHarvester command:"
    theharvester -d example.com -l 100 -b all -v -f basic_results.html

    # Advanced theHarvester commands
    echo "Advanced theHarvester commands:"
    theharvester -d example.com -l 500 -b all -v -f advanced_results.html
    # Add more advanced commands as needed

    # Additional OSINT tools
    echo "Additional OSINT tools:"
    # Add more OSINT tools and commands here

    echo "Email OSINT using theHarvester completed."
}

# Function to perform Domain OSINT using Recon-ng
function perform_domain_osint() {
    echo "Performing Domain OSINT using Recon-ng..."

    # Advanced Recon-ng commands
    echo "Advanced Recon-ng commands:"
    recon-ng --no-check -m recon/domains-hosts/google_site_web -c "show options; set SOURCE example.com; run"
    # Add more advanced commands as needed

    echo "Domain OSINT using Recon-ng completed."
}

# Function to perform SpiderFoot OSINT
function perform_spiderfoot_osint() {
    echo "Performing OSINT using SpiderFoot..."

    # Advanced SpiderFoot commands for domain
    echo "Advanced SpiderFoot commands for domain:"
    spiderfoot -d example.com -o advanced_domain_results.html
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for phones
    echo "Advanced SpiderFoot commands for phones:"
    spiderfoot -p +1234567890 -o advanced_phone_results.html
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for email
    echo "Advanced SpiderFoot commands for email:"
    spiderfoot -e user@example.com -o advanced_email_results.html
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for IP address
    echo "Advanced SpiderFoot commands for IP address:"
    spiderfoot -i 192.168.0.1 -o advanced_ip_results.html
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for social media profiles
    echo "Advanced SpiderFoot commands for social media profiles:"
    spiderfoot -s facebook.com/user -o advanced_social_results.html
    # Add more advanced commands as needed

    echo "SpiderFoot OSINT completed."
}

# Main menu
while true; do
    clear
    echo "===== Initial Recon with Information Gathering ====="
    initial_recon_options
    read -p "Enter your choice (0-3): " choice
    perform_initial_recon $choice
    read -p "Press enter to continue..."
done
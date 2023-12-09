import subprocess

# Function to display initial reconnaissance options
def initial_recon_options():
    print("===== Initial Reconnaissance with Information Gathering =====")
    print("1. Email OSINT (theHarvester)")
    print("2. Domain OSINT (Recon-ng)")
    print("3. SpiderFoot OSINT")
    print("0. Exit")

# Function to perform initial reconnaissance
def perform_initial_recon(recon_choice):
    if recon_choice == '1':
        perform_email_osint()
    elif recon_choice == '2':
        perform_domain_osint()
    elif recon_choice == '3':
        perform_spiderfoot_osint()
    elif recon_choice == '0':
        print("Exiting the script. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter a valid option (0-3).")

# Function to perform Email OSINT using theHarvester
def perform_email_osint():
    print("===== Performing Email OSINT using theHarvester =====")

    # Basic theHarvester command
    subprocess.run(['theharvester', '-d', 'example.com', '-l', '100', '-b', 'all', '-v', '-f', 'basic_results.html'])

    # Additional OSINT tools
    # Add more OSINT tools and commands here

    print("Email OSINT using theHarvester completed.")

# Function to perform Domain OSINT using Recon-ng
def perform_domain_osint():
    print("===== Performing Domain OSINT using Recon-ng =====")

    # Advanced Recon-ng commands
    subprocess.run(['recon-ng', '--no-check', '-m', 'recon/domains-hosts/google_site_web', '-c', 'show options; set SOURCE example.com; run'])
    # Add more advanced commands as needed

    print("Domain OSINT using Recon-ng completed.")

# Function to perform SpiderFoot OSINT
def perform_spiderfoot_osint():
    print("===== Performing OSINT using SpiderFoot =====")

    # Advanced SpiderFoot commands for domain
    subprocess.run(['spiderfoot', '-d', 'example.com', '-o', 'advanced_domain_results.html'])
    # Add more advanced commands as needed

    # Advanced SpiderFoot commands for phones, email, IP address, and social media profiles
    subprocess.run(['spiderfoot', '-p', '+1234567890', '-e', 'user@example.com', '-i', '192.168.0.1', '-s', 'facebook.com/user', '-o', 'advanced_results.html'])
    # Add more advanced commands as needed

    print("SpiderFoot OSINT completed.")

# Main menu
while True:
    subprocess.run('clear', shell=True)
    initial_recon_options()
    choice = input("Enter your choice (0-3): ")
    perform_initial_recon(choice)
    input("Press enter to continue...")

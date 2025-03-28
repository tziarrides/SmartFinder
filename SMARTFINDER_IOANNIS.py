# SmartFinder: Network Scanning Tool
#Ioannis Tziarridis 20968783

import nmap  # Import the nmap library for network scanning
import tkinter as tk  # Import tkinter for creating the graphical user interface (GUI)
from PIL import Image, ImageTk  # Import Pillow for logo image handle
from tkinter import messagebox, scrolledtext  # Import tkinter components for message after scan and scrolledtext for the tabs content
import socket  # Import socket for network-related functions
from mac_vendor_lookup import MacLookup  # Import mac-vendor-lookup for MAC address manufacturer 

def main_gui():
    global main, mac_lookup
    main = tk.Tk()  # Create the main window
    main.title("SmartFinder")  # Title of the main application window
    main.resizable(width=True, height=True)  # Resizing of the main window
    main.geometry("1000x830")  # Window size
    main.config(background="#e0f7fa")  # Background color for the main window
    
    # Load and display the logo image
    image = Image.open('Logo.png')
    image = image.resize((100, 100), Image.LANCZOS)  # Resize the image to smaller 
    image = ImageTk.PhotoImage(image)  # Update the image after resizing
   
    header_frame = tk.Frame(main, bg="#e0f7fa")  # Create a frame for the header
    header_frame.grid(row=0, column=0, sticky='nsew')  # Place the frame at the top using grid

    image_label = tk.Label(header_frame, image=image)  # Create a label to display image
    image_label.grid(row=0, column=0, sticky='ne')  # Place the image in the header 

    title_label = tk.Label(header_frame, text="SmartFinder Network Scanning Tool", font=("Arial", 28, "bold"), background="#007bff", fg="white")  # Title label
    title_label.grid(row=0, column=1, padx=10)  # Place the title label after the image

    create_buttons()  # Create the buttons tabs
    mac_lookup = MacLookup()  # Initialize MacLookup instance for MAC address lookups
    main.mainloop()  # Start the Tkinter event loop

def create_buttons():
    button_frame = tk.Frame(main, bg="#e0f7fa")  # Create a frame for the buttons
    button_frame.grid(row=1, column=0, sticky='nsew')  # Place the button frame below the header

    # Create buttons to use them as tabs and style them with colors and font 
    network_scan_button = tk.Button(button_frame, text="Network Scan", command=show_network_scan, bg="#007bff", fg="white", font=("Arial", 14))
    network_scan_button.pack(side=tk.LEFT, padx=5, pady=5)

    faq_button = tk.Button(button_frame, text="FAQ", command=show_faq, bg="#007bff", fg="white", font=("Arial", 14))
    faq_button.pack(side=tk.LEFT, padx=5, pady=5)

    passwords_button = tk.Button(button_frame, text="Password Tips", command=show_passwords, bg="#007bff", fg="white", font=("Arial", 14))
    passwords_button.pack(side=tk.LEFT, padx=5, pady=5)

    network_security_button = tk.Button(button_frame, text="Network Security", command=show_network_security, bg="#007bff", fg="white", font=("Arial", 14))
    network_security_button.pack(side=tk.LEFT, padx=5, pady=5)

    devrecommendations_button = tk.Button(button_frame, text="Device Security", command=show_devrecommendations, bg="#007bff", fg="white", font=("Arial", 14))
    devrecommendations_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a main frame to hold the content
    global content_frame
    content_frame = tk.Frame(main, bg="#e0f7fa")
    content_frame.grid(row=2, column=0, sticky='nsew')

    show_network_scan()  # Show the network scan content by default

def show_network_scan():
    clear_content_frame() # Clear the frame so the new content to be added 
    setup_scan_tab(content_frame)

def show_faq():
    clear_content_frame()
    setup_faq_tab(content_frame)

def show_passwords():
    clear_content_frame()
    setup_passwords_tab(content_frame)

def show_network_security():
    clear_content_frame()
    setup_network_security_tab(content_frame)

def show_devrecommendations():
    clear_content_frame()
    setup_devrecommendations_tab(content_frame)

def clear_content_frame():
    for widget in content_frame.winfo_children():
        widget.destroy()

def setup_scan_tab(scan_tab):
    global result_area
    # Create a frame for the Network Scan tab
    frame = tk.Frame(scan_tab, bg="#e0f7fa")
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Button to start the network scanning 
    scan_button = tk.Button(frame, text="Scan My Network", command=scan_network, background="#28a745", foreground="white", font=("Arial", 20, "bold"), relief="raised")
    scan_button.pack(pady=5)

    # Text area for displaying the results of the network scan
    result_area = scrolledtext.ScrolledText(frame, width=100, height=25, font=("Arial", 12), bg="#ffffff", fg="#333333", borderwidth=3, relief="sunken")
    result_area.pack(padx=10, pady=10)

def setup_faq_tab(faq_tab):
    # Title for the Frequently Asked Questions (FAQ) tab
    faq_label = tk.Label(faq_tab, text="Frequently Asked Questions", font=("Arial", 20, "bold"), background="#007bff", foreground="white")
    faq_label.pack(pady=10)

    # Content for the Frequently Asked Questions (FAQ) tab
    faq_content = (
        """


        1. What is SmartFinder?
            SmartFinder is a free to use network scanning tool that helps the home owners and business owners to identify 
            devices that are connected to their network and at the same time it provides the user with password, network 
            and device recommendations for their security, in order for the regular user to elevate the security.

        2. How does SmartFinder work?
            SmartFinder uses network scanning techniques to detect devices on your local network, and as a result it shows 
            the IP, MAC addresses, and identifies their manufacturers to help the user to identify the devices 
            that are connected to the local network in order for the user to be aware of every device on their network.

        3. How can I understand the scan results?
           The scan results will show you the IP and MAC addresses of devices, along with their operating systems. 
            This information can help you identify unauthorized devices on your network since the other devices
            will be recognized from their manufacturer. 

        4. What should be done if you dont recognise a device and yoy think that is unauthorised:
            If you find an unknown device, consider changing your Wi-Fi password as fast as possible to make sure 
            that everyone unauthorised will loose the acces to your network and dont risk to threat exposure.It means that the 
            unkown device is connected and needs identification,the owner of the network knows exactly which devices are
            connected at times.
            
        5. How can I use SmartFinder?
            To start using Smartfinder you have to download the SmartFinder tool from the GitHub repository at 
            https://github.com/tziarrides/SmartFinder.gitand. Install all the libraries needed with the command in terminal 
            pip install pyhton-nmap scapy mac-vendor-lookup Pillow and the to run the tool python SMARTFINDER_IOANNIS.py.
            On the main window, click the "Scan My Network" button to start the scan of the network and see the results which
            are the devices that are connected to your network.
           
           """
    )

    # Text area for displaying the FAQ content
    faq_text = scrolledtext.ScrolledText(faq_tab, width=100, height=25, font=("Arial", 11))
    faq_text.insert(tk.END, faq_content)  # Insert FAQ content into text area
    faq_text.config(state=tk.DISABLED)  # Make the text area read-only so it is not able to change
    faq_text.pack(padx=10, pady=10)

def setup_passwords_tab(passwords_tab):
    # Title for the Password Security Tips 
    password_label = tk.Label(passwords_tab, text="Password Security Tips", font=("Arial", 20, "bold"), background="#0056b3", foreground="white")
    password_label.pack(pady=10)

    # Content with recommendations for password education
    password_recommendations = (
        """

        Passwords are very important to each person and company, as they protect the personal data of individuals and 
        businesses. Weak, small, and easy to guess passwords can be exploited, risking personal life or the operations
        of the business. Everyone has to take some steps ahead for their own online security. 

        Recommended actions for safe passwords:

        1. Do not use short passwords prefer to use at least 16 characters, which will take a billion years to crack.
        Also use special characters, numbers, and uppercase letters to make your passwords even harder to crack.

        2. Avoid using common words for passwords, such as "12345678", "password", or predictable keyboard patterns like
        "qwertyuio".

        3. Do not use words related to your personal life or business information, as hackers often use information from 
        social media to guess passwords, such as "name.surname.dateofbirth" or "nameofcompany.dateofcreation".
        This makes it easier for attackers to guess your passwords by making a list of possible passwords and
        start to try them on your accounts.

        4. Always use MFA (Multi-Factor Authentication) whenever possible. There are several authentication apps available
        available for all the devices into like Google Authenticator, Microsoft Authenticator,or you can use text messages
        or calls to a personal mobile number or face recognition with MFA. This adds extra layers of protection because
        even if the password is found, without the second authentication, the attacker will not gain access to the account
        imagine how difficult itt will be if its reqired even more of those togetrher.

        5. Do not use password hints that can be used to predict your password or any recovery questions, as most of them 
        can be found on personal social media accounts.

        6. Use a password manager like 1Password and LastPass to securely store and generate new passwords for all
        your accounts. Homeowners will no longer need to reuse passwords for multiple websites but instead, they will have 
        unique and complex passwords generated by these password managers, which will be autofilled when saved.
        For businesses, they can select a business plan with the password manager to share all the passwords that are
        needed across employees, without all the employess access to everywhere but only where they have to.
       
        
        """ )

    # Text area to displaying password security recommendations
    password_text = scrolledtext.ScrolledText(passwords_tab, width=100, height=25, font=("Arial", 11))
    password_text.insert(tk.END, password_recommendations)  # Add password tips into the text area
    password_text.config(state=tk.DISABLED)  # Make the text area not to be edited
    password_text.pack(padx=10, pady=10)

def setup_network_security_tab(network_security_tab):
    # Title for the Network Security Recommendations tab
    network_security_label = tk.Label(network_security_tab, text="Network Security Recommendations", font=("Arial", 22, "bold"), background="#0056b3", foreground="white")
    network_security_label.pack(pady=10)

    # Recommendations for securing your network content
    network_security_content = (
        """

        Network protection is very important for every individual, especially for homeowners and businesses.
        If an attacker or hacker gains access to a network due to weak protection, it can risk the privacy and
        information of the entire network, allowing them to track different devices, find data, and 
        steal or attack devices, causing problems for your home or business.
        Businesses must be very careful because a compromised Wi-Fi can expose customer data, financial data,
        and future business plans.

        Recommendations to secure your Wi-Fi and network:

        1. Always change the default settings of the router and replace the admin password with a strong password 
        because most default passwords can be exploited by hackers to gain control of the network. Use a strong
        password to secure the Wi-Fi with WPA3 encryption and in the case WPA3 is not available, use WPA2 then.

        2. Create a separate Wi-Fi network for visitors to prevent them from connecting to the same network as employees 
        and administration, keeping the main network secure and private.

        3. Regularly check all connected devices on the network to identify any unauthorized devices.

        4. Devices connected to the network can be targeted by hackers. Turn off smart devices
        like cameras, microphones, and smart lamps when they are not in use so basically the hackers have less 
        opportunities to access the network via something which is not having security encryprion on it .

        5. Ensure that all the software is updated regularly and change the Wi-Fi password every 3-6 months to prevent
        unauthorized access. This include all the devices that are using the internet.

        
          """)

    # Text area for displaying network security recommendations
    network_security_text = scrolledtext.ScrolledText(network_security_tab, width=100, height=25, font=("Arial", 11))
    network_security_text.insert(tk.END, network_security_content)  # Add recommendations regarding network into the text area
    network_security_text.config(state=tk.DISABLED)  # Make the text area not edited
    network_security_text.pack(padx=10, pady=10)

def setup_devrecommendations_tab(devrecommendations_tab):
    # Title for the Device Security Recommendations tab style
    devrecommendations_label = tk.Label(devrecommendations_tab, text="Device Security Recommendations", font=("Arial", 20, "bold"), background="#0056b3", foreground="white")
    devrecommendations_label.pack(pady=10)

    # Device protection recommendations content
    devrecommendations_content = (
        """
        Everyone uses multiple devices at home or at work, like laptops and mobile phones. If they are not properly
        secured, attacks can steal data from them and use them to find almost anything about personal life or business
        operations and use it against each individual. That is why is essential to secure devices to ensure safety 
        online and at all times.

        Recommendations for devices:

        1. Every device must be locked using a 6+ digit PIN or password to secure data in case the device is in the hands
        of an unauthorized person.

        2. Always check for updates on devices connected to the Internet, as updates can fix 
        security issues to prevent attacks.

        3. Use antivirus programs like Windows Defender, Panda Antivirus, or Avast Antivirus to protect personal data.
        Antivirus programs can detect viruses and other threats from emails that may be phishing or spam, or from any
        downloads made on devices that can steal information or disrupt business operations. 
        Be carefull in every download you make in all the devices.

        4. Always back up important data, such as photos and personal files, to an external drive that is properly secured or
        use a cloud service like Google Drive or Dropbox. In the unlikely event of device failure, the data will be secured 
        and not lost especially for customer records and daily updates for the business. Most of the attackers have financial 
        reasons behind the attack so secure very well any data that has financial information.

        5. Check app permissions on devices before every download especially for apps that request permissions not needed
       for their functionality.

        6. Avoid using public Wi-Fi, especially for financial operations and accessing personal accounts, as unsecured 
        connections are monitored by hackers to steal data like passwords and personal information.
        Employees must be trained to use a VPN for secure connections when working remotely like ExpressVPN or 
        Surfshark.

        7. Turn off unused features like Bluetooth and Wi-Fi to reduce the risk of attacks and unauthorized access.       
       """)

    # Text area for displaying device security recommendations
    devrecommendations_text = scrolledtext.ScrolledText(devrecommendations_tab, width=100, height=25, font=("Arial", 11))
    devrecommendations_text.insert(tk.END, devrecommendations_content)  # Add recommendations of the device into the text area
    devrecommendations_text.config(state=tk.DISABLED)  # Make the text area not to be editted 
    devrecommendations_text.pack(padx=10, pady=10)

def manufacturer_info(mac):
    # Directly use the MAC address for lookup
    try:
        manufacturer = mac_lookup.lookup(mac)  # Look up the manufacturer using the mac-vendor-lookup library
        return f"Manufacturer: {manufacturer}"  # Return the manufacturer name
    except Exception:
        return "Manufacturer: Unknown"  # Return an error message if the lookup fails


def scan_network():
    try:
        nm = nmap.PortScanner()  # Create an instance of the nmap PortScanner
        local_ip = socket.gethostbyname(socket.gethostname())  # Get the local IP address
        subnet = '.'.join(local_ip.split('.')[:-1]) + '.0/24'  # Define the subnet to scan from the ip 

        # Ping scan on the subnet to get the online hosts 
        nm.scan(subnet, arguments='-sn')  # Ping scan
        devices = nm.all_hosts()  # Get all detected hosts

        result_area.delete(1.0, tk.END)  # Clear previous results

        if devices:  # Check if any devices were found
            for device in devices:
                ip = f"Device IP: {device}\n"
                mac_address = nm[device]['addresses'].get('mac', 'N/A')  # Get the MAC address
                os = nm[device]['osmatch'][0]['name'] if 'osmatch' in nm[device] else 'Not Detected'  # Get OS info
                manufacturer = manufacturer_info(mac_address) 

                result_area.insert(tk.END, f"{ip} MAC Address: {mac_address}\nOperating System: {os}\n{manufacturer}\n") # Display the results in result area 

                result_area.insert(tk.END, "__________________________________________" + "\n")  # Line to seperate the results from each other 

        else:  # If no devices were found as a message 
            messagebox.showinfo("Scan Results", "No devices connected")
        
        # Show the number of devices found
        messagebox.showinfo("Scan Results", f"{len(devices)} devices found connected")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



if __name__ == "__main__":
    main_gui()  # Initialize the SmartFinder application GUI
# SmartFinder
Ioannis Tziarridis

<a href="itziarridis@uclan.ac.uk">itziarridis@uclan.ac.uk</a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><h2>Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#tools">Development tools</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
SmartFinder is a network scanning tool that helps network owners identify devices connected to their own network and provides security recommendations for passwords, devices, and their network. It uses network scanning techniques to find all the devices that are connected on your local network so the owner will be able to monitor all the connected devices by showing to the user devices details like their IP, MAC addresses, operating system and identifying their manufacturers. This helps the owner to recognize if there is an unauthorized device that is using their internet, in order to prevent data losses, personal information leaks and bandwidth issues due to too many devices using the internet at the same time but also SmartFinder provides educational recommendations to the user to maximize their cybersecurity protection and prevent attacks to occur.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Development tools
- Python 3.x
- nmap library
- tkinter (comes pre-installed with Python)
- mac-vendor-lookup library
- Pillow

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To install SmartFinder you have to have Python 3.x installed and the required libraries. 
Follow these steps:

### Prerequisites
- Nmap (https://pypi.org/project/python-nmap/) A Python library for using nmap and san the network 
- Tkinter (https://docs.python.org/3/library/tkinter.html) For the Graphical User Interface
- Pillow (https://pillow.readthedocs.io/en/stable/) A Python Imaging Library that is used for the logo of SmartFinder.
- socket (https://realpython.com/python-sockets/) Socket is critical for network communication and enables to exchange data.
- mac-vendor-lookup (https://pypi.org/project/mac-vendor-lookup/) A python library for looking MAC address manufacturers up.

### Installation
1. Download SmartFinder from Github at
   or use the command in terminal 
    ```sh
    git clone https://github.com/tziarrides/SmartFinder.git
   ```
2. Install the necessary libraries
    ```sh
   pip install python-nmap scapy mac-vendor-lookup Pillow 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
1. Run the application with the command:
   ```sh
   python pathtofile/SMARTFINDER_IOANNIS.py
   ```
2. Click on the "Scan My Network" button to start scanning for devices in the connected network.
3. Read all the scan results displayed in the application to recognize the connected devices. The results will show the IP, MAC addresses, Operating system, and the Manufacturer of detected devices. This information will help you identify unauthorized devices on your network in order to take the steps to secure the network usually the ones that the owner cannot recognize in the results are the unauthorised ones.
4. Read and follow all the security recommendations regarding network security, device protection, and password strategies to significantly increase your protection against attacks.

Examples: 
In the office in the case that you already know the devices that are connected to the network, you can use SmartFinder to find if any extra devices are also connected resulting in bandwithloss and even worse if the device is used to attack the company. 

Another exaple is at a family home where all family members have devices connected to the network. So with SmartFinder you will be able to see which devices are currently connected causing delayed connections and in the worst senario a hacker is connected to the same network.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact
Ioannis Tziarridis - <a href="mailto:itziarridis@uclan.co.uk">itziarridis@uclan.co.uk</a> - [GitHub Account](https://github.com/your_username)

Project Link: [https://github.com/tziarrides/SmartFinder.git](https://github.com/tziarrides/SmartFinder.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
I want to thank my supervisors for the help they provided for this project
<p align="right">(<a href="#readme-top">back to top</a>)</p>

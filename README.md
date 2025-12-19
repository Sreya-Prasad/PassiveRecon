# PassiveRecon – Passive Information Gathering Tool

## Overview
PassiveRecon is a **Python-based passive information gathering tool** developed as part of a cybersecurity learning task.  
The tool collects **publicly available information** about a given domain without actively scanning or attacking the target.

This project demonstrates the fundamentals of **passive reconnaissance**, which is the first and most important phase of penetration testing.

---

## Task Objective
Create a passive information gathering tool that can retrieve:
- Domain IP address
- WHOIS information
- DNS records
- Subdomains (passive)

The project is implemented as a **Python CLI tool** and stored in a GitHub repository for demonstration and explanation.

---

## Features
- Domain to IP resolution
- WHOIS information lookup
- DNS record enumeration (A, MX, NS)
- Passive subdomain discovery using DNS resolution
- Beginner-friendly and demo-safe
- Runs in an isolated Python virtual environment

---

## Environment Used
- **Operating System:** Kali Linux
- **Language:** Python 3
- **Reason:** Kali Linux uses an externally managed Python environment, so a virtual environment is recommended.

---

## Project Structure
PassiveRecon/
├── src/
│ └── passiverecon.py
├── venv/
├── requirements.txt
└── README.md

---
## How to Run / Installation

Follow these steps to use PassiveRecon on your local machine:

### Step 1: [Clone the Repository](#clone-the-repository)
### Step 2: [Create a Virtual Environment](#virtual-environment-setup)
### Step 3: [Install Required Libraries](#install-dependencies)
### Step 4: [Run the Tool](#usage)

## Clone the Repository

Open your terminal and run:
```bash
git clone https://github.com/Sreya_Prasad/PassiveRecon.git
cd PassiveRecon
```

## Virtual Environment Setup (Important)

Kali Linux does not allow system-wide Python package installation using `pip`.  
To avoid breaking system Python, a **virtual environment** is used.

### Step 1: Install venv support
```bash
sudo apt update
sudo apt install python3-venv -y
```
### Step 2: Create a virtual environment
```bash
python3 -m venv venv
```

### Step 3: Activate the virtual environment
#### Linux / macOS / Kali
```bash
source venv/bin/activate
```
#### Windows
```bash
venv\Scripts\activate
```
You should see (venv) in the terminal prompt.

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run the tool using:
```bash
python src/passiverecon.py
```
### Enter a domain when prompted:
```bash
Enter domain name (example.com): facebook.com
```
The tool will display:
- IP address
- WHOIS information
- DNS records
- Subdomains (if publicly available)

### Notes
* The virtual environment (venv) is not included in the repository and must be created locally.
* Subdomain results depend on public availability and may vary per domain.
* This tool is designed for passive reconnaissance only — it does not actively interact with target servers.

## Sample Output (Example)

```bash
Enter domain: facebook.com

IP Address: 157.240.20.35
WHOIS: ...
DNS Records: ...
Subdomains: www.facebook.com, m.facebook.com, ...
```
(Note: Results may vary due to DNS rotation and public data availability.)

## Subdomain Enumeration Explanation

Subdomains are discovered passively by checking commonly used subdomain names and resolving them using DNS.
This method:
* Does not scan ports
* Does not send intrusive requests
* Does not violate ethical guidelines
Some public OSINT sources may block automated requests, so DNS-based discovery ensures reliability for learning and demonstration purposes.

## Future Improvements

* Add multiple passive OSINT sources
* Save output to a report file
* Add command-line arguments
* Improve subdomain enumeration accuracy

## Disclaimer

This project is intended for educational purposes and ethical use only. Do not use this tool for illegal activities. Always have permission before gathering information on a target.

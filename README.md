# PassiveRecon – Passive Information Gathering Tool

## 📌 Overview
PassiveRecon is a **Python-based passive information gathering tool** developed as part of a cybersecurity learning task.  
The tool collects **publicly available information** about a given domain without actively scanning or attacking the target.

This project demonstrates the fundamentals of **passive reconnaissance**, which is the first and most important phase of penetration testing.

---

## 🎯 Task Objective
Create a passive information gathering tool that can retrieve:
- Domain IP address
- WHOIS information
- DNS records
- Subdomains (passive)

The project is implemented as a **Python CLI tool** and stored in a GitHub repository for demonstration and explanation.

---

## 🛠️ Features
- Domain to IP resolution
- WHOIS information lookup
- DNS record enumeration (A, MX, NS)
- Passive subdomain discovery using DNS resolution
- Beginner-friendly and demo-safe
- Runs in an isolated Python virtual environment

---

## 🖥️ Environment Used
- **Operating System:** Kali Linux
- **Language:** Python 3
- **Reason:** Kali Linux uses an externally managed Python environment, so a virtual environment is recommended.

---

## 📂 Project Structure
PassiveRecon/
├── src/
│ └── passiverecon.py
├── venv/
├── requirements.txt
└── README.md

---

## 🔐 Virtual Environment Setup (Important)

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
```bash
source venv/bin/activate
```
You should see (venv) in the terminal prompt.

## 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️Usage
Run the tool using:
```bash
python src/passiverecon.py
```

Enter a domain when prompted:
```bash
Enter domain name (example.com): facebook.com
```

## 📊 Sample Output (Example)

* IP Address: 57.144.56.1
* WHOIS Information: Domain registration and ownership details
* DNS Records: A, MX, NS records
* Subdomains:
```bash
www.facebook.com
mail.facebook.com
m.facebook.com
```
(Note: Results may vary due to DNS rotation and public data availability.)

## 🌐 Subdomain Enumeration Explanation

Subdomains are discovered passively by checking commonly used subdomain names and resolving them using DNS.

This method:
* Does not scan ports
* Does not send intrusive requests
* Does not violate ethical guidelines
Some public OSINT sources may block automated requests, so DNS-based discovery ensures reliability for learning and demonstration purposes.

## ⚠️ Known Limitations

* Subdomain results depend on DNS availability
* Passive sources may block or rate-limit requests
* Output data may change over time
These behaviors are normal in real-world reconnaissance.

## 🚧 Future Improvements

* Add multiple passive OSINT sources
* Save output to a report file
* Add command-line arguments
* Improve subdomain enumeration accuracy

## 📜 Disclaimer

This tool is developed for educational purposes only.
It performs passive reconnaissance using publicly available information and should be used responsibly.

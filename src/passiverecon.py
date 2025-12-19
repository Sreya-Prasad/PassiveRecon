import socket
import whois
import dns.resolver
import requests

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "Could not resolve IP"

def get_whois(domain):
    try:
        return whois.whois(domain)
    except:
        return "WHOIS lookup failed"

def get_dns(domain):
    records = {}
    for record_type in ["A", "MX", "NS"]:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [str(rdata) for rdata in answers]
        except:
            records[record_type] = []
    return records

def get_subdomains(domain):
    common_subs = [
        "www", "mail", "ftp", "webmail", "smtp", "ns1", "ns2",
        "blog", "test", "dev", "api", "portal", "admin",
        "support", "m", "mobile", "docs"
    ]

    found = []

    for sub in common_subs:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            found.append(subdomain)
        except:
            pass

    return found


def main():
    domain = input("Enter domain name (example.com): ").strip()

    print("\n[+] IP Address")
    print(get_ip(domain))

    print("\n[+] WHOIS Information")
    print(get_whois(domain))

    print("\n[+] DNS Records")
    dns_records = get_dns(domain)
    for k, v in dns_records.items():
        print(f"{k}: {v}")

    print("\n[+] Subdomains (Passive)")
    subs = get_subdomains(domain)
    if not subs:
    	print("No subdomains found or source blocked.")
    else:
    	for sub in subs[:20]:
        	print(sub)

if __name__ == "__main__":
    main()

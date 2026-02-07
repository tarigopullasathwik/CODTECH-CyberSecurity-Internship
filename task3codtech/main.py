from port_scanner import port_scan
from brute_forcer import brute_force

print("=== Penetration Testing Toolkit ===")
print("1. Port Scanner")
print("2. Brute Force Module")

choice = input("Select an option: ")

if choice == "1":
    target = input("Enter target IP: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    port_scan(target, start_port, end_port)

elif choice == "2":
    username = input("Enter username: ")
    passwords = ["admin", "123456", "password", "root"]
    brute_force(username, passwords)

else:
    print("Invalid choice")

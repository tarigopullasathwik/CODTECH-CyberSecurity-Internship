import socket

def port_scan(target, start_port, end_port):
    print("Port Scanner Started")
    print(f"Target: {target}")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        if s.connect_ex((target, port)) == 0:
            print(f"Port {port} is OPEN")

        s.close()

    print("Scan finished")

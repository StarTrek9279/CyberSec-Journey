import socket
import time

def scan_ports(target_ip):
    print(f"\nTarget: {target_ip}")
    print("Scanning Target port in range 1-1024...")

    scan_start_time = time.time()
    open_ports = []

    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            result = s.connect_ex((target_ip, port))

            if result == 0:
                print(f"Port {port} is open.")
                open_ports.append(port)
            s.close()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt by the user.")
        return

    except Exception as e:
        print(f"Error Occured: {e}")
        return

    scan_end_time = time.time()
    if open_ports == []:
        print(f"{len(open_ports)} were found to be open in the range 1-1024.")
    else:
        print("No open ports in the range 1-1024.")
    print(f"Total Scan Time: {scan_end_time - scan_start_time:.2f} seconds")


if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    scan_ports(target_ip)






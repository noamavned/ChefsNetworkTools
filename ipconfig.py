import subprocess


def run_ipconfig():
    result = subprocess.run(["ipconfig"], capture_output=True, text=True)
    output = result.stdout

    interfaces = []
    current_interface = None

    for line in output.splitlines():
        if line.strip() == "":
            continue
        if line.startswith("Ethernet adapter") or line.startswith("Wireless LAN adapter"):
            current_interface = {"name": line.strip(":"), "details": []}
            interfaces.append(current_interface)
        elif current_interface and (line.startswith("   ") or line.startswith("\t")):
            current_interface["details"].append(line.strip())

    return interfaces, output

def print_simplified_ipconfig(l):
    interfaces, _ = run_ipconfig()
    print(f"Simplified Ipconfig\n{'='*l}")

    for interface in interfaces:
        print(f"Interface: {interface['name']}")
        for detail in interface["details"]:
            print(f"  {detail}")
        print()
    
    print('='*l)

def print_full_ipconfig(l):
    _, full_output = run_ipconfig()
    print(f"FULL Ipconfig\n{'='*l}")

    print(full_output)

    print('='*l)

def choice():
    pass
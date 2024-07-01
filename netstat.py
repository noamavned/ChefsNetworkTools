import subprocess

def run_netstat(timeout=10):
    try:
        result = subprocess.run(["netstat", "-an"], capture_output=True, text=True, timeout=timeout)
        netstat_output = result.stdout.strip()
    except subprocess.TimeoutExpired as e:
        netstat_output = e.stdout.decode('utf-8', 'ignore').strip()

    return netstat_output

def print_netstat(l, timeout=10):
    netstat_output = run_netstat(timeout)
    print("Netstat Output\n{'='*l}")
    print(netstat_output)
    print('='*l)
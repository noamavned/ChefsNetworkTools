import subprocess


def run_hostname():
    result = subprocess.run(["hostname"], capture_output=True, text=True)
    hostname = result.stdout.strip()
    return hostname

def print_hostname(l):
    hostname = run_hostname()
    print(f"Hostname: {hostname}\n{'='*l}")
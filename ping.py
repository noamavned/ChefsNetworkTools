import subprocess


def run_ping(path):
    result = subprocess.run(["ping", path], capture_output=True, text=True)
    ping = result.stdout.strip()
    return ping

def print_ping(path, l):
    ping = run_ping(path)
    print(f"Ping -> {path}\n{'='*l}\n{ping}\n{'='*l}")
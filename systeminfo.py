import subprocess


def run_systeminfo():
    result = subprocess.run(["systeminfo"], capture_output=True, text=True)
    systeminfo = result.stdout.strip()
    return systeminfo

def print_systeminfo(l):
    systeminfo = run_systeminfo()
    print(f"systeminfo\n{'='*l}\n{systeminfo}\n{'='*l}")
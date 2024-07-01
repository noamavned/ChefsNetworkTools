import subprocess
import re
import cutie


def get_profiles():
    result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    output = result.stdout.strip()
    profiles = re.findall(r'All User Profile\s+:\s+(.+)', output)
    return profiles

def select_profile(l):
    profiles = get_profiles()
    print('CHOOSE PROFILE')
    print("-"*l)
    profile = profiles[cutie.select(profiles, selected_index=0)]
    return profile

def get_info(profile):
    result = subprocess.run(["netsh", "wlan", "show", "profile", f'name={profile}', 'key=clear'], capture_output=True, text=True)
    output = result.stdout.strip()
    return output

def get_pass(profile):
    key_content = re.search(r'Key Content\s+:\s+(\S+)', get_info(profile))
    key_content = key_content.group(1) if key_content else "Password was not found"
    return key_content

def print_profiles(l):
    profiles_output = get_profiles()
    print(f"Profiles on interface Wi-Fi\n{'='*l}")
    for i in profiles_output:
        print(f'-  {i}\n')
    print('='*l)

def print_pass(profile, l):
    print(f"{'='*l}\nPassword for {profile}: {get_pass(profile)}")
    print('='*l)

def print_info(profile, l):
    print(f"Info for {profile}\n{'='*l}\n{get_info(profile)}")
    print('='*l)
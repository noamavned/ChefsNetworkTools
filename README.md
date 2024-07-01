# Network Tools

**Network Tools** is a Python script that provides various network-related functionalities such as ping, ipconfig, system information, netstat, hostname, and WiFi history.

## Features

- **Ping**: Ping a default or custom URL.
- **Ipconfig**: Display full or simplified ipconfig information.
- **Systeminfo**: Display system information.
- **Netstat**: Display network statistics.
- **Hostname**: Display the hostname.
- **WiFi History**: 
  - See profiles on interface Wi-Fi.
  - Get the password of a profile on interface Wi-Fi.
  - Get full info of a profile on interface Wi-Fi.

## Requirements

- Python 3
- Required modules:
  - `cutie`

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/noamavned/ChefsNetworkTools.git
   cd ChefsNetworkTools

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Window CMD use `.\env\Scripts\activate`
   I recommend using Powershell so the command will be `.\env\Scripts\Activate.ps1`

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt

4. **Run the script**:
   ```sh
   python -u app.py

## Navigate through the menu:

- Use arrow keys to select an action.
- Press Enter to confirm the selection.
- Follow the prompts for each action.

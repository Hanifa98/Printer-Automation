# Network Printer Installer

This Python script is a GUI-based application that allows users to scan for a network printer, download its driver, and install the printer on a Windows machine. The script uses `tkinter` for the GUI, `os` for network communication, and `subprocess` to handle the printer installation process.

## Features

- **Printer Accessibility Check**: Pings the printer to verify if it's accessible via the network.
- **Driver Download**: Downloads the printer driver from a provided URL.
- **Printer Installation**: Installs the printer on a Windows machine using the provided driver.

## Requirements

Before using this application, make sure you have the following:

- Python 3.x
- Required Python packages:
  - `requests`
  - `tkinter`
  
To install the required package, run:

```bash
pip install requests
```

`tkinter` is usually included with Python, but if it's missing, install it through your OS package manager.

## Usage

1. **Clone or Download the Script**  
   Clone the repository or download the script from [this link](#).

2. **Run the Script**  
   Open a terminal or command prompt and navigate to the directory where the script is located. Then, run the following command:

   ```bash
   python script_name.py
   ```

3. **Using the Application**  
   - Enter the printer IP address in the GUI.
   - Click **Scan Printer** to check if the printer is accessible.
   - Click **Install Printer** to download the printer driver and install the printer.

## Configuration

- **Printer IP Address**: Update the hardcoded printer IP address in the script or modify the input to accept dynamic IP addresses.
- **Printer Driver URL**: Provide the appropriate download URL for the printer driver.

## Notes

- This script is designed for **Windows**. The printer installation command (`subprocess.run(...)`) uses `rundll32` to invoke the printer installation UI.
- If you're using Linux or macOS, modify the `install_printer` function to use the appropriate system commands.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Troubleshooting

- Ensure the printer IP address is correct and accessible from the local network.
- Check that the driver URL is valid and accessible.
- For Linux/macOS, update the `install_printer` function to use compatible installation commands.


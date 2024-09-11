import os
import subprocess
import requests
import tkinter as tk
from tkinter import messagebox

# Function to check if the printer IP is accessible
def is_printer_accessible(ip):
    response = os.system(f"ping -n 1 {ip}")  # Use -c 1 for Linux/macOS
    return response == 0

# Function to download the printer driver
def download_driver(driver_url, save_path):
    response = requests.get(driver_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    return save_path

# Function to install the printer (simplified for Windows)
def install_printer(ip, driver_path):
    try:
        subprocess.run(["rundll32", "printui.dll", "PrintUIEntry", "/if", f"/b {ip}", f"/f {driver_path}", f"/r {ip}", "/m", "HP LaserJet P1005"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# GUI application class
class PrinterInstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Printer Installer")
        
        self.label = tk.Label(root, text="Printer IP: 10.157.100.101")
        self.label.pack(pady=10)
        
        self.scan_button = tk.Button(root, text="Scan Printer", command=self.scan_printer)
        self.scan_button.pack(pady=10)
        
        self.install_button = tk.Button(root, text="Install Printer", command=self.install_printer)
        self.install_button.pack(pady=10)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
        
    def scan_printer(self):
        ip = "printer IP" #printer ip
        if is_printer_accessible(ip):
            self.status_label.config(text=f"Printer at {ip} is accessible")
        else:
            self.status_label.config(text=f"Printer at {ip} is NOT accessible")
    
    def install_printer(self):
        ip = "Printer IP" #insert printer IP
        driver_url = "Printer driver" #instert download url from web page
        driver_path = download_driver(driver_url, f"{ip}_driver.inf")
        
        if install_printer(ip, driver_path):
            messagebox.showinfo("Success", f"Printer at {ip} installed successfully.")
        else:
            messagebox.showerror("Failure", f"Failed to install printer at {ip}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrinterInstallerApp(root)
    root.mainloop()

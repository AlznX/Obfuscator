import os
import sys
import socket
import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your Discord webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1294835451013628024/CB1Y7XqFIaAltZrjgUBGt-77ccluLnOXBgLucO_ELm2FOhPbwmlqXHkoQ2DUVPaX1kq0"

def log_to_discord(message):
    data = {
        "content": message
    }
    requests.post(WEBHOOK_URL, json=data)

def kill_roblox():
    os.system("taskkill /f /im RobloxPlayerBeta.exe")

def on_confirm():
    # Get the computer name
    computer_name = socket.gethostname()
    
    # Log the action to Discord
    log_message = f"{computer_name} has just used your Python script to close Roblox."
    log_to_discord(log_message)
    
    # Kill Roblox
    kill_roblox()
    root.quit()

def on_cancel():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Close Roblox")
root.geometry("300x100")

# Create the confirmation message
message = tk.Label(root, text="Are you sure you want to close Roblox?")
message.pack(pady=10)

# Create the Yes and No buttons
yes_button = tk.Button(root, text="Yes", command=on_confirm)
yes_button.pack(side=tk.LEFT, padx=20)

no_button = tk.Button(root, text="No", command=on_cancel)
no_button.pack(side=tk.RIGHT, padx=20)

# Start the GUI event loop
root.mainloop()

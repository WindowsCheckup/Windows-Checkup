import tkinter as tk
from tkinter import ttk, messagebox
import psutil
import platform
import socket

class WindowsCheckupTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows Checkup Tool")
        self.root.geometry("400x500")

        # Title label
        ttk.Label(self.root, text="System Checkup", font=("Arial", 16)).pack(pady=10)

        # System Info Frame
        self.system_info_frame = ttk.LabelFrame(self.root, text="System Information")
        self.system_info_frame.pack(fill="both", padx=10, pady=5)
        
        # System info
        self.system_info_text = tk.StringVar()
        self.system_info_label = ttk.Label(self.system_info_frame, textvariable=self.system_info_text)
        self.system_info_label.pack(padx=10, pady=5)
        
        # Performance Frame
        self.performance_frame = ttk.LabelFrame(self.root, text="Performance Metrics")
        self.performance_frame.pack(fill="both", padx=10, pady=5)
        
        # CPU usage
        self.cpu_usage_text = tk.StringVar()
        self.cpu_usage_label = ttk.Label(self.performance_frame, textvariable=self.cpu_usage_text)
        self.cpu_usage_label.pack(padx=10, pady=5)
        
        # Memory usage
        self.memory_usage_text = tk.StringVar()
        self.memory_usage_label = ttk.Label(self.performance_frame, textvariable=self.memory_usage_text)
        self.memory_usage_label.pack(padx=10, pady=5)
        
        # Disk usage
        self.disk_usage_text = tk.StringVar()
        self.disk_usage_label = ttk.Label(self.performance_frame, textvariable=self.disk_usage_text)
        self.disk_usage_label.pack(padx=10, pady=5)

        # Buttons
        ttk.Button(self.root, text="Refresh", command=self.update_metrics).pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

        # Initialize metrics
        self.update_metrics()

    def update_metrics(self):
        # Get system information
        system_info = f"OS: {platform.system()} {platform.release()}\n" \
                      f"Hostname: {socket.gethostname()}\n" \
                      f"IP Address: {socket.gethostbyname(socket.gethostname())}\n" \
                      f"Processor: {platform.processor()}\n"
        self.system_info_text.set(system_info)
        
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        self.cpu_usage_text.set(f"CPU Usage: {cpu_usage}%")
        
        # Get memory usage
        memory_info = psutil.virtual_memory()
        memory_usage = f"Memory Usage: {memory_info.percent}% " \
                       f"({memory_info.used // (1024 ** 2)} MB / {memory_info.total // (1024 ** 2)} MB)"
        self.memory_usage_text.set(memory_usage)
        
        # Get disk usage
        disk_info = psutil.disk_usage('/')
        disk_usage = f"Disk Usage: {disk_info.percent}% " \
                     f"({disk_info.used // (1024 ** 3)} GB / {disk_info.total // (1024 ** 3)} GB)"
        self.disk_usage_text.set(disk_usage)

# Main application
root = tk.Tk()
app = WindowsCheckupTool(root)
root.mainloop()

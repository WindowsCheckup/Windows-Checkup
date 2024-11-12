# Windows Checkup Tool

A simple Windows checkup tool built in Python that provides real-time system information and performance metrics through a graphical user interface (GUI). The tool displays essential information about CPU usage, memory usage, disk usage, and other system details.

## Features

- **System Information**: Displays OS details, hostname, IP address, and processor info.
- **Performance Metrics**:
  - CPU usage in real-time.
  - Memory usage in both percentage and actual MB.
  - Disk usage in both percentage and actual GB.
- **Refresh Button**: Manually refreshes system metrics.
- **Exit Button**: Closes the tool.

## Prerequisites

This tool requires:
- **Python 3.6+**
- **`psutil` library** for system metrics.

To install `psutil`, run:
```bash
pip install psutil

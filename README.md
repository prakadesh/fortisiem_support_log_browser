# FortiSIEM Support Log Viewer

FortiSIEM Support Log Viewer is a Python application designed to extract and view logs from FortiSIEM systems. This application offers a graphical interface to easily navigate and analyze log files, both locally and over SSH. The application supports various features, including SSH connections, extracting log files from tar archives, and viewing log contents.

## Features

- **SSH Connection**: Connect to remote servers to fetch log files.
- **Tarball Extraction**: Extract log files from tar archives.
- **Log Viewing**: View backend and appserver logs with syntax highlighting.
- **System Information**: Display system information from log files.
- **Search and Filter Logs**: Search for specific events or errors in the logs.
- **Theme Support**: Switch between light, dark, and system themes.

## Installation

The script automatically installs the required packages if they are not already installed.

## Usage

### Running the Application

To run the application, execute the following command:

**Windows**
```shell
pythonw log_browser.py
```

**MacOS/Linux GUI**
```shell
python log_browser.py
```

### SSH Connection

1. Open the application.
2. Go to `File > Open via SSH`.
3. Enter the SSH credentials and connect to the remote server.
4. Fetch logs from the server.

### Opening Local Log Files

1. Open the application.
2. Go to `File > Open tar` to select a tarball containing the logs.
3. Go to `File > Open Existing Directory` to select a directory containing the logs.

### Viewing Logs

- Select the desired date from the dropdown menu to view logs for that specific date.
- Double-click on log entries to view detailed log messages.

### Themes

Switch between light, dark, and system themes from `Edit > Preferences`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any enhancements or bug fixes.

## Acknowledgements

Special thanks to the developers of the libraries used in this project, including Tkinter, Paramiko, SCP, ttkthemes, Pillow, and others.

### Downloading an Existing Remote Archive

1. Go to `File > Download Remote File` and enter the same SSH credentials used for the SSH log workflow.
2. Select one of the ten newest `.tar` archives in the remote `/tmp` directory.
3. Choose a new local destination. Existing files are never overwritten.
4. The archive is downloaded directly with SFTP, with transferred bytes, percentage, speed, and ETA shown during the transfer. The completed download is size-verified and its SHA256 digest is displayed.

This workflow never runs `phziplogs`, splits archives, or changes remote files. Cancelling or a failed transfer removes the local partial file.

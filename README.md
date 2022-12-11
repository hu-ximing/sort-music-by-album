English | [中文](./README_cn.md)

# Sorting music files by their albums

This script will move music files belonging to the same album to directories named after their album names, directories that do not exist will be created. The script parses the album information contained in the file's metadata and handles special characters that are not suitable for inclusion in the path.

**Important**:

When running on Microsoft Windows, please ensure you disable the [Maximum Path Length Limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell). To do that, run the following command in Administrator PowerShell.

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
-Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

Usage:

```shell
python3 sort.py /path/to/files
```

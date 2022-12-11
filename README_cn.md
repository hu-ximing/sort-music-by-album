[English](./README.md) | 中文

# 根据专辑归类音乐文件

这个脚本会把属于相同专辑的音乐文件移动到以它们专辑名称命名的目录中，不存在的目录会被创建。脚本会分析包含在文件元数据中的专辑信息，并处理不适合包含在路径中的特殊字符。仅当至少有3个文件属于同一专辑才会创建目录。

**重要提示**:

在 Microsoft Windows 上运行时，请确保您已关闭[最大路径长度限制](https://learn.microsoft.com/zh-cn/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell)。要做到这一点，在管理员 PowerShell 中执行以下命令。

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
-Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

用法:

```shell
python3 sort.py /path/to/files
```

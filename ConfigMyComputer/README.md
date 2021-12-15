# Install WSL

- [WSL官方安装步骤](https://docs.microsoft.com/en-us/windows/wsl/install)
  - 我按照官方步骤没有不能直接wsl --install，成功的步骤如下：
    1. 检查Windows Subsystem for Linux是否为enabled，更改后重启
    2. 在Microsoft Store下载Debian
    3. 在Debian里输入UNIX username，新建
    4. 回到Powershell for Administrator, 运行wsl，成功
  - 安装wsl2的步骤：
    1. wsl --set-default-version 2，设置默认wsl环境（？）
    2. wsl -l -v 查看所有Distro的版本，但我在操作上一步以后，Debian依然显示为1
    3. wsl --set-version Debian 2，要求启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化
    4. bcdedit /set hypervisorlaunchtype auto，重启 [参考](https://www.jianshu.com/p/12040389e0e2)


- 为什么wsl2?
  - wsl1：假Linux内核，文件都存在windows上，如果符合这种文件存储习惯，wsl1更快
  - wsl2：真Linux内核，可跑Docker，但是读Windows文件较慢
- 

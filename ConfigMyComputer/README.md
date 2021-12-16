# Install WSL

- [WSL官方安装步骤](https://docs.microsoft.com/en-us/windows/wsl/install)
  - 我按照官方步骤没有不能直接wsl --install，成功的步骤如下：
    1. 检查Windows Subsystem for Linux是否为enabled，更改后重启
    2. 开启开发者模式，重启
    3. 在Microsoft Store下载Debian
    4. 在Debian里输入UNIX username，新建
    5. 回到Powershell for Administrator, 运行wsl，成功
  - 安装wsl2的步骤：
    1. wsl --set-default-version 2，设置默认wsl环境（？）
    2. wsl -l -v 查看所有Distro的版本，但我在操作上一步以后，Debian依然显示为1
    3. wsl --set-version Debian 2，要求启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化
        - ~~bcdedit /set hypervisorlaunchtype auto，重启 [参考](https://www.jianshu.com/p/12040389e0e2), 但是没用~~
        - 进入BIOS模式，搜索virtual相关选项，Disabled -> Enabled
  - **修改Linux镜像的步骤**：[参考](https://blog.csdn.net/qq_39263240/article/details/79342582)，记得sudo
    - 直接改GPG Error，理论上应该如下操作，不过我缺失了 gnupg, gnupg2 and gnupg1这些包，得先装上
      apt-key adv --recv-keys --keyserver keyserver.ubuntu.com XXXXXX
    
      apt-get update



## 延伸阅读
- [为什么wsl2?](https://docs.microsoft.com/en-us/windows/wsl/compare-versions)
  - wsl1：假Linux内核，文件都存在windows上，如果符合这种文件存储习惯，wsl1更快
  - wsl2：真Linux内核，可跑Docker，但是读Windows文件较慢
- vim关键快捷键：
  - 删除行：dd
  - 保存退出：https://blog.csdn.net/matrix_google/article/details/76164297

<br>
[安装VSCode与Git的官方操作](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

# Install VSCode
1. 安装VSCode包 64bit Installer on Win，[网址](https://code.visualstudio.com/download#)
2. 安装相关remote development相关extension
3. sudo apt-get update: 更新Debian
4. sudo apt-get install wget ca-certificates: 安装wget以从web server下载数据；安装ca-certificatestes通过SSL相关验证
5. 

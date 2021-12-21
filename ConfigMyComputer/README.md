# Install WSL（Debian）

- **[WSL官方安装步骤](https://docs.microsoft.com/en-us/windows/wsl/install)**
  - 我按照官方步骤不能直接wsl --install，成功的步骤如下：
    1. 检查Windows Subsystem for Linux是否为enabled，更改后重启
    2. 开启开发者模式，重启
    3. 在Microsoft Store下载Debian
    4. 在Debian里输入UNIX username，新建
    5. 回到Powershell for Administrator, 运行wsl，成功
  - **安装wsl2的步骤**：
    1. wsl --set-default-version 2，设置默认wsl环境（？）
    2. wsl -l -v 查看所有Distro的版本，但我在操作上一步以后，Debian依然显示为1
    3. wsl --set-version Debian 2，要求启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化
        - ~~bcdedit /set hypervisorlaunchtype auto，重启 [参考](https://www.jianshu.com/p/12040389e0e2), 但是没用~~
        - 进入BIOS模式，搜索virtual相关选项，Disabled -> Enabled
  - **查看wsl系统文件夹**： 在Debian里输入 explorer.exe .
- **修改Linux镜像的步骤**：[参考](https://blog.csdn.net/qq_38238114/article/details/104584376)，记得sudo
  - **使用Debian源**：修改源之前看清楚这到底是Debian还是Ubuntu的，如果用了Ubuntu的源的话，大概率会mess up下载的包的版本，导致unmet dependencies
  - **使用http源**：Debian未自动支持HTTPS源，如果使用，先sudo apt install apt-transport-https ca-certificates
  - **报错 No PUBKEY的话**：
<!--     直接改GPG Error，理论上应该如下操作，不过我缺失了 gnupg, gnupg2 and gnupg1这些包，得先装上 -->
    - sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 648ACFD622F3D138
      - 在key之前或许需要加上0X，表示十六进制整数
      - apt-get install dirmngr
    - apt-get update
- **安装推荐包**，如vim, build-essential：[参考](https://sysin.org/blog/debian-11-install/#17-%E5%AE%89%E8%A3%85%E5%BF%85%E5%A4%87%E5%B7%A5%E5%85%B7)
  - 目前已安装包：vim, build-essential
  - 但在所有的安装之前，记得养成 apt-get update 的好习惯
- **自绝经脉法**：出现恶心的unmet dependencies问题的时候，实在无法解决就删Debian重来吧


## 延伸阅读
- [为什么wsl2?](https://docs.microsoft.com/en-us/windows/wsl/compare-versions)
  - wsl1：假Linux内核，文件都存在windows上，如果符合这种文件存储习惯，wsl1更快
  - wsl2：真Linux内核，可跑Docker，但是读Windows文件较慢
- vim关键快捷键：
  - 删除行：dd
  - 保存退出：https://blog.csdn.net/matrix_google/article/details/76164297

</br>
</br>

[安装VSCode与Git的官方操作](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)

# Install VSCode
1. 安装VSCode包 64bit Installer on Win，[网址](https://code.visualstudio.com/download#)
2. 安装相关remote development相关extension
3. sudo apt-get update: 更新Debian
4. sudo apt-get install wget ca-certificates: 安装wget以从web server下载数据；安装ca-certificatestes通过SSL相关验证

# Install Git
- sudo apt-get install git-all --[Git官网](https://github.com/git-guides/install-git)

# Install Python
- [教程](https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/)
  - 在安装前注意检查linux当前所在位置，建议直接通过网页下载Python tar.gz，然后在linux中进行解压
- 配置pyenv+virtualenv: https://github.com/XinyueYu16/Computer_Basics_Notes/issues/4

# Install Jupyter + Config Kernal
【或许我应该尝试抛弃jupyter notebook,转投VSCode Jupyter?】
- Jupyter 使用 pip install jupyter 下载，顺便下载ipykernel, ipython 
- Jupyter 必备 nbextension: jupyter contrib nbextension install --user
- config Kernel: https://albertauyeung.github.io/2020/08/17/pyenv-jupyter.html/#adding-kernels-to-jupyter




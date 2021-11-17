# 环境控制、版本控制、GIT



### 环境控制三重境界

本地裸跑 —— 相信运气

pyenv跑 —— 改变python及包环境，相信软件依赖

docker —— 相信科学（但是windows的docker需要wsl2，而wsl2虽然有linux内核但是当文件都在windows上的时候存取会变慢……所以除了使用docker时，我都是用wsl





### 实际操作

一些为了达成版本控制和同事大神的探讨：

- 当同项目的脚本来源有多个repo时，如何在一个repo里记录多个repo脚本的变化？
  - ……建议是另一个repo也一起git commit
  - 或者比如R装包的话，可以把从tar.gz装包的语句写进script里
  - 真的不可以放进一个repo吗？？？
- 用log和csv的时间戳将脚本和结果对应起来，不过有一定前提：
  - 在脚本生成csv/xlsx后不再修改数据
- 所有项目都git也有点重，可以尝试：
  - 保存**多版本代码**
- 一些良好习惯：
  - **用命令行跑脚本**，避免忽视Error
  - 写Jupyter Notebook时不要上下移动cell block，**不要有选择性地跑cell**
  - **commit前记得保存当前编辑过的脚本**

——版本控制保心护肝造福全家人人有责——





### git控制

1. 创建git: git init
2. 设置需要被track的文件：git add 
    - 只是记录需要被track，当他们发生改变的时候git status会提醒，但是不会保存快照；
    - 每一次文件被修改后都要add；
    - 不希望被track的文件可以放入.gitignore
3. 保存文件快照：git commit -m
    - 当前快照被保存至本地仓库
5. 查看历史版本：git log --pretty=oneline 
    - 可以取前6位数进行checkout
6. 回到快照节点：git checkout
    - 当前状态为HEAD
    - 当checkout到未被命名的分支以后，处于分离状态，detached HEAD
7. 强制回到状态：git reset --hard \[6位数\]
    - 确保回到你想要修改的分支上，再做这个操作
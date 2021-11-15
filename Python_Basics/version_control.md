# 环境控制、版本控制、GIT

## 环境控制

本地裸跑 —— 相信运气

pyenv跑 —— 改变python及包环境，相信软件依赖

docker —— 相信科学（但是windows的docker需要wsl2，而wsl2虽然有linux内核但是当文件都在windows上的时候存取会变慢……所以除了使用docker时，我都是用wsl

## git控制
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

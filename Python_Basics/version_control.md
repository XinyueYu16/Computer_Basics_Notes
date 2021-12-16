# 环境控制、版本控制、GIT

</br>

### 环境控制三重境界

本地裸跑 —— 相信运气

pyenv+virtualencv跑 —— 改变python及包环境，相信软件依赖(pyenv修改python环境，virtualenv控制项目包环境)

docker —— 相信科学（但是windows的docker需要wsl2，而wsl2虽然有linux内核但是当文件都在windows上的时候存取会变慢……所以除了使用docker时，我都是用wsl


</br>


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
  - 在切换branch后记得清除环境变量(global environment)

——版本控制保心护肝造福全家人人有责——


</br>


### git控制

1. 创建git: git init
2. 当从远程下载内容时: 
    - fetch: 只取不合, harmless
    - pull：取+合，建议只在空白branch上进行该操作
3. 开发时：
    - 任何开发都先branch到development_branch，**不要在main/master上进行add或commit**
    - 或者 git checkout -b new_branch_name，一键生成并切换到新branch
4. 设置需要被track的文件：git add 
    - 只是记录需要被track，当他们发生改变的时候git status会提醒，但是不会保存快照；
    - 每一次文件被修改后都要add；
    - 不希望被track的文件可以放入.gitignore
5. 暂存内容：[git stash](https://www.cnblogs.com/tocy/p/git-stash-reference.html)

    - 当你在当前分支的内容没有commit（不想让过多未完成commit污染log）没法checkout其他分支
    - git stash list: 查看所有被暂存的名称
    - git stash pop: 从list中去除最新暂存的一个，并且释放到当前空间
    - git stash apply: 根据指定名字释放到当前空间，默认第一个，不从list中删除
    - git stash drop stash@{0}: 删除指定的stash，但是注意每删除一次序号都会变……如果想要从上往下删，不停git stash drop stash@{0}就可以
    - git stash 会在远程仓库被共享吗?

6. 保存文件快照：git commit -m
    - 当前快照被保存至本地仓库

7. 查看历史版本：git log --pretty=oneline 
    - 可以取前6位数进行checkout

8. **回到快照节点：git checkout**
    - 当前状态为HEAD
    - 当checkout到未被命名的分支以后，处于分离状态，detached HEAD

9. 强制回到状态：git reset --hard \[6位数\]
    - 确保回到你想要修改的分支上，再做这个操作

10. 多commit合并: git squash
    - git rebase -i HEAD~3 
      - Linux里面莫名奇妙地不能这么做，但是Terminal/wsl可以
      - HEAD后面的~数量尽量要比需要squash的大，然后就可以看到尽可能多的commit
      - 在需要squash的行里 commit转成s

11. bump2version: bump2version major|minor|patch

12. 上传: git push
    - 第一次push的时候需要 git push --set-upstream origin branchname
    - 当远程的内容与本地内容不一致，且本地内容不是基于远程内容枝上分叉出来的时候，如果想采取本地更改，git push -f (不要试图 -f master或main)

### 其他git知识
- .gitkeep：
  - git无法追踪空文件夹，所以在空文件夹下放.gitkeep以便追踪
  - .gitkeep常被用来使git忽略一个文件夹下的所有文件，并保留该文件夹（这种用法需要在.gitignore中加入 `!.gitkeep` ）

    

**实例操作：**

- *开发petal过程中需要rebase新的master*：git stash save ->  git checkout -> git fetch -> git pull -> git checkout -> HEAD git rebase -> git stash apply-> git add -> git commit -> git push (git squash)




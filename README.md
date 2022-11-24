# git commmit
 - 要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
 - 关联一个远程库时必须给远程库指定一个名字，origin是默认习惯命名；
 - 关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
 - 此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；

  
## 参考链接
https://segmentfault.com/u/mataotao/articles?page=4

### **本地**

1. git init，初始化本地仓库 .git
2. git status -sb，显示当前所有文件的状态
3. git add 文件路径，用来将变动加到暂存区
4. git commit -m "信息"，用来正式提交变动，提交至 .git 仓库
5. 如果有新的变动，我们只需要依次执行 git add xxx 和 git commit -m 'xxx' 两个命令即可。
6. git log 查看变更历史
   
###  **上传更新(用ssh不要用http)**
* git remote add origin 
* git push -u origin master
  
### **更新**
* git add 文件路径
* git commit -m "上传了啥"
* git pull  （一定不要忘记这一个命令）
* git push


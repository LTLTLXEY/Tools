# 一个简单的Docker匹配命令执行脚本

#### 使用方法

* chmod +x edk.sh
  * -h                  :Help
  * -contid -s     :Only to stop and delete contid-docker
  * -contid -a     :Stop and delete all dockers that use the same image as the speciified container,and delete the image
  * -contid -sp   :Stop all dockers that use the same image as the specified container
  * -contid -st    :Start all dockers that use the same image as the specified container
  * -contid -re    :Restart the contid-docker
  * -contid -in    :Enter the contid-docker
  * -removealldo  :Stop and delete all running and stopped dockers
  * -removeallim  :Stop and delete all running and stopped dockers, and delete all images
* -contid替换为 docker的容器ID号
  * docker ps -a
* 所有操作不可逆，请谨慎操作
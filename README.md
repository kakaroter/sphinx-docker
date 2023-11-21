# 解压驱动并挂载驱动服务
unzip chromedriver_linux64.zip
# 挂载chromedriver
nohup ./chromedriver &
# 查看是否挂载成功
result=$(ps aux | grep -v grep | grep chromedriver)
if [-n $result];then
    echo "驱动挂载成功"
else
    echo "驱动挂载失败"
fi
# 安装部署自动化环境
sudo pip3 install python3-tk
sudo pi3 install python3-pyatspi
sudo pip3 install pillow==5.4.1
sudo pip3 install pyscreeze==0.1.28 
sudo pip3 install PyAutoGUI==0.9.53
sudo pip3 install selenium

清华源：https://pypi.tuna.tsinghua.edu.cn/simple/
注：[驱动下载地址](http://chromedriver.storage.googleapis.com/index.html)
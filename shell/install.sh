#!/bin/bash
# 安装脚本程序(root权限)

# 安装必要的软件和依赖库
apt-get install python3
apt-get install python3-pip
apt-get install git
apt-get install mysql-server
apt-get install firefox
apt-get install teamviewer

pip3 install requests
pip3 install selenium
pip3 install openpyxl
pip3 install PyMySQL
pip3 install pillow

# 在指定目录Clone项目
mkdir /data
mkdir /data/code
cd /data/code
git clone https://github.com/TauWu/auto_post.git

# 创建程序中需要的目录
mkdir /data/bin
mkdir /data/imgs
mkdir /data/docs
mkdir /data/config
chmod 777 -R /data

# 移动 浏览器、用户配置文件、共享文件夹
cp /data/code/auto_post/bin/test.user0.tar.gz /data/bin
cd /data/bin
tar zxvf test.user0.tar.gz
cp /data/code/auto_post/bin/geckodriver /bin/
cp /data/code/auto_post/bin/smb.conf /etc/samba/smb.conf

# 创建数据库
mysql -u root -p < /data/code/auto_post/database/create_database.sql

echo "安装完成，请按照提示发送房源信息表格和图片"
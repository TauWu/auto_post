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

# git基础配置
echo "请输入您的git用户名"
read username
git config --global user.name "$username"

echo "请输入您的git邮箱"
read email
git config --global user.email "$email"

# 在指定目录Clone项目
mkdir /data
mkdir /data/code
cd /data/code
git clone git@github.com:TauWu/auto_post.git

# 创建程序中需要的目录
mkdir /data/bin
mkdir /data/imgs
mkdir /data/docs
chmod 777 -R /data

# 移动 浏览器、用户配置文件、共享文件夹
cp /data/code/auto_post/bin/test.user0.tar.gz /data/bin
cd /data/bin
tar zxvf test.user0.tar.gz
cp /data/code/auto_post/bin/geckodriver /bin/
cp /data/code/auto_post/bin/smb.conf /etc/samba/smb.conf
cp /data/code/auto_post/shell/开始发布 ~/Desktop
cp /data/code/auto_post/shell/数据导入 ~/Desktop
cp /data/code/auto_post/shell/用户操作 ~/Desktop

# 创建数据库
mysql -u root -p < /data/code/auto_post/database/create_database.sql
cd auto_post
./auto_post_main.py

echo "安装完成，请按照提示发送房源信息表格和图片"
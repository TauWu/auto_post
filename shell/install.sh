#!/bin/bash
# 安装脚本程序(root权限)

# 安装必要的软件和依赖库
apt-get install python3
apt-get install python3-pip
apt-get install git
apt-get install mysql-server
apt-get install firefox 
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

# 创建程序中需要的目录
mkdir /data/bin
mkdir /data/imgs
chmod 777 -R /data
cp /data/code/auto_post/bin/test.user0.tar.gz /data/bin
cd /data/bin
tar zxvf test.user0.tar.gz

# 在指定目录Clone项目
mkdir /data
mkdir /data/code
cd /data/code
git clone git@github.com:TauWu/auto_post.git

# 创建数据库
mysql -u root -p < /data/code/auto_post/database/create_database.sql
cd auto_post
./auto_post_main.py
# AUTO_POST

## 基础信息

Author | CreateDate | ProjectName | ChineseName
--- | --- | --- | ---
Tau Woo | 2018-01-20 | auto_post | 58自动房源发帖工具

## 实现方法
- 1.读取用户整理好的房源信息模板，将整理好的数据经过初步筛选进入数据库中
- 2.读取用户配置好的发帖需求列表模板，从数据库筛选limit5倍数量的房源
- 3.从第一条需求开始，使用selenium自动操作浏览器完成发帖任务
>- 3.1有对发帖结果的监控
>- 3.2有对发帖过程图片上传超时的监控
>- 3.3有对不合格照片的像素处理和上传失败的监控

## OS
OS | Version
--- | ---
DevOS |Linux Deepin-15.5 (Debian 6.3.0-11)
DBOS | Ubuntu 5.4.0-6ubuntu1~16.04.4
MySQL | MySQL 14.14 Distrib 5.7.21, for Linux (i686)

## 软件依赖
### 软件
```bash
apt-get install python3
apt-get install python3-pip
apt-get install git
apt-get install mysql-server
apt-get install firefox
apt-get install teamviewer
```

### Python依赖库
```bash
pip3 install requests
pip3 install selenium
pip3 install openpyxl
pip3 install PyMySQL
pip3 install pillow

```
## 根目录介绍
目录 | 详情
--- | ---
bin | 依赖软件或静态的配置文件
constant | 常量
log | 日志输出目录
module | 工作模块
shell | 安装等脚本
util | 工具、基础模块
database | 数据库建表语句
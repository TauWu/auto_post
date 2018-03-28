# 创建链接
ln /data/code/auto_post/shell/开始发布 ~/Desktop/开始发布
ln /data/code/auto_post/shell/用户操作 ~/Desktop/用户操作
ln -s /data/imgs/ ~/Desktop/photos

# git基础配置
echo "请输入您的git用户名"
read username
git config --global user.name "$username"

echo "请输入您的git邮箱"
read email
git config --global user.email "$email"
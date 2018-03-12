use auto_post;

-- 用户表
CREATE TABLE `auto_post_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `username` varchar(20) NOT NULL COMMENT '登录名',
  `password` varchar(20) NOT NULL COMMENT '密码',
  `usertype` tinyint NOT NULL COMMENT '用户类型 1-只有安居客没有58账号 2-同时有安居客和58账号',
  `name` varchar(20) COMMENT '员工姓名',
  
  `deleted` int DEFAULT 0 COMMENT '删除标记',
  `modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近修改时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 推广房源信息表
CREATE TABLE `auto_post_house_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
  `community` varchar(30) NOT NULL COMMENT '小区名称',
  `floor` int NOT NULL COMMENT '楼层',
  `total_floor` int NOT NULL COMMENT '总楼层',
  `addr_dist` varchar(10) NOT NULL COMMENT '区域',
  `addr_busi` varchar(20) NOT NULL COMMENT '商圈地址',
  `addr_more` varchar(50) NOT NULL COMMENT '商圈详细地址',
  `area` int NOT NULL COMMENT '房间面积',
  `price` int NOT NULL COMMENT '房间租金',
  `pay_method` varchar(10) NOT NULL COMMENT '付款方式',
  `title` varchar(127) NOT NULL COMMENT '房源标题',
  
  `deleted` int NOT NULL DEFAULT 0 COMMENT '删除标记',
  `modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近修改时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
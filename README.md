
#爬取京东商品详情以及商品评论的爬虫。
以下为主要思路：
1. 爬虫代码(jd_comment_spiders.py)）；
删除表 DROP TABLE jd_skus ;
CREATE DATABASE jd_skus CHARACTER SET utf8 COLLATE utf8_general_ci;


创建京东商品表
CREATE TABLE `skus1` (
  `SKU_ID` varchar(100) NOT NULL default '',
  `SKU_INTRODUCE` longtext default NULL,
  `SKU_SIZE` longtext default NULL,
  `SKU_PRICE` longtext default NULL,
  `SKU_LABEL` longtext default NULL,
  `SKU_TITLE` longtext default NULL,
  `SKU_COMMENT_NUMS` varchar(100) default NULL,
  `SKU_GOOD_RATE` varchar(100) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
alter table skus add unique key(SKU_ID)  ;    设置ARTIST_ID 唯一不重复



CREATE TABLE `skus_label` (
  `SKU_ID` varchar(100) NOT NULL default '',
  `SHOP_SCORE` varchar(100) default NULL,
  `SKU_LABEL1` longtext default NULL,
  `SKU_LABEL3` longtext default NULL,
  `SKU_LABEL5` longtext default NULL,
  `SKU_LABEL7` longtext default NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
   设置ARTIST_ID 唯一不重复

创建京东商品评论表
CREATE TABLE `sku_comments` (
  `SKU_ID` varchar(100) NOT NULL default '',
  `COMMENTS_LENS` varchar(100) default NULL,
  `COMMENTS_LIKE_NUMS` varchar(100) default NULL,
  `COMMENTS_REPLY_NUMS` varchar(100) default NULL,
  `COMMENTS_DETAILS` longtext default NULL,
  `COMMENTS_LEVE` longtext default NULL,
  `COMMENTS_TIME` longtext default NULL,
  `COMMENTS_SED_DETAILS` longtext default NULL,
  `COMMENTS_SED_TIME` longtext default NULL,
  `COMMENTS_SED_FIR_DAY` varchar(100) default NULL
)ENGINE=MyISAM DEFAULT CHARSET=utf8;



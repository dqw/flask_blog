-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2013 年 04 月 16 日 23:36
-- 服务器版本: 5.5.29
-- PHP 版本: 5.4.14-1~precise+1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `flask_blog`
--

-- --------------------------------------------------------

--
-- 表的结构 `fb_post`
--

CREATE TABLE IF NOT EXISTS `fb_post` (
  `post_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `post_author` int(11) NOT NULL DEFAULT '0',
  `post_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_title` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `post_content` text COLLATE utf8_unicode_ci NOT NULL,
  `post_modified` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `fb_post`
--

INSERT INTO `fb_post` (`post_id`, `post_author`, `post_date`, `post_title`, `post_content`, `post_modified`) VALUES
(2, 1, '2013-04-16 00:00:00', 'aa', 'bb', '2013-04-16 00:00:00');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

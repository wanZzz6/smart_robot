/*
 Navicat Premium Data Transfer

 Source Server         : 服务器
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : ***
 Source Schema         : QA

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 19/04/2019 13:59:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for QA_list
-- ----------------------------
DROP TABLE IF EXISTS `QA_list`;
CREATE TABLE `QA_list`  (
  `id` int(11) NOT NULL,
  `question` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `answer` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of QA_list
-- ----------------------------
INSERT INTO `QA_list` VALUES (0, '你叫什么名字', '1、Targaryan家族的风暴降生丹妮莉丝坦格利安一世,不焚者,弥林女王,安达尔人和先民的女王,大草原上的卡丽熙,解放者以及龙之母。\r\n1、Targaryan家族的风暴降生丹妮莉丝坦格利安一世,不焚者,弥林女王,安达尔人和先民的女王,大草原上的卡丽熙,解放者以及龙之母。\r\n');
INSERT INTO `QA_list` VALUES (1, '你好', 'Hi');
INSERT INTO `QA_list` VALUES (2, '你今年多大了', '22岁');
INSERT INTO `QA_list` VALUES (3, '说一段英语', 'sorry,the number you dailed is busy now The subscriber you dialed is busy now. Please redial later.');
INSERT INTO `QA_list` VALUES (4, '屏幕截图', ',');
INSERT INTO `QA_list` VALUES (5, '我想听音乐', ',');
INSERT INTO `QA_list` VALUES (6, '我想敲代码', ',');
INSERT INTO `QA_list` VALUES (7, '百度搜索', ',');
INSERT INTO `QA_list` VALUES (8, '打开记事本', ',');
INSERT INTO `QA_list` VALUES (9, '播放音乐', ',');


SET FOREIGN_KEY_CHECKS = 1;

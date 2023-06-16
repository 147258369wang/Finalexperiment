/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50730
 Source Host           : localhost:3306
 Source Schema         : store_management

 Target Server Type    : MySQL
 Target Server Version : 50730
 File Encoding         : 65001

 Date: 16/06/2023 21:07:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cargo
-- ----------------------------
DROP TABLE IF EXISTS `cargo`;
CREATE TABLE `cargo`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NULL DEFAULT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `num` decimal(10, 2) NULL DEFAULT NULL,
  `owner_id` int(11) NULL DEFAULT NULL,
  `store_id` int(11) NULL DEFAULT NULL,
  `status` int(11) NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cargo
-- ----------------------------
INSERT INTO `cargo` VALUES (17, 1, '花生', 0.00, 2, 1, NULL, '2023-06-07 13:12:03');
INSERT INTO `cargo` VALUES (18, 2, '海带', 0.00, 2, 2, NULL, '2023-06-07 13:12:17');
INSERT INTO `cargo` VALUES (19, 3, '罗非鱼', 0.00, 2, 3, NULL, '2023-06-07 13:12:34');

-- ----------------------------
-- Table structure for in_store
-- ----------------------------
DROP TABLE IF EXISTS `in_store`;
CREATE TABLE `in_store`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo_id` int(11) NULL DEFAULT NULL,
  `owner_id` int(11) NULL DEFAULT NULL,
  `store_id` int(11) NULL DEFAULT NULL,
  `num` decimal(10, 2) NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  `status` int(11) NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of in_store
-- ----------------------------
INSERT INTO `in_store` VALUES (20, 17, 2, 1, 20.00, '2023-06-07 13:12:03', 1);
INSERT INTO `in_store` VALUES (21, 18, 2, 2, 20.00, '2023-06-07 13:12:19', 1);
INSERT INTO `in_store` VALUES (22, 19, 2, 3, 20.00, '2023-06-07 13:12:35', 1);

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `cargo_id` int(11) NULL DEFAULT NULL,
  `num` decimal(10, 2) NULL DEFAULT NULL,
  `status` int(11) NULL DEFAULT 1,
  `time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES (6, 14, 17, 20.00, 2, '2023-06-07 13:13:12');
INSERT INTO `order` VALUES (7, 14, 18, 20.00, 2, '2023-06-07 13:13:15');
INSERT INTO `order` VALUES (8, 14, 19, 20.00, 2, '2023-06-07 13:13:17');

-- ----------------------------
-- Table structure for out_store
-- ----------------------------
DROP TABLE IF EXISTS `out_store`;
CREATE TABLE `out_store`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NULL DEFAULT NULL,
  `store_id` int(11) NULL DEFAULT NULL,
  `num` decimal(10, 2) NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP,
  `status` int(11) NULL DEFAULT 1,
  `owner_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of out_store
-- ----------------------------
INSERT INTO `out_store` VALUES (6, 17, 14, 1, 20.00, '2023-06-07 13:13:12', 1, 2);
INSERT INTO `out_store` VALUES (7, 18, 14, 2, 20.00, '2023-06-07 13:13:15', 1, 2);
INSERT INTO `out_store` VALUES (8, 19, 14, 3, 20.00, '2023-06-07 13:13:18', 1, 2);

-- ----------------------------
-- Table structure for store
-- ----------------------------
DROP TABLE IF EXISTS `store`;
CREATE TABLE `store`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` int(11) NULL DEFAULT NULL,
  `capacity` decimal(10, 2) NULL DEFAULT NULL COMMENT '容量',
  `unit` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '容量单位',
  `exist_amount` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of store
-- ----------------------------
INSERT INTO `store` VALUES (1, '干货仓库', 1, 200.00, '立方米', 0.00);
INSERT INTO `store` VALUES (2, '湿货仓库', 2, 200.00, '立方米', 0.00);
INSERT INTO `store` VALUES (3, '冷货仓库', 3, 100.00, '立方米', 0.00);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `account` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `password` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tel` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `type` int(11) NULL DEFAULT 3,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '管理员', 'admin', '123456', NULL, 1);
INSERT INTO `user` VALUES (2, '张三', 'sup', '123456', '13876509340', 2);
INSERT INTO `user` VALUES (14, '王五', 'cus', '123456', '16578958890', 3);

SET FOREIGN_KEY_CHECKS = 1;

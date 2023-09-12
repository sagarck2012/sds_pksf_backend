/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.38-MariaDB : Database - pksfdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pksfdb` /*!40100 DEFAULT CHARACTER SET utf8 */;

/*Table structure for table `farm_crop` */

DROP TABLE IF EXISTS `farm_crop`;

CREATE TABLE `farm_crop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `farm_crop` */

insert  into `farm_crop`(`id`,`name`,`created_at`,`created_by`,`last_updated_at`,`last_updated_by`) values (1,'Grain',NULL,'',NULL,''),(2,'Pulse',NULL,'',NULL,''),(3,'Oil',NULL,'',NULL,''),(4,'Spices',NULL,'',NULL,''),(5,'Vegetable',NULL,'',NULL,''),(6,'Tuber',NULL,'',NULL,''),(7,'Fruit',NULL,'',NULL,''),(8,'Flower',NULL,'',NULL,''),(9,'Cash Crop',NULL,'',NULL,'');

/*Table structure for table `farm_croptype` */

DROP TABLE IF EXISTS `farm_croptype`;

CREATE TABLE `farm_croptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `crop_id` int(11) NOT NULL,
  `local_name` varchar(70) DEFAULT NULL,
  `major_nutrient` varchar(70) DEFAULT NULL,
  `photo` longtext,
  `scientific_name` varchar(70) DEFAULT NULL,
  `seasonal` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` (`crop_id`),
  CONSTRAINT `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `farm_croptype` */

insert  into `farm_croptype`(`id`,`name`,`created_at`,`created_by`,`last_updated_at`,`last_updated_by`,`crop_id`,`local_name`,`major_nutrient`,`photo`,`scientific_name`,`seasonal`) values (3,'Paddy','2020-11-10 09:43:33.782030','2','2020-11-10 09:43:33.782030','2',1,'Dhan','\"Energy	121kcal, Fat 0.38g, Saturated Fats 0.09g, Monounsaturated Fats','','Oryza sativa',0),(4,'TEST',NULL,'2',NULL,'2',1,NULL,NULL,NULL,NULL,0),(5,'TEST',NULL,'2',NULL,'2',1,NULL,NULL,NULL,NULL,0),(6,'test',NULL,'2',NULL,'2',1,NULL,NULL,NULL,NULL,0),(7,'test',NULL,'2',NULL,'2',1,NULL,NULL,NULL,NULL,0);

/*Table structure for table `farm_vegetable` */

DROP TABLE IF EXISTS `farm_vegetable`;

CREATE TABLE `farm_vegetable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `soil_type` varchar(255) NOT NULL,
  `harvesting_period` varchar(100) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `vegetable_type_id` int(11) NOT NULL,
  `expected_production` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` (`vegetable_type_id`),
  CONSTRAINT `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` FOREIGN KEY (`vegetable_type_id`) REFERENCES `farm_croptype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `farm_vegetable` */

insert  into `farm_vegetable`(`id`,`name`,`soil_type`,`harvesting_period`,`created_at`,`created_by`,`last_updated_at`,`last_updated_by`,`vegetable_type_id`,`expected_production`) values (4,'BRRI  52(Ropa Amon)- Sorna','Low land & flood affected area','June(North Bengal), July(Others area)','2020-11-10 09:44:20.219939','2','2020-11-10 09:44:20.219939','2',3,'4-5 Ton'),(5,'BRRI  51(Ropa Amon)','Low land & flood affected area','June(North Bengal), July(Others area)','2020-11-10 09:44:47.307241','2','2020-11-10 09:44:47.307241','2',3,'4-5 Ton'),(6,'BRRI 49(Ropa Amon)-Nazirsal','Doash, Atel','June-July','2020-11-10 09:45:22.907788','2','2020-11-10 09:45:22.907788','2',3,'5-5.5 Ton'),(7,'BRRI  50(Ropa Boro)-Fragrant rice','Bele Doash, Atel Doash, High and medium elevation land','December','2020-11-10 09:45:54.626666','2','2020-11-10 09:45:54.626666','2',3,'6-6.5 Ton');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

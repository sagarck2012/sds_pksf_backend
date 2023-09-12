-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: pksfdb
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `barcodegenerator_barcode`
--

DROP TABLE IF EXISTS `barcodegenerator_barcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `barcodegenerator_barcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cratemanagement_crate`
--

DROP TABLE IF EXISTS `cratemanagement_crate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cratemanagement_crate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crate_no` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `total_number_of_package` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cratemanagement_package`
--

DROP TABLE IF EXISTS `cratemanagement_package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cratemanagement_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `package_code` varchar(20) NOT NULL,
  `weight` int(11) NOT NULL,
  `packaging_date` datetime(6) DEFAULT NULL,
  `vegetable_type` varchar(30) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `crate_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cratemanagement_pack_crate_id_43dbf500_fk_cratemana` (`crate_id`),
  CONSTRAINT `cratemanagement_pack_crate_id_43dbf500_fk_cratemana` FOREIGN KEY (`crate_id`) REFERENCES `cratemanagement_crate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `devices_device`
--

DROP TABLE IF EXISTS `devices_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devices_device` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `mac_address` varchar(20) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `plot_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `devices_device_plot_id_61062b2f_fk_farming_plot_id` (`plot_id`),
  CONSTRAINT `devices_device_plot_id_61062b2f_fk_farming_plot_id` FOREIGN KEY (`plot_id`) REFERENCES `farming_plot` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_crop`
--

DROP TABLE IF EXISTS `farm_crop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_crop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `delete_status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_croptype`
--

DROP TABLE IF EXISTS `farm_croptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_croptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eng_name` varchar(100) NOT NULL,
  `photo` longtext,
  `local_name` varchar(100) NOT NULL,
  `scientific_name` varchar(100) DEFAULT NULL,
  `major_nutrient` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `crop_id` int(11) NOT NULL,
  `delete_status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `farm_croptype_eng_name_a8fccaa5_uniq` (`eng_name`),
  UNIQUE KEY `farm_croptype_local_name_633fec16_uniq` (`local_name`),
  KEY `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` (`crop_id`),
  CONSTRAINT `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_district`
--

DROP TABLE IF EXISTS `farm_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `district_code` varchar(20) DEFAULT NULL,
  `division_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_district_division_id_8eee956f_fk_farm_division_id` (`division_id`),
  CONSTRAINT `farm_district_division_id_8eee956f_fk_farm_division_id` FOREIGN KEY (`division_id`) REFERENCES `farm_division` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_division`
--

DROP TABLE IF EXISTS `farm_division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_division` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `division_code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_farmer`
--

DROP TABLE IF EXISTS `farm_farmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_farmer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(100) DEFAULT NULL,
  `crop_list` varchar(100) DEFAULT NULL,
  `total_land` int(11) NOT NULL,
  `name` varchar(70) NOT NULL,
  `nid_number` varchar(10) DEFAULT NULL,
  `photo` longtext,
  `phone_number` varchar(11) NOT NULL,
  `secondary_contact` varchar(200) DEFAULT NULL,
  `post_code` varchar(4) DEFAULT NULL,
  `permanent_address` varchar(200) DEFAULT NULL,
  `is_local` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `delete_status` int(11) NOT NULL,
  `farmer_district_id` int(11) DEFAULT NULL,
  `farmer_division_id` int(11) DEFAULT NULL,
  `farmer_upazila_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_farmer_farmer_district_id_b3db0bee_fk_farm_district_id` (`farmer_district_id`),
  KEY `farm_farmer_farmer_division_id_18b88e11_fk_farm_division_id` (`farmer_division_id`),
  KEY `farm_farmer_farmer_upazila_id_59514f65_fk_farm_upazila_id` (`farmer_upazila_id`),
  CONSTRAINT `farm_farmer_farmer_district_id_b3db0bee_fk_farm_district_id` FOREIGN KEY (`farmer_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_farmer_farmer_division_id_18b88e11_fk_farm_division_id` FOREIGN KEY (`farmer_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_farmer_farmer_upazila_id_59514f65_fk_farm_upazila_id` FOREIGN KEY (`farmer_upazila_id`) REFERENCES `farm_upazila` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_land`
--

DROP TABLE IF EXISTS `farm_land`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_land` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `longitude` varchar(11) NOT NULL,
  `latitude` varchar(11) NOT NULL,
  `area` double NOT NULL,
  `photo` longtext,
  `soil_type` varchar(100) NOT NULL,
  `climate_type` varchar(100) NOT NULL,
  `flood_prone` tinyint(1) NOT NULL,
  `farmer_is_owner` tinyint(1) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `post_code` varchar(4) NOT NULL,
  `thana` varchar(100) DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `land_district_id` int(11) DEFAULT NULL,
  `land_division_id` int(11) DEFAULT NULL,
  `land_upazila_id` int(11) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_land_land_district_id_8ae2aca9_fk_farm_district_id` (`land_district_id`),
  KEY `farm_land_land_division_id_b79cc2be_fk_farm_division_id` (`land_division_id`),
  KEY `farm_land_land_upazila_id_cf97c8a1_fk_farm_upazila_id` (`land_upazila_id`),
  KEY `farm_land_owner_id_00f58273_fk_farm_owner_id` (`owner_id`),
  CONSTRAINT `farm_land_land_district_id_8ae2aca9_fk_farm_district_id` FOREIGN KEY (`land_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_land_land_division_id_b79cc2be_fk_farm_division_id` FOREIGN KEY (`land_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_land_land_upazila_id_cf97c8a1_fk_farm_upazila_id` FOREIGN KEY (`land_upazila_id`) REFERENCES `farm_upazila` (`id`),
  CONSTRAINT `farm_land_owner_id_00f58273_fk_farm_owner_id` FOREIGN KEY (`owner_id`) REFERENCES `farm_owner` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_owner`
--

DROP TABLE IF EXISTS `farm_owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(100) NOT NULL,
  `crop_list` varchar(100) NOT NULL,
  `total_land` int(11) NOT NULL,
  `name` varchar(70) NOT NULL,
  `nid_number` varchar(10) NOT NULL,
  `photo` longtext,
  `phone_number` varchar(11) NOT NULL,
  `secondary_contact` varchar(200) DEFAULT NULL,
  `post_code` varchar(4) DEFAULT NULL,
  `permanent_address` varchar(200) DEFAULT NULL,
  `is_local` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `delete_status` int(11) NOT NULL,
  `district_id` int(11) DEFAULT NULL,
  `division_id` int(11) DEFAULT NULL,
  `upazila_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_owner_district_id_799da51b_fk_farm_district_id` (`district_id`),
  KEY `farm_owner_division_id_c6637dae_fk_farm_division_id` (`division_id`),
  KEY `farm_owner_upazila_id_c353803d_fk_farm_upazila_id` (`upazila_id`),
  CONSTRAINT `farm_owner_district_id_799da51b_fk_farm_district_id` FOREIGN KEY (`district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_owner_division_id_c6637dae_fk_farm_division_id` FOREIGN KEY (`division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_owner_upazila_id_c353803d_fk_farm_upazila_id` FOREIGN KEY (`upazila_id`) REFERENCES `farm_upazila` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_upazila`
--

DROP TABLE IF EXISTS `farm_upazila`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_upazila` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `upazila_code` varchar(20) DEFAULT NULL,
  `district_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_upazila_district_id_5e9d0b93_fk_farm_district_id` (`district_id`),
  CONSTRAINT `farm_upazila_district_id_5e9d0b93_fk_farm_district_id` FOREIGN KEY (`district_id`) REFERENCES `farm_district` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farm_vegetable`
--

DROP TABLE IF EXISTS `farm_vegetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_vegetable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `soil_type` varchar(255) NOT NULL,
  `harvesting_period` varchar(100) NOT NULL,
  `expected_production` varchar(100) DEFAULT NULL,
  `seasonal` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `vegetable_type_id` int(11) NOT NULL,
  `delete_status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` (`vegetable_type_id`),
  CONSTRAINT `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` FOREIGN KEY (`vegetable_type_id`) REFERENCES `farm_croptype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farming_harvesting`
--

DROP TABLE IF EXISTS `farming_harvesting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farming_harvesting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_status` varchar(50) NOT NULL,
  `total_labor_hour` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `seeding_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farming_harvesting_farmer_id_5f340e1d_fk_farm_farmer_id` (`farmer_id`),
  KEY `farming_harvesting_seeding_id_be23a6b8_fk_farming_seeding_id` (`seeding_id`),
  CONSTRAINT `farming_harvesting_farmer_id_5f340e1d_fk_farm_farmer_id` FOREIGN KEY (`farmer_id`) REFERENCES `farm_farmer` (`id`),
  CONSTRAINT `farming_harvesting_seeding_id_be23a6b8_fk_farming_seeding_id` FOREIGN KEY (`seeding_id`) REFERENCES `farming_seeding` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farming_plot`
--

DROP TABLE IF EXISTS `farming_plot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farming_plot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_procurement` varchar(50) DEFAULT NULL,
  `costing` int(11) NOT NULL,
  `expected_harvesting_time` int(11) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `crop_status` varchar(50) DEFAULT NULL,
  `total_labor_hour` int(11) NOT NULL,
  `fertilizers` varchar(200) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `plot_id` varchar(100) DEFAULT NULL,
  `sensor_data_seeding` longtext,
  `sensor_data_harvesting` longtext,
  `classification_id` int(11) DEFAULT NULL,
  `crop_id` int(11) DEFAULT NULL,
  `farmer_id` int(11) NOT NULL,
  `seeding_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farming_plot_seeding_id_2367c300_fk_farming_seeding_id` (`seeding_id`),
  KEY `farming_plot_type_id_394eabf3_fk_farm_croptype_id` (`type_id`),
  KEY `farming_plot_classification_id_3a7f16c9_fk_farm_vegetable_id` (`classification_id`),
  KEY `farming_plot_crop_id_5d2e2be4_fk_farm_crop_id` (`crop_id`),
  KEY `farming_plot_farmer_id_1412357f_fk_farm_farmer_id` (`farmer_id`),
  CONSTRAINT `farming_plot_classification_id_3a7f16c9_fk_farm_vegetable_id` FOREIGN KEY (`classification_id`) REFERENCES `farm_vegetable` (`id`),
  CONSTRAINT `farming_plot_crop_id_5d2e2be4_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`),
  CONSTRAINT `farming_plot_farmer_id_1412357f_fk_farm_farmer_id` FOREIGN KEY (`farmer_id`) REFERENCES `farm_farmer` (`id`),
  CONSTRAINT `farming_plot_seeding_id_2367c300_fk_farming_seeding_id` FOREIGN KEY (`seeding_id`) REFERENCES `farming_seeding` (`id`),
  CONSTRAINT `farming_plot_type_id_394eabf3_fk_farm_croptype_id` FOREIGN KEY (`type_id`) REFERENCES `farm_croptype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farming_plotstatuslog`
--

DROP TABLE IF EXISTS `farming_plotstatuslog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farming_plotstatuslog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crop_status` varchar(50) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `plot_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farming_plotstatuslog_plot_id_85222d3b_fk_farming_plot_id` (`plot_id`),
  CONSTRAINT `farming_plotstatuslog_plot_id_85222d3b_fk_farming_plot_id` FOREIGN KEY (`plot_id`) REFERENCES `farming_plot` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `farming_seeding`
--

DROP TABLE IF EXISTS `farming_seeding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farming_seeding` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_name` varchar(100) DEFAULT NULL,
  `land_usage` int(11) NOT NULL,
  `status` varchar(64) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `land_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farming_seeding_land_id_a8893ac2_fk_farm_land_id` (`land_id`),
  CONSTRAINT `farming_seeding_land_id_a8893ac2_fk_farm_land_id` FOREIGN KEY (`land_id`) REFERENCES `farm_land` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `i_menu_name`
--

DROP TABLE IF EXISTS `i_menu_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `i_menu_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_by` varchar(20) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `i_module_action`
--

DROP TABLE IF EXISTS `i_module_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `i_module_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(300) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_by` varchar(20) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `menuname_id` int(11) DEFAULT NULL,
  `modulename_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `i_module_action_modulename_id_8de46812_fk_i_module_name_id` (`modulename_id`),
  KEY `i_module_action_menuname_id_7c550641_fk_i_menu_name_id` (`menuname_id`),
  CONSTRAINT `i_module_action_menuname_id_7c550641_fk_i_menu_name_id` FOREIGN KEY (`menuname_id`) REFERENCES `i_menu_name` (`id`),
  CONSTRAINT `i_module_action_modulename_id_8de46812_fk_i_module_name_id` FOREIGN KEY (`modulename_id`) REFERENCES `i_module_name` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `i_module_name`
--

DROP TABLE IF EXISTS `i_module_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `i_module_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `modulename` varchar(300) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_by` varchar(20) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `menuname_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `i_module_name_menuname_id_4d80ee18_fk_i_menu_name_id` (`menuname_id`),
  CONSTRAINT `i_module_name_menuname_id_4d80ee18_fk_i_menu_name_id` FOREIGN KEY (`menuname_id`) REFERENCES `i_menu_name` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `i_privilege`
--

DROP TABLE IF EXISTS `i_privilege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `i_privilege` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_type` int(11) NOT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `updated_by` varchar(20) DEFAULT NULL,
  `updated_date` datetime(6) DEFAULT NULL,
  `menuname_id` int(11) DEFAULT NULL,
  `modulename_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `i_privilege_menuname_id_78a3b139_fk_i_menu_name_id` (`menuname_id`),
  KEY `i_privilege_modulename_id_5e0ba066_fk_i_module_name_id` (`modulename_id`),
  KEY `i_privilege_role_id_f0c5d4fa_fk_users_role_id` (`role_id`),
  KEY `i_privilege_url_id_37ba2706_fk_i_module_action_id` (`url_id`),
  KEY `i_privilege_user_id_72dd76a5_fk_users_user_id` (`user_id`),
  CONSTRAINT `i_privilege_menuname_id_78a3b139_fk_i_menu_name_id` FOREIGN KEY (`menuname_id`) REFERENCES `i_menu_name` (`id`),
  CONSTRAINT `i_privilege_modulename_id_5e0ba066_fk_i_module_name_id` FOREIGN KEY (`modulename_id`) REFERENCES `i_module_name` (`id`),
  CONSTRAINT `i_privilege_role_id_f0c5d4fa_fk_users_role_id` FOREIGN KEY (`role_id`) REFERENCES `users_role` (`id`),
  CONSTRAINT `i_privilege_url_id_37ba2706_fk_i_module_action_id` FOREIGN KEY (`url_id`) REFERENCES `i_module_action` (`id`),
  CONSTRAINT `i_privilege_user_id_72dd76a5_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users_role`
--

DROP TABLE IF EXISTS `users_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `address` varchar(200) NOT NULL,
  `nid` varchar(12) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `nid` (`nid`),
  KEY `users_user_role_id_854f2687_fk_users_role_id` (`role_id`),
  CONSTRAINT `users_user_role_id_854f2687_fk_users_role_id` FOREIGN KEY (`role_id`) REFERENCES `users_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'pksfdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-19 18:00:16

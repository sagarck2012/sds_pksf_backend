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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add seeding',7,'add_seeding'),(26,'Can change seeding',7,'change_seeding'),(27,'Can delete seeding',7,'delete_seeding'),(28,'Can view seeding',7,'view_seeding'),(29,'Can add plot',8,'add_plot'),(30,'Can change plot',8,'change_plot'),(31,'Can delete plot',8,'delete_plot'),(32,'Can view plot',8,'view_plot'),(33,'Can add harvesting',9,'add_harvesting'),(34,'Can change harvesting',9,'change_harvesting'),(35,'Can delete harvesting',9,'delete_harvesting'),(36,'Can view harvesting',9,'view_harvesting'),(37,'Can add crop',10,'add_crop'),(38,'Can change crop',10,'change_crop'),(39,'Can delete crop',10,'delete_crop'),(40,'Can view crop',10,'view_crop'),(41,'Can add crop type',11,'add_croptype'),(42,'Can change crop type',11,'change_croptype'),(43,'Can delete crop type',11,'delete_croptype'),(44,'Can view crop type',11,'view_croptype'),(45,'Can add district',12,'add_district'),(46,'Can change district',12,'change_district'),(47,'Can delete district',12,'delete_district'),(48,'Can view district',12,'view_district'),(49,'Can add division',13,'add_division'),(50,'Can change division',13,'change_division'),(51,'Can delete division',13,'delete_division'),(52,'Can view division',13,'view_division'),(53,'Can add production house',14,'add_productionhouse'),(54,'Can change production house',14,'change_productionhouse'),(55,'Can delete production house',14,'delete_productionhouse'),(56,'Can view production house',14,'view_productionhouse'),(57,'Can add vegetable',15,'add_vegetable'),(58,'Can change vegetable',15,'change_vegetable'),(59,'Can delete vegetable',15,'delete_vegetable'),(60,'Can view vegetable',15,'view_vegetable'),(61,'Can add upazila',16,'add_upazila'),(62,'Can change upazila',16,'change_upazila'),(63,'Can delete upazila',16,'delete_upazila'),(64,'Can view upazila',16,'view_upazila'),(65,'Can add owner',17,'add_owner'),(66,'Can change owner',17,'change_owner'),(67,'Can delete owner',17,'delete_owner'),(68,'Can view owner',17,'view_owner'),(69,'Can add land',18,'add_land'),(70,'Can change land',18,'change_land'),(71,'Can delete land',18,'delete_land'),(72,'Can view land',18,'view_land'),(73,'Can add farmer',19,'add_farmer'),(74,'Can change farmer',19,'change_farmer'),(75,'Can delete farmer',19,'delete_farmer'),(76,'Can view farmer',19,'view_farmer'),(77,'Can add device',20,'add_device'),(78,'Can change device',20,'change_device'),(79,'Can delete device',20,'delete_device'),(80,'Can view device',20,'view_device'),(81,'Can add crate info',21,'add_crateinfo'),(82,'Can change crate info',21,'change_crateinfo'),(83,'Can delete crate info',21,'delete_crateinfo'),(84,'Can view crate info',21,'view_crateinfo'),(85,'Can add crating',22,'add_crating'),(86,'Can change crating',22,'change_crating'),(87,'Can delete crating',22,'delete_crating'),(88,'Can view crating',22,'view_crating'),(89,'Can add packaging',23,'add_packaging'),(90,'Can change packaging',23,'change_packaging'),(91,'Can delete packaging',23,'delete_packaging'),(92,'Can view packaging',23,'view_packaging'),(93,'Can add receiving',24,'add_receiving'),(94,'Can change receiving',24,'change_receiving'),(95,'Can delete receiving',24,'delete_receiving'),(96,'Can view receiving',24,'view_receiving'),(97,'Can add shipping',25,'add_shipping'),(98,'Can change shipping',25,'change_shipping'),(99,'Can delete shipping',25,'delete_shipping'),(100,'Can view shipping',25,'view_shipping'),(101,'Can add shipping detail',26,'add_shippingdetail'),(102,'Can change shipping detail',26,'change_shippingdetail'),(103,'Can delete shipping detail',26,'delete_shippingdetail'),(104,'Can view shipping detail',26,'view_shippingdetail'),(105,'Can add receiving detail',27,'add_receivingdetail'),(106,'Can change receiving detail',27,'change_receivingdetail'),(107,'Can delete receiving detail',27,'delete_receivingdetail'),(108,'Can view receiving detail',27,'view_receivingdetail'),(109,'Can add packaging detail',28,'add_packagingdetail'),(110,'Can change packaging detail',28,'change_packagingdetail'),(111,'Can delete packaging detail',28,'delete_packagingdetail'),(112,'Can view packaging detail',28,'view_packagingdetail'),(113,'Can add packaging damaged',29,'add_packagingdamaged'),(114,'Can change packaging damaged',29,'change_packagingdamaged'),(115,'Can delete packaging damaged',29,'delete_packagingdamaged'),(116,'Can view packaging damaged',29,'view_packagingdamaged'),(117,'Can add crating detail',30,'add_cratingdetail'),(118,'Can change crating detail',30,'change_cratingdetail'),(119,'Can delete crating detail',30,'delete_cratingdetail'),(120,'Can view crating detail',30,'view_cratingdetail'),(121,'Can add menu_name',31,'add_menu_name'),(122,'Can change menu_name',31,'change_menu_name'),(123,'Can delete menu_name',31,'delete_menu_name'),(124,'Can view menu_name',31,'view_menu_name'),(125,'Can add module_action',32,'add_module_action'),(126,'Can change module_action',32,'change_module_action'),(127,'Can delete module_action',32,'delete_module_action'),(128,'Can view module_action',32,'view_module_action'),(129,'Can add module_name',33,'add_module_name'),(130,'Can change module_name',33,'change_module_name'),(131,'Can delete module_name',33,'delete_module_name'),(132,'Can view module_name',33,'view_module_name'),(133,'Can add role',34,'add_role'),(134,'Can change role',34,'change_role'),(135,'Can delete role',34,'delete_role'),(136,'Can view role',34,'view_role'),(137,'Can add user',35,'add_user'),(138,'Can change user',35,'change_user'),(139,'Can delete user',35,'delete_user'),(140,'Can view user',35,'view_user'),(141,'Can add privilege',36,'add_privilege'),(142,'Can change privilege',36,'change_privilege'),(143,'Can delete privilege',36,'delete_privilege'),(144,'Can view privilege',36,'view_privilege');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
  KEY `devices_device_plot_id_61062b2f_fk_production_plot_id` (`plot_id`),
  CONSTRAINT `devices_device_plot_id_61062b2f_fk_production_plot_id` FOREIGN KEY (`plot_id`) REFERENCES `production_plot` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devices_device`
--

LOCK TABLES `devices_device` WRITE;
/*!40000 ALTER TABLE `devices_device` DISABLE KEYS */;
/*!40000 ALTER TABLE `devices_device` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(20,'devices','device'),(10,'farm','crop'),(11,'farm','croptype'),(12,'farm','district'),(13,'farm','division'),(19,'farm','farmer'),(18,'farm','land'),(17,'farm','owner'),(14,'farm','productionhouse'),(16,'farm','upazila'),(15,'farm','vegetable'),(9,'farming','harvesting'),(8,'farming','plot'),(7,'farming','seeding'),(21,'processing','crateinfo'),(22,'processing','crating'),(30,'processing','cratingdetail'),(23,'processing','packaging'),(29,'processing','packagingdamaged'),(28,'processing','packagingdetail'),(24,'processing','receiving'),(27,'processing','receivingdetail'),(25,'processing','shipping'),(26,'processing','shippingdetail'),(6,'sessions','session'),(31,'users','menu_name'),(32,'users','module_action'),(33,'users','module_name'),(36,'users','privilege'),(34,'users','role'),(35,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-13 12:58:37.445313'),(2,'auth','0001_initial','2021-01-13 12:58:39.608792'),(3,'admin','0001_initial','2021-01-13 12:58:47.662546'),(4,'admin','0002_logentry_remove_auto_add','2021-01-13 12:58:49.546170'),(5,'admin','0003_logentry_add_action_flag_choices','2021-01-13 12:58:49.588331'),(6,'contenttypes','0002_remove_content_type_name','2021-01-13 12:58:50.879930'),(7,'auth','0002_alter_permission_name_max_length','2021-01-13 12:58:51.733975'),(8,'auth','0003_alter_user_email_max_length','2021-01-13 12:58:52.569678'),(9,'auth','0004_alter_user_username_opts','2021-01-13 12:58:52.634100'),(10,'auth','0005_alter_user_last_login_null','2021-01-13 12:58:53.339145'),(11,'auth','0006_require_contenttypes_0002','2021-01-13 12:58:53.380994'),(12,'auth','0007_alter_validators_add_error_messages','2021-01-13 12:58:53.445044'),(13,'auth','0008_alter_user_username_max_length','2021-01-13 12:58:54.292423'),(14,'auth','0009_alter_user_last_name_max_length','2021-01-13 12:58:55.271326'),(15,'auth','0010_alter_group_name_max_length','2021-01-13 12:58:56.092451'),(16,'auth','0011_update_proxy_permissions','2021-01-13 12:58:56.144426'),(17,'auth','0012_alter_user_first_name_max_length','2021-01-13 12:58:56.953850'),(18,'farm','0001_initial','2021-01-13 12:59:01.413290'),(19,'farming','0001_initial','2021-01-13 12:59:24.389330'),(20,'devices','0001_initial','2021-01-13 12:59:31.733012'),(21,'processing','0001_initial','2021-01-13 12:59:39.310841'),(22,'sessions','0001_initial','2021-01-13 12:59:57.451127'),(23,'users','0001_initial','2021-01-13 13:00:01.067906'),(24,'processing','0002_auto_20210113_1551','2021-01-13 15:51:36.058741'),(25,'processing','0003_auto_20210113_1657','2021-01-13 16:57:32.816552'),(26,'processing','0004_auto_20210119_1220','2021-01-19 12:20:48.696185'),(27,'processing','0005_crateinfo_delete_status','2021-01-19 16:16:36.802995');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

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
  `delete_status` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_crop`
--

LOCK TABLES `farm_crop` WRITE;
/*!40000 ALTER TABLE `farm_crop` DISABLE KEYS */;
INSERT INTO `farm_crop` VALUES (1,'Grain',NULL,'',NULL,'',0),(2,'Pulse',NULL,'',NULL,'',0),(3,'Oil',NULL,'',NULL,'',0),(4,'Spices',NULL,'',NULL,'',0),(5,'Vegetable',NULL,'',NULL,'',0),(6,'Tuber',NULL,'',NULL,'',0),(7,'Fruit',NULL,'',NULL,'',0),(8,'Flower',NULL,'',NULL,'',0),(9,'Cash Crop',NULL,'',NULL,'',0);
/*!40000 ALTER TABLE `farm_crop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_croptype`
--

DROP TABLE IF EXISTS `farm_croptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_croptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eng_name` varchar(100) NOT NULL,
  `local_name` varchar(100) NOT NULL,
  `photo` longtext,
  `scientific_name` varchar(100) DEFAULT NULL,
  `major_nutrient` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `delete_status` int(11) NOT NULL,
  `crop_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` (`crop_id`),
  CONSTRAINT `farm_croptype_crop_id_2426db0b_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_croptype`
--

LOCK TABLES `farm_croptype` WRITE;
/*!40000 ALTER TABLE `farm_croptype` DISABLE KEYS */;
INSERT INTO `farm_croptype` VALUES (135,'Eggplant','Begun',NULL,'Solanum melongena','Vitamin A, C, E, K, Calcium, Magnesium, Zinc ',NULL,'',NULL,'',0,5),(136,'Luffa','Jhinga',NULL,'Luffa acutangula','Protein, Bita-Carotine, Vitamin C, Calcium, Phosphorus',NULL,'',NULL,'',0,5),(137,'Radish','Mula',NULL,'Raphanus sativus','Vitamin A, Calcium, Iron',NULL,'',NULL,'',0,5),(138,'Ladies Finger','Dherosh',NULL,'Abelmoschus esculentus','Vitamin A, B,C; Iodin',NULL,'',NULL,'',0,5),(139,'Yardlong Bean','Borboti',NULL,'Vigna Sesquipedalis','Vitamin A,C; Magnesium, Calcium, Iron,  Potassium',NULL,'',NULL,'',0,5),(140,'Cabbage','Badhacopy',NULL,'Brassica oleracea var capitata','Vitamin A, B1, B2, B6, E, C, K; Calcium, Iron, Iodin, Potassium, Salfa',NULL,'',NULL,'',0,5),(141,'Gourd/Calabash','Lau/Kodu',NULL,'Lagenaria siceraria','Vitamin C, Calcium, Phosphorus, Potasium, Nicotinic Acid, Vitamin B-1,',NULL,'',NULL,'',0,5),(142,'Bean','Seam',NULL,'Phaseolus','Protein, Vitamin C, Zinc, Mineral',NULL,'',NULL,'',0,5),(143,'Bitter Gourd/Baslam Pear/ Bitter Melon/Alligator Pear','Korola',NULL,'Momordica charantia','Protein, Calcium, Iron, Vitamin c',NULL,'',NULL,'',0,5),(144,'Sweet Pumpkin','Misti Kumra',NULL,'Cucurbitaceae','Vitamin A, B-Complex, C & E, Potassium, Magnesium, Calcium, Manganis, ',NULL,'',NULL,'',0,5),(145,'Pointed Gourd','Potol',NULL,'Trichosanthes dioica','Vitamin A, Vitamin B1 & 2, Vitamin C, Calcium, Antioxident',NULL,'',NULL,'',0,5),(146,'Cucumber','Sosha',NULL,'Cucumis sativus','Protein, Calcium,Iron, Carotin, Vitamin C',NULL,'',NULL,'',0,5),(147,'Lal Shak','Lal Shak',NULL,'Amaranthus gangeticus','Vitamin A, Calcium',NULL,'',NULL,'',0,5),(148,'Tomato','Tomato',NULL,'Lycopersicon esculentum','Protein, Fiber, Sodium, Potasium, Copper, Iron, Vitamin C',NULL,'',NULL,'',0,5),(149,'Cauliflower','Fulcopy',NULL,'Brassica oleracea var. botrytis','Sulfar, Potasium, Phosphorus, Minerals',NULL,'',NULL,'',0,5);
/*!40000 ALTER TABLE `farm_croptype` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_district`
--

LOCK TABLES `farm_district` WRITE;
/*!40000 ALTER TABLE `farm_district` DISABLE KEYS */;
INSERT INTO `farm_district` VALUES (1,'Dhaka',NULL,3),(2,'Faridpur',NULL,3),(3,'Gazipur',NULL,3),(4,'Gopalganj',NULL,3),(5,'Jamalpur',NULL,8),(6,'Kishoreganj',NULL,3),(7,'Madaripur',NULL,3),(8,'Manikganj',NULL,3),(9,'Munshiganj',NULL,3),(10,'Mymensingh',NULL,8),(11,'Narayanganj',NULL,3),(12,'Narsingdi',NULL,3),(13,'Netrokona',NULL,8),(14,'Rajbari',NULL,3),(15,'Shariatpur',NULL,3),(16,'Sherpur',NULL,8),(17,'Tangail',NULL,3),(18,'Bogura',NULL,5),(19,'Joypurhat',NULL,5),(20,'Naogaon',NULL,5),(21,'Natore',NULL,5),(22,'ChapaiNawabganj',NULL,5),(23,'Pabna',NULL,5),(24,'Rajshahi',NULL,5),(25,'Sirajganj',NULL,5),(26,'Dinajpur',NULL,6),(27,'Gaibandha',NULL,6),(28,'Kurigram',NULL,6),(29,'Lalmonirhat',NULL,6),(30,'Nilphamari',NULL,6),(31,'Panchagarh',NULL,6),(32,'Rangpur',NULL,6),(33,'Thakurgaon',NULL,6),(34,'Barguna',NULL,1),(35,'Barishal',NULL,1),(36,'Bhola',NULL,1),(37,'Jhalokati',NULL,1),(38,'Patuakhali',NULL,1),(39,'Pirojpur',NULL,1),(40,'Bandarban',NULL,2),(41,'Brahmanbaria',NULL,2),(42,'Chandpur',NULL,2),(43,'Chattogram',NULL,2),(44,'Cumilla',NULL,2),(45,'CoxsBazar',NULL,2),(46,'Feni',NULL,2),(47,'khagrachhari',NULL,2),(48,'Lakshmipur',NULL,2),(49,'Noakhali',NULL,2),(50,'Rangamati',NULL,2),(51,'Habiganj',NULL,7),(52,'Maulvibazar',NULL,7),(53,'Sunamganj',NULL,7),(54,'Sylhet',NULL,7),(55,'Bagerhat',NULL,4),(56,'Chuadanga',NULL,4),(57,'Jashore',NULL,4),(58,'Jhenaidah',NULL,4),(59,'Khulna',NULL,4),(60,'Kushtia',NULL,4),(61,'Magura',NULL,4),(62,'Meherpur',NULL,4),(63,'Narail',NULL,4),(64,'Satkhira',NULL,4);
/*!40000 ALTER TABLE `farm_district` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_division`
--

LOCK TABLES `farm_division` WRITE;
/*!40000 ALTER TABLE `farm_division` DISABLE KEYS */;
INSERT INTO `farm_division` VALUES (1,'Barishal',NULL),(2,'Chattogram',NULL),(3,'Dhaka',NULL),(4,'Khulna',NULL),(5,'Rajshahi',NULL),(6,'Rangpur',NULL),(7,'Sylhet',NULL),(8,'Mymensingh',NULL);
/*!40000 ALTER TABLE `farm_division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_farmer`
--

DROP TABLE IF EXISTS `farm_farmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_farmer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `present_post_code` varchar(4) DEFAULT NULL,
  `present_address` varchar(200) DEFAULT NULL,
  `permanent_post_code` varchar(4) DEFAULT NULL,
  `permanent_address` varchar(200) DEFAULT NULL,
  `crop_list` varchar(200) DEFAULT NULL,
  `total_land` int(11) NOT NULL,
  `name` varchar(70) NOT NULL,
  `nid_number` varchar(10) DEFAULT NULL,
  `photo` longtext,
  `phone_number` varchar(11) NOT NULL,
  `secondary_contact_no` varchar(11) DEFAULT NULL,
  `is_local` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `delete_status` int(11) NOT NULL,
  `permanent_district_id` int(11) DEFAULT NULL,
  `permanent_division_id` int(11) DEFAULT NULL,
  `permanent_upazilla_id` int(11) DEFAULT NULL,
  `present_district_id` int(11) DEFAULT NULL,
  `present_division_id` int(11) DEFAULT NULL,
  `present_upazilla_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_farmer_permanent_district_id_ceabd422_fk_farm_district_id` (`permanent_district_id`),
  KEY `farm_farmer_permanent_division_id_7c4c2f17_fk_farm_division_id` (`permanent_division_id`),
  KEY `farm_farmer_permanent_upazilla_id_e5bdbfe8_fk_farm_upazila_id` (`permanent_upazilla_id`),
  KEY `farm_farmer_present_district_id_b6194405_fk_farm_district_id` (`present_district_id`),
  KEY `farm_farmer_present_division_id_d2bb75af_fk_farm_division_id` (`present_division_id`),
  KEY `farm_farmer_present_upazilla_id_1f5de378_fk_farm_upazila_id` (`present_upazilla_id`),
  CONSTRAINT `farm_farmer_permanent_district_id_ceabd422_fk_farm_district_id` FOREIGN KEY (`permanent_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_farmer_permanent_division_id_7c4c2f17_fk_farm_division_id` FOREIGN KEY (`permanent_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_farmer_permanent_upazilla_id_e5bdbfe8_fk_farm_upazila_id` FOREIGN KEY (`permanent_upazilla_id`) REFERENCES `farm_upazila` (`id`),
  CONSTRAINT `farm_farmer_present_district_id_b6194405_fk_farm_district_id` FOREIGN KEY (`present_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_farmer_present_division_id_d2bb75af_fk_farm_division_id` FOREIGN KEY (`present_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_farmer_present_upazilla_id_1f5de378_fk_farm_upazila_id` FOREIGN KEY (`present_upazilla_id`) REFERENCES `farm_upazila` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_farmer`
--

LOCK TABLES `farm_farmer` WRITE;
/*!40000 ALTER TABLE `farm_farmer` DISABLE KEYS */;
INSERT INTO `farm_farmer` VALUES (1,NULL,'01739129488','1200',NULL,'Vegetable711',200,'Test Name2','2848919748','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','01551164102',NULL,0,'2020-11-09 03:51:07.785760','1','2020-11-09 03:51:07.785760','1',0,1,3,161,NULL,NULL,NULL),(2,NULL,'01739129488','1200',NULL,'Vegetable711',200,'Md. Ridwan Mizan','2848919748','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','01551164102',NULL,0,'2020-11-09 03:52:27.614887','1','2020-11-09 03:52:27.614887','1',1,1,3,161,NULL,NULL,NULL),(3,NULL,'01739129488','1200',NULL,'Vegetable711',200,'Ridwan Mizan','2848919748','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','01551164102',NULL,0,'2020-11-17 18:08:02.603433','1','2020-11-17 18:08:02.603433','1',0,1,3,161,NULL,NULL,NULL),(4,NULL,'01739129488','1200',NULL,'Vegetable711',200,'Ridwan Mizan','2848919748','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','01551164102',NULL,0,'2020-11-19 14:42:03.747489','1','2020-11-19 14:42:03.748461','1',0,1,3,161,NULL,NULL,NULL),(5,'1204','Banani','1205','Banani4','abcd',5,'test farmer','2848919748','photo...','01739129488','01620810044',1,'2021-01-07 15:15:35.624674','1','2021-01-07 15:15:35.624674','1',0,21,5,357,21,5,357);
/*!40000 ALTER TABLE `farm_farmer` ENABLE KEYS */;
UNLOCK TABLES;

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
  `soil_type` varchar(100) DEFAULT NULL,
  `climate_type` varchar(100) DEFAULT NULL,
  `flood_prone` tinyint(1) NOT NULL,
  `farmer_is_owner` tinyint(1) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `post_code` varchar(4) DEFAULT NULL,
  `thana` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `comment` longtext,
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_land`
--

LOCK TABLES `farm_land` WRITE;
/*!40000 ALTER TABLE `farm_land` DISABLE KEYS */;
INSERT INTO `farm_land` VALUES (31,'92','23',103,'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','test type','test climate',0,1,'free','1207','Test Thana',NULL,1,'2020-12-23 15:07:23.749761','3','2020-12-23 15:07:23.749761','2',NULL,1,3,500,3),(32,'92','23',103,'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','test type','test climate',0,1,'free','1207','Test Thana',NULL,1,'2021-01-07 15:52:54.708946','3','2021-01-07 15:52:54.708946','2',NULL,1,3,500,3),(33,'92','23',103,'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','test type','test climate',0,1,'free','1207','Test Thana','test address',1,'2021-01-07 15:53:34.813577','3','2021-01-07 15:53:34.813577','2',NULL,1,3,500,3);
/*!40000 ALTER TABLE `farm_land` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_owner`
--

DROP TABLE IF EXISTS `farm_owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_owner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `present_post_code` varchar(4) DEFAULT NULL,
  `present_address` varchar(200) DEFAULT NULL,
  `permanent_post_code` varchar(4) DEFAULT NULL,
  `permanent_address` varchar(200) DEFAULT NULL,
  `crop_list` varchar(100) NOT NULL,
  `total_land` int(11) NOT NULL,
  `name` varchar(70) NOT NULL,
  `nid_number` varchar(10) NOT NULL,
  `photo` longtext,
  `phone_number` varchar(11) NOT NULL,
  `secondary_contact_no` varchar(200) DEFAULT NULL,
  `is_local` tinyint(1) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `delete_status` int(11) NOT NULL,
  `permanent_district_id` int(11) DEFAULT NULL,
  `permanent_division_id` int(11) DEFAULT NULL,
  `permanent_upazilla_id` int(11) DEFAULT NULL,
  `present_district_id` int(11) DEFAULT NULL,
  `present_division_id` int(11) DEFAULT NULL,
  `present_upazilla_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_owner_permanent_district_id_9be1a643_fk_farm_district_id` (`permanent_district_id`),
  KEY `farm_owner_permanent_division_id_cfb00f35_fk_farm_division_id` (`permanent_division_id`),
  KEY `farm_owner_permanent_upazilla_id_a73eb33f_fk_farm_upazila_id` (`permanent_upazilla_id`),
  KEY `farm_owner_present_district_id_5a088fd0_fk_farm_district_id` (`present_district_id`),
  KEY `farm_owner_present_division_id_d3852224_fk_farm_division_id` (`present_division_id`),
  KEY `farm_owner_present_upazilla_id_1a1e3bcc_fk_farm_upazila_id` (`present_upazilla_id`),
  CONSTRAINT `farm_owner_permanent_district_id_9be1a643_fk_farm_district_id` FOREIGN KEY (`permanent_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_owner_permanent_division_id_cfb00f35_fk_farm_division_id` FOREIGN KEY (`permanent_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_owner_permanent_upazilla_id_a73eb33f_fk_farm_upazila_id` FOREIGN KEY (`permanent_upazilla_id`) REFERENCES `farm_upazila` (`id`),
  CONSTRAINT `farm_owner_present_district_id_5a088fd0_fk_farm_district_id` FOREIGN KEY (`present_district_id`) REFERENCES `farm_district` (`id`),
  CONSTRAINT `farm_owner_present_division_id_d3852224_fk_farm_division_id` FOREIGN KEY (`present_division_id`) REFERENCES `farm_division` (`id`),
  CONSTRAINT `farm_owner_present_upazilla_id_1a1e3bcc_fk_farm_upazila_id` FOREIGN KEY (`present_upazilla_id`) REFERENCES `farm_upazila` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_owner`
--

LOCK TABLES `farm_owner` WRITE;
/*!40000 ALTER TABLE `farm_owner` DISABLE KEYS */;
INSERT INTO `farm_owner` VALUES (1,NULL,'01911318752','1207','Shyamoli','Fruti, Peddy',2148,'Test name','2848919748','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','01739129488',NULL,0,'2020-11-08 05:10:46.746964','1','2020-11-08 05:10:46.747963','1',0,1,3,500,NULL,NULL,NULL),(2,NULL,'01911318752','1207','Shyamoli','Fruti, Peddy',2148,'Test name','2848919748','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','01739129488',NULL,0,'2020-11-08 05:19:36.106634','1','2020-11-08 05:19:36.106634','1',1,1,3,500,NULL,NULL,NULL),(3,NULL,'01911318752','1207','Shyamoli','Fruit, Peddy',2148,'Test name','2848919748','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','01739129488',NULL,0,'2020-11-09 04:16:08.722265','1','2020-11-09 04:16:08.722265','1',1,1,3,500,NULL,NULL,NULL),(4,'1234','Banani','1234','Banani4','abcd',2,'test owner','2848919748','asdfda','01739129488','01620810044',0,'2021-01-07 15:30:23.086002','1','2021-01-07 15:30:23.086002','1',0,21,5,357,21,5,357);
/*!40000 ALTER TABLE `farm_owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farm_productionhouse`
--

DROP TABLE IF EXISTS `farm_productionhouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `farm_productionhouse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `branch` varchar(100) NOT NULL,
  `branch_code` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `head_office` varchar(200) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(4) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_productionhouse`
--

LOCK TABLES `farm_productionhouse` WRITE;
/*!40000 ALTER TABLE `farm_productionhouse` DISABLE KEYS */;
INSERT INTO `farm_productionhouse` VALUES (1,'DataSoft','Bananai','IoT','4736','01739129488','ridwanmizan@gmail.com','shyamoli','2021-01-06 12:03:28.000000','0','2021-01-06 12:03:32.000000','0');
/*!40000 ALTER TABLE `farm_productionhouse` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=506 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_upazila`
--

LOCK TABLES `farm_upazila` WRITE;
/*!40000 ALTER TABLE `farm_upazila` DISABLE KEYS */;
INSERT INTO `farm_upazila` VALUES (1,'Amtali',NULL,34),(2,'Bamna',NULL,34),(3,'BargunaSadar',NULL,34),(4,'Betagi',NULL,34),(5,'Patharghata',NULL,34),(6,'Taltali',NULL,34),(7,'Muladi',NULL,35),(8,'Babuganj',NULL,35),(9,'Agailjhara',NULL,35),(10,'BarishalSadar',NULL,35),(11,'Bakerganj',NULL,35),(12,'Banaripara ',NULL,35),(13,'Gaurnadi',NULL,35),(14,'Hizla',NULL,35),(15,'Mehendiganj',NULL,35),(16,'Wazirpur',NULL,35),(17,'BholaSadar',NULL,36),(18,'Burhanuddin',NULL,36),(19,'CharFesson',NULL,36),(20,'Doulatkhan',NULL,36),(21,'Lalmohan',NULL,36),(22,'Manpura',NULL,36),(23,'Tazumuddin',NULL,36),(24,'JhalokatiSadar',NULL,37),(25,'Kathalia',NULL,37),(26,'Nalchity',NULL,37),(27,'Rajapur',NULL,37),(28,'Bauphal',NULL,38),(29,'Dashmina',NULL,38),(30,'Galachipa',NULL,38),(31,'Kalapara',NULL,38),(32,'Mirzaganj',NULL,38),(33,'PatuakhaliSadar',NULL,38),(34,'Dumki',NULL,38),(35,'Rangabali',NULL,38),(36,'Bhandaria',NULL,39),(37,'Kawkhali',NULL,39),(38,'Mathbaria',NULL,39),(39,'Nazirpur',NULL,39),(40,'Nesarabad',NULL,39),(41,'PirojpurSadar',NULL,39),(42,'Indurkani',NULL,39),(43,'BandarbanSadar',NULL,40),(44,'Thanchi',NULL,40),(45,'Lama',NULL,40),(46,'Naikhongchhari',NULL,40),(47,'Alikadam',NULL,40),(48,'Rowangchhari',NULL,40),(49,'Ruma',NULL,40),(50,'BrahmanbariaSadar',NULL,41),(51,'Ashuganj',NULL,41),(52,'Nasirnagar',NULL,41),(53,'Nabinagar',NULL,41),(54,'Sarail',NULL,41),(55,'Karnafuli',NULL,43),(56,'Kasba',NULL,41),(57,'Akhaura',NULL,41),(58,'Bancharampur',NULL,41),(59,'Bijoynagar',NULL,41),(60,'ChandpurSadar',NULL,42),(61,'Faridganj',NULL,42),(62,'Haimchar',NULL,42),(63,'Hajiganj',NULL,42),(64,'Kachua',NULL,42),(65,'Matlabnorth',NULL,42),(66,'Matlabsouth',NULL,42),(67,'Shahrasti',NULL,42),(68,'Anwara',NULL,43),(69,'Banshkhali',NULL,43),(70,'Boalkhali',NULL,43),(71,'Chandanaish',NULL,43),(72,'Fatikchhari',NULL,43),(73,'Hathazari',NULL,43),(74,'Lohagara',NULL,43),(75,'Mirsharai',NULL,43),(76,'Patiya ',NULL,43),(77,'Rangunia ',NULL,43),(78,'Raozan ',NULL,43),(79,'Sandwip ',NULL,43),(80,'Satkania',NULL,43),(81,'Sitakunda',NULL,43),(82,'Barura ',NULL,44),(83,'Brahmanpara ',NULL,44),(84,'Burichang',NULL,44),(85,'Chandina ',NULL,44),(86,'Chauddagram ',NULL,44),(87,'Daudkandi ',NULL,44),(88,'Lalmai ',NULL,44),(89,'Homna ',NULL,44),(90,'CumillaSadar',NULL,44),(91,'Laksam ',NULL,44),(92,'Monohargonj',NULL,44),(93,'Meghna ',NULL,44),(94,'Muradnagar ',NULL,44),(95,'Nangalkot ',NULL,44),(96,'SadarSouth',NULL,44),(97,'Titas ',NULL,44),(98,'Chakaria ',NULL,45),(99,'CoxsBazarSadar',NULL,45),(100,'Kutubdia',NULL,45),(101,'Maheshkhali',NULL,45),(102,'Ramu',NULL,45),(103,'Teknaf',NULL,45),(104,'Ukhiya',NULL,45),(105,'Pekua',NULL,45),(106,'FeniSadar',NULL,46),(107,'Chhagalnaiya',NULL,46),(108,'Daganbhuiyan',NULL,46),(109,'Parshuram',NULL,46),(110,'Fulgazi',NULL,46),(111,'Sonagazi',NULL,46),(112,'Dighinala',NULL,47),(113,'KhagrachhariSadar',NULL,47),(114,'Lakshmichhari',NULL,47),(115,'Mahalchhari',NULL,47),(116,'Manikchhari',NULL,47),(117,'Matiranga',NULL,47),(118,'Panchhari',NULL,47),(119,'Ramgarh',NULL,47),(120,'LakshmipurSadar',NULL,48),(121,'Raipur',NULL,48),(122,'Ramganj',NULL,48),(123,'Ramgati',NULL,48),(124,'Kamalnagar',NULL,48),(125,'NoakhaliSadar',NULL,49),(126,'Begumganj',NULL,49),(127,'Chatkhil',NULL,49),(128,'Companiganj',NULL,49),(129,'Senbug',NULL,49),(130,'Hatia',NULL,49),(131,'Kabirhat',NULL,49),(132,'Sonaimuri',NULL,49),(133,'Subarnachar',NULL,49),(134,'RangamatiSadar',NULL,50),(135,'Belaichari',NULL,50),(136,'Baghaichari',NULL,50),(137,'Barkal',NULL,50),(138,'Juraichari',NULL,50),(139,'Rajasthali',NULL,50),(140,'Kaptai',NULL,50),(141,'Langadu',NULL,50),(142,'Naniarchar',NULL,50),(143,'Kawkhali',NULL,50),(144,'Dhamrai',NULL,1),(145,'Dohar',NULL,1),(146,'Keraniganj',NULL,1),(147,'Nawabganj',NULL,1),(148,'Savar',NULL,1),(149,'FaridpurSadar',NULL,2),(150,'Boalmari',NULL,2),(151,'Alfadanga',NULL,2),(152,'Madhukhali',NULL,2),(153,'Bhanga',NULL,2),(154,'Nagarkanda',NULL,2),(155,'Charbhadrasan',NULL,2),(156,'Sadarpur',NULL,2),(157,'Shaltha',NULL,2),(158,'GazipurSadar',NULL,3),(159,'Kaliakair',NULL,3),(160,'Kapasia',NULL,3),(161,'Sripur',NULL,3),(162,'Kaliganj',NULL,3),(163,'Gurudaspur',NULL,21),(164,'GopalganjSadar',NULL,4),(165,'Kashiani',NULL,4),(166,'Kotalipara',NULL,4),(167,'Muksudpur',NULL,4),(168,'Tungipara',NULL,4),(169,'Dewanganj',NULL,5),(170,'Bokshiganj',NULL,5),(171,'Islampur',NULL,5),(172,'JamalpurSadar',NULL,5),(173,'Madarganj',NULL,5),(174,'Melandaha',NULL,5),(175,'Sarishabari',NULL,5),(176,'Austagram',NULL,6),(177,'Bajitpur',NULL,6),(178,'Bhairab',NULL,6),(179,'Hossainpur',NULL,6),(180,'Itna',NULL,6),(181,'Karimganj',NULL,6),(182,'Katiadi',NULL,6),(183,'KishoreganjSadar',NULL,6),(184,'Kuliarchar',NULL,6),(185,'Mithamain',NULL,6),(186,'Nikli',NULL,6),(187,'Pakundia',NULL,6),(188,'Tarail',NULL,6),(189,'MadaripurSadar',NULL,7),(190,'Kalkini',NULL,7),(191,'Rajoir',NULL,7),(192,'Shibchar',NULL,7),(193,'ManikganjSadar',NULL,8),(194,'Singair',NULL,8),(195,'Shibalaya',NULL,8),(196,'Saturia',NULL,8),(197,'Harirampur',NULL,8),(198,'Ghior',NULL,8),(199,'Daulatpur',NULL,8),(200,'Lohajang',NULL,9),(201,'Sreenagar',NULL,9),(202,'MunshiganjSadar',NULL,9),(203,'Sirajdikhan',NULL,9),(204,'Tongibari',NULL,9),(205,'Gazaria',NULL,9),(206,'Bhaluka',NULL,10),(207,'Trishal',NULL,10),(208,'Haluaghat',NULL,10),(209,'Muktagachha',NULL,10),(210,'Dhobaura',NULL,10),(211,'Fulbaria',NULL,10),(212,'Gaffargaon',NULL,10),(213,'Gauripur',NULL,10),(214,'Ishwarganj',NULL,10),(215,'MymensinghSadar',NULL,10),(216,'Nandail',NULL,10),(217,'Phulpur',NULL,10),(218,'Araihazar',NULL,11),(219,'Sonargaon',NULL,11),(220,'Bandar',NULL,11),(221,'NarayanganjSadar',NULL,11),(222,'Rupganj',NULL,11),(223,'Belabo',NULL,12),(224,'Monohardi',NULL,12),(225,'NarsingdiSadar ',NULL,12),(226,'Palash',NULL,12),(227,'Raipura',NULL,12),(228,'Shibpur',NULL,12),(229,'Kendua',NULL,13),(230,'Atpara',NULL,13),(231,'Barhatta',NULL,13),(232,'Durgapur',NULL,13),(233,'Kalmakanda',NULL,13),(234,'Madan',NULL,13),(235,'Mohanganj',NULL,13),(236,'NetrokonaSadar',NULL,13),(237,'Purbadhala',NULL,13),(238,'Khaliajuri',NULL,13),(239,'Baliakandi',NULL,14),(240,'Goalanda',NULL,14),(241,'Pangsha',NULL,14),(242,'Kalukhali',NULL,14),(243,'RajbariSadar',NULL,14),(244,'ShariatpurSadar',NULL,15),(245,'Damudya',NULL,15),(246,'Naria ',NULL,15),(247,'Zajira',NULL,15),(248,'Bhedarganj',NULL,15),(249,'Gosairhat',NULL,15),(250,'Jhenaigati',NULL,16),(251,'Nakla',NULL,16),(252,'Nalitabari',NULL,16),(253,'SherpurSadar',NULL,16),(254,'Sreebardi',NULL,16),(255,'TangailSadar',NULL,17),(256,'Sakhipur',NULL,17),(257,'Basail',NULL,17),(258,'Madhupur',NULL,17),(259,'Ghatail',NULL,17),(260,'Kalihati',NULL,17),(261,'Nagarpur',NULL,17),(262,'Mirzapur',NULL,17),(263,'Gopalpur',NULL,17),(264,'Delduar',NULL,17),(265,'Bhuapur',NULL,17),(266,'Dhanbari',NULL,17),(267,'BagerhatSadar',NULL,55),(268,'Chitalmari',NULL,55),(269,'Fakirhat',NULL,55),(270,'Kachua',NULL,55),(271,'Mollahat ',NULL,55),(272,'Mongla',NULL,55),(273,'Morrelganj',NULL,55),(274,'Rampal',NULL,55),(275,'Sarankhola',NULL,55),(276,'Damurhuda',NULL,56),(277,'ChuadangaSadar',NULL,56),(278,'Jibannagar',NULL,56),(279,'Alamdanga',NULL,56),(280,'Abhaynagar',NULL,57),(281,'Keshabpur',NULL,57),(282,'Bagherpara',NULL,57),(283,'JashoreSadar',NULL,57),(284,'Chaugachha',NULL,57),(285,'Manirampur',NULL,57),(286,'Jhikargachha',NULL,57),(287,'Sharsha',NULL,57),(288,'JhenaidahSadar',NULL,58),(289,'Maheshpur',NULL,58),(290,'Kaliganj',NULL,58),(291,'Kotchandpur',NULL,58),(292,'Shailkupa',NULL,58),(293,'Harinakundu',NULL,58),(294,'Terokhada',NULL,59),(295,'Batiaghata',NULL,59),(296,'Dacope',NULL,59),(297,'Dumuria',NULL,59),(298,'Dighalia',NULL,59),(299,'Koyra',NULL,59),(300,'Paikgachha',NULL,59),(301,'Phultala',NULL,59),(302,'Rupsa',NULL,59),(303,'KushtiaSadar',NULL,60),(304,'Kumarkhali',NULL,60),(305,'Daulatpur',NULL,60),(306,'Mirpur',NULL,60),(307,'Bheramara',NULL,60),(308,'Khoksa',NULL,60),(309,'MaguraSadar',NULL,61),(310,'Mohammadpur',NULL,61),(311,'Shalikha',NULL,61),(312,'Sreepur',NULL,61),(313,'Gangni',NULL,62),(314,'MujibNagar',NULL,62),(315,'MeherpurSadar',NULL,62),(316,'NarailSadar',NULL,63),(317,'Lohagara',NULL,63),(318,'Kalia',NULL,63),(319,'SatkhiraSadar',NULL,64),(320,'Assasuni',NULL,64),(321,'Debhata',NULL,64),(322,'Tala',NULL,64),(323,'Kalaroa',NULL,64),(324,'Kaliganj',NULL,64),(325,'Shyamnagar ',NULL,64),(326,'Adamdighi',NULL,18),(327,'BograSadar',NULL,18),(328,'Sherpur',NULL,18),(329,'Dhunat',NULL,18),(330,'Dhupchanchia',NULL,18),(331,'Gabtali',NULL,18),(332,'Kahaloo',NULL,18),(333,'Nandigram',NULL,18),(334,'Shajahanpur',NULL,18),(335,'Sariakandi',NULL,18),(336,'Shibganj',NULL,18),(337,'Sonatala',NULL,18),(338,'JoypurhatSadar',NULL,19),(339,'Akkelpur',NULL,19),(340,'Kalai',NULL,19),(341,'Khetlal',NULL,19),(342,'Panchbibi',NULL,19),(343,'NaogaonSadar ',NULL,20),(344,'Mohadevpur',NULL,20),(345,'Manda',NULL,20),(346,'Niamatpur ',NULL,20),(347,'Atrai',NULL,20),(348,'Raninagar',NULL,20),(349,'Patnitala ',NULL,20),(350,'Dhamoirhat',NULL,20),(351,'Sapahar',NULL,20),(352,'Porsha',NULL,20),(353,'Badalgachhi',NULL,20),(354,'NatoreSadar',NULL,21),(355,'Baraigram',NULL,21),(356,'Bagatipara',NULL,21),(357,'Lalpur',NULL,21),(358,'Singra',NULL,21),(359,'Naldanga',NULL,21),(360,'Bholahat',NULL,22),(361,'Gomastapur',NULL,22),(362,'Nachole',NULL,22),(363,'ChapainawabganjSadar',NULL,22),(364,'Shibganj',NULL,22),(365,'Atgharia',NULL,23),(366,'Bera',NULL,23),(367,'Bhangura',NULL,23),(368,'Chatmohar',NULL,23),(369,'Faridpur',NULL,23),(370,'Ishwardi',NULL,23),(371,'PabnaSadar',NULL,23),(372,'Santhia',NULL,23),(373,'Sujanagar',NULL,23),(374,'Bagha',NULL,24),(375,'Bagmara',NULL,24),(376,'Charghat',NULL,24),(377,'Durgapur',NULL,24),(378,'Godagari',NULL,24),(379,'Mohanpur',NULL,24),(380,'Paba',NULL,24),(381,'Puthia',NULL,24),(382,'Tanore',NULL,24),(383,'SirajganjSadar',NULL,25),(384,'Belkuchi',NULL,25),(385,'Chauhali',NULL,25),(386,'Kamarkhanda',NULL,25),(387,'Kazipur',NULL,25),(388,'Raigonj',NULL,25),(389,'Shahjadpur',NULL,25),(390,'Tarash',NULL,25),(391,'Ullapara',NULL,25),(392,'Birampur',NULL,26),(393,'Birganj',NULL,26),(394,'Biral',NULL,26),(395,'Bochaganj',NULL,26),(396,'Chirirbandar',NULL,26),(397,'Fulbari',NULL,26),(398,'Ghoraghat',NULL,26),(399,'Hakimpur',NULL,26),(400,'Kaharole',NULL,26),(401,'Khansama',NULL,26),(402,'DinajpurSadar',NULL,26),(403,'Nawabganj',NULL,26),(404,'Parbatipur',NULL,26),(405,'Fulchhari',NULL,27),(406,'GaibandhaSadar',NULL,27),(407,'Gobindaganj',NULL,27),(408,'Palashbari',NULL,27),(409,'Sadullapur',NULL,27),(410,'Saghata',NULL,27),(411,'Sundarganj',NULL,27),(412,'KurigramSadar',NULL,28),(413,'Nageshwari',NULL,28),(414,'Bhurungamari',NULL,28),(415,'Phulbari',NULL,28),(416,'Rajarhat',NULL,28),(417,'Ulipur',NULL,28),(418,'Chilmari',NULL,28),(419,'Rowmari',NULL,28),(420,'CharRajibpur',NULL,28),(421,'LalmonirhatSadar',NULL,29),(422,'Aditmari',NULL,29),(423,'Kaliganj',NULL,29),(424,'Hatibandha',NULL,29),(425,'Patgram',NULL,29),(426,'NilphamariSadar',NULL,30),(427,'Saidpur',NULL,30),(428,'Jaldhaka',NULL,30),(429,'Kishoreganj',NULL,30),(430,'Domar',NULL,30),(431,'Dimla',NULL,30),(432,'PanchagarhSadar',NULL,31),(433,'Debiganj',NULL,31),(434,'Boda',NULL,31),(435,'Atwari',NULL,31),(436,'Tetulia',NULL,31),(437,'Badarganj',NULL,32),(438,'Mithapukur',NULL,32),(439,'Gangachara',NULL,32),(440,'Kaunia',NULL,32),(441,'RangpurSadar',NULL,32),(442,'Pirgachha',NULL,32),(443,'Pirganj',NULL,32),(444,'Taraganj',NULL,32),(445,'ThakurgaonSadar',NULL,33),(446,'Pirganj',NULL,33),(447,'Baliadangi',NULL,33),(448,'Haripur',NULL,33),(449,'Ranisankail',NULL,33),(450,'Ajmiriganj',NULL,51),(451,'Baniachong',NULL,51),(452,'Bahubal',NULL,51),(453,'Chunarughat',NULL,51),(454,'HabiganjSadar',NULL,51),(455,'Lakhai',NULL,51),(456,'Madhabpur',NULL,51),(457,'Nabiganj',NULL,51),(458,'Shayestaganj',NULL,51),(459,'MoulvibazarSadar',NULL,52),(460,'Barlekha',NULL,52),(461,'Juri',NULL,52),(462,'Kamalganj',NULL,52),(463,'Kulaura',NULL,52),(464,'Rajnagar',NULL,52),(465,'Sreemangal',NULL,52),(466,'Bishwambarpur',NULL,53),(467,'Chhatak',NULL,53),(468,'Derai',NULL,53),(469,'Dharampasha',NULL,53),(470,'Dowarabazar',NULL,53),(471,'Jagannathpur',NULL,53),(472,'Jamalganj',NULL,53),(473,'Shalla',NULL,53),(474,'SunamganjSadar',NULL,53),(475,'SouthSunamganj',NULL,53),(476,'Tahirpur',NULL,53),(477,'SylhetSadar',NULL,54),(478,'Beanibazar',NULL,54),(479,'Bishwanath',NULL,54),(480,'SouthSurma',NULL,54),(481,'Balaganj',NULL,54),(482,'Companiganj',NULL,54),(483,'Fenchuganj',NULL,54),(484,'Golapganj',NULL,54),(485,'Gowainghat',NULL,54),(486,'Jaintiapur',NULL,54),(487,'Kanaighat',NULL,54),(488,'Zakiganj',NULL,54),(489,'Osmaninagar',NULL,54),(490,'DhakaNorthCityCorporation',NULL,1),(491,'DhakaSouthCityCorporation',NULL,1),(492,'Debidwar',NULL,44),(493,'Guimara',NULL,47),(495,'Tarakanda',NULL,10),(496,'RajshahiCityCorporation',NULL,24),(497,'KhulnaCityCorporation',NULL,59),(498,'ChattogramCityCorporation',NULL,43),(499,'CumillaCityCorporation',NULL,44),(500,'GazipurCityCorporation',NULL,3),(501,'NarayanganjCitycorporation',NULL,11),(502,'BarishalCityCorporation',NULL,35),(503,'MymensinghCityCorporation',NULL,10),(504,'RangpurCityCorporation',NULL,32),(505,'SylhetCityCorporation',NULL,54);
/*!40000 ALTER TABLE `farm_upazila` ENABLE KEYS */;
UNLOCK TABLES;

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
  `seasonal` tinyint(1) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `delete_status` int(11) NOT NULL,
  `vegetable_type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` (`vegetable_type_id`),
  CONSTRAINT `farm_vegetable_vegetable_type_id_0377ae6c_fk_farm_croptype_id` FOREIGN KEY (`vegetable_type_id`) REFERENCES `farm_croptype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farm_vegetable`
--

LOCK TABLES `farm_vegetable` WRITE;
/*!40000 ALTER TABLE `farm_vegetable` DISABLE KEYS */;
INSERT INTO `farm_vegetable` VALUES (60,'Islampuri','Bele, Atel Soil/All types of soil','Winter','36 Ton/Hectre',1,NULL,'',NULL,'',0,135),(61,'Singnath','Bele, Atel Soil/All types of soil','All Time','30 Ton/Hectre',0,NULL,'',NULL,'',0,135),(62,'Tarapuri','Bele, Atel Soil/All types of soil','All Time','80 Ton/Hectre',0,NULL,'',NULL,'',0,135),(63,'Bari Jhinga 1','All types of soil','All Time','10-15 Ton/Hectre',0,NULL,'',NULL,'',0,136),(64,'Bari Mula 1(Tasakisan)','Bele Doash','Winter','65-70 Ton/Hectre',1,NULL,'',NULL,'',0,137),(65,'Everest F1','Bele Doash','All Time','50-60 Ton/Hectre',0,NULL,'',NULL,'',0,137),(66,'Mino Early Long White','Bele Doash','Summer','40-50 Ton/Hectre',1,NULL,'',NULL,'',0,137),(67,'Shauni','Doash,Bele Doash','Summer','5-7 Ton/Hectre',1,NULL,'',NULL,'',0,138),(68,'Bari Dherosh','Doash,Bele Doash','Summer','8-10 Ton/Hectre',1,NULL,'',NULL,'',0,138),(69,'Kabuli Doarf','Doash,Bele Doash','All Time','4-5 Ton/Hectre',0,NULL,'',NULL,'',0,138),(70,'Japani Pacific Green','Doash,Bele Doash','All Time','5-6 Ton/Hectre',0,NULL,'',NULL,'',0,138),(71,'Bari Borboti 1','Doash,Bele Doash','Summer','10-12 Ton/Hectre',1,NULL,'',NULL,'',0,139),(72,'Vegornatoki','Doash,Bele Doash','Summer','9-10Ton/Hectre',1,NULL,'',NULL,'',0,139),(73,'Hybrid Isha Kha','Bele Doash, Poli Doash','Winter','75-80 Ton/Hectre',1,NULL,'',NULL,'',0,140),(74,'Hybrid Bronco','Bele Doash, Poli Doash','All Time','75-80 Ton/Hectre',0,NULL,'',NULL,'',0,140),(75,'Summer Warrior','Bele Doash, Poli Doash','Summer','75-80 Ton/Hectre',1,NULL,'',NULL,'',0,140),(76,'Provati','Bele Doash, Poli Doash','Winter','110 Ton/Hectre',1,NULL,'',NULL,'',0,140),(77,'Hazari','Doash, Atel Doash','Winter','25-30 Ton/Hectre',1,NULL,'',NULL,'',0,141),(78,'Bari Lau-1','Doash, Atel Doash','All Time','25-30 Ton/Hectre',0,NULL,'',NULL,'',0,141),(79,'Bari Seam 1','Doash,Bele Doash','Winter','20-22 Ton/Hectre',1,NULL,'',NULL,'',0,142),(80,'B U Seam 3','Doash,Bele Doash','All Time','7-8 Ton/Hectre',0,NULL,'',NULL,'',0,142),(81,'Ipsha Seam 2','Doash,Bele Doash','All Time','7-8 Ton/Hectre',0,NULL,'',NULL,'',0,142),(82,'Bari Korola 1','Doash,Bele Doash','All Time','25-30 Ton/Hectre',0,NULL,'',NULL,'',0,143),(83,'Goz Korola','Doash,Bele Doash','All Time','20-25 Ton/Hectre',0,NULL,'',NULL,'',0,143),(84,'Suprema','Doash, Atel Doash','All Time','18-20 Ton/Hectre',0,NULL,'',NULL,'',0,144),(85,'Sweety','Doash, Atel Doash','All Time','18-20 Ton/Hectre',0,NULL,'',NULL,'',0,144),(86,'Dreamgold','Doash, Atel Doash','All Time','18-20 Ton/Hectre',0,NULL,'',NULL,'',0,144),(87,'Solid Gold','Doash, Atel Doash','All Time','18-20 Ton/Hectre',0,NULL,'',NULL,'',0,144),(88,'Bari Potol 1','Bele Doash, Doash','Summer','30-38 Ton/Hectre',1,NULL,'',NULL,'',0,145),(89,'Baro Potol 2','Bele Doash, Doash','Summer','30 Ton/Hectre',1,NULL,'',NULL,'',0,145),(90,'Baromasi','Doash','All Time','10-12 Ton/Hectre',0,NULL,'',NULL,'',0,146),(91,'Potia Giant','Doash','All Time','10-12 Ton/Hectre',0,NULL,'',NULL,'',0,146),(92,'Alta Peti','Bele Doash, Atel Doash','All Time','5-6 Ton/Hectre',0,NULL,'',NULL,'',0,147),(93,'Bari lal Shak 1','Bele Doash, Atel Doash','All Time','5-6 Ton/Hectre',0,NULL,'',NULL,'',0,147),(94,'Bari Tomato 4','Atel Doash','Early Winter','20-40 Ton/Hectre',1,NULL,'',NULL,'',0,148),(95,'Roma VF','Atel Doash','Early Winter','20-40 Ton/Hectre',1,NULL,'',NULL,'',0,148),(96,'Manik','Atel Doash','Winter','20-40 Ton/Hectre',1,NULL,'',NULL,'',0,148),(97,'Ratan','Atel Doash','Winter','20-40 Ton/Hectre',1,NULL,'',NULL,'',0,148),(98,'Bari Tomato 6(Chaiti)','Atel Doash','All Time','20-40 Ton/Hectre',0,NULL,'',NULL,'',0,148),(99,'Aghrahoni','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(100,'Early Patnai','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(101,'Super Snowball','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(102,'Heat master','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(103,'Poushali','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(104,'Snowball X','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(105,'Chandrima 60 F1','Doash, Atel','Early Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(106,'Maghi Benarosi','Doash, Atel','Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(107,'White Mountain','Doash, Atel','Winter','35-60 Ton/Hectre',1,NULL,'',NULL,'',0,149),(108,'Bari Fulcopy 1','Doash, Atel','Winter','50-60 Ton/Hectre',1,NULL,'',NULL,'',0,149);
/*!40000 ALTER TABLE `farm_vegetable` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `i_menu_name`
--

LOCK TABLES `i_menu_name` WRITE;
/*!40000 ALTER TABLE `i_menu_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `i_menu_name` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `i_module_action`
--

LOCK TABLES `i_module_action` WRITE;
/*!40000 ALTER TABLE `i_module_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `i_module_action` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `i_module_name`
--

LOCK TABLES `i_module_name` WRITE;
/*!40000 ALTER TABLE `i_module_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `i_module_name` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `i_privilege`
--

LOCK TABLES `i_privilege` WRITE;
/*!40000 ALTER TABLE `i_privilege` DISABLE KEYS */;
/*!40000 ALTER TABLE `i_privilege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_crating_detail`
--

DROP TABLE IF EXISTS `process_crating_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_crating_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(255) DEFAULT NULL,
  `scanned_by` varchar(100) NOT NULL,
  `scanned_at` datetime(6) DEFAULT NULL,
  `removed_by` varchar(100) NOT NULL,
  `removed_at` datetime(6) DEFAULT NULL,
  `process_crating_master_id` int(11) DEFAULT NULL,
  `process_packaging_detail_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_crating_deta_process_crating_mast_81a99891_fk_process_c` (`process_crating_master_id`),
  KEY `process_crating_deta_process_packaging_de_3de01fc0_fk_process_p` (`process_packaging_detail_id`),
  CONSTRAINT `process_crating_deta_process_crating_mast_81a99891_fk_process_c` FOREIGN KEY (`process_crating_master_id`) REFERENCES `process_crating_master` (`id`),
  CONSTRAINT `process_crating_deta_process_packaging_de_3de01fc0_fk_process_p` FOREIGN KEY (`process_packaging_detail_id`) REFERENCES `process_packaging_detail` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_crating_detail`
--

LOCK TABLES `process_crating_detail` WRITE;
/*!40000 ALTER TABLE `process_crating_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_crating_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_crating_master`
--

DROP TABLE IF EXISTS `process_crating_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_crating_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_no_of_package` int(11) NOT NULL,
  `create_at` datetime(6) DEFAULT NULL,
  `create_by` varchar(100) NOT NULL,
  `modify_at` datetime(6) DEFAULT NULL,
  `modify_by` varchar(100) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `crate_id` int(11) DEFAULT NULL,
  `process_receiving_master_id` int(11) DEFAULT NULL,
  `process_shipping_master_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_crating_mast_process_receiving_ma_d4960173_fk_process_r` (`process_receiving_master_id`),
  KEY `process_crating_mast_process_shipping_mas_bc3f6daf_fk_process_s` (`process_shipping_master_id`),
  KEY `process_crating_mast_crate_id_8e3fc459_fk_processin` (`crate_id`),
  CONSTRAINT `process_crating_mast_crate_id_8e3fc459_fk_processin` FOREIGN KEY (`crate_id`) REFERENCES `processing_crateinfo` (`id`),
  CONSTRAINT `process_crating_mast_process_receiving_ma_d4960173_fk_process_r` FOREIGN KEY (`process_receiving_master_id`) REFERENCES `process_receiving_master` (`id`),
  CONSTRAINT `process_crating_mast_process_shipping_mas_bc3f6daf_fk_process_s` FOREIGN KEY (`process_shipping_master_id`) REFERENCES `process_shipping_master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_crating_master`
--

LOCK TABLES `process_crating_master` WRITE;
/*!40000 ALTER TABLE `process_crating_master` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_crating_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_packaging_damaged`
--

DROP TABLE IF EXISTS `process_packaging_damaged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_packaging_damaged` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `processing_id` varchar(128) DEFAULT NULL,
  `sticker_qr_code` varchar(255) NOT NULL,
  `sticker_bar_code` varchar(20) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `deleted_by` varchar(100) NOT NULL,
  `deleted_at` datetime(6) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `comment` longtext,
  `process_crating_master_id` int(11) DEFAULT NULL,
  `process_packaging_master_id` int(11) DEFAULT NULL,
  `process_receiving_master_id` int(11) DEFAULT NULL,
  `process_shipping_master_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_packaging_da_process_crating_mast_7b6d6bb0_fk_process_c` (`process_crating_master_id`),
  KEY `process_packaging_da_process_packaging_ma_282bdba3_fk_process_p` (`process_packaging_master_id`),
  KEY `process_packaging_da_process_receiving_ma_9207811c_fk_process_r` (`process_receiving_master_id`),
  KEY `process_packaging_da_process_shipping_mas_58eb89d9_fk_process_s` (`process_shipping_master_id`),
  CONSTRAINT `process_packaging_da_process_crating_mast_7b6d6bb0_fk_process_c` FOREIGN KEY (`process_crating_master_id`) REFERENCES `process_crating_master` (`id`),
  CONSTRAINT `process_packaging_da_process_packaging_ma_282bdba3_fk_process_p` FOREIGN KEY (`process_packaging_master_id`) REFERENCES `process_packaging_master` (`id`),
  CONSTRAINT `process_packaging_da_process_receiving_ma_9207811c_fk_process_r` FOREIGN KEY (`process_receiving_master_id`) REFERENCES `process_receiving_master` (`id`),
  CONSTRAINT `process_packaging_da_process_shipping_mas_58eb89d9_fk_process_s` FOREIGN KEY (`process_shipping_master_id`) REFERENCES `process_shipping_master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_packaging_damaged`
--

LOCK TABLES `process_packaging_damaged` WRITE;
/*!40000 ALTER TABLE `process_packaging_damaged` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_packaging_damaged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_packaging_detail`
--

DROP TABLE IF EXISTS `process_packaging_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_packaging_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `processing_id` varchar(128) DEFAULT NULL,
  `sticker_qr_code` varchar(255) NOT NULL,
  `sticker_bar_code` varchar(20) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `printed_by` varchar(100) NOT NULL,
  `printed_at` datetime(6) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `comment` longtext,
  `process_crating_master_id` int(11) DEFAULT NULL,
  `process_packaging_master_id` int(11) DEFAULT NULL,
  `process_receiving_master_id` int(11) DEFAULT NULL,
  `process_shipping_master_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_packaging_de_process_crating_mast_f218e6d7_fk_process_c` (`process_crating_master_id`),
  KEY `process_packaging_de_process_packaging_ma_ab60ca7c_fk_process_p` (`process_packaging_master_id`),
  KEY `process_packaging_de_process_receiving_ma_1b3b55a2_fk_process_r` (`process_receiving_master_id`),
  KEY `process_packaging_de_process_shipping_mas_5141aab3_fk_process_s` (`process_shipping_master_id`),
  CONSTRAINT `process_packaging_de_process_crating_mast_f218e6d7_fk_process_c` FOREIGN KEY (`process_crating_master_id`) REFERENCES `process_crating_master` (`id`),
  CONSTRAINT `process_packaging_de_process_packaging_ma_ab60ca7c_fk_process_p` FOREIGN KEY (`process_packaging_master_id`) REFERENCES `process_packaging_master` (`id`),
  CONSTRAINT `process_packaging_de_process_receiving_ma_1b3b55a2_fk_process_r` FOREIGN KEY (`process_receiving_master_id`) REFERENCES `process_receiving_master` (`id`),
  CONSTRAINT `process_packaging_de_process_shipping_mas_5141aab3_fk_process_s` FOREIGN KEY (`process_shipping_master_id`) REFERENCES `process_shipping_master` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_packaging_detail`
--

LOCK TABLES `process_packaging_detail` WRITE;
/*!40000 ALTER TABLE `process_packaging_detail` DISABLE KEYS */;
INSERT INTO `process_packaging_detail` VALUES (1,'1','qr/harvest_id','1301201234',NULL,'1','2021-01-13 10:59:09.000000','packaged',NULL,NULL,1,NULL,NULL),(2,'1','qr/harvest_id','1301201235',NULL,'1','2021-01-13 11:00:07.000000','packaged',NULL,NULL,1,NULL,NULL),(3,'1','qr/harvest_id','1301201236',NULL,'1','2021-01-13 11:00:38.000000','packaged',NULL,NULL,1,NULL,NULL);
/*!40000 ALTER TABLE `process_packaging_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_packaging_master`
--

DROP TABLE IF EXISTS `process_packaging_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_packaging_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `quantity` varchar(64) DEFAULT NULL,
  `packaging_unit` varchar(64) DEFAULT NULL,
  `packaging_unit_per_package` varchar(64) DEFAULT NULL,
  `total_no_of_sticker` int(11) NOT NULL,
  `exp_date` date DEFAULT NULL,
  `processing_id` varchar(128) DEFAULT NULL,
  `processing_date` date DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `crop_id` int(11) DEFAULT NULL,
  `crop_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_packaging_master_crop_id_6c107970_fk_farm_crop_id` (`crop_id`),
  KEY `process_packaging_ma_crop_type_id_72443364_fk_farm_crop` (`crop_type_id`),
  CONSTRAINT `process_packaging_ma_crop_type_id_72443364_fk_farm_crop` FOREIGN KEY (`crop_type_id`) REFERENCES `farm_croptype` (`id`),
  CONSTRAINT `process_packaging_master_crop_id_6c107970_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_packaging_master`
--

LOCK TABLES `process_packaging_master` WRITE;
/*!40000 ALTER TABLE `process_packaging_master` DISABLE KEYS */;
INSERT INTO `process_packaging_master` VALUES (1,'30','kg','10',3,'2021-01-11','1','2021-01-11','2021-01-11 10:05:29.290212','1','2021-01-11 10:05:29.290212','1',5,135);
/*!40000 ALTER TABLE `process_packaging_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_receiving_detail`
--

DROP TABLE IF EXISTS `process_receiving_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_receiving_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contact_no` varchar(16) NOT NULL,
  `status` varchar(24) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `received_at` datetime(6) DEFAULT NULL,
  `received_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `process_crating_master_id` int(11) DEFAULT NULL,
  `process_receiving_master_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_receiving_de_process_crating_mast_082a9669_fk_process_c` (`process_crating_master_id`),
  KEY `process_receiving_de_process_receiving_ma_a3c87497_fk_process_r` (`process_receiving_master_id`),
  CONSTRAINT `process_receiving_de_process_crating_mast_082a9669_fk_process_c` FOREIGN KEY (`process_crating_master_id`) REFERENCES `process_crating_master` (`id`),
  CONSTRAINT `process_receiving_de_process_receiving_ma_a3c87497_fk_process_r` FOREIGN KEY (`process_receiving_master_id`) REFERENCES `process_receiving_master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_receiving_detail`
--

LOCK TABLES `process_receiving_detail` WRITE;
/*!40000 ALTER TABLE `process_receiving_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_receiving_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_receiving_master`
--

DROP TABLE IF EXISTS `process_receiving_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_receiving_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hub_address` longtext NOT NULL,
  `contact_no` varchar(16) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `status` varchar(24) NOT NULL,
  `total_no_of_crate` int(11) NOT NULL,
  `received_at` datetime(6) DEFAULT NULL,
  `received_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_receiving_master`
--

LOCK TABLES `process_receiving_master` WRITE;
/*!40000 ALTER TABLE `process_receiving_master` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_receiving_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_shipping_detail`
--

DROP TABLE IF EXISTS `process_shipping_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_shipping_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shipping_id` varchar(128) DEFAULT NULL,
  `status` varchar(24) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `process_crating_master_id` int(11) DEFAULT NULL,
  `process_shipping_master_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `process_shipping_det_process_crating_mast_7e25fa55_fk_process_c` (`process_crating_master_id`),
  KEY `process_shipping_det_process_shipping_mas_c15a9e4a_fk_process_s` (`process_shipping_master_id`),
  CONSTRAINT `process_shipping_det_process_crating_mast_7e25fa55_fk_process_c` FOREIGN KEY (`process_crating_master_id`) REFERENCES `process_crating_master` (`id`),
  CONSTRAINT `process_shipping_det_process_shipping_mas_c15a9e4a_fk_process_s` FOREIGN KEY (`process_shipping_master_id`) REFERENCES `process_shipping_master` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_shipping_detail`
--

LOCK TABLES `process_shipping_detail` WRITE;
/*!40000 ALTER TABLE `process_shipping_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_shipping_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_shipping_master`
--

DROP TABLE IF EXISTS `process_shipping_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_shipping_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_address` longtext NOT NULL,
  `contact_no` varchar(16) NOT NULL,
  `status` varchar(24) NOT NULL,
  `total_no_of_crate` int(11) NOT NULL,
  `shipping_id` varchar(128) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_shipping_master`
--

LOCK TABLES `process_shipping_master` WRITE;
/*!40000 ALTER TABLE `process_shipping_master` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_shipping_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processing_crateinfo`
--

DROP TABLE IF EXISTS `processing_crateinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `processing_crateinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crate_no` varchar(255) DEFAULT NULL,
  `empty_weight` int(11) DEFAULT NULL,
  `max_weight` int(11) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `bar_code` varchar(255) DEFAULT NULL,
  `dimension` varchar(255) DEFAULT NULL,
  `delete_status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processing_crateinfo`
--

LOCK TABLES `processing_crateinfo` WRITE;
/*!40000 ALTER TABLE `processing_crateinfo` DISABLE KEYS */;
INSERT INTO `processing_crateinfo` VALUES (3,'47360002',3,33,'2021-01-19 12:50:15.897109','1',NULL,'1','ready','394750190121','5x3x2 mm3',1),(4,'47360002',1,15,'2021-01-19 15:21:17.208178','1',NULL,NULL,'ready','824382190121','5x3x2 mm3',0);
/*!40000 ALTER TABLE `processing_crateinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production_harvesting`
--

DROP TABLE IF EXISTS `production_harvesting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `production_harvesting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `harvest_cycle` int(11) NOT NULL,
  `crop_status` varchar(50) DEFAULT NULL,
  `total_labor_hour` int(11) NOT NULL,
  `quantity` varchar(64) NOT NULL,
  `processing_id` varchar(128) DEFAULT NULL,
  `status` varchar(64) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `farmer_id` int(11) DEFAULT NULL,
  `seeding_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `production_harvesting_farmer_id_4cc9fed3_fk_farm_farmer_id` (`farmer_id`),
  KEY `production_harvestin_seeding_id_4ccc53ea_fk_productio` (`seeding_id`),
  CONSTRAINT `production_harvestin_seeding_id_4ccc53ea_fk_productio` FOREIGN KEY (`seeding_id`) REFERENCES `production_seeding` (`id`),
  CONSTRAINT `production_harvesting_farmer_id_4cc9fed3_fk_farm_farmer_id` FOREIGN KEY (`farmer_id`) REFERENCES `farm_farmer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production_harvesting`
--

LOCK TABLES `production_harvesting` WRITE;
/*!40000 ALTER TABLE `production_harvesting` DISABLE KEYS */;
INSERT INTO `production_harvesting` VALUES (1,1,'ok',120,'10','','partially harvested','2021-01-06 12:42:11.109916','1','2021-01-06 12:42:11.109916','1',1,3),(2,2,'ok',120,'10',NULL,'partially harvested','2021-01-06 12:48:36.504192','1','2021-01-06 12:48:36.504192','1',1,3),(3,3,'ok',5,'5',NULL,'fully harvested','2021-01-06 12:51:09.982781','1','2021-01-07 12:51:09.000000','1',1,3),(4,1,'ripe',5,'50',NULL,'partially harvested','2021-01-10 15:11:59.526710','1','2021-01-10 15:11:59.526710','1',1,4),(5,2,'ripe',5,'10',NULL,'partially harvested','2021-01-10 15:12:26.200363','1','2021-01-10 15:12:26.200363','1',1,4),(6,3,'ripe',5,'15',NULL,'partially harvested','2021-01-10 15:13:12.380246','1','2021-01-10 15:13:12.380246','1',1,4),(7,4,'ripe',5,'15',NULL,'fully harvested','2021-01-10 15:13:30.492312','1','2021-01-10 15:13:30.492312','1',1,4);
/*!40000 ALTER TABLE `production_harvesting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production_plot`
--

DROP TABLE IF EXISTS `production_plot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `production_plot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_procurement` varchar(50) DEFAULT NULL,
  `costing` int(11) NOT NULL,
  `expected_harvesting_time` int(11) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `total_labor_hour` int(11) NOT NULL,
  `crop_variant` int(11) NOT NULL,
  `fertilizers` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `plot_uuid` varchar(100) DEFAULT NULL,
  `sensor_data_seeding` longtext,
  `sensor_data_harvesting` longtext,
  `comment` longtext,
  `crop_id` int(11) DEFAULT NULL,
  `crop_type_id` int(11) DEFAULT NULL,
  `seeding_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `production_plot_crop_id_286b2372_fk_farm_crop_id` (`crop_id`),
  KEY `production_plot_crop_type_id_219ed5db_fk_farm_croptype_id` (`crop_type_id`),
  KEY `production_plot_seeding_id_2d0cec85_fk_production_seeding_id` (`seeding_id`),
  CONSTRAINT `production_plot_crop_id_286b2372_fk_farm_crop_id` FOREIGN KEY (`crop_id`) REFERENCES `farm_crop` (`id`),
  CONSTRAINT `production_plot_crop_type_id_219ed5db_fk_farm_croptype_id` FOREIGN KEY (`crop_type_id`) REFERENCES `farm_croptype` (`id`),
  CONSTRAINT `production_plot_seeding_id_2d0cec85_fk_production_seeding_id` FOREIGN KEY (`seeding_id`) REFERENCES `production_seeding` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production_plot`
--

LOCK TABLES `production_plot` WRITE;
/*!40000 ALTER TABLE `production_plot` DISABLE KEYS */;
INSERT INTO `production_plot` VALUES (3,NULL,0,0,'2021-01-06 12:34:48.070582','fully harvested',0,60,'0','2021-01-06 12:34:48.070582','1','2021-01-06 12:34:48.070582','1',NULL,'0','0','0',1,135,3),(4,NULL,0,0,'2021-01-06 12:34:48.119578','fully harvested',0,60,'0','2021-01-06 12:34:48.119578','1','2021-01-06 12:34:48.119578','1',NULL,'0','0','0',1,135,3),(5,NULL,0,0,'2021-01-10 15:06:13.500705','fully harvested',0,60,'0','2021-01-10 15:06:13.500705','1','2021-01-10 15:06:13.500705','1',NULL,'0','0','0',5,135,4);
/*!40000 ALTER TABLE `production_plot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production_seeding`
--

DROP TABLE IF EXISTS `production_seeding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `production_seeding` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `seed_name` varchar(100) DEFAULT NULL,
  `land_usage` int(11) NOT NULL,
  `status` varchar(64) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `farmer_id` int(11) NOT NULL,
  `land_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `production_seeding_farmer_id_1dc3cead_fk_farm_farmer_id` (`farmer_id`),
  KEY `production_seeding_land_id_4bb56038_fk_farm_land_id` (`land_id`),
  CONSTRAINT `production_seeding_farmer_id_1dc3cead_fk_farm_farmer_id` FOREIGN KEY (`farmer_id`) REFERENCES `farm_farmer` (`id`),
  CONSTRAINT `production_seeding_land_id_4bb56038_fk_farm_land_id` FOREIGN KEY (`land_id`) REFERENCES `farm_land` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production_seeding`
--

LOCK TABLES `production_seeding` WRITE;
/*!40000 ALTER TABLE `production_seeding` DISABLE KEYS */;
INSERT INTO `production_seeding` VALUES (3,'potato',50,'fully harvested','2021-01-06 12:34:48.019580','1','2021-01-06 12:34:48.019580','1',1,31),(4,'cabbage',50,'fully harvested','2021-01-10 15:06:13.446729','1','2021-01-10 15:06:13.446729','1',5,31);
/*!40000 ALTER TABLE `production_seeding` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_role`
--

LOCK TABLES `users_role` WRITE;
/*!40000 ALTER TABLE `users_role` DISABLE KEYS */;
INSERT INTO `users_role` VALUES (1,'Super Admin','2020-11-17 18:04:38.000000','0','2020-11-17 18:04:46.000000','0');
/*!40000 ALTER TABLE `users_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `nid` varchar(12) DEFAULT NULL,
  `phone_number` varchar(11) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `created_by` varchar(100) NOT NULL,
  `last_updated_at` datetime(6) DEFAULT NULL,
  `last_updated_by` varchar(100) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `production_house_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `nid` (`nid`),
  KEY `users_user_production_house_id_8cd1ede5_fk_farm_prod` (`production_house_id`),
  KEY `users_user_role_id_854f2687_fk_users_role_id` (`role_id`),
  CONSTRAINT `users_user_production_house_id_8cd1ede5_fk_farm_prod` FOREIGN KEY (`production_house_id`) REFERENCES `farm_productionhouse` (`id`),
  CONSTRAINT `users_user_role_id_854f2687_fk_users_role_id` FOREIGN KEY (`role_id`) REFERENCES `users_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'Narayanganj','pbkdf2_sha256$216000$94XA39Dc7iBy$wU1u2EM/70P6tlZKRtizCnxR9VUpsbOnejFt9q3GsyA=','ridwanmizan@gmail.com','Md. Ridwan Mizan','2848919748','01739129488','',1,'2021-01-06 12:04:51.872746','','2021-01-06 12:04:51.872746','',NULL,1,1);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

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

-- Dump completed on 2021-01-21 19:11:28

-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: query_portal
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('Client','Support Team') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'rajat','rajat12@yopmail.com','$2b$12$kNnQMNmjOQOTbHAUhqcVeOBcrkylHXu4kdJ9Ega1AJRTR6.jrAv1O','Client','2025-11-09 14:07:11'),(2,'parul','parul12@yopmail.com','$2b$12$RqqJiM99WJuaJgSZaxRxvOC0vfmfiHPIeSgwVi7/p799PFJs/jwYK','Support Team','2025-11-09 15:10:59'),(3,'abc','abc@12','$2b$12$slYMo9E5.JG0G7MqbUnLLebhAj4E/Chj4lVTEglboQL2k85VMEhpC','Client','2025-11-13 19:01:12'),(4,'abc','ab23@yopmail.com','$2b$12$1hlxYcJuQKi.b4IGDXCRreDVmsZPe3biz06vjKRjsKoCVEbJ2hIqu','Client','2025-11-13 19:03:59'),(5,'tre','rk12@yopmail.com','$2b$12$eix27AUt5CZEaWx.NOeJVuZh8QAKPh7va0n.cr19ON41U4YPIUVSq','Support Team','2025-11-13 19:06:27'),(6,'jatin','jatin12@yopmail.com','$2b$12$Syjs2eFVlxGMyvH7aDVRXeQj0BeeOyU9/SZtI/7eoxX1P49HckNQq','Client','2025-11-14 06:09:29'),(7,'mukul','mukul@yopmail.com','$2b$12$8CBKnJ6hoonkCdCDjQYC4e.009EsJk2q68poROK0UaIaVIQQSqOW.','Client','2025-11-14 06:15:12'),(8,'xyz','xyz@yopmail.com','$2b$12$NeCB9IuM/l6Vcl6E0sqOAOfoBa1CCmCLwhfCzGl1Q7UbPfw3BsT.2','Client','2025-11-14 06:19:42'),(9,'gaurav ','gaurav@yopmail.com','$2b$12$ah2/FtGeVBn2RnWTaAkj4u4hWAUuqzj29V.ZUR9xwHXuMjKpUVBim','Client','2025-11-14 06:23:06'),(10,'mark','mark@yopmail.com','$2b$12$uzafSLFwlHN.DljAAMRZlufu..zvDwdcj9xv3vwxhtIJmsZBeDa12','Client','2025-11-14 06:29:23'),(11,'john','john@yopmail.com','$2b$12$yp.mjEJb/25Zzm8E8DT/aOWOlnFsLxuFyQ2cJ4MRpDhCcTcooBbwm','Client','2025-11-14 06:33:16'),(12,'piyush','piyush@yopmail.com','$2b$12$WpVzl4GIDE9yEH7ErsdYOON4dSs5etUC6OdF4OzMRlBu/irHidZuK','Client','2025-11-14 06:46:45');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-14 12:37:33

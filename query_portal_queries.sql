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
-- Table structure for table `queries`
--

DROP TABLE IF EXISTS `queries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `queries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `email` varchar(255) NOT NULL,
  `heading` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `status` enum('Open','Closed') DEFAULT 'Open',
  `query_created_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `query_closed_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_query` (`user_id`),
  CONSTRAINT `fk_user_query` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `queries`
--

LOCK TABLES `queries` WRITE;
/*!40000 ALTER TABLE `queries` DISABLE KEYS */;
INSERT INTO `queries` VALUES (3,1,'rajat12@yopmail.com','Test','dssd','990909090','Closed','2025-11-12 01:54:10','2025-11-14 00:37:01'),(4,1,'rajat12@yopmail.com','Test33','sdfsfdfd','9909090890','Open','2025-11-13 01:14:54',NULL),(5,4,'ab23@yopmail.com','fraud','facing fraud error ','7654808545','Closed','2025-11-14 00:35:43','2025-11-14 00:37:01'),(6,6,'jatin12@yopmail.com','Credit card fraud','Facing Issue of credit card limit used but I don\'t use that limit.','8797578957','Open','2025-11-14 11:42:38',NULL),(7,7,'mukul@yopmail.com','Fraud Detect in ATM Machine','Issue registered that the whole amount is deducted from the bank ','6764256632','Open','2025-11-14 11:48:32',NULL),(8,8,'xyz@yopmail.com','Debit card not working','Issue registered that the user debit card is not working properly in the atm machine.','9874638292','Open','2025-11-14 11:52:26',NULL),(9,9,'gaurav@yopmail.com','Issue For Duplicate notes in ATM machine','Complaint registered for giving duplicate notes from ATM Machine','7853920472','Open','2025-11-14 11:55:31',NULL),(10,10,'mark@yopmail.com','Error in your bank server','Error detect during transaction the bank server is temporary down.\n','7643992523','Open','2025-11-14 12:01:16',NULL),(11,11,'john@yopmail.com','Hack the system','Query Registered that the hacker create the another page for transaction and do fraud to empty the bank account\n','6546893428','Open','2025-11-14 12:05:12',NULL),(12,12,'piyush@yopmail.com','OTP error during transaction','issue registered that at the time of transaction OTP will be invalid every time.','9875432346','Open','2025-11-14 12:19:41',NULL);
/*!40000 ALTER TABLE `queries` ENABLE KEYS */;
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

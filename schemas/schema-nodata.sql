-- MariaDB dump 10.19  Distrib 10.7.3-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: kimetsu_no_yaiba
-- ------------------------------------------------------
-- Server version	10.7.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ataques`
--

DROP TABLE IF EXISTS `ataques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ataques` (
  `id_ataque` int(11) NOT NULL,
  `nombre_ataque` tinytext DEFAULT NULL,
  `arma` tinytext NOT NULL,
  PRIMARY KEY (`id_ataque`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ataques`
--

LOCK TABLES `ataques` WRITE;
/*!40000 ALTER TABLE `ataques` DISABLE KEYS */;
/*!40000 ALTER TABLE `ataques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cazadores`
--

DROP TABLE IF EXISTS `cazadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cazadores` (
  `id_cazador` int(11) NOT NULL,
  `nombre` tinytext DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `rango` tinytext DEFAULT NULL,
  `pais_origen` tinytext NOT NULL,
  PRIMARY KEY (`id_cazador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cazadores`
--

LOCK TABLES `cazadores` WRITE;
/*!40000 ALTER TABLE `cazadores` DISABLE KEYS */;
/*!40000 ALTER TABLE `cazadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cazadores_ataques`
--

DROP TABLE IF EXISTS `cazadores_ataques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cazadores_ataques` (
  `id_cazador_ataque` int(11) NOT NULL,
  `id_ataque` int(11) DEFAULT NULL,
  `id_cazador` int(11) DEFAULT NULL,
  `desde` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id_cazador_ataque`),
  KEY `cazadores_ataques_ataques_id_ataque_fk` (`id_ataque`),
  KEY `cazadores_ataques_cazadores_id_cazador_fk` (`id_cazador`),
  CONSTRAINT `cazadores_ataques_ataques_id_ataque_fk` FOREIGN KEY (`id_ataque`) REFERENCES `ataques` (`id_ataque`),
  CONSTRAINT `cazadores_ataques_cazadores_id_cazador_fk` FOREIGN KEY (`id_cazador`) REFERENCES `cazadores` (`id_cazador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cazadores_ataques`
--

LOCK TABLES `cazadores_ataques` WRITE;
/*!40000 ALTER TABLE `cazadores_ataques` DISABLE KEYS */;
/*!40000 ALTER TABLE `cazadores_ataques` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demonios`
--

DROP TABLE IF EXISTS `demonios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `demonios` (
  `id_demonio` int(11) NOT NULL,
  `nombre` tinytext NOT NULL,
  `rango` tinytext NOT NULL,
  PRIMARY KEY (`id_demonio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demonios`
--

LOCK TABLES `demonios` WRITE;
/*!40000 ALTER TABLE `demonios` DISABLE KEYS */;
/*!40000 ALTER TABLE `demonios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_enfrentamientos`
--

DROP TABLE IF EXISTS `detalle_enfrentamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `detalle_enfrentamientos` (
  `id_detalle_enfrentamiento` int(11) NOT NULL,
  `id_cazador` int(11) DEFAULT NULL,
  `id_demonio` int(11) DEFAULT NULL,
  `id_enfrentamiento` int(11) DEFAULT NULL,
  `estado_cazador` tinytext DEFAULT NULL,
  `estado_demonio` tinytext DEFAULT NULL,
  PRIMARY KEY (`id_detalle_enfrentamiento`),
  KEY `detalle_enfrentamientos_cazadores_id_cazador_fk` (`id_cazador`),
  KEY `detalle_enfrentamientos_demonios_id_demonio_fk` (`id_demonio`),
  KEY `detalle_enfrentamientos_enfrentamientos_id_enfrentamiento_fk` (`id_enfrentamiento`),
  CONSTRAINT `detalle_enfrentamientos_cazadores_id_cazador_fk` FOREIGN KEY (`id_cazador`) REFERENCES `cazadores` (`id_cazador`),
  CONSTRAINT `detalle_enfrentamientos_demonios_id_demonio_fk` FOREIGN KEY (`id_demonio`) REFERENCES `demonios` (`id_demonio`),
  CONSTRAINT `detalle_enfrentamientos_enfrentamientos_id_enfrentamiento_fk` FOREIGN KEY (`id_enfrentamiento`) REFERENCES `enfrentamientos` (`id_enfrentamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_enfrentamientos`
--

LOCK TABLES `detalle_enfrentamientos` WRITE;
/*!40000 ALTER TABLE `detalle_enfrentamientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_enfrentamientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enfrentamientos`
--

DROP TABLE IF EXISTS `enfrentamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enfrentamientos` (
  `id_enfrentamiento` int(11) NOT NULL,
  `fecha` datetime DEFAULT NULL,
  PRIMARY KEY (`id_enfrentamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enfrentamientos`
--

LOCK TABLES `enfrentamientos` WRITE;
/*!40000 ALTER TABLE `enfrentamientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `enfrentamientos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-12 13:10:27

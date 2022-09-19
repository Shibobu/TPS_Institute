-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: ejbiblioteca
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autores` (
  `id_Autor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id_Autor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `autoresxlibros`
--

DROP TABLE IF EXISTS `autoresxlibros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autoresxlibros` (
  `id_Libro` int NOT NULL,
  `id_Autor` int NOT NULL,
  `fecha_Ingreso` date NOT NULL,
  `fecha_alta` date DEFAULT NULL,
  `motivo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_Libro`,`id_Autor`),
  KEY `FK_Autor_AutorXLibros` (`id_Autor`),
  CONSTRAINT `FK_Autor_AutorXLibros` FOREIGN KEY (`id_Autor`) REFERENCES `autores` (`id_Autor`) ON UPDATE CASCADE,
  CONSTRAINT `FK_Libro_AutorXLibros` FOREIGN KEY (`id_Libro`) REFERENCES `libros` (`id_Libro`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autoresxlibros`
--

LOCK TABLES `autoresxlibros` WRITE;
/*!40000 ALTER TABLE `autoresxlibros` DISABLE KEYS */;
/*!40000 ALTER TABLE `autoresxlibros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bibliotecas`
--

DROP TABLE IF EXISTS `bibliotecas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bibliotecas` (
  `cuit` varchar(12) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `id_Domic` int DEFAULT NULL,
  `id_Biblio` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_Biblio`),
  KEY `FK_Direcciones_Bibliotecas` (`id_Domic`),
  CONSTRAINT `FK_Direcciones_Bibliotecas` FOREIGN KEY (`id_Domic`) REFERENCES `direcciones` (`id_Domic`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bibliotecas`
--

LOCK TABLES `bibliotecas` WRITE;
/*!40000 ALTER TABLE `bibliotecas` DISABLE KEYS */;
/*!40000 ALTER TABLE `bibliotecas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direcciones`
--

DROP TABLE IF EXISTS `direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `direcciones` (
  `id_Domic` int NOT NULL AUTO_INCREMENT,
  `calle` varchar(200) NOT NULL,
  `number` int DEFAULT NULL,
  `localidad` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_Domic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `direcciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ejemplares`
--

DROP TABLE IF EXISTS `ejemplares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ejemplares` (
  `id_Ejemp` int NOT NULL AUTO_INCREMENT,
  `ubicacion` varchar(100) DEFAULT NULL,
  `id_Libro` int DEFAULT NULL,
  PRIMARY KEY (`id_Ejemp`),
  KEY `FK_Libros_Ejemplares` (`id_Libro`),
  CONSTRAINT `FK_Libros_Ejemplares` FOREIGN KEY (`id_Libro`) REFERENCES `libros` (`id_Libro`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ejemplares`
--

LOCK TABLES `ejemplares` WRITE;
/*!40000 ALTER TABLE `ejemplares` DISABLE KEYS */;
/*!40000 ALTER TABLE `ejemplares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ejemplaresxprestamos`
--

DROP TABLE IF EXISTS `ejemplaresxprestamos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ejemplaresxprestamos` (
  `id_Ejemp` int NOT NULL,
  `id_Prestamos` int NOT NULL,
  PRIMARY KEY (`id_Ejemp`,`id_Prestamos`),
  KEY `FK_Prestamos_EjemplaresXPrestamos` (`id_Prestamos`),
  CONSTRAINT `FK_Ejemplares_EjemplaresXPrestamos` FOREIGN KEY (`id_Ejemp`) REFERENCES `ejemplares` (`id_Ejemp`) ON UPDATE CASCADE,
  CONSTRAINT `FK_Prestamos_EjemplaresXPrestamos` FOREIGN KEY (`id_Prestamos`) REFERENCES `prestamos` (`id_Prestamos`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ejemplaresxprestamos`
--

LOCK TABLES `ejemplaresxprestamos` WRITE;
/*!40000 ALTER TABLE `ejemplaresxprestamos` DISABLE KEYS */;
/*!40000 ALTER TABLE `ejemplaresxprestamos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros` (
  `id_Libro` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(200) NOT NULL,
  `editorial` varchar(150) DEFAULT NULL,
  `page_Numb` int DEFAULT NULL,
  `id_Biblio` int DEFAULT NULL,
  PRIMARY KEY (`id_Libro`),
  KEY `FK_Bibliotecas_Libros` (`id_Biblio`),
  CONSTRAINT `FK_Bibliotecas_Libros` FOREIGN KEY (`id_Biblio`) REFERENCES `bibliotecas` (`id_Biblio`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestamos`
--

DROP TABLE IF EXISTS `prestamos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestamos` (
  `id_Prestamos` int NOT NULL AUTO_INCREMENT,
  `fecha_Prestamos` date NOT NULL,
  `fecha_Devolucion` date DEFAULT NULL,
  `id_Usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_Prestamos`),
  KEY `FK_Usuarios_Prestamos` (`id_Usuario`),
  CONSTRAINT `FK_Usuarios_Prestamos` FOREIGN KEY (`id_Usuario`) REFERENCES `usuarios` (`id_Usuario`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestamos`
--

LOCK TABLES `prestamos` WRITE;
/*!40000 ALTER TABLE `prestamos` DISABLE KEYS */;
/*!40000 ALTER TABLE `prestamos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `dni` varchar(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `id_Domic` int DEFAULT NULL,
  `id_Biblio` int DEFAULT NULL,
  `id_Usuario` int NOT NULL,
  PRIMARY KEY (`id_Usuario`),
  KEY `FK_Bibliotecas_Usuarios` (`id_Biblio`),
  KEY `FK_Direcciones_Usuarios` (`id_Domic`),
  CONSTRAINT `FK_Bibliotecas_Usuarios` FOREIGN KEY (`id_Biblio`) REFERENCES `bibliotecas` (`id_Biblio`) ON UPDATE CASCADE,
  CONSTRAINT `FK_Direcciones_Usuarios` FOREIGN KEY (`id_Domic`) REFERENCES `direcciones` (`id_Domic`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-15 15:15:37

-- MySQL dump 10.13  Distrib 5.5.33, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: nxgame
-- ------------------------------------------------------
-- Server version	5.5.33-0+wheezy1

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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event` int(11) NOT NULL,
  `episode` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `question` text NOT NULL,
  `title` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,19,1,2,'<img src=/images/litenhestmedfemben.jpg width=40%>','r3bu5'),(2,19,1,3,'<a href=/images/storhestmedfyraben.mp4>Ibland gÃ¥r jag vilse.</a>','Promenad'),(3,19,1,5,'/ 9 13 1 7 5 19 / 13 10 21 11 19 11 15 18 19 20 5 14 . 10 16 7','Siffror Ã¤r nice!'),(4,19,1,1,'<div style=\"background-color:#fff; width:400px; height:200px;\">\r\n<p style=\"color:#fff;\">VÃ¤lkommen! Svaret Ã¤r kaktuslime</p> </div> ','The introduction'),(5,19,1,4,'<img src=/images/FEMTUSEN.jpg width=30%>','SkÃ¶nhet pÃ¥ rÃ¤tt avstÃ¥nd'),(6,19,2,4,'<a href=/images/svaretaerinteclasohlson.mp4>Funky new musicgenre</a>\r\n\r\nFrÃ¥g-fix:\r\nSista ska vara:\r\n<img src=/images/ifix.png>','Writing with the piano'),(7,19,2,5,'<img src=\"/images/reptilier.jpg\" width=\"15%\">\r\n','ArbetsfÃ¶rmedlingen'),(8,19,2,1,'The answer is already up south!','Light and magic'),(9,19,2,2,'Bara Ankan cyklade ofta nog pÃ¥ onsdagar. Papaya, citroner, oliver, rambutan, nektarin','Gott!'),(10,19,2,3,'Nu Ã¤r det dax att <img src=/images/walking.jpg width=15%> igen pÃ¥ Tyngelvi.','Undra vad man skulle gÃ¶ra nu egentligen?'),(11,19,3,1,'<a href=/images/camera.mp4>Instabil kamera</a> ','Camerafocus'),(12,19,3,2,'<a href=/images/tigerkaka.mp3>Poem</a>\r\n\r\n','Colours of opportunity'),(13,19,3,3,'Vi har efter lÃ¥ng avlyssning av alla trÃ¤d upptÃ¤ckt att det ligger ubÃ¥tar i skogen som fÃ¶rsÃ¶ker kommunicera med mÃ¥nbasen.\r\nDin uppgift, should you choose to accept it, Ã¤r att ta reda pÃ¥ vad dessa mystiska vÃ¥gor innehÃ¥ller.\r\nVi har valt att teama ihop dig med vÃ¥r avlyssningsexpert <i>Franz MÃ¼ller</i>. Tillsammans med honom, mÃ¥ste ni lyckas hitta ryssen.','From Russia with love'),(14,19,3,4,'<a href=/images/Kolmepukkia.mp4>I wanna play a game</a>\r\n\r\nHint:\r\n<img src=/images/dejavu.jpg width=40%>','FemTusen'),(15,20,1,1,'Vem Ã¤r sÃ¤hmst?','Peter Ã¤r sÃ¤mst');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-05 13:09:16

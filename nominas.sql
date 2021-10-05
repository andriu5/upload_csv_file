SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Notificaciones_Proactivas
-- -----------------------------------------------------
-- DROP SCHEMA IF EXISTS `Notificaciones_Proactivas`

-- -----------------------------------------------------
-- Schema Notificaciones_Proactivas
-- -----------------------------------------------------
-- CREATE SCHEMA IF NOT EXISTS `Notificaciones_Proactivas` DEFAULT CHARACTER SET utf8 ;
USE `Notificaciones_Proactivas`;


-- DROP TABLE IF EXISTS `Notificaciones_Proactivas`.`nomina_usuarios`;

-- -----------------------------------------------------
-- Table `Notificaciones_Proactivas`.`nomina_usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Notificaciones_Proactivas`.`nomina_usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rut` VARCHAR(45) NOT NULL DEFAULT '',
  `nombre` VARCHAR(500) NULL DEFAULT NULL,
  `email_ejecutivo` VARCHAR(255) NULL,
  `custom1` TEXT NULL DEFAULT NULL,
  `custom2` TEXT NULL DEFAULT NULL,
  `custom3` TEXT NULL DEFAULT NULL,
  `custom4` TEXT NULL DEFAULT NULL,
  `custom5` TEXT NULL DEFAULT NULL,
  `fecha_creacion` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
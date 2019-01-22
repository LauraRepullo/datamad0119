-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`SALESPERSON`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SALESPERSON` (
  `Name Salesperson` VARCHAR(45) NULL,
  `Surname Salesperson` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `idSALESPERSONS` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSALESPERSONS`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`INVOICES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`INVOICES` (
  `Date` VARCHAR(45) NULL,
  `idINVOICES` VARCHAR(45) NOT NULL,
  `SALESPERSON_idSALESPERSONS` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idINVOICES`),
  INDEX `fk_INVOICES_SALESPERSON1_idx` (`SALESPERSON_idSALESPERSONS` ASC),
  CONSTRAINT `fk_INVOICES_SALESPERSON1`
    FOREIGN KEY (`SALESPERSON_idSALESPERSONS`)
    REFERENCES `mydb`.`SALESPERSON` (`idSALESPERSONS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CUSTOMERS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CUSTOMERS` (
  `idCUSTOMERS` INT NOT NULL AUTO_INCREMENT,
  `Name Customer` VARCHAR(45) NOT NULL,
  `Phone` INT NULL,
  `Adress` VARCHAR(100) NULL,
  `City` VARCHAR(45) NULL,
  `ZIP` VARCHAR(45) NULL,
  PRIMARY KEY (`idCUSTOMERS`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CARS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CARS` (
  `VIN` INT NOT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` DATE NULL,
  `Color` VARCHAR(45) NULL,
  `INVOICES_idINVOICES` VARCHAR(45) NOT NULL,
  `CUSTOMERS_idCUSTOMERS` INT NOT NULL,
  `SALESPERSON_idSALESPERSONS` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VIN`),
  INDEX `fk_CARS_INVOICES1_idx` (`INVOICES_idINVOICES` ASC),
  INDEX `fk_CARS_CUSTOMERS1_idx` (`CUSTOMERS_idCUSTOMERS` ASC),
  INDEX `fk_CARS_SALESPERSON1_idx` (`SALESPERSON_idSALESPERSONS` ASC),
  CONSTRAINT `fk_CARS_INVOICES1`
    FOREIGN KEY (`INVOICES_idINVOICES`)
    REFERENCES `mydb`.`INVOICES` (`idINVOICES`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CARS_CUSTOMERS1`
    FOREIGN KEY (`CUSTOMERS_idCUSTOMERS`)
    REFERENCES `mydb`.`CUSTOMERS` (`idCUSTOMERS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CARS_SALESPERSON1`
    FOREIGN KEY (`SALESPERSON_idSALESPERSONS`)
    REFERENCES `mydb`.`SALESPERSON` (`idSALESPERSONS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`INVOICES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`INVOICES` (
  `Date` VARCHAR(45) NULL,
  `idINVOICES` VARCHAR(45) NOT NULL,
  `SALESPERSON_idSALESPERSONS` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idINVOICES`),
  INDEX `fk_INVOICES_SALESPERSON1_idx` (`SALESPERSON_idSALESPERSONS` ASC),
  CONSTRAINT `fk_INVOICES_SALESPERSON1`
    FOREIGN KEY (`SALESPERSON_idSALESPERSONS`)
    REFERENCES `mydb`.`SALESPERSON` (`idSALESPERSONS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

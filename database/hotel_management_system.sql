CREATE DATABASE IF NOT EXISTS management;
USE management;

--Customer table
CREATE TABLE `customer` (
  `Ref` int NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Mother` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Postcode` varchar(45) DEFAULT NULL,
  `Mobile` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Nationality` varchar(45) DEFAULT NULL,
  `IdProof` varchar(45) DEFAULT NULL,
  `IdNumber` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Ref`)
);

-- Details table
CREATE TABLE `details` (
  `Floor` varchar(45) DEFAULT NULL,
  `RoomNo` varchar(45) NOT NULL,
  `RoomType` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`RoomNo`)
);

-- Register table
CREATE TABLE `register` (
  `First Name` varchar(45) NOT NULL,
  `Last Name` varchar(45) DEFAULT NULL,
  `Contact` varchar(45) DEFAULT NULL,
  `Email` varchar(45) NOT NULL,
  `Security Question` varchar(45) DEFAULT NULL,
  `Security Answer` varchar(45) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Email`)
);

-- Room table
CREATE TABLE `room` (
  `Contact` varchar(45) DEFAULT NULL,
  `Checkin` varchar(45) DEFAULT NULL,
  `Checkout` varchar(45) DEFAULT NULL,
  `Roomtype` varchar(45) DEFAULT NULL,
  `Roomavailable` varchar(45) NOT NULL,
  `Meal` varchar(45) DEFAULT NULL,
  `Noofdays` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Roomavailable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

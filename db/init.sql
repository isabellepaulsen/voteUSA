-- drop database voterdb;
create database voterdb;

use voterdb;

CREATE TABLE
  Users (
    User_ID int PRIMARY KEY AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    MiddleName varchar(100),
    LastName varchar(100) NOT NULL,
    Age int NOT NULL,
    StreetAddress1 varchar(250) NOT NULL,
    StreetAddress2 varchar(250) NOT NULL,
    City varchar(250) NOT NULL,
    State varchar(250) NOT NULL,
    ZipCode varchar(10),
    ID1 varchar(250) NOT NULL,
    ID2 varchar(250) NOT NULL,
    Email varchar(100) UNIQUE,
    Password varchar(255) NOT NULL,
    Salt varchar(255) NOT NULL,
    Role varchar(15) NOT NULL
  );

INSERT INTO 
  Users (
    FirstName, MiddleName, LastName, Age, StreetAddress1, StreetAddress2, City, State, ZipCode, ID1, ID2, Email, Password, Salt, Role
  )
  Values (
  "Eric", "J", "T", 22, "Coralville","20th Ave","Coralville", "Iowa", "52241", "dl", "birth cert", "voter@e", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu", "Voter"
  );

  INSERT INTO 
  Users (
    FirstName, MiddleName, LastName, Age, StreetAddress1, StreetAddress2, City, State, ZipCode, ID1, ID2, Email, Password, Salt, Role
  )
  Values (
  "Eric", "J", "T", 22, "Coralville","20th Ave","Coralville", "Iowa", "52241", "dl", "birth cert", "admin@e", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu", "Admin"
  );


INSERT INTO 
  Users (
    FirstName, MiddleName, LastName, Age, StreetAddress1, StreetAddress2, City, State, ZipCode, ID1, ID2, Email, Password, Salt, Role
  )
  Values (
  "Eric", "J", "T", 22, "Coralville","20th Ave","Coralville", "Iowa", "52241", "dl", "birth cert", "manager@e", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLumRpSXkDFN6Cpy807ztE28ClpOpnUyku", "$2b$12$nK0Sgy5GdoEKsFn7BbqWLu", "Manager"
  );



DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `get_user_auth` (IN mail varchar(255))
BEGIN
   SELECT User_ID, Password, Salt, Role FROM Users WHERE STRCMP(Email, mail) = 0;
END$$

DELIMITER ;

DELIMITER $$
-- USE `voterdb`$$
CREATE PROCEDURE `insert_user` (IN name1 varchar(100), IN name2 varchar(100), IN name3 varchar(100), IN age int, IN address1 varchar(250),
IN address2 varchar(250), IN city varchar(250), IN state varchar(100),
IN zip int, IN ID1 varchar (20), IN ID2 varchar(20), IN email varchar(100), IN password varchar(255), IN salt varchar(255), IN role varchar(255))
BEGIN
  INSERT INTO voterdb.Users(FirstName, MiddleName, LastName, Age, StreetAddress1, StreetAddress2, City, State, ZipCode, ID1, ID2 , Email, Password, Salt, Role) 
  VALUES (name1, name2, name3, age, address1, address2, city, state, zip, ID1, ID2, email, password, salt, role);
END$$

DELIMITER ;



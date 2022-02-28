create table Pet(
    petID int,
    petName varChar(255),
    petAge int,
    favouriteFood int
)
 create table Petnamelist(
     petID int,
     pname varCHAR(20),
    FOREIGN KEY (petID) REFERENCES Pet
    ON DELETE CASCADE);

 )
 INSERT INTO Pet
  (petID, petName, petAge, favouriteFood)
  VALUES
  (1,"Tom",10,"tuna"),
  (2,"Coco",6,"bone"),
  (3,"Gary",1,"cheese");

INSERT INTO Petnamelist
    (petID, pname)
  VALUES
  (1,"garfield"),
  (1,"Tom"),
  (2,"doggo"),
  (2,"Coco");
)
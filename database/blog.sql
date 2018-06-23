CREATE DATABASE Blog;

CREATE TABLE Users(
    ID int NOT NULL,
    Username varchar(255),
    HashedPassword varchar(255),
    PRIMARY KEY(ID)
    );
    

CREATE TABLE Posts(
    ID int NOT NULL,
    Title varchar(255),
    Body text,
    AuthorID int,
    PRIMARY KEY(ID),
    FOREIGN KEY (AuthorID) REFERENCES users(id)
    );

CREATE TABLE Comments(
    ID int NOT NULL,
    Comment text,
    AuthorID int,
    PostID int,
    PRIMARY KEY(ID),
    FOREIGN KEY (AuthorID) REFERENCES users(id),
    FOREIGN KEY (PostID) REFERENCES posts(id)
    );

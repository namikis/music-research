CREATE TABLE musics (
    id int AUTO_INCREMENT,
    music_name VARCHAR(300),
    valence decimal(4,3),
    energy decimal(4,3),
    music_id CHAR(30),
    artist_name VARCHAR(300),
    PRIMARY KEY (id)
);

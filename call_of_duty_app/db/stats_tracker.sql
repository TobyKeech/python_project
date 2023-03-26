DROP TABLE IF EXISTS codprofiles;
DROP TABLE IF EXISTS platforms;
DROP TABLE IF EXISTS weapons;


CREATE TABLE platforms (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE weapons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    ammo VARCHAR(255),
    range VARCHAR(255)
);

CREATE TABLE codprofiles (
    id SERIAL PRIMARY KEY,
    gamer_tag VARCHAR(255),
    kills INT,
    deaths INT,
    rank INT, 
    platform_id INT NOT NULL REFERENCES platforms(id),
    weapon_id INT NOT NULL REFERENCES weapons(id)
);


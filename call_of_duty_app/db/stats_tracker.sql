DROP TABLE IF EXISTS codprofiles;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS weapons;


CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT
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
    rank VARCHAR(255), 
    user_id INT NOT NULL REFERENCES users(id),
    weapon_id INT NOT NULL REFERENCES weapons(id)
);


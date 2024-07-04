CREATE DATABASE IF NOT EXISTS bookstore_db
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE bookstore_db;

-- DROP TABLE IF EXISTS authors;
CREATE TABLE authors (id BINARY(16) NOT NULL, name VARCHAR(255) UNIQUE NOT NULL, PRIMARY KEY (id));

INSERT INTO authors (id, name) VALUES (UUID_TO_BIN('34c045ce-cd8a-4ff7-a9fe-2bff4289331d', true), 'Erik Larson');
INSERT INTO authors (id, name) VALUES (UUID_TO_BIN('b5c09148-c073-4bd4-909c-30ec51360377', true), 'Stephen King');
INSERT INTO authors (id, name) VALUES (UUID_TO_BIN('12fbdc9c-6fa1-46cb-8f4b-e33b0373db91', true), 'Bonnie Blaylock');

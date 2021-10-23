CREATE DATABASE file_tracker;


CREATE TABLE text_files (
    id serial,
    file_name varchar(100),
    file_size integer
);
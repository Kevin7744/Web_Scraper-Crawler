-- Active: 1701169624194@@127.0.0.1@3306
CREATE DATABASE scraping;

use scraping ;

CREATE TABLE pages (
id BIGINT(7) NOT NULL AUTO_INCREMENT,
title VARCHAR(200), content VARCHAR(10000),
created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id)
);


DESCRIBE pages;


INSERT INTO pages (title, content) VALUES ('Test page title', 
'this is some test page content. 
It can be up to 10,000 characters long'
);


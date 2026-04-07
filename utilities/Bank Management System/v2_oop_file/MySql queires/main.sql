--  use this in your workbench

CREATE DATABASE IF NOT EXISTS BankManagementSystem;

USE BankManagementSystem;

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    balance INT
);

SELECT * FROM accounts;
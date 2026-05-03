-- 1. Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS grocery_db;
USE grocery_db;

-- 2. Create the inventory table
CREATE TABLE IF NOT EXISTS inventory (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    current_stock INT NOT NULL,
    min_threshold INT DEFAULT 10, -- The limit that triggers an alert
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 3. Insert fresh data for testing
-- Notice: Apples and Bread will trigger the alert because they are below their threshold
INSERT INTO inventory (product_name, current_stock, min_threshold) VALUES 
('Fresh Milk (1L)', 25, 10),
('Red Apples', 4, 15),       -- LOW STOCK
('Whole Wheat Bread', 3, 10), -- LOW STOCK
('Organic Eggs (12pk)', 40, 12),
('Cooking Oil (1L)', 15, 5);

-- 4. Verify the data
SELECT * FROM inventory;
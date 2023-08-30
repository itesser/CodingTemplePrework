CREATE TABLE IF NOT EXISTS customers(
	cust_id int,
    cust_name varchar(255),
    address varchar(255)
);

INSERT INTO customers
VALUES(
	001, 
    'Mary Sue',
    '1785 Brighton Ln, Maysbury, TX 77521'
),
(
	002,
    'Kaladin Stormblessed',
    '4 Bridge Wy, Uruthiru, AK 97721'
),
(
	003,
    'Yarin Arelius',
    '432 Uncrowned Ave #1, Sacred Valley, CA'
);

SELECT * FROM customers


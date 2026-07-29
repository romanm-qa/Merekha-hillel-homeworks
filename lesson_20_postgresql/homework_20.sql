create table categories (
id serial primary key,
name varchar(100) not null
);

create table products (
id serial primary key,
name varchar(150) not null,
description text,
price numeric(10, 2) not null,
category_id integer not null,
foreign key (category_id) references categories(id)
);

INSERT INTO categories (name)
VALUES
    ('Electronics'),
    ('Books'),
    ('Home appliances');

INSERT INTO products (name, description, price, category_id)
VALUES
    ('Laptop', 'Laptop for work and study', 32000.00, 1),
    ('Python Basics', 'Book for learning Python', 650.00, 2),
    ('Microwave', 'Microwave oven for the kitchen', 4800.00, 3),
    ('Headphones', 'Wireless headphones', 2500.00, 1);

SELECT
    products.name AS product_name,
    products.description,
    products.price,
    categories.name AS category_name
FROM products
JOIN categories ON products.category_id = categories.id;
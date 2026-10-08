-- ===== Day 1: table, INSERT, SELECT =====
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    available BOOLEAN DEFAULT TRUE
);

INSERT INTO books (title, author, year) VALUES ('Clean Code', 'Robert C. Martin', 2008);
INSERT INTO books (title, author, year) VALUES ('Python Crash Course', 'Eric Matthes', 2019);
INSERT INTO books (title, author, year) VALUES ('The Pragmatic Programmer', 'Andrew Hunt', 1999);
INSERT INTO books (title, author, year) VALUES ('Django for Beginners', 'William Vincent', 2022);

SELECT * FROM books;
SELECT title, author FROM books;
SELECT * FROM books WHERE year > 2000;

-- ===== Day 2: WHERE, ORDER BY, UPDATE, DELETE =====
UPDATE books SET available = FALSE WHERE id = 3;
SELECT * FROM books WHERE available = TRUE;
SELECT * FROM books WHERE title LIKE '%Python%';
SELECT * FROM books ORDER BY year DESC;
DELETE FROM books WHERE id = 4;
SELECT * FROM books;

-- (1) unavailable books
SELECT * FROM books WHERE available = FALSE;

-- (2) books after 2010
SELECT * FROM books WHERE year > 2010;

-- (3) books sorted alphabetically by title
SELECT * FROM books ORDER BY title;

-- (4) author containing 'Martin'
SELECT * FROM books WHERE author LIKE '%Martin%';
-- ===== Day 3: library schema =====

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    available BOOLEAN DEFAULT TRUE,
    borrow_count INTEGER DEFAULT 0
);

CREATE TABLE members (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE borrowings (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    borrowed_at DATE NOT NULL,
    returned_at DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

INSERT INTO books (title, author, year) VALUES ('Clean Code', 'Robert C. Martin', 2008);
INSERT INTO books (title, author, year) VALUES ('Python Crash Course', 'Eric Matthes', 2019);
INSERT INTO members (name, email) VALUES ('Ali', 'ali@example.com');
INSERT INTO members (name, email) VALUES ('Sara', 'sara@example.com');
INSERT INTO borrowings (book_id, member_id, borrowed_at) VALUES (1, 2, '2026-09-01');

SELECT * FROM borrowings;
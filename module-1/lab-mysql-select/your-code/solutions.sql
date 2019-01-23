#challenge 1

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.title AS TITLE, publishers.pub_name AS PUBLISHER
FROM authors, titles, publishers
WHERE title_id = title_id



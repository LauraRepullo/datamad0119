#challenge 1

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.title AS TITLE, publishers.pub_name AS PUBLISHER
FROM authors, titles, publishers
WHERE title_id = title_id

#challenge 2

SELECT 	authors.au_id AS 'AUTHOR ID', 
		authors.au_lname AS 'LAST NAME', 
        authors.au_fname AS 'FIRST NAME', 
        publishers.pub_name AS 'PUBLISHER',
        COUNT(titles.title_id) AS 'TITLE COUNT'
FROM authors
LEFT JOIN titleauthor
ON titleauthor.au_id=authors.au_id
LEFT JOIN titles
ON titles.title_id=titleauthor.title_id 
LEFT JOIN publishers
ON titles.pub_id=publishers.pub_id
GROUP BY authors.au_id, publishers.pub_name;

#challenge 3

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', SUM(sales.qty) AS 'TOTAL'
FROM authors
INNER JOIN titleauthor
ON titleauthor.au_id=authors.au_id
INNER JOIN sales
ON titleauthor.title_id=sales.title_id
GROUP BY authors.au_id
ORDER BY SUM(sales.qty) DESC
LIMIT 3 ;

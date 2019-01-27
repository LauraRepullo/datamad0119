#CHALLENGE1
#STEP1
SELECT titles.title_id AS 'TITLE ID',
authors.au_id AS 'ID AUTHOR', 
titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 AS 'SALES_ROYALTY' 
FROM titles
LEFT JOIN sales
ON sales.title_id = titles.title_id
LEFT JOIN titleauthor
ON titleauthor.title_id = titles.title_id
LEFT JOIN authors
ON authors.au_id=titleauthor.au_id

#STEP2

SELECT title_id as 'TITLE ID',
au_id AS 'AUTHOR ID',
SUM(SALES_ROYALTY) AS 'AGGREGATED_ROYALTY'
FROM (SELECT titles.title_id,
authors.au_id, 
titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 AS 'SALES_ROYALTY' 
FROM titles
LEFT JOIN sales
ON sales.title_id = titles.title_id
LEFT JOIN titleauthor
ON titleauthor.title_id = titles.title_id
LEFT JOIN authors
ON authors.au_id=titleauthor.au_id) summary
group by title_id, au_id

#STEP3_ no encuentro el fallo:

SELECT summary.au_id, (SUM(SALES_ROYALTY) + titles.advance) AS profit
FROM (SELECT titles.title_id,
authors.au_id, 
titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 AS 'SALES_ROYALTY' 
FROM titles
LEFT JOIN titleauthor ON titleauthor.title_id = titles.title_id
LEFT JOIN sales ON sales.title_id = titles.title_id
LEFT JOIN authors ON authors.au_id=titleauthor.au_id) summary
LEFT JOIN titles on titles.title_id=summary.title_id
GROUP BY au_id
ORDER by profit DESC
LIMIT 3



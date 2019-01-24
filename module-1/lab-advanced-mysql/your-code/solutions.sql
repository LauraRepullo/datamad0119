#STEP1:
#SELECT sales.title_id AS 'TITLE ID',
 authors.au_id AS 'AUTHOR ID', 
 titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 AS 'SALES ROYALTY'
#FROM sales
#LEFT JOIN titleauthor
#ON titleauthor.title_id=sales.title_id
#LEFT JOIN authors
#ON titleauthor.au_id=authors.au_id
#LEFT JOIN titles
#ON 	titleauthor.title_id=titles.title_id



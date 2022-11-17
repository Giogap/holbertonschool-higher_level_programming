-- script displays the number of shows linked to each.
SELECT B.name AS genre, COUNT(A.show_id) AS number_of_shows
FROM tv_show_genres A
INNER JOIN tv_genres B
ON A.genre_id = B.id
GROUP BY A.genre_id
ORDER BY number_of_shows DESC;
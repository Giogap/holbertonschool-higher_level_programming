-- Write a script that lists all shows contained
SELECT B.title, A.genre_id
FROM tv_show_genres A
RIGHT JOIN tv_shows B
ON B.id = A.show_id
ORDER BY B.title, A.genre_id ASC;
-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT B.title, A.genre_id
FROM tv_show_genres A
RIGHT JOIN tv_shows B
ON B.id = A.show_id
WHERE B.id IS NULL
OR A.show_id IS NULL
ORDER BY B.title, A.genre_id ASC;
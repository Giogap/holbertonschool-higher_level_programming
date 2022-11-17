--  script to lists all genres of the show Dexter.
SELECT A.name
FROM tv_genres A
LEFT JOIN tv_show_genres B
ON A.id = B.genre_id
LEFT JOIN tv_shows C
ON B.show_id = C.id
WHERE title='Dexter'
ORDER BY A.name ASC;
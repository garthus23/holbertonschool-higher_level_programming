-- Join Database and print selected Columns
-- Join Database and print selected Columns
SELECT tv_genres.name AS genre, count(tv_genres.id) AS number_of_shows FROM tv_genres RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;

-- A script
-- that lists linked tables
USE download;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_shows ON tv_show_id = tv_shows.id
JOIN tv_show_genres ON tv_show_genre_id = tv_show_genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

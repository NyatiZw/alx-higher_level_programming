-- A script
-- that lists linked tables

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_shows ON hbtn_0d_tvshows.tv_show_id = tv_shows.id
JOIN tv_show_genres ON hbtn_0d_tvshows.tv_show_genre_id = tv_show_genres.id
WHERE ty_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

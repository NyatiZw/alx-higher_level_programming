-- A script
-- that lists linked tables

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
JOIN tv_shows ON hbtn_0d_tvshows_id = tv_shows.id
JOIN tv_shows_genres ON hbtn_0d_tv_show_genre_id = tv_show_genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

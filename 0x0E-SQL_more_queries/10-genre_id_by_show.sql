-- A script
-- that lists linked tables
SELECT tv_shows.title, tv_show_genre_id
FROM download.hbtn_0d_tvshows
JOIN tv_shows.title AND tv_show_genres
ORDER BY tv_shows.title AND tv_genres.genre_id ASC;

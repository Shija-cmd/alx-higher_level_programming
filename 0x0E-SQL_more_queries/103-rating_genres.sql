-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS x
       INNER JOIN `tv_show_genres` AS y
       ON y.`genre_id` = x.`id`

       INNER JOIN `tv_show_ratings` AS z
       ON z.`show_id` = y.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;

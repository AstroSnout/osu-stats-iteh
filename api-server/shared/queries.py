from sqlalchemy.sql import text


class PremadeQueries:
    @staticmethod
    def top_plays(user_rank, user_range, mods, strict):
        top = user_rank + user_range if user_rank + user_range <= 10000 else 10000
        bot = user_rank - user_range if user_rank - user_range >= 1 else 1
        top = user_range if top < user_range else top
        bot = 10000 - user_range if bot > 10000 - user_range else bot
        if strict:
            mods = f" AND my_scores.enabled_mods = '{mods}'" if mods else " AND my_scores.enabled_mods = \"\""
        else:
            mods = f" AND my_scores.enabled_mods LIKE '%{mods}%'" if mods else ""

        return text(f'''
            SELECT
                my_beatmaps.beatmap_id,
                my_beatmaps.beatmapset_id,
                CONCAT(my_beatmaps.artist, " - ", my_beatmaps.title, " [", my_beatmaps.version, "]") AS beatmap_name,
                TIME_FORMAT(SEC_TO_TIME(CAST(my_beatmaps.hit_length AS UNSIGNED)), "%i:%s") AS play_time,
                TIME_FORMAT(SEC_TO_TIME(CAST(my_beatmaps.total_length AS UNSIGNED)), "%i:%s") AS total_time,
                ROUND(AVG(my_scores.pp), 2) AS pp_avg,
                ROUND(AVG(my_scores.accuracy), 2) AS acc_avg,
                my_scores.enabled_mods,
                (CONCAT("https://assets.ppy.sh/beatmaps/", my_beatmaps.beatmapset_id,"/covers/cover.jpg")) thumb_url,
                (CONCAT("https://osu.ppy.sh/beatmapsets/", my_beatmaps.beatmapset_id,"/download")) dl_link,
                COUNT(DISTINCT(my_users.user_id)) count,
                ROUND(CAST(((COUNT(DISTINCT(my_users.user_id)) / ({top}-{bot}) ) * 100) as FLOAT),2) occurrence
            FROM
                my_scores
            JOIN my_users ON my_scores.user_id = my_users.user_id
            JOIN my_beatmaps ON my_scores.beatmap_id = my_beatmaps.beatmap_id
            WHERE
                my_users.rank >= {bot} AND my_users.rank <= {top}{mods}
            GROUP BY
                my_beatmaps.beatmap_id
            ORDER BY
                `count`
            DESC
        ''')


# There's a nicer way of doing all of this
# But SQL querries were explicitly asked for

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time
from shared import calculator


db = SQLAlchemy()


def init_my_users():
    db.engine.execute(
        f'''
            CREATE TABLE IF NOT EXISTS my_users (
                user_id int unsigned primary key,
                accuracy float unsigned,            # accuracy_new
                playcount mediumint(11) unsigned,
                rank int(10) unsigned,              # rank_score_index
                pp float unsigned,                  # rank_score
                country char(2)                     # country_acronym
            );
            '''
    )


def init_my_beatmaps():
    db.engine.execute(
        f'''
            CREATE TABLE IF NOT EXISTS my_beatmaps (
                beatmap_id int unsigned primary key,  # beatmaps
                beatmapset_id int unsigned,           # beatmaps
                artist varchar(80),                   # beatmapsets
                title varchar(80),                    # beatmapsets
                version varchar(80),                  # beatmaps
                bpm float unsigned,                   # beatmaps
                total_length mediumint(11) unsigned,  # beatmaps
                hit_length mediumint(11) unsigned,    # beatmaps
                difficulty_rating float unsigned      # beatmaps                
            );
            '''
    )


def init_my_scores():
    db.engine.execute(
        f'''
        CREATE TABLE IF NOT EXISTS my_scores (
            score_id int unsigned primary key,
            beatmap_id int unsigned,
            user_id int unsigned,
            accuracy float unsigned,  # countXXX calculation - scores
            pp float unsigned,
            enabled_mods varchar(20)
        );
        '''
    )


def fill_my_users():
    # Just copies all of the users to my table
    # The official database should have the top 10000 ranked users, no more
    db.engine.execute(
        '''
        INSERT IGNORE INTO osu_simplified.my_users
        SELECT
            ous.user_id,
            ous.accuracy_new as accuracy,
            ous.playcount,
            ous.rank_score_index as 'rank',
            ous.rank_score as pp,
            ous.country_acronym as country
        FROM osu_official.osu_user_stats as ous
        '''
    )


def fill_my_scores():
    # Tracking execution time since this tends to take a lot of time and I'm a curious person
    print(f"[{datetime.now()}] Filling out 'my_scores' table")
    start = time.time()
    for i in range(10000):
        db.engine.execute(
            f'''
            INSERT IGNORE INTO
                osu_simplified.my_scores
            SELECT
                osh.score_id,
                osh.beatmap_id,
                osh.user_id,
                (
                (osh.count50*50 + (osh.countkatu+osh.count100)*100 + (osh.count300+osh.countgeki)*300)
                /
                ((osh.countmiss+osh.count50+osh.countkatu+osh.count100+osh.count300+osh.countgeki)*300)
                ) * 100 as accuracy,
                osh.pp,
                osh.enabled_mods
            FROM
                osu_official.osu_scores_high osh
            JOIN
                osu_official.osu_user_stats ous ON osh.user_id = ous.user_id
            WHERE
                ous.rank_score_index = {i}
            GROUP BY
                osh.beatmap_id
            ORDER BY
                osh.pp
            DESC
            LIMIT 10
            '''
        )
        end = time.time()
        print(f'[{datetime.today().strftime("%H:%M:%S")}] Queried rank #{i} (Run time {round(end - start, 2)}s)')
    print("Script execution time:", round(end - start, 2))


def fill_my_scores_alt():
    print(f"[{datetime.now()}] Filling out 'my_scores' table")
    start = time.time()
    db.engine.execute(
        f'''
            LOCK TABLES my_scores WRITE, osu_scores_high READ, my_users READ
            INSERT INTO my_scores
            SELECT * FROM
                (
                SELECT
                    osh.score_id,
                    osh.beatmap_id,
                    osh.user_id,
                    ROW_NUMBER() OVER (PARTITION BY osh.user_id ORDER BY osh.pp DESC) as rank_play,
                    (
                    (osh.count50*50 + (osh.countkatu+osh.count100)*100 + (osh.count300+osh.countgeki)*300)
                    /
                    ((osh.countmiss+osh.count50+osh.countkatu+osh.count100+osh.count300+osh.countgeki)*300)
                    ) * 100 as accuracy,
                    osh.pp,
                    osh.enabled_mods
                FROM
                    osu_scores_high osh
                WHERE
                    osh.user_id IN (SELECT user_id FROM my_users)
                ) kk
            WHERE kk.rank_play < 11;
            UNLOCK TABLES;
            '''
    )
    end = time.time()
    print("Script execution time:", round(end - start, 2))


def fill_my_beatmaps():
    print("Getting beatmaps from my_scores")
    # All beatmap IDs from my_scores
    bmaps = db.engine.execute(
        f'''
        SELECT beatmap_id
        FROM osu_simplified.my_scores
        '''
    ).fetchall()
    # Removes duplicate beatmap IDs
    unique_bmaps = list(set([x[0] for x in bmaps]))
    # Fetches relevant info on beatmaps from the official osu! database
    for bid in unique_bmaps:
        db.engine.execute(
            f'''
            INSERT IGNORE INTO 
                osu_simplified.my_beatmaps
            SELECT
                obmap.beatmap_id,
                obmap.beatmapset_id,
                obmapset.artist,
                obmapset.title,
                obmap.version,
                obmap.bpm,
                obmap.total_length,
                obmap.hit_length,
                obmap.difficultyrating
            FROM 
                osu_official.osu_beatmaps obmap
            JOIN 
                osu_official.osu_beatmapsets obmapset ON obmap.beatmapset_id = obmapset.beatmapset_id
            WHERE
                obmap.beatmap_id = {bid}
                '''
        )
    return


def enabled_mods_num_to_mod ():
    scoresdb = db.engine.execute(
        f'''
        SELECT * FROM my_scores
        '''
    ).fetchall()
    for x in scoresdb:
        scoreid = x[0]
        mod = ''.join(calculator.num_to_mod(x[5]))
        db.engine.execute(
            f'''
                UPDATE my_scores
                SET my_scores.enabled_mods = '{mod}'
                WHERE score_id = {scoreid}
            '''
        )
    return


def init_all_tables():
    # Creates tables
    print("Creating tables...")
    init_my_users()
    init_my_scores()
    init_my_beatmaps()
    # Populates the tables from official osu! database
    print("Populating tables...")
    fill_my_users()
    fill_my_scores()
    fill_my_beatmaps()
    # Converts bitwise numeric representations of mods to string (readability)
    print("Converting mods...")
    enabled_mods_num_to_mod()

















































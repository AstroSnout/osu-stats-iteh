# osu!stats
A website showing some stats from a rhythm game "osu!".
  
The website grabs the data of top 10000 players on the leaderboards (updated monthly), looks at their top 10 plays and then aggregates the data based on beatmap frequency within a range of ranks that the user inputs on the website. The idea is to help players playing the game see what the "easy" maps are, as they are much more likely to appear within top 10 plays of a lot players.
  
API server is based on Python's Flask.  
Front-end is based on Vue.js (along with the complimentary HTML stack).   
MySQL database was used for the project.  
  
Initially, most of my data was grabbed using a python scraper (to scrape relevant IDs from the leaderboards on the website) and then received data was used to ping the available API about 10000 times (highly unoptimal). Thankfuly, I've managed to grab a hold of the official (although limited) production database backups. However, with the database being ~4GB, my querry times were abyssmal and the database had a lot of info irrelevant to the project, so I managed to simplify the database to ~5MB.  
  
If you, for whatever reason, require the production backups of the database, I suggest you contact peppy at contact@ppy.sh.  
If you need my simplified backup, feel free to reach out at tasin.filip@gmail.com or via discord Trishma#0702.  

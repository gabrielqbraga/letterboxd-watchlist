# letterboxd-watchlist
This repository checks where you can watch movies from your letterboxd watchlist.

It utilizes The Movie Database API(https://developers.themoviedb.org/3/getting-started/introduction) to check in which streaming service you can watch each movie from your Letterboxd Watchlist.

# How to Use
You will need to obtain an API_key from tmdb(https://www.themoviedb.org/settings/api). After this, paste your key in the indicated variable on index.py.
Then, you will need to import the csv file of your watchlist. You will enter https://letterboxd.com/YOUR_USERNAME/watchlist/ and 'Export Watchlist'. Now replace for the file in the root.
Run index.py. The results will appear in results.txt.

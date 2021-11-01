# Reddit Movies

Find and index full movies from selected subs

## Install

```bash
pip install reddit_movies
```

## Usage

```python
from reddit_movies import *

r = RedditInternetArchiveMovies()
for movie in r.scrap():
    print(movie)

r = RedditExploitationMovies()
for movie in r.scrap():
    print(movie)

r = RedditSciFiMovies()
for movie in r.scrap():
    print(movie)

r = RedditYoutubeMovies()
for movie in r.scrap():
    print(movie)

r = RedditCartoons()
for movie in r.scrap():
    print(movie)

r = RedditDocumentaries()
for movie in r.scrap():
    print(movie)

r = RedditTVShows()
for movie in r.scrap():
    print(movie)
```

## Credentials

This package will parse the rss feed for each sub, the official reddit api is also supported if you provide authentication

If you want to use praw then you need to set your credentials, either pass them in the constructor or create `~/.config/reddit_movies/praw.json`
```json
{
  "client": "Cijxxm8Dg6dxxx",
  "secret": "7HixxxujbWsrmzvgw9xxxxx"
}
```

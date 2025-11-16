class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(artist)
        Song.genres.append(genre)
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
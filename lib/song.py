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

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Midnight Train", "Sauti Sol", "Pop")
song3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
song4 = Song("Ouglegba", "Wizkid", "Afrobeats")

print(Song.count)
print(Song.artists)  
print(Song.genres)  
print(Song.genre_count)
print(Song.artist_count)  

Song.add_to_artists(song4.artist)
Song.add_to_artists(song2.artist)
Song.add_to_artists(song3.artist)

Song.add_to_genres(song4.genre)
Song.add_to_genres(song2.genre)
Song.add_to_genres(song3.genre)

 
# 1. Query all of the entries in the Genre table
# Answer: SELECT * from Genre

# 2. Using the INSERT statement, add one of your favorite artists to the Artist table.
# Answer: INSERT into Artist
#         values (null, "Muse", 1994)#

# 3. Using the INSERT statement, add one, or more, albums by your artist to the Album table.
# Answer: INSERT into Album
#         select null, "Absolution", "09/07/1999", 5000, "East/West Taste", Artist.ArtistId, Genre.GenreId
#         FROM Artist, Genre
#         WHERE Artist.ArtistName = "Muse"
#         AND Genre.Label = "Rock"

# 4. Using the INSERT statement, add some songs that are on that album to the Song table.
# Answer: INSERT into Song
#         values (null, "Stockholm Syndrome", 500, "07/14/2003", 2, 28, 23)
#         INSERT into Song
#         values (null, "New Born", 700, "06/04/2001", 2, 28, 23)

# 5. Write a SELECT query that provides the song titles, album title, and artist name for all of the data you just entered in. Use the LEFT JOIN keyword sequence to connect the tables, and the WHERE keyword to filter the results to the album and artist you added. Reminder: Direction of join matters. Try the following statements and see the difference in results.
  # SELECT a.Title, s.Title FROM Album a LEFT JOIN Song s ON s.AlbumId = a.AlbumId;
  # SELECT a.Title, s.Title FROM Song s LEFT JOIN Album a ON s.AlbumId = a.AlbumId;

# Answer (no NULL values returned):
#         SELECT Song.Title as 'Song Title', Album.Title as 'Album Title', Ar       tist.ArtistName as 'Artist Name'
#         FROM Song
#         LEFT JOIN Album ON Album.AlbumId = Song.AlbumId
#         LEFT JOIN Artist ON Album.artistID = Artist.artistID
#         WHERE Album.Title = "Absolution" and Artist.ArtistName = "Muse"
#
# Answer 2 (can return NULL values)
# SELECT a.Title as 'Album Title', s.Title as 'Song Title', art.ArtistName as 'Artist Name'
#         FROM Album a
#         LEFT JOIN Artist art ON a.artistID = art.artistID
#         LEFT JOIN Song s ON s.AlbumId = a.AlbumId
#         WHERE a.Title = "Absolution" and art.ArtistName = "Muse"

# 6. Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
# Answer: SELECT Album.Title, count() as "Total Songs"
#         FROM Album
#         JOIN Song on Song.AlbumId = Album.AlbumId
#         GROUP BY Song.AlbumId

# 7. Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
# Answer: SELECT Artist.ArtistName as "Artist", count(*) as "Number of Songs"
#         From Song
#         LEFT JOIN Artist ON Song.ArtistId = Artist.ArtistId
#         GROUP BY Song.ArtistId

# Answer 2: SELECT Artist.ArtistName as "Artist", count(*) as "Number of Songs"
#           From Artist
#           JOIN Song ON Song.ArtistId = Artist.ArtistId
#           GROUP BY Song.ArtistId

# Answer 3 (shows all artists, even artists with 0 songs):
#           SELECT Artist.ArtistName as "Artist", count(Song.ArtistId) as "Number of Songs"
#           From Artist
#           LEFT JOIN Song ON Song.ArtistId = Artist.ArtistId
#           GROUP BY Artist.ArtistId

# 8. Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
# Answer: SELECT Genre.Label as "Genre", count(Song.GenreId)
#         FROM Song
#         LEFT JOIN Genre ON Song.GenreId = Genre.GenreId
#         GROUP BY Song.GenreId

# 9. Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.
# Answer: SELECT Album.Title, MAX(Album.AlbumLength) as "Album Duration"
#         FROM Album

# 10. Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.
# Answer: SELECT Song.Title, MAX(Song.SongLength) as "Song Duration"
#         FROM Song

# 11. Modify the previous query to also display the title of the album.
# Answer: SELECT Song.Title, MAX(Song.SongLength) as "Song Duration", Album.Title as "Album Title"
#         FROM Song
#         LEFT JOIN Album

# EXTRA PRACTICE --------------------------------------------------------

# Get Number of albums by each artist
# Answer: SELECT Artist.ArtistName, count() as "Number of Albums"
#         FROM Album
#         LEFT JOIN Artist ON Artist.ArtistId = Album.ArtistId
#         GROUP BY Album.ArtistId

# Get songs that are classified as rock, pop, or punk
# Note: genreId is not mandatory (may be null) on song
# Answer: SELECT Song.Title as "Song Name", Genre.Label as "Genre"
#         FROM Song
#         JOIN Genre ON Genre.GenreId = Song.GenreId
#         WHERE Genre.GenreId = 2 OR Genre.GenreId = 7 OR Genre.GenreId = 9

# Get the TOTAL NUMBER songs that are classified as rock, pop, or punk
# Group by Genre
# Answer: SELECT Genre.Label as "Genre", count(*) as "Total Songs"
#         FROM Genre
#         JOIN Song ON Song.GenreId = Genre.GenreId
#         WHERE Song.GenreId = 2 OR Song.GenreId = 7 OR Song.GenreId = 9
#         GROUP BY Song.GenreId
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

# Answer: SELECT a.Title as 'Album Title', s.Title as 'Song Title', art.ArtistName as 'Artist Name'
#         FROM Album a
#         LEFT JOIN Artist art ON a.artistID = art.artistID
#         LEFT JOIN Song s ON s.AlbumId = a.AlbumId
#         WHERE a.Title = "Absolution" and art.ArtistName = "Muse"
# Note: a regular join works here, too

# 6. Write a SELECT statement to display how many songs exist for each album. You'll need to use the COUNT() function and the GROUP BY keyword sequence.
# Answer: SELECT a.Title as 'Album title', count() as 'Total Songs'
#         FROM Song s, Album a
#         WHERE s.albumID = a.albumID
#         GROUP BY a.Title

# 7. Write a SELECT statement to display how many songs exist for each artist. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

# 8. Write a SELECT statement to display how many songs exist for each genre. You'll need to use the COUNT() function and the GROUP BY keyword sequence.

# 9. Using MAX() function, write a select statement to find the album with the longest duration. The result should display the album title and the duration.

# 10. Using MAX() function, write a select statement to find the song with the longest duration. The result should display the song title and the duration.

# 11. Modify the previous query to also display the title of the album.
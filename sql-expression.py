from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instuctions from out localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create varibles for the "artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create varibles for the "album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistID"))
)

# create varibles for the "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumID")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # query 1 - select all records from the "artist" table
    #select_query = artist_table.select()

    # query 2 - select only name column from the "artist" table
    #select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query 3 - select only queen from the Artist table
    #select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - select only by 'artistId' #51 from the "Artist" table
    #select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 4 - select only the albums with 'artistId' #51 from the "Album" table
    #select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 5 - select the tracks froms the composer "Queen"
    select_query = track_table.select().where(track_table.c.Composer == "Queen")



    results = connection.execute(select_query)
    for result in results:
        print(result)

    

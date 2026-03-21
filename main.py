"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist

if __name__ == "__main__":
    # make the songs first
    artist1 = Artist("Kendrick Lamar", "Hip-Hop")
    album1 = Album("DAMN.", True, [2017, 2018])
    song1 = Song(artist1, album1, 220)

    artist2 = Artist("Alanis Morissette", "Alternative")
    album2 = Album("Jagged Little Pill", False, [1995, 1996])
    song2 = Song(artist2, album2, 245)

    # make the podcasts
    artist3 = Artist("Joe Rogan", "Comedy")
    album3 = Album("The Joe Rogan Experience", True, [2009, 2010])
    poadcast1 = Podcast(artist3, album3, 9000, True)

    artist4 = Artist("Sarah Koenig", "Journalism")
    album4 = Album("Serial", False, [2014, 2015])
    poadcast2 = Podcast(artist4, album4, 5400)
import fresh_tomatoes
import media

interstellar = media.Movie("Interstellar",
						2,
						"From director Christopher Nolan (Inception, The Dark Knight trilogy) comes the story of a team of pioneers undertaking the most important mission in human history.",
						"https://i.ytimg.com/vi_webp/Df7IEKqimOY/movieposter.webp",
						"https://www.youtube.com/watch?v=0vxOhd4qlnA",
						165);

moulin_rouge = media.Movie("Moulin Rouge",
						2,
						"A poet falls for a beautiful courtesan whom a jealous duke covets.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BODg5MTk2YmYtMzQyOC00OGUzLWFlZDYtMjBkNTk3MTA3ZjU0XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=dMSvKpVwavk",
						127)

dark_knight_rises = media.Movie("The Dark Knight Rises",
						2,
						"Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=g8evyE9TuYk",
						164)

man_of_steel = media.Movie("Man of Steel",
						2,
						"Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5ODk1NDkxMF5BMl5BanBnXkFtZTcwNTA5OTY0OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=T6DJcgm3wNY",
						143)

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
						2,
						"A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5OTk4MTM3M15BMl5BanBnXkFtZTgwODcxNjg3MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=vw61gCe2oqI",
						113)

wedding_crashers = media.Movie("Wedding Crashers",
						3,
						"John Beckwith and Jeremy Grey, a pair of committed womanizers who sneak into weddings to take advantage of the romantic tinge in the air, find themselves at odds with one another when John meets and falls for Claire Cleary.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BZmJkNzViYjYtZWZlNy00OGE4LWI2MzUtYTcwNjY3Y2MyODIwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=ZeUSo8voIXM",
						119)

zoolander = media.Movie("Zoolander",
						2,
						"At the end of his career, a clueless fashion model is brainwashed to kill the Prime Minister of Malaysia.",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEwOTMxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
						"https://www.youtube.com/watch?v=MaEeSJZYkpY",
						90)

movies = [dark_knight_rises,
          edge_of_tomorrow,
          interstellar,
          man_of_steel,
          moulin_rouge,
          wedding_crashers,
          zoolander]

fresh_tomatoes.open_movies_page(movies)                     

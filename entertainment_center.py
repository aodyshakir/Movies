import fresh_tomatoes
import media

toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/oYRpH2GaLdM")
print(toy_story.storyline)

Scorpion_King = media.Movie("The Scorpion King 2",
                            "the story centers on Wreck-It Ralph's adventures in the Internet data",
                            "https://upload.wikimedia.org/wikipedia/en/7/72/Scorpion_King_2_DVD_Cover.jpg",
                            "https://youtu.be/VSB4wGIdDwo")
# print(seven_lucky_kids.storyline)

matrix = media.Movie("Matrix",
                     "A movie about the reality of life itself.",
                     "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

footloose = media.Movie("Footloose",
                        "A story of an upbeat Chicago teen who moves to a small town.",
                        "http://upload.wikimedia.org/wikipedia/en/e/e4/FootloosePoster.jpg",
                        "https://www.youtube.com/watch?v=xxOuSqokKok")
# print(black_panther.storyline)

# black_panther.show_trailer()

movies = [toy_story, Scorpion_King, matrix, footloose]
fresh_tomatoes.open_movies_page(movies)

class Movie:
    name = "Cricket"
    genre = "Biography"
    year = 2018
    def movieDetail(self):
        print(f"{self.name} is a {self.genre} movie which was released in {self.year}")

movie1 = Movie()
movie2 = Movie()

movie1.movieDetail()

movie2.name = "Red Alert"
movie2.genre = "Action"
movie2.year = 2022

movie2.movieDetail()
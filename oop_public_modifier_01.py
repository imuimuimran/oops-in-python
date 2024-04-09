# Public Modifier
class movie_information:
    def __init__(self, movie_name, relese_date, budget):
        self.movie_name = movie_name
        self.relese_date = relese_date
        self.budget = budget
        
    def movie_info(self, movie_name, relese_date, budget):
        self.movie_name = movie_name
        self.relese_date = relese_date
        self.budget = budget

movie1 = movie_information("Titanic", 1998, 200000)
movie2 = movie_information("Avatar", 2007, 500000)

print(movie1.movie_name, movie1.relese_date, movie1.budget)
print(movie2.movie_name, movie2.relese_date, movie2.budget)
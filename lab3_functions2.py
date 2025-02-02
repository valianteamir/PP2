movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def mv(movie):
    return movie["imdb"] > 5.5

def flt(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

def getmov(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def avgof(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies) if movies else 0

def avg_cat(movies, category):
    category_movies = getmov(movies, category)
    return avgof(category_movies)

# Example usage
print(mv(movies[0]))  # True
print(flt(movies))  # List of movies with IMDB > 5.5
print(getmov(movies, "Drama"))  # List of Drama movies
print(avgof(movies))  # Average IMDB of all movies
print(avg_cat(movies, "Drama"))  # Average IMDB of Drama movies

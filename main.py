from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "3 Idiots",
        "director": "Rajkumar Hirani",
        "genre": "Comedy Drama",
        "language": "Hindi",
        "release_year": 2009,
    },
    {
        "id": 2,
        "title": "Baahubali",
        "director": "S S Rajamouli",
        "genre": "Action Drama",
        "language": "Telugu",
        "release_year": 2015,
    },
]


@app.get("/")
def home():
    return {"message": "Movie API is running"}


@app.get("/movies")
def all_movies():
    return movies


@app.get("/movies/{movie_id}")
def get_by_id(movie_id: int):
    for existingMovie in movies:
        if existingMovie["id"] == movie_id:
            return existingMovie
    raise HTTPException(status_code=404, detail="Movie not found !!!")


class MovieUpdate(BaseModel):
    title: str
    director: str
    genre: str
    language: str
    release_year: int


@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, updatedMovie: MovieUpdate):
    for listedMovie in movies:
        if listedMovie["id"] == movie_id:
            listedMovie.update(updatedMovie.model_dump())
            return {"message": "Movie updated Successfully", "movie": listedMovie}
    raise HTTPException(status_code=404, detail="Movie not found")

import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# 1 этап


def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, avg_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# 2 этап


def rating_tier(rating):
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7.0:
        return "хорошо"
    else:
        return "средне" if rating >= 5.0 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# 3 этап

for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

idx = 0
while idx < len(movies):
    if movies[idx]["rating"] > 9.0:
        print(f"Найден шедевр: {movies[idx]['title']}")
        break
    idx += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# 4 этап


def normalize_title(title):
    words = title.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(capitalized_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    year = movie["year"]
    rating = movie["rating"]
    return f'"{title}" ({year}) - {rating}/10, {duration}, жанры: {genres}'


# 5 этап


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]


# 6 этап


def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


avg_rate = average_rating(movies)
high_rated_movies_dict = {
    m["title"]: m["rating"] for m in movies if m["rating"] > avg_rate
}

# 7 этап


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    for movie in movies_a:
        genres_a |= movie["genres"]

    genres_b = set()
    for movie in movies_b:
        genres_b |= movie["genres"]

    return genres_a - genres_b


# 8 этап


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


total_duration_over_7 = sum(m["duration_min"] for m in movies if m["rating"] > 7)

# отчет


def build_report(movies):
    avg_rate = average_rating(movies)
    _, _, avg_age = catalog_age_stats(movies)
    top_3 = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]

    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)
    all_unique_genres = ", ".join(sorted(all_genres(movies)))

    print("\n --- Отчет по каталогу ---\n")
    print(f"Средний рейтинг: {avg_rate}")
    if avg_age == 1:
        print(f"Средний возраст фильмов: {avg_age} год\n")
    elif avg_age in (2, 3, 4):
        print(f"Средний возраст фильмов: {avg_age} года\n")
    else:
        print(f"Средний возраст фильмов: {avg_age} лет\n")

    print("Топ 3 фильма:")
    for movie in top_3:
        print(f"  {format_report_line(movie)}")

    print("\nКоличество фильмов по жанрам:")
    for genre, count in sorted_genres:
        print(f"  {genre} - {count}")

    print("\nФильмы с рейтингом выше 8.0:")
    for movie in iter_high_rated(movies):
        print(f"  {format_report_line(movie)}")

    print(f"\nВсе жанры каталога: {all_unique_genres}")


if __name__ == "__main__":
    build_report(movies)

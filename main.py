from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError

client = MongoClient(
    "mongodb+srv://dasha_nikulina_db_user:i1NiqhBGVComXERd@cluster0.yt6ola5.mongodb.net/",
    server_api=ServerApi("1"),
)

db = client.cats_db

# CREATE

data = db.cats.insert_many(
    [
        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"],
        },
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)


def exceptions(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PyMongoError as e:
            print(f"Database error: {e}")

    return handler


# READ
@exceptions
def read_cats():
    all_cats = db.cats.find({})
    for cat in all_cats:
        print(cat)


@exceptions
def read_one_cat(name):
    one_cat = db.cats.find_one({"name": name})
    print(one_cat)


# UPDATE
@exceptions
def update_age(name, age):
    db.cats.update_one({"name": name}, {"$set": {"age": age}})
    updated_cat = db.cats.find_one({"name": name})
    print(updated_cat)


@exceptions
def update_features(name, *args):
    db.cats.update_one({"name": name}, {"$push": {"features": {"$each": list(args)}}})


# DELETE
@exceptions
def delete_one_cat(name):
    db.cats.delete_one({"name": name})
    print(f"{name} was deleted")


@exceptions
def delete_all():
    db.cats.delete_many({})
    print("All cats were deleted")

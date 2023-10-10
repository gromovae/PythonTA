from setup_database import engine, Film
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update


Session = sessionmaker(bind=engine)
session = Session()
film_1 = Film(id=0, title="Atonement_error", director="Joe Wright", release_year=2007)
film_2 = Film(id=1, title="Star Wars: Episode IV – A New Hope", director="George Lucas", release_year=1977)
film_3 = Film(id=2, title="Macbeth", director="Justin Kurzel", release_year=2015)

session.add(film_1)
session.add(film_2)
session.add(film_3)

session.commit()
session.close()

session = Session()
films = session.query(Film).all()
for film in films:
    print(film.id, film.title, film.director, film.release_year)

session.query(Film).delete()
session.commit()
session.close()

from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class based model for the "programer" table
class Programer(base):
    __tablename__ = "Programer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new incidence of sessionmaker, then point to out engine (the db)
Session = sessionmaker(db)
# opens and actual session by calling the session() subclass defined above
session = Session()

# creating the database by using the declarative_base subclass
base.metadata.create_all(db)

# creating records on our programer table
ada_lovelace = Programer(
    first_name= "Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programer"
)

alan_turing = Programer(
    first_name= "Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programer(
    first_name= "Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programer(
    first_name= "Margaret",
    last_name="Hamilton",
    gender="f",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programer(
    first_name= "Bill",
    last_name="Gates",
    gender="M",
    nationality="British",
    famous_for="Microsoft"
)

tim_berners_lee = Programer(
    first_name= "Tim",
    last_name="Berners-lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

james_bagge = Programer(
    first_name= "James",
    last_name="Bagge",
    gender="M",
    nationality="Irish",
    famous_for="Coding"
)

# add each instance of out programers to out session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(james_bagge)

# # commit our session to the database
# session.commit()

# update single record
# programer = session.query(Programer).filter_by(id=7).first()
# programer.famous_for = "World President"
# session.commit()

# update multiply records
# people = session.query(Programer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# delete single record
# fname = input("Enter first name:")
# lname = input("Enter last name:")
# programer = session.query(Programer).filter_by(
#     first_name=fname, last_name=lname).first()
# # defensive programing
# if programer is not None:
#     print("Programer Found: ", programer.first_name + " " + programer.last_name)
#     confirmation = input("are you sure you want to delete this (Y/N): ")
#     if confirmation.lower() == "y":
#         session.delete(programer)
#         session.commit()
#         print("Programer has been delete")
#     else:
#         print("Programer not deleted")
# else:
#     print("no record found")

# for deleting all records one by one only use if sure and use defensive programing
# programers = session.query(Programer)
# for programers in programers:
#     confirmation = input("are you sure you want to delete this (Y/N): ")
#     if confirmation.lower() == "y":
#         session.delete(programer)
#         session.commit()
#         print("Programers has been delete")
#     else:
#         print("Programer not deleted")

# query the database to find all Programers
programers = session.query(Programer)
for programer in programers:
    print(
        programer.id,
        programer.first_name + " " + programer.last_name,
        programer.gender,
        programer.nationality,
        programer.famous_for,
        sep=" | "
        )
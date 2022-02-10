from app import db, Players, Teams 

db.drop_all()
db.create_all()

SG = Players(first_name='Stevie',surname="G",club='Pool',age=41)
db.session.add(SG)
db.session.commit()




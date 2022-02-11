from app import db, Players, Teams 

db.drop_all()
db.create_all()

# SG = Players(first_name='Stevie', surname='G', club='Pool', age=42)
# WR = Players(first_name='Wazza', surname='Roo', club='Toffees', age=41)

# Pool = Teams(name='Pool', founded=1892)
# Toffees = Teams(name='Toffees', founded=1878)

# SG = Players(first_name='Stevie',surname="G",club='Pool',age=41)
# db.session.add(SG)
# db.session.commit()

# from app import db, Countries, Cities

# #Creates all tables classes defined
# db.create_all()

# # Adds example to table Countries
# uk = Countries(name = 'United Kingdom')
# db.session.add(uk)
# db.session.commit() 

# ldn = Cities(name='London', country = uk)
# mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

# db.session.add(ldn)
# db.session.commit()
# db.session.add(mcr)
# db.session.commit()

# print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
# print(f"London's country is: {ldn.country.name}")
# print(f"Manchester's country is: {mcr.country.name}")


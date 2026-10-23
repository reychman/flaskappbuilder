from app import app, db
from app.models import Categoria, Ingrediente

with app.app_context():
    metadata = Categoria.metadata

    print("Se crearon las tablas...")

    for table in metadata.sorted_tables:
        print(f"Creando tabla {table.name}...")

    metadata.create_all(bind=db.engine)
    db.create_all()
    print("Se crearon las tablas correctamente.")

#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow

from api.db.db_extensions import db_obj


class Personne(db_obj.Model):
    id_personne = db_obj.Column(db_obj.Integer, primary_key=True)
    nom = db_obj.Column(db_obj.String(128))
    ville = db_obj.Column(db_obj.String(128))

    def __init__(self, nom, ville) -> None:
        super().__init__()
        self.nom = nom
        self.ville = ville

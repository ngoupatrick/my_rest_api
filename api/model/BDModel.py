#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow

from api.db.db_extensions import db_obj

FOR_NEW = "N"
FOR_UPDATE = "U"


class Personne(db_obj.Model):
    id_personne = db_obj.Column(db_obj.Integer, primary_key=True)
    nom = db_obj.Column(db_obj.String(128))
    ville = db_obj.Column(db_obj.String(128))

    def __init__(self, nom, ville) -> None:
        super().__init__()
        self.nom = nom
        self.ville = ville

    def personne(self, options=FOR_NEW):
        if self.nom.strip() == '' or self.ville.strip():
            return 1
        if options == FOR_NEW:
            db_obj.session.add(self)
        if options == FOR_UPDATE:
            if self.id_personne == 0:
                return 1
        db_obj.session.commit()
        return 0


class User(db_obj.Model):
    id_user = db_obj.Column(db_obj.Integer, primary_key=True)
    id_personne = db_obj.Column(db_obj.Integer)
    login = db_obj.Column(db_obj.String(60))
    pass_hash = db_obj.Column(db_obj.String(128))

    def __init__(self, id_personne, login, pass_hash) -> None:
        super().__init__()
        self.id_personne = id_personne
        self.login = login
        self.pass_hash = pass_hash

    def user(self, options=FOR_NEW):
        if self.login.strip() == '' or self.pass_hash.strip() == '' or self.id_personne == 0:
            return 1
        if options == FOR_NEW:
            db_obj.session.add(self)
        if options == FOR_UPDATE:
            if self.id_user == 0:
                return 1
        db_obj.session.commit()
        return 0

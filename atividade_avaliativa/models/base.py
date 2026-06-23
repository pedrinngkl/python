from . import db

class ModeloBase(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    
    def salvar(self):
        db.session.add(self)
        db.session.commit()
        
    def excluir(self):
        db.session.delete(self)
        db.session.commit()

from app import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    pa_qb = db.Column(db.Float())
    pa_wr = db.Column(db.Float())
    pa_rb = db.Column(db.Float())
    pa_te = db.Column(db.Float())

    def __repr__(self):
        return '<Team {}, pa_qb {}, pa_wr {}, pa_rb {}, pa_te {}>'.format(self.name, self.pa_qb, self.pa_wr, self.pa_rb, self.pa_te)
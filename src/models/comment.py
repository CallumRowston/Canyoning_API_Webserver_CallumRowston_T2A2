from init import db, ma
from marshmallow import fields

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(250))
    date_posted = db.Column(db.Date)

    canyon_id = db.Column(db.Integer, db.ForeignKey('canyons.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    canyon = db.relationship('Canyon', back_populates='comments')
    user = db.relationship('User', back_populates='comments')
    
class CommentSchema(ma.Schema):

    # Validation
    # user = fields.Nested('UserSchema', only=['name', 'email'])
    # canyon = fields.Nested('CanyonSchema')

    class Meta:
        fields = ('id', 'message', 'date', 'card', 'user')
        ordered = True

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define a base model for other database tables to inherit
class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    def __init__(self, *args):
        super().__init__(*args)

#class YourModel(BaseModel):
#"""model for one of your table"""
#    __tablename__ = 'my_table'
#    # define your model

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here


# The User class 
class User(db.Model):    
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String, nullable=False)    
    posts = db.relationship("Posts", cascade = "delete")

    #Returns a dictionary of important attributes 
    def serialize(self):    
        return {        
            "id": self.id,        
            "name": self.name,        
            "posts" : [p.serialize() for p in self.posts]
        }


# The Post class
class Posts(db.Model):    
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)    
    user_id =  db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    weekly_summary_id = db.Column(db.Integer, db.ForeignKey("weekly_summaries.id"), nullable=False) 
    created_at = db.Column(db.String, nullable=False)
    post_text = db.Column(db.String, nullable=False)
    sadness_amount = db.Column(db.Float, nullable = False)
    fear_amount = db.Column(db.Float, nullable = False)
    joy_amount = db.Column(db.Float, nullable = False)
    anger_amount = db.Column(db.Float, nullable = False)
    #Returns a dictionary of important attributes 
    def serialize(self):    
        return {        
            "id": self.id,        
            "user_id": self.user_id,        
            "created_at": self.created_at,
            "post_text" : self.post_text,
            "weekly_summary_id" : self.weekly_summary_id,
            "emotions" : {"sadness" : self.sadness_amount, "fear" : self.fear_amount, "joy" : self.joy_amount, "anger":self.anger_amount}
        }
    
# The WeeklySummaries class
class WeeklySummaries(db.Model):    
    __tablename__ = "weekly_summaries"
    id = db.Column(db.Integer, primary_key=True)    
    week_of = db.Column(db.String, nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    summary_text = db.Column(db.String, nullable=True) 

    #Should I do cascade = "delete"?
    analyzed_posts = db.relationship("Posts", cascade = "delete")


    #Returns a dictionary of important attributes 
    def serialize(self):    
        return {        
            "id": self.id,
            "user_id": self.user_id,
            "week_of": self.week_of,        
            "analyzed_posts" : [a_p.serialize() for a_p in self.analyzed_posts],
            "summary_text" : self.summary_text
        }
    

    

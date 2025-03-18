from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    # Nombre de la tabla 'user'
    __tablename__ = "user"
    
    # Propiedades:
    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)
    # Propiedades de la tabla
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    mail: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # Relacion uno a muchos con Post, la tabla "muchos"
    # Esta línea define la relación desde el lado "uno", tabla post
    posts = relationship("Post", back_populates="user")

    # Relaciones con Follower, la tabla "muchos"
    # Esta línea define la relación desde el lado "uno", tabla post
    from_id = relationship("Follower", back_populates="from_id_1")
    to_id = relationship("Follower", back_populates="to_id_2")

    # Función para renderizar los datos de la tabla
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mail": self.mail,
        }
    
class Follower(db.Model):
    __tablename__ = "follower"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Relación muchos a uno con User, la tabla "uno"
    # Claves foráneas que hace referencia a la tabla "uno" (User)
    user_from_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    user_to_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    # Relaciones con User, la tabla "uno"
    from_id_1 = relationship("User", back_populates="from_id") 
    to_id_2 = relationship("User", back_populates="to_id") 

    def serialize(self):
        return {
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id,
        }

class Comment(db.Model):
    __tablename__ = "comment"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    
    # Relación muchos a uno con User, la tabla "uno"
    # Clave foránea que hace referencia a la tabla "uno" (User)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    # Esta línea define la relación desde el lado "muchos"
    user = relationship("User", back_populates="posts")

    # Relación muchos a uno con Post, la tabla "uno"
    # Clave foranea que hace referencia a la tabla "uno" (Post)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)
    # Esta línea define la relación desde el lado "muchos"
    posts = relationship("Post", back_populates="comments")

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id,
        }

class Post(db.Model):
    __tablename__ = "post"

    # Llave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Relación muchos a uno con User, la tabla "uno"
    # Clave foránea que hace referencia a la tabla "uno" (User)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    # Esta línea define la relación desde el lado "muchos"
    user = relationship("User", back_populates="comments")

    # Relacion uno a muchos con Media, la tabla "muchos"
    # Esta línea define la relación desde el lado "uno", tabla media
    medias = relationship("Media", back_populates="posts")

    # Relacion uno a muchos con Comments, la tabla "muchos"
    # Esta línea define la relación desde el lado "uno", tabla comment
    comments = relationship("Comment", back_populates="posts")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
    
class Media(db.Model):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(200), nullable=False)
    url: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

     # Clave foránea que referencia a la tabla "uno" (Post)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

    # Relación con Post, la tabla "uno"
    posts = relationship("Post", back_populates="medias")

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }
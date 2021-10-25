import sqlalchemy


class Blogs():
    metadata = sqlalchemy.MetaData()

    blogs_table = sqlalchemy.Table(
        "blogs",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("title", sqlalchemy.String(100)),
    )


class Posts():
    metadata = sqlalchemy.MetaData()

    posts_table = sqlalchemy.Table(
        "posts",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("title", sqlalchemy.String(100)),
        sqlalchemy.Column("content", sqlalchemy.Text()),
        sqlalchemy.Column("draft", sqlalchemy.Boolean()),
        sqlalchemy.Column("blog_posts", sqlalchemy.ForeignKey("blogs.id")),
    )


class Tags():
    metadata = sqlalchemy.MetaData()

    posts_table = sqlalchemy.Table(
        "tags",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("content", sqlalchemy.String(30)),
        sqlalchemy.Column("posts_tags", sqlalchemy.ForeignKey("posts.id")),
    )
  
   
class Users():
    metadata = sqlalchemy.MetaData()

    users_table = sqlalchemy.Table(
        "users",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String(100)),
        sqlalchemy.Column("hashed_password", sqlalchemy.String()),
        sqlalchemy.Column("is_superuser", sqlalchemy.Boolean()),
        sqlalchemy.Column("is_sub", sqlalchemy.Boolean(), sqlalchemy.ForeignKey("blogs.id")),
    )
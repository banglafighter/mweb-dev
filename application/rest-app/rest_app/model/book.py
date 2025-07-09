from mweb_orm import MWebModel
from mweb_orm.orm import mweb_orm


class Book(MWebModel):
    title: str = mweb_orm.Column("title", mweb_orm.String(), nullable=False)
    pages: int = mweb_orm.Column("pages", mweb_orm.Integer())
    authorId: int = mweb_orm.Column("author_id", mweb_orm.BigInteger().with_variant(mweb_orm.Integer(), "sqlite"), foreign_key=mweb_orm.ForeignKey("author.id"), nullable=False)
    author = mweb_orm.Relationship("Author")

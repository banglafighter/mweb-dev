from mweb_orm import MWebModel, mweb_orm


class Author(MWebModel):
    name: str = mweb_orm.Column("name", mweb_orm.String(), nullable=False)
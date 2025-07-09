from mweb_orm import MWebModel
from mweb_orm.orm import mweb_orm


class Author(MWebModel):
    name: str = mweb_orm.Column("name", mweb_orm.String(), nullable=False)
from mweb_orm import MWebModel
from mweb_orm.orm import mweb_orm


class Operator(MWebModel):
    __db_key__ = "MWebSaaS"
    name: str = mweb_orm.Column("name", mweb_orm.String(), nullable=False)
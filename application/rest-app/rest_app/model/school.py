from datetime import date, datetime, time
from mweb_orm import MWebModel
from mweb_orm.orm import mweb_orm


class School(MWebModel):
    name: str = mweb_orm.Column("name", mweb_orm.String(255), nullable=False)
    numberOfStudent: int = mweb_orm.Column("number_of_student", mweb_orm.Integer())
    location: str = mweb_orm.Column("location", mweb_orm.String(255))
    email: str = mweb_orm.Column("email", mweb_orm.String(100))
    isActive: bool = mweb_orm.Column("is_active", mweb_orm.Boolean())
    totalAssetAmount: float = mweb_orm.Column("total_asset_amount", mweb_orm.Float())
    description: str = mweb_orm.Column("description", mweb_orm.Text())

    openingTime: time = mweb_orm.Column("opening_time", mweb_orm.Time())
    establishedDate: date = mweb_orm.Column("established_date", mweb_orm.Date())
    lastInspectedAt: datetime = mweb_orm.Column("last_inspected_at", mweb_orm.DateTime())


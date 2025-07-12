from mweb_crud import dto
from mweb_crud.data_transfer.base_dto import MWebDTO
from rest_app.model.school import School


class SchoolDetailsDTO(MWebDTO):
    name = dto.String(required=True, error_messages={"required": "Please enter name"})
    numberOfStudent = dto.Integer(allow_none=True)
    location = dto.String(allow_none=True)
    email = dto.Email(allow_none=True)
    isActive = dto.Boolean(allow_none=True)
    totalAssetAmount = dto.Float(allow_none=True)
    description = dto.String(allow_none=True)
    openingTime = dto.Time(allow_none=True, format="%H:%M:%S")
    establishedDate = dto.Date(allow_none=True, format="%d/%m/%Y")
    lastInspectedAt = dto.DateTime(allow_none=True, format="%d/%m/%Y %H:%M:%S")


class SchoolCreateDTO(SchoolDetailsDTO):
    class Meta:
        model = School


class SchoolUpdateDTO(SchoolDetailsDTO):
    class Meta:
        model = School

    id = dto.Integer(required=True, error_messages={"required": "Please enter id"})


class SchoolUploadDTO(MWebDTO):
    image = dto.File(allow_none=True)
    id = dto.Integer(required=True, error_messages={"required": "Please enter id"})

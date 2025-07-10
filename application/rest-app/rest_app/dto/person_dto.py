from mweb_crud import dto
from mweb_crud.data_transfer.base_dto import MWebDTO


class PersonDetailsDTO(MWebDTO):
    firstname = dto.String(required=True, error_messages={"required": "Please enter first name"})
    lastname = dto.String(allow_none=True)
    email = dto.Email(required=True, error_messages={"required": "Please enter email."})
    income = dto.Float(allow_none=True)


class PersonCreateDTO(PersonDetailsDTO):
    class Meta:
        # model = Person
        pass


class PersonUpdateDTO(PersonDetailsDTO):
    class Meta:
        model = None

    id = dto.Integer(required=True, error_messages={"required": "Please enter id"})


class PersonUploadDTO(MWebDTO):
    image = dto.File(allow_none=True)
    id = dto.Integer(required=True, error_messages={"required": "Please enter id"})

    class Meta:
        model = None

from mweb_orm import MWebModel
from mweb_orm.orm import mweb_orm


class FileExample(MWebModel):
    title: str = mweb_orm.Column("title", mweb_orm.String(100))
    alterText: str = mweb_orm.Column("alter_text", mweb_orm.String(100))
    pdfFile: str = mweb_orm.Column("pdf_file", mweb_orm.String(250))
    docFile: str = mweb_orm.Column("doc_file", mweb_orm.String(250))
    archiveFile: str = mweb_orm.Column("archive_file", mweb_orm.String(250))
    anyFile: str = mweb_orm.Column("any_file", mweb_orm.String(250))
    imageFile: str = mweb_orm.Column("image_file", mweb_orm.String(250))
    customNameFile: str = mweb_orm.Column("custom_name_file", mweb_orm.String(250))

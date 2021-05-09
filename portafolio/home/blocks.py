from wagtail.core import blocks


class StudyBlock(blocks.StructBlock):
    institution = blocks.CharBlock(
        help_text="Nombre de la Institución/Casa de Estudio."
    )
    title = blocks.CharBlock(
        help_text="Título Obtenido"
    )
    init_date = blocks.CharBlock(
        help_text="Mes y año en el que iniciaste."
    )
    finished_date = blocks.CharBlock(
        help_text="Mes y año en el que culminaste."
    )

    class Meta:
        icon = "pencil"
        template = "home/blocks/study_block.html"

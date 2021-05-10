from wagtail.core import blocks


class SkillBlock(blocks.StructBlock):
    icon = blocks.CharBlock(
        help_text="Escribe el nombre del Icono. Ej. fa-node-js"
    )

    class Meta:
        icon = "icon"
        template = "home/blocks/skill_block.html"


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

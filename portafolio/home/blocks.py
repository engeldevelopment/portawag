from wagtail.core import blocks


class ExperienceBlock(blocks.StructBlock):
    position = blocks.CharBlock(max_length=80)
    enterprise = blocks.CharBlock(max_length=200)
    rol_description = blocks.TextBlock(max_length=255)
    init_date = blocks.CharBlock(
        help_text="Mes y año en el que iniciaste. Ej. Octubre 2012"
    )
    finished_date = blocks.CharBlock(
        help_text="Mes y año en el que culminaste. Ej. Octubre 2018"
    )

    class Meta:
        icon = "code"
        template = "home/blocks/experience_block.html"


class SkillBlock(blocks.StructBlock):
    icon = blocks.CharBlock(
        help_text="Escribe el nombre del Icono. Ej. fa-node-js"
    )

    class Meta:
        icon = "pick"
        template = "home/blocks/skill_block.html"


class WorkflowBlock(blocks.StructBlock):
    text = blocks.CharBlock(max_length=80)

    class Meta:
        icon = "success"
        template = "home/blocks/workflow_block.html"


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
        icon = "edit"
        template = "home/blocks/study_block.html"


class AwardBlock(blocks.StructBlock):
    description = blocks.CharBlock(max_length=255)

    class Meta:
        icon = "pick"
        template = "home/blocks/award_block.html"

from wagtail.core import blocks

# TODO: Agregar el block WorkflowBlock para la sección de workflow
# TODO: Agregar SkillBlock y WorkflowBlock a un block SkillsAndWorkflowsBlock.


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

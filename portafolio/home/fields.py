from wagtail.core.fields import RichTextField


class BoldAndItalicRichTextField(RichTextField):
    def __init__(
            self,
            *args,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.features = ["bold", "italic"]

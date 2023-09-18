pages = [
    {"title": "About us", "url": "about"},
    {"title": "Contact us", "url": "contact"},
    {"title": "Glossary", "url": "glossary"},
    {"title": "Services", "url": "services"},
    {"title": "News", "url": "news"},
    {"title": "APIs", "url": "apis"},
]


class DataMixin:
    def get_context(self, **kwargs):
        return {**kwargs, 'pages': pages}

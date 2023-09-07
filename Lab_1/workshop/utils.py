pages = [
    # {"title": "Staff", "url": "staff"},
    {"title": "Services", "url": "services"},
    {"title": "APIs", "url": "apis"},
]


class DataMixin:
    def get_context(self, **kwargs):
        return {**kwargs, 'pages': pages}

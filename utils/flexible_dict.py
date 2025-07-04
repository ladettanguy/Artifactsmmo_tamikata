class FlexibleDict(dict):

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise KeyError(item)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError:
            raise KeyError(item)
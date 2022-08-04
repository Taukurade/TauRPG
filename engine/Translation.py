import json
from dotmap import DotMap
__all__ = ['LocaleMap']


class LocaleMap:
    def __init__(self,lang_file) -> None:
        self.map = DotMap(json.load(open(f'locales/{lang_file}','r',encoding='utf-8')))

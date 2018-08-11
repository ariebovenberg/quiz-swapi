import datetime
import json
import sys
from functools import partial
from pathlib import Path

import quiz


_DEFAULT_URL = 'https://api.graphcms.com/simple/v1/swapi'
_SCHEMA_PATH = Path(__file__).parent / 'schema.json'

with _SCHEMA_PATH.open('rt') as rfile:
    schema = json.load(rfile)


_SCALARS = {
    'DateTime': datetime.datetime,
}

_CLASSES = quiz.types.gen(quiz.schema.load(schema), _SCALARS)


def executor(url=_DEFAULT_URL, **kwargs):
    return quiz.executor(url=url, **kwargs)


query = partial(quiz.query, query_cls=_CLASSES['Query'])


# Add the classes to the module
__this = sys.modules[__name__]
for _name, _value in _CLASSES.items():
    setattr(__this, _name, _value)

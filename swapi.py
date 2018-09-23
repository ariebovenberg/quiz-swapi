from functools import partial
from pathlib import Path

import quiz

URL = 'https://api.graphcms.com/simple/v1/swapi'
_SCHEMA_PATH = Path(__file__).parent / 'schema.json'

schema = quiz.Schema.from_path(_SCHEMA_PATH, module=__name__)
schema.populate_module()
query = schema.query


execute = partial(quiz.execute, url=URL)
executor = partial(quiz.executor, url=URL)
execute_async = partial(quiz.execute_async, url=URL)
async_executor = partial(quiz.async_executor, url=URL)

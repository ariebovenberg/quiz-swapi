import pytest
import requests

import quiz
import swapi

_ = swapi.quiz.selector


@pytest.fixture(scope='session')
def execute():
    return swapi.executor(client=requests.Session())


def test_module():
    assert issubclass(swapi.Starship, quiz.Object)


def test_execute(execute):
    operation = swapi.query(
        _
        .Starship(name='Millennium Falcon')[
            _
            .name
            .hyperdriveRating
            .pilots(orderBy=swapi.PersonOrderBy.height_DESC)[
                _
                .name
                .height
                .homeworld[
                    _.name
                ]
            ]
        ]
    )

    result = execute(operation)
    assert 'errors' not in result

import quiz

import swapi

_ = quiz.SELECTOR


def test_module():
    assert issubclass(swapi.Starship, quiz.Object)


def test_execute():
    operation = swapi.query[
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
    ]
    result = swapi.execute(operation)
    assert result.Starship.pilots[0].homeworld.name == 'Kashyyyk'


def test_get_schema():
    schema = quiz.Schema.from_url(swapi.URL)
    assert isinstance(schema, quiz.Schema)

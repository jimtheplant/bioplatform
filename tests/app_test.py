import datetime
import uuid
from unittest.mock import Mock

import graphene
import pytest

from bioplatform.app import app_factory
from bioplatform.util import Status

BASE_SCALAR_TEST_DATA = [
    {
        "queries": [
            {
                "class_name": "SimpleStringSingleField",
                "query_fields": [
                    ("test1", graphene.String(), "Testing")

                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleIntSingleField",
                "query_fields": [
                    ("test1", graphene.Int(), 1)
                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleFloatSingleField",
                "query_fields": [
                    ("test1", graphene.Float(), 1.0)
                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleBooleanSingleField",
                "query_fields": [
                    ("test1", graphene.Boolean(), True)

                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleIDSingleField",
                "query_fields": [
                    ("test1", graphene.ID(), str(uuid.uuid4()))

                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleDateSingleField",
                "query_fields": [
                    ("test1", graphene.Date(), datetime.date(2019, 9, 15))

                ]
            }
        ]
    },
    {
        "queries": [
            {
                "class_name": "SimpleDateTimeSingleField",
                "query_fields": [
                    ("test1", graphene.Date(), datetime.date(2019, 9, 15))

                ]
            }
        ]
    },
]


@pytest.fixture()
def simple_query_factory():
    def _simple_query_factory(query_name, query_fields):
        query_dict = {}
        for field in query_fields:
            query_dict.update(field)
        return type(query_name, (graphene.ObjectType,), query_dict)

    return _simple_query_factory


@pytest.fixture()
def query_field_factory():
    def _query_field_factory(field_name, field_type, field_value):
        return {
            field_name: field_type, "resolve_" + field_name: lambda self, info: field_value
        }

    return _query_field_factory


@pytest.fixture()
def initializer_mock_factory():
    def _mock_initializer(return_value):
        mock_initializer = Mock()
        mock_initializer.init.return_value = return_value
        return mock_initializer

    return _mock_initializer


@pytest.fixture()
def initializers_factory(initializer_mock_factory, query_field_factory, simple_query_factory):
    def _initializers_factory(param):
        initializers = []
        for query_info in param["queries"]:
            query_fields = []
            for field in query_info["query_fields"]:
                query_fields.append(query_field_factory(*field))
            query = simple_query_factory(query_info["class_name"], query_fields)
            initializers.append(initializer_mock_factory(query))
        return initializers

    return _initializers_factory


def test_app_factory_no_initializers():
    app = app_factory([])
    schema = app.routes[0].app.schema
    assert app.routes[0].path == "/"
    response = schema.execute("{appStatus}")
    assert response.data == {'appStatus': Status.OK.value}


def format_expected_response(field_type, data):
    if type(field_type) == graphene.Date:
        return data.strftime("%Y-%m-%d")
    return data


@pytest.mark.parametrize("param", BASE_SCALAR_TEST_DATA)
def test_app_factory_initializers_base_scalars_no_dates(initializers_factory, param):
    initializers = initializers_factory(param)
    app = app_factory(initializers)
    schema = app.routes[0].app.schema
    assert app.routes[0].path == "/"
    response = schema.execute("{appStatus}")
    assert response.data == {'appStatus': Status.OK.value}
    queries_to_test = []
    for query_info in param["queries"]:
        for query_field_info in query_info["query_fields"]:
            queries_to_test.append(query_field_info)
    for query in queries_to_test:
        response = schema.execute("{" + query[0] + "}")
        assert response.errors is None
        assert response.data == {
            query[0]: format_expected_response(query[1], query[2])
        }

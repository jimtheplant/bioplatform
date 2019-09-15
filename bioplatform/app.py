from graphene import Schema
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp

from .types import BioPlatformInitializer
from .util import AppStatus

DEFAULT_QUERY_TYPES = [
    AppStatus
]


def __initialize_modules(initializer: BioPlatformInitializer, query_types):
    query_types.append(initializer.init())


def __create_starlette_app(base_schema: Schema):
    app = Starlette()
    gql_app = GraphQLApp(schema=base_schema)
    app.add_route('/', gql_app)
    return app


def app_factory(initializer: BioPlatformInitializer, extra_types=None):
    """
    This function acts as the main app factory. Creates the BaseQuery object with the queries from other BioPlatform
    modules. By default, the app will have an AppStatus query.
    :param initializer: A BioPlatformInitializer from a modules
    :param extra_types: Any types that are not present in a module's base query, but could be used by other modules
    :return: A Starlette app object with a GQL endpoint at '/'
    """
    query_types = []
    query_types.extend(DEFAULT_QUERY_TYPES)
    __initialize_modules(initializer, query_types)
    base_query = type("BaseQuery", tuple(query_types), {})
    base_schema = Schema(query=base_query, types=extra_types)
    return __create_starlette_app(base_schema)

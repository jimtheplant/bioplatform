import graphene


class Status(graphene.Enum):
    OK = "OK"
    WARN = "WARNING"
    ERROR = "ERROR"


class AppStatus(graphene.ObjectType):
    app_status = graphene.Field(Status)
    version = graphene.String(default_value="0.0.1")

    @classmethod
    def resolve_app_status(cls, info):
        return Status.OK

import graphene

import bible.schema


class Query(bible.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
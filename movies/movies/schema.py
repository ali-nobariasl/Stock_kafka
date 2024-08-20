













import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api')))

import graphene
import api.schema as qu

class Query(qu.Query,graphene.ObjectType):
    pass

class Mutation(qu.Mutation,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)

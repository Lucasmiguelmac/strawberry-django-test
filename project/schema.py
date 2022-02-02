from functools import partial
import inspect
from asgiref.sync import sync_to_async
import strawberry
from typing import List

from fruits.api import types, resolvers
from fruits.models import Color, Fruit


@strawberry.type
class Query:
    fruits: List[types.Fruit] = strawberry.django.field()

@strawberry.type
class Mutation:

    create_fruit: Fruit = strawberry.mutation(
        resolver=resolvers.create_fruit
    )
    

schema = strawberry.Schema(query=Query, mutation=Mutation)
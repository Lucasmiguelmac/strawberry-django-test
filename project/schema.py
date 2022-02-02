import strawberry
from typing import List

from fruits.api import types, resolvers

@strawberry.type
class Query:
    fruits: List[types.Fruit] = strawberry.django.field()

@strawberry.type
class Mutation:

    create_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.create_fruit
    )
    update_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.update_fruit
    )
    delete_fruit: types.Fruit = strawberry.mutation(
        resolver=resolvers.delete_fruit
    )

schema = strawberry.Schema(query=Query, mutation=Mutation)
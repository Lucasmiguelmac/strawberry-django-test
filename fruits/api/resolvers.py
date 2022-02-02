from asgiref.sync import sync_to_async
from strawberry.types import Info

from fruits import models
from fruits.api import types
from project.common.utils import data_to_dict

@sync_to_async
def create_fruit(
    self, info: Info, data: types.FruitInput
) -> types.Fruit:
    color = models.Color.objects.get_or_create(name=data.color)[0]
    fruit_data = data_to_dict(data)
    fruit_data.pop("color")
    fruit = models.Fruit(**fruit_data, color=color)
    fruit.save()
    return fruit
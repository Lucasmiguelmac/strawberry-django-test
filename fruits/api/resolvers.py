from copy import deepcopy
from asgiref.sync import sync_to_async
from django.shortcuts import get_object_or_404
import strawberry
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
    fruit_obj = models.Fruit(**fruit_data, color=color)
    fruit_obj.save()
    return fruit_obj

@sync_to_async
def update_fruit(
    self, info: Info, data: types.UpdateFruitInput
) -> types.Fruit:
    fruit_data: dict = data_to_dict(data)
    fruit_obj: models.Fruit = get_object_or_404(models.Fruit, pk=int(data.id))
    if data.color:
        fruit_data["color"] = models.Color.objects.get_or_create(
            name=data.color
        )[0]
    for key, value in fruit_data.items():
        setattr(fruit_obj, key, value)
    fruit_obj.save(
        update_fields=[key for key in fruit_data.keys()] 
    )
    return fruit_obj

@sync_to_async
def delete_fruit(
    self, info: Info, data: types.DeleteFruitInput
) -> types.Fruit:
    fruit_obj: models.Fruit = get_object_or_404(
        models.Fruit,
        pk=int(data.id)
    )
    deleted_obj = deepcopy(fruit_obj)
    fruit_obj.delete()
    return deleted_obj
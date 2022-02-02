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


# def update_fruit(
#     self, fruit_obj: Fruit,
# )


# def update_fruit(
#     self, name: str=None, color: str=None, amount: int=None, obj_id: int=None 
# ) -> types.Fruit:
#     updated_fruit_dict = {k:v for (k, v) in locals()["args"].items() if v}
#     fruit_obj = Fruit.objects.get(id=obj_id)        
#     color = updated_fruit_dict.get("color", False)
#     if color:
#         color_obj = Color.objects.get_or_create(name=color)[0]
#         return fruit_obj.update(**updated_fruit_dict, color=color_obj)
#     return fruit_obj.update(**updated_fruit_dict)
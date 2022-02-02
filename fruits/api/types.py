import strawberry
import strawberry_django
from fruits import models
from strawberry.arguments import UNSET
from strawberry_django import auto
from typing import List, Optional


@strawberry_django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: 'Color'
    amount: auto

@strawberry_django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: List[Fruit]

@strawberry.django.input(models.Fruit)
class FruitInput:
    id: auto
    name: auto
    color: str
    amount: auto

@strawberry.django.input(models.Color)
class ColorInput:
    id: auto
    fruits: auto

@strawberry.django.input(models.Fruit)
class UpdateFruitInput:
    name: Optional[str] = UNSET
    color: Optional[Color] = UNSET
    amount: Optional[int] = UNSET
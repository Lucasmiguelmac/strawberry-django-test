import strawberry_django
from fruits import models

@strawberry_django.type(models.Fruit)
class Fruit:
    name: str
    color: str
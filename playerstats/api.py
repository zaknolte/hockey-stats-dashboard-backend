from ninja import ModelSchema, Router, Field, Schema
from typing import List, Union, Optional
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Player
from teamstats.api import TeamSchema, SimpleTeamSchema


player_router = Router()

    
class PlayerSchema(ModelSchema):
    # position: List[PlayerPositionSchema]
    position: list[str] = Field(..., alias="position")
    team: Optional[SimpleTeamSchema] = None
    class Config:
        model = Player
        model_fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "team",
            "picture",
            "position",
            "jersey_number",
            "birthday",
            "birth_city",
            "birth_state",
            "birth_country",
            "height_inches",
            "weight",
            "is_active",
            "is_rookie",
            "handed"
        ]

    # Player.position is list of dicts
    # Schema will return - position: [position: {...}, position: {...}]
    # Flatten response to just a list of values with resolver - position: [...]
    @staticmethod
    def resolve_position(obj):
         return [i.position for i in obj.position.all()]
     
     
class PlayerNameSchema(Schema):
    name: str = Field(..., alias="full_name")
    id: int
     
     
@player_router.get("/", response=PlayerSchema)
# make sure int typing is before str for parameter
# passed ints can be converted to str so do int first to preserve type
def get_player(request, player: Union[int, str]):
    kwargs = {}
    try:
        kwargs["pk"] = int(player)
    except ValueError:
        kwargs["full_name"] = player
    return Player.objects.get(**kwargs)


@player_router.get("/all", response=List[PlayerSchema])
def get_all_players(request):
    return Player.objects.select_related("team").prefetch_related("position").all()

@player_router.get("/all_names", response=List[PlayerNameSchema])
def get_player_names(request):
    return Player.objects.values("id", "full_name").order_by("full_name")

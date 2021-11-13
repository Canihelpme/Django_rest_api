from rest_framework import serializers
from .models import Game
from .models import GameCategory
from .models import Player
from .models import PlayerScore


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail')

    class Meta:
        model = GameCategory
        fields = ('url',
                  'pk',
                  'name',
                  'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'release_date',
            'played')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    # To display all the details for the game.

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_data',
            'game')

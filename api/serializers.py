from rest_framework import serializers

from api.models import Board, Cell
from api.models import LEVELS_DICT


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = ('id','level','finished')


class CellSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cell
        fields = ('id', 'board', 'has_mine', 'marked_as_mined', 
                  'x_cordenade', 'y_cordenade', 'value')


class DetailBoardSerializer(serializers.ModelSerializer):
    cell_set = CellSerializer(many=True)
    table_size = serializers.ReadOnlyField()
    
    class Meta:
        model = Board
        fields = ('id', 'finished', 'cell_set', 'table_size')
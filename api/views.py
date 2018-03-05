from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .serializers import BoardSerializer, DetailBoardSerializer, CellSerializer
from .models import Board, Cell


class CreateBoard(generics.CreateAPIView):
    """
    Create a new board to start the game
    """
    serializer_class = BoardSerializer


class DetailBoard(generics.RetrieveUpdateAPIView):
    """ Return a board details and asociated cells """
    serializer_class = DetailBoardSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Board, id=pk)
        if not obj.mines_placed:
            obj.place_mines()
        return Board.objects.filter(id=pk)


class MarkCellAsMined(generics.UpdateAPIView):
    """ Mark cell as mined """
    serializer_class = CellSerializer

    def get_queryset(self):
        board_id = self.request.POST.get('board_id', None)
        board = get_object_or_404(Board, id=board_id)
        return Cell.objects.filter(board=board)


detail_board = DetailBoard.as_view() 
create_board = CreateBoard.as_view()
mark_cell_as_mined = MarkCellAsMined.as_view()

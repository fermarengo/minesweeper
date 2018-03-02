from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .serializers import BoardSerializer, DetailBoardSerializer
from .models import Board


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


detail_board = DetailBoard.as_view() 
create_board = CreateBoard.as_view()

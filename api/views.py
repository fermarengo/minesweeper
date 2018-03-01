from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics

from .serializers import BoardSerializer, ShowBoardSerializer


class CreateBoard(generics.CreateAPIView):
    """
    Create a new board to start the game
    """
    serializer_class = BoardSerializer

class ShowBoard(generics.RetrieveUpdateAPIView):
    """ Return a board details and asociated cells """
    serializer_class = ShowBoardSerializer


show_board = ShowBoard.as_view() 
create_board = CreateBoard.as_view()

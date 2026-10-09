from __future__ import annotations  # Permet de typer Card dans Card
import sys
from termcolor import colored, cprint
from colorama import Back, Style
from random import shuffle

class CardValue:
    def __init__(self,valuetext,valuepts):
        self.valuetext = valuetext
        self.valuepts = valuepts


class CardColor:
    def __init__(self,shade : str ,shade_name : str ,foreground_color : str ,background_color : str ):
        self.shade = shade      
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color

class Card:
    def __init__(self,valuetext,valuepts,shade,shade_name,foreground_color,background_color):

        self.cardvalue = CardValue(valuetext,valuepts)
        self.cardcolor = CardColor(shade,shade_name,foreground_color,background_color):



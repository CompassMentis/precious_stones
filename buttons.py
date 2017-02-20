import pygame

from drawing_surface import scale_vertices, draw_rectangle, draw_text, \
    grow_rectangle
from drawing_surface import ColourPalette
from settings import Vector, config

class ButtonCollection(object):
    def __init__(self):
        self.buttons = []

    def add(self, rectangle, action, text=None):
        button = VisibleButton(rectangle, action, text) if text \
            else Button(rectangle, action)
        self.buttons.append(button)
        return button

    def process_mouse_click(self, current_player):
        mouse_position = pygame.mouse.get_pos()
        for button in self.buttons:
            # Assume only button for each location
            if button.clicked(mouse_position):
                return button.action.activate(current_player)
        return []


    def reset(self):
        self.__init__()

class Button(object):
    def __init__(self, rectangle, action):
        self.rectangle = rectangle
        self.action = action

    @property
    def scaled_rectangle(self):
        return scale_vertices(self.rectangle)

    def clicked(self, mouse_position):
        return self.scaled_rectangle[0] <= \
               mouse_position[0] <= \
               self.scaled_rectangle[0] + self.scaled_rectangle[2] and \
               self.scaled_rectangle[1] <= \
               mouse_position[1] <= \
               self.scaled_rectangle[1] + self.scaled_rectangle[3]

    def embody(self):
        self._draw()


    def _draw(self):
        draw_rectangle(
            grow_rectangle(self.rectangle, 2),
            ColourPalette.button,
            # line_width=2
        )


class VisibleButton(Button):
    def __init__(self, rectangle, action, text):
        super().__init__(rectangle, action)
        self.text = text

    def _draw(self):
        draw_rectangle(self.rectangle, ColourPalette.button)
        draw_text(Vector(self.rectangle[0], self.rectangle[1]) +
                  config.button_text_location,
                  self.text)

buttons = ButtonCollection()
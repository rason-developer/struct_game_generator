import os

EVENTS_CODE =  '''

import pygame as py 
from resources.default.df_win_options import DF_FPS

class EventController:
    def __init__(self):
        self.clock = py.time.Clock()
    
    def run(self)->bool:
        self.clock.tick(DF_FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                return False
        return True

'''
WINDOW_CODE = '''
from resources.default.df_win_options import * 
import pygame as py 
from resources.colors.colors import ColorRGB as test_color

class WindowController:
    def __init__(self, isDefault=True, size_window= None):
        self.win = None
        self.title = py.display.set_caption(TITLE)
        self.__initialize(isDefault, size_window)
        
         
    def __initialize(self, isDefault, size_window):
        self.win = py.display.set_mode((DF_WIN_SIZE)) if isDefault else py.display.set_mode((size_window))
        
    
    def run(self):
        self.win.fill(test_color.BLACK)
    

'''
UPDATE_CODE = '''
import pygame as py


class UpdateController:
    def __init__(self):
        pass
    def run(self):
        py.display.update()

'''

GAME_CODE = '''
from components.events import EventController
from components.update import UpdateController
from components.window import WindowController

class Game:
    def __init__(self):
        self.event_controller = EventController()
        self.update_controller = UpdateController()
        self.window_controller = WindowController()
        
        self.isRunning = True
    def run(self):
        while self.isRunning:
            self.isRunning = self.event_controller.run()
            self.update_controller.run()
            self.window_controller.run()     
       
'''
COLORS_CODE = '''
class ColorRGB:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    
'''
DEFAULT_WINDOWS_CODE = '''
# DEFAULT WINDOW WIDTH | HEIGHT

DF_WIN_WIDTH = 800
DF_WIN_HEIGHT = 600
DF_WIN_SIZE = (DF_WIN_WIDTH, DF_WIN_HEIGHT)

TITLE = "Game"

DF_FPS = 30
'''

DEFAULT_GAME_RUN_CODE = '''
from game_connector import game


def run():
    a = game.Game()
    a.run()
if __name__ == "__main__":
    run()
'''

def create_project_structure():
    folders = [
        'components',
        'objects',
        'game_connector',
        'resources',
        'resources/default',
        'resources/colors'
    ]

    files = [
        ('components/__init__.py', ''),
        ('components/events.py', EVENTS_CODE),
        ('components/update.py', UPDATE_CODE),
        ('components/window.py', WINDOW_CODE),
        ('objects/__init__.py', ''),
        ('game_connector/__init__.py', ''),
        ('game_connector/game.py', GAME_CODE),
        ('resources/__init__.py', ''),
        ('resources/default/__init__.py', ''),
        ('resources/default/df_win_options.py', DEFAULT_WINDOWS_CODE),
        ('resources/colors/__init__.py', ''),
        ('resources/colors/colors.py', COLORS_CODE),
        ('default.py',DEFAULT_GAME_RUN_CODE)
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file, content in files:
        with open(file, 'w') as f:
            f.write(content)

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()



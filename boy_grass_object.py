from pico2d import *
import random
from pathlib import Path


def load_asset(filename):
    return load_image(str(Path(__file__).resolve().parent / filename))


# Game object class here
class Grass:
    def __init__ (self):
        self.image = load_asset('grass.png')

    def draw(self):
        self.image.draw(400, 30)
    
    def update(self):   
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = 0
        self.image = load_asset('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_asset('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, self.x, self.y, frame_width // 2, frame_height // 2)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 570
        self.type = random.randint(0, 1)
        self.frame = 0
        if self.type == 0:
            self.image = load_asset('ball21x21.png')
        else:
            self.image = load_asset('ball41x41.png')

    def update(self):
        pass
    
    def draw(self):
        if self.type == 0:
            self.image.draw(self.x, self.y)
        else:
            self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




def reset_world():
    global running
    running = True

    global world
    world = []

    global grass
    grass = Grass()# Grass클레스를 이용하여 객체생성
    world.append(grass)

    global team
    team = [Boy() for i in range(11)]# Boy클래스를 이용하여 객체 11개 생성
    world += team

    global zombie
    zombie = [Zombie() for i in range(1)]# Zombie클래스를 이용하여 객체 11개 생성
    world += zombie

    global ball
    ball = [Ball() for i in range(20)]# Ball클래스를 이용하여 객체 20개 생성
    world += ball




def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()

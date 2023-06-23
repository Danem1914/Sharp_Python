"""Lil tikes first python project"""

from typing import Optional, Tuple
import arcade
import pyglet

#constants
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class JakeSpace(arcade.Window):
    """
    window creation
    """
    def __init__(self, width, height, title):
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jake Space")
        #mouse invis
        self.set_mouse_platform_visible(False)

        #laser pewpew
        self.laser_sound = arcade.load_sound("laser.wav")

        #player info
        self.player_sprite = None
        self.score = 0

        self.background = None

        #arcade.set_background_color(arcade.color.BLACK) -- might not be needed if i load background image

    def setup(self):
        """SET UP THE GAME AND INITIALIZE THE VARIABLES."""

        #background texture
        self.background = arcade.load_texture("stars.png")

        #sprite lists
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        #Score
        self.score = 0

        self.player_sprite = arcade.Sprite("orangeship_1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        #renders the screen

        #this command has to happen before we start drawing
        arcade.start_render()

        #this draws our background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH, self.background)

        #this draws our ship
        self.player_list.draw()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)

def main():
    window = JakeSpace (SCREEN_WIDTH, SCREEN_HEIGHT, "Jake Space")
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
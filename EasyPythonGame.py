"""Lil tikes first python project"""

from typing import Optional, Tuple
import arcade
import pyglet

#constants
from typing import Optional, Tuple
import arcade
import pyglet

#constants
SPRITE_SCALING = 0.25
SPRITE_SCALING_LASER = 0.5
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

MOVEMENT_SPEED = 5
BULLET_SPEED = 10

class Ship(arcade.Sprite):
    """Player class"""

    def update(self):
        self.center_x += self.change_x
        #stops player from leaving screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1



class JakeSpace(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Jake Space")
        #initialize variables
        self.set_mouse_visible(False)
        self.player_list = None
        self.bullet_list = None
        self.player_sprite = None
        self.laser_sound = arcade.load_sound("laser.wav")
        
    def setup(self):

        """Setup and initialize variables"""
        self.background = arcade.load_texture("stars.png")

        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.player_sprite = Ship ("orangeship_1.png", SPRITE_SCALING )
        #player position
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 75
        #helps performance by loading all sprits in a batch files from a list
        self.player_list.append(self.player_sprite)

    def on_draw(self):

        #renders/draws back ground
        self.clear()
        arcade.start_render
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH, self.background)
        #draws sprites from batch file
        self.player_list.draw()
        self.bullet_list.draw()

    def on_update(self, delta_time):
        #updates location
        self.player_list.update()
        self.bullet_list.update()

        """
        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet) #add asteroids later <---------------------
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()
        """
        
    def on_key_press(self, key, modifiers):
        #user controlled movement commands
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        #pewpew
        if key == arcade.key.SPACE:
            bullet = arcade.Sprite("laserRed01.PNG", SPRITE_SCALING_LASER)
            arcade.play_sound(self.laser_sound)

        #bullet = arcade.Sprite("laserRed01.PNG", SPRITE_SCALING_LASER)

            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top
            bullet.change_y = BULLET_SPEED
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        #must have key release or else player moves in the direction until other input is entered
        if key == arcade.key.LEFT or arcade.key.RIGHT:
            self.player_sprite.change_x = 0

        if key == arcade.key.SPACE:
            self.bullet = None

def main():
    window = JakeSpace (SCREEN_WIDTH, SCREEN_HEIGHT, "Jake Space")
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
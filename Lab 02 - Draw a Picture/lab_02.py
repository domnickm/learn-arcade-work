import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.CYBER_YELLOW)
arcade.start_render()

# Draw the Grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0,arcade.color.BITTER_LIME)

#Draw the Sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.ORANGE)


#  Finish and run
arcade.finish_render()
arcade.run()
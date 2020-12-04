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

#Draw car with wheels
arcade.draw_rectangle_filled(600,150,140,70, arcade.color.BLACK)
arcade.draw_circle_filled(500,110,50, arcade.color.BLUE)
arcade.draw_circle_filled(500,110,45, arcade.color.LIGHT_BLUE)
arcade.draw_circle_filled(650,90,30,arcade.color.BLUE)
arcade.draw_circle_filled(650,90,25,arcade.color.LIGHT_BLUE)


#  Finish and run
arcade.finish_render()
arcade.run()
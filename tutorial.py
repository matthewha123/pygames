import pygame as pg
import snakeHead as sH
import GameObjects

import random

pg.init()

width = 400
height = 700

screen = pg.display.set_mode((width,height))
done = False

clock = pg.time.Clock()

head = sH.SnakeHead(40, 40)
count = 0

bodies = []


f = GameObjects.Food(20, 20, "food")
bodies.append(f)

b = GameObjects.Damage(65,35, 1)
bodies.append(b)

def draw_GameObjects(screen, bodies):
	for b in bodies:
		b.draw(screen)

def generate_bodies(bodies):
	global count
	starting_x = {num for num in range(0,400,45)}
	if(count > 300):
		count = 0
		empty_spaces = random.randint(0,3)
		dmg_block_locations = random.sample(starting_x,8 - empty_spaces)
		for x in dmg_block_locations:
			bodies.append(GameObjects.Damage(x,40,random.randint(2,10)))
		for x in (starting_x - dmg_block_locations):
			pass
			
		
		

while not done:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			done= True
	
	key_presses = pg.key.get_pressed()
	
	
	screen.fill((0,0,0))
	generate_bodies(bodies)
	head.move(pg.mouse.get_pos())
	head.detect_collisions(bodies,screen)
	draw_GameObjects(screen,bodies)
	b.draw(screen)
	
	head.draw(screen)

	pg.display.flip()
	
	count += 1
	clock.tick(60)
pg.quit()

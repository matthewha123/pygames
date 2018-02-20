# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:58:17 2018

@author: matth
"""
import pygame as pg
import GameObjects


class SnakeHead:
	square = 25
	color = (0,128,255)
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
		self.tails = []
	def move(self,newPos):
		self.x = newPos[0]
		self.y = newPos[1]
		
		for index,t in enumerate(self.tails):
			t.move(newPos, index+1.2,index, self.square)
	def draw(self, screen):
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
		pg.draw.rect(screen, self.color, self.rect)
		self.draw_tail(screen)
		
	def add_tail(self):
		tail = SnakeTail(self.x, self.y + (self.square+2)*(1 + len(self.tails)))
		self.tails.append(tail)
		
	def draw_tail(self,screen):
		for index,t in enumerate(self.tails):
			t.draw(screen)
	
	def subtract_tail(self,dmg):
		for i in range(dmg):
			del self.tails[len(self.tails)-1]
	
	def detect_collisions(self,bodies,screen):
		for index,b in enumerate(bodies):
			if(self.rect.colliderect(b.rect) and not(b.ignore)):
				b.destroy()
				if(type(b) == GameObjects.Food):
					print("adding")
					self.add_tail()
				elif(type(b) == GameObjects.Damage):
					print("subtracting")

					self.subtract_tail(b.dmg)
			

class SnakeTail:
	color = (255,255,255)
	square = 20
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
	def move(self, mousePos, delay_factor, index, head_square):
		goal_x = mousePos[0] +(self.square/6)
		goal_y = mousePos[1] + (head_square+4)*(index+1)
		
		diffX = goal_x - self.x
		diffY = goal_y - self.y
		
		dx = diffX/delay_factor
		dy = diffY/delay_factor
		
		self.x += dx
		self.y += dy
		
	def draw(self,screen):
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
		pg.draw.rect(screen, self.color, self.rect)
	def destroy(self):
		pass

		
		
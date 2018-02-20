# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:43:45 2018

@author: matth
"""
import pygame as pg

class Food:
	square = 15
	color = (255,255,255)
	def __init__(self,x,y,kind):
		self.x = x
		self.y = y
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
		self.kind = kind
		self.ignore = False

	def destroy(self):
		self.ignore = True
		
	def draw(self,screen):
		if not self.ignore:
			pg.draw.rect(screen, self.color, self.rect)


class Damage:
	square = 40
	color = (255,0,0)
	def __init__(self,x,y,dmg):
		self.x = x
		self.y = y
		self.dmg = dmg
		self.rect = pg.Rect(self.x,self.y,self.square,self.square)
		font = pg.font.SysFont("comicsansms",14)
		self.text = font.render(str(dmg),True,(255,255,255))
		self.ignore = False
	
	def draw(self,screen):
		if not self.ignore:
			pg.draw.rect(screen,self.color,self.rect)
			screen.blit(self.text, (self.x + (self.square - self.text.get_width())/2,
							  self.y + (self.square- self.text.get_height())/2))
	def destroy(self):
		self.ignore = True


		
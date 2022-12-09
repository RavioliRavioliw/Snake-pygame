import pygame 
from pygame.locals import *
from pygame.math import Vector2
import random


pygame.init()

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

fonts = pygame.font.Font("freesansbold.ttf", 20)
f_onts = pygame.font.Font("freesansbold.ttf", 50)

snake_grill = 20
reso_grill = 40

clicked = False

screen = pygame.display.set_mode((reso_grill * snake_grill, reso_grill * snake_grill))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((white))

class Snake:
	def __init__(self):
		self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
		self.direction = Vector2(0,1)
		self.bloku = False
		self.kek = True
	

	def draw_snake(self):
		if self.kek:
			for grill in self.body:
				pos_x = int(grill.x * snake_grill)
				pos_y = int(grill.y * snake_grill)
				grill_rect = pygame.Rect(pos_x, pos_y , snake_grill, snake_grill)
				pygame.draw.rect(screen, (255, 0, 0), grill_rect)

	def move(self):
		if self.bloku:
			coopy = self.body[:]
			coopy.insert(0, self.body[0] + self.direction)
			self.body = coopy[:]
			self.bloku = False
		else:
			coopy = self.body[:-1]
			coopy.insert(0, self.body[0] + self.direction)
			self.body = coopy[:]

	def add(self):
		self.bloku = True

	def check(self):
		if self.body[0].x <= -1 or self.body[0].y <= -1 or self.body[0].x > 40 or self.body[0].y > 40:
			return True
			self.kek = False
		for block in self.body[1:]:
			if block == self.body[0]:
				return True
				self.kek = False

class Fruit:

	def __init__(self):
		self.randomi()
		

	def draw(self):
		fruit_rect = pygame.Rect(int(self.pos.x * snake_grill), int(self.pos.y * snake_grill), snake_grill, snake_grill )
		pygame.draw.rect(screen, (0, 255, 0), fruit_rect)

	def randomi(self):
		self.x = random.randint(0, reso_grill -10 )
		self.y = random.randint(0,	reso_grill -10 )
		self.pos = Vector2(self.x, self.y)


class button():

	width = 180
	height = 70
	button_col = (124, 124, 124)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = (0, 0, 245)

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text
		


	def draw_button(self):

		global clicked
		action = False

		pos = pygame.mouse.get_pos()
	
		button_rect = Rect(self.x, self.y, self.width, self.height)
		

		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)

			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True

			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)


		text_img = fonts.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action

snake = Snake()
again = button(300, 350, 'Play Again?')
fruit = Fruit()

class game_core:
	def __init__(self):
		pass

	def close(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_DOWN:
					if snake.direction.y != -1:
						snake.direction = Vector2(0,1)
				if event.key == K_UP:
					if snake.direction.y != 1:
						snake.direction = Vector2(0,-1)
				if event.key == K_RIGHT:
					if snake.direction.x != -1:
						snake.direction = Vector2(1,0)
				if event.key == K_LEFT:
					if snake.direction.x != 1:
						snake.direction = Vector2(-1,0)	
		if snake.check():
			snake.direction= Vector2(0, 0)
			snake.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
			self.Game_over()

		if fruit.pos == snake.body[0]:
			fruit.randomi()
			snake.add()
			
	def Pasue(self):
		pass

	def Main_menu(self):
		pass

	def Game_over(self):
		game_over_text = f_onts.render("Game Over", False, (124, 124, 124))
		screen.blit(game_over_text, (280, 0))
		if again.draw_button():
			snake.kek = True
			snake.direction= Vector2(0, 1)




core = game_core()


while True:
	screen.blit(background, (0, 0))

	snake.draw_snake()
	fruit.draw()
	core.close()


	snake.move()
	clock.tick(10)
	
	pygame.display.update()


if __name__ == __main__:
	pass


	
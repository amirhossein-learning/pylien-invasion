import pygame.font

class Button:
	# this class creates the game starting button to show to player
	def __init__(self, ai_game, msg):
		# class constructor
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		#
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		#
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		#
		self._preg_msg(msg)

	def _preg_msg(self, msg):
		# this method chagnes msg str to an image to show it at the center of the screen
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		#
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# this method displays the botton and the image init
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)		

import pygame


pygame.init()
FONT = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
	displaySurf = pygame.display.get_surface()  # surface
	debugSurf = FONT.render(str(info), True, 'white')
	debugRect = debugSurf.get_rect(topleft=(x, y))
	pygame.draw.rect(displaySurf, 'black', debugRect)
	displaySurf.blit(debugSurf, debugRect)

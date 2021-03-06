import pygame


class TileSpriteSheet(object):
    def __init__(self, tiles_spritesheet):
        self.sprite_sheet = pygame.load.image("images/tiles_spritesheet.png")

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height].convert)

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        return image

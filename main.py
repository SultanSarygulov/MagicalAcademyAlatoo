import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Magical Academy Ala-Too')
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('KZ_Century_Gothic.ttf', 50)
        self.font1 = pygame.font.Font('KZ_Century_Gothic.ttf', 30)

        #load spritesheets
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/baklava.png')
        self.bandit_spritesheet = Spritesheet('img/tent.png')
        self.tennis_spritesheet = Spritesheet('img/tennis.png')
        self.desk_spritesheet = Spritesheet('img/desk.png')
        self.floorA_spritesheet = Spritesheet('img/floor_a.png')
        self.floorB_spritesheet = Spritesheet('img/floor_b.png')
        self.floorC_spritesheet = Spritesheet('img/floor_c.jpg')
        self.hall_spritesheet = Spritesheet('img/hall.png')
        self.stage_spritesheet = Spritesheet('img/stage.png')
        self.basketball_spritesheet = Spritesheet('img/basketball.png')
        self.volleyball_spritesheet = Spritesheet('img/volleyball.png')
        self.football_spritesheet = Spritesheet('img/football.png')
        self.sporthall_spritesheet = Spritesheet('img/sporthall.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')

        self.bruh = pygame.mixer.Sound('bruh.mp3')
 
    def createMap(self): 
        #creating map duh
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "U":
                    Block(self, j, i)
                if column == "S":
                    Block(self, j, i)
                if column == "G":
                    GrassBush(self, j, i)
                if column == "А":
                    FloorA(self, j, i)
                if column == "а":
                    FloorAA(self, j, i)
                if column == "H":
                    Hall(self, j, i)
                if column == "С":
                    Stage(self, j, i)
                if column == "Б":
                    FloorB(self, j, i)
                if column == "Ц":
                    FloorC(self, j, i)
                if column == "Ç":
                    Sporthall(self, j, i)
                if column == "?":
                    Tennis(self, j, i)
                if column == "!":
                    Basketball(self, j, i)
                if column == "#":
                    Volleyball(self, j, i)
                if column == "Ф":
                    Football(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "Q":
                    Bandit(self, j, i)
                

    def new(self):
        #new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.bandits = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createMap()
    
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE )
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)

    def update(self):
        #game loops update
        self.all_sprites.update()

    def draw(self):
        #game loops draw
        self.screen.fill(GRAY)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):

        bg = pygame.image.load('img/dead.png')
        intro = 0

        while 1:
            self.screen.blit(bg, (0, 0))

            if intro == 0:
                restart = self.font.render('Restart game',True, BLUE)
                mainMenu = self.font.render('Main menu', True, BLACK)
            elif intro == 1:
                restart = self.font.render('Restart game',True, BLACK)
                mainMenu = self.font.render('Main menu', True, BLUE)

            self.screen.blit(restart, (WIN_WIDTH/3, WIN_HEIGHT/3))
            self.screen.blit(mainMenu, (WIN_WIDTH/3, 1.5*WIN_HEIGHT/3))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.intro_screen()
                    self.new()
                    self.main()
        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        intro += 1
                    elif event.key == pygame.K_UP:
                        intro -= 1
                    elif event.key == pygame.K_RETURN:
                        if intro == 0:
                            self.main()
                            self.new()
                        elif intro == 1:
                            self.intro_screen()
                            self.new()
                            self.main()
                            
            intro = intro % 2
            pygame.display.update()
    
    def intro_screen(self):

        bg = pygame.image.load('img/pixel_casttle.png')
        intro = 0

        while 1:
            self.screen.blit(bg, (0, 0))
            title = self.font.render('MAGICAL  ACADEMY  ALA-TOO ',True, RED)
            goal = self.font1.render('Cleanse our Magic Academy from', True, BLACK)
            goal1 = self.font1.render('baklava mutants and bandits', True, BLACK)
            controls = self.font1.render('Press arrow keys for movement', True, DARK_GRAY)
            controls1 = self.font1.render('Press spacebar for attack', True, DARK_GRAY)


            if intro == 0:
                start = self.font.render('Start game',True, BLUE)
                quit = self.font.render('Quit game', True, BLACK)
            elif intro == 1:
                start = self.font.render('Start game',True, BLACK)
                quit = self.font.render('Quit game', True, BLUE)

            self.screen.blit(start, (WIN_WIDTH/3, WIN_HEIGHT/3))
            self.screen.blit(quit, (WIN_WIDTH/3, 1.5*WIN_HEIGHT/3))
            self.screen.blit(title, (WIN_WIDTH/9, WIN_HEIGHT/10))
            self.screen.blit(goal, (WIN_WIDTH/70, 2*WIN_HEIGHT/3))
            self.screen.blit(goal1, (WIN_WIDTH/70, 2.19 * WIN_HEIGHT/3))
            self.screen.blit(controls, (WIN_WIDTH/70, 2.5*WIN_HEIGHT/3))
            self.screen.blit(controls1, (WIN_WIDTH/70, 2.69 * WIN_HEIGHT/3))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        intro += 1
                    elif event.key == pygame.K_UP:
                        intro -= 1
                    elif event.key == pygame.K_RETURN:
                        if intro == 0:
                            return True
                        elif intro == 1:
                            pygame.quit()
                            sys.exit()
            intro = intro%2

            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
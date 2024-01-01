import pygame
import random

running  = True

class GameState:
    def __init__(self):
        pass
    running = True;
    applePosition = [0,0]
    score = 0
    timeTimer = 0
    timeDiff = 200

class Player:
    def __init__(self):
        pass
    snakeChain = []
    snakeLength = 3
    direction = [0,1]
    currentPosition = [10,12]

def EndGame():
    game.running = False

def MoveSnake():
    currentPosition = player.snakeChain[len(player.snakeChain)-1]
    nextPosition = [(currentPosition[0]+player.direction[0]),(currentPosition[1]+player.direction[1])]
    CollisionCheck(nextPosition)
    player.snakeChain.append(nextPosition)
    grid[nextPosition[0]][nextPosition[1]] = 1
    oldPosition = player.snakeChain.pop(0)
    grid[oldPosition[0]][oldPosition[1]] = 0

def RandomApplePlacement():
    xPos = random.randrange(2,27)
    yPos = random.randrange(2,37)
    if (grid[xPos][yPos] == 0):
        return [xPos,yPos]
    else:
        return RandomApplePlacement()

def PlaceApple(first = False):
    if first:
        game.applePosition = RandomApplePlacement()
        grid[game.applePosition[0]][game.applePosition[1]] = 2
    else:
        oldPosition = game.applePosition
        grid[game.applePosition[0]][game.applePosition[1]] = 0
        game.applePosition = RandomApplePlacement()
        grid[game.applePosition[0]][game.applePosition[1]] = 2

def EatApple():
    newXPos = game.applePosition[0]
    newYPos = game.applePosition[1]
    player.snakeChain.append([newXPos,newYPos])
    player.snakeLength += 1
    PlaceApple()
    grid[newXPos][newYPos] = 1
    game.score += 1
    if game.timeDiff > 50:
        game.timeDiff -= 8

def CollisionCheck(position):
    if grid[position[0]][position[1]] != 0:
        if grid[position[0]][position[1]] == 2:
            EatApple()
        elif grid[position[0]][position[1]] == 3:
            print("Collision with wall detected")
            EndGame()
        elif grid[position[0]][position[1]] == 1:
            print("Collision with self detected")
            EndGame()
        return
    else:
        return

game = GameState()
player = Player()
game.running = True
pygame.init()
grid = [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]
gridTop = []
gridMain = []
player.snakeChain = []
player.snakeLength = 3
SCREENWIDTH = 800
SCREENHEIGHT = 600
player.direction = [0, 1]
applePosition = [0,0]

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("PySnake")

MovementCheck = pygame.USEREVENT+1
pygame.time.set_timer(MovementCheck, 25)
green = (0, 200, 0)
purple = (200, 0, 200)
red = (200, 0, 0)
blue = (0, 0, 200)
black = (0, 0, 0)
grid[10][10] = 1
player.snakeChain.append([10,10])
grid[10][11] = 1
player.snakeChain.append([10,11])
grid[10][12] = 1
player.snakeChain.append([10,12])
PlaceApple(True)


while game.running != False:  
    screen.fill(black)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if player.direction != [0,1]:
                    player.direction = [0,-1]
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if player.direction != [0,-1]:
                    player.direction = [0,1]
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if player.direction != [1,0]
                    player.direction = [-1,0]
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if player.direction != [-1,0]: 
                    player.direction = [1,0]

        if event.type == MovementCheck:
            game.timeTimer += 25
            if game.timeTimer > game.timeDiff:
                MoveSnake()
                game.timeTimer = 0

    ypos = 0
    for row in grid:
        xpos = 0
        for square in row:
            thisX = 20*xpos
            thisY = 20*ypos
            thisRect = pygame.Rect(thisX,thisY,20,20)
            if square == 1:
                pygame.draw.rect(screen, green, thisRect)
            if square == 2:
                pygame.draw.rect(screen, red, thisRect)
            if square == 3:
                pygame.draw.rect(screen, purple, thisRect)
            xpos += 1
        ypos += 1
    

    pygame.display.update()
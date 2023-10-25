import pygame
import sys
import random

# Inicializar Pygame
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1000, 800
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de la Serpiente")
score = 0
sound1 = pygame.mixer.Sound('comer.mp3')
sound2 = pygame.mixer.Sound('moneda.mp3')
sound3 = pygame.mixer.Sound('uh.mp3')
manzana = pygame.image.load("manzana.png")
patata = pygame.image.load("patata.png")
zanahoria = pygame.image.load("zanahoria.png")
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# Inicialización de la serpiente
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, 1)  # Inicialmente, se mueve hacia arriba

# Inicialización de la comida
food = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
boost = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
slow = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
sumada = 0

font = pygame.font.Font(None, 50)

# Velocidad de la serpiente

snake_speed = 10
clock = pygame.time.Clock()

# Función para dibujar la serpiente, la comida, y los potenciadores en la pantalla
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    mansana = pygame.draw.rect(screen, BLACK, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    screen.blit(manzana, mansana)

def draw_boost(boost):
    velosida = pygame.draw.rect(screen, BLACK, (boost[0] * GRID_SIZE, boost[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    screen.blit(zanahoria, velosida)
    
def draw_slow(slow):
    podria = pygame.draw.rect(screen, BLACK, (slow[0] * GRID_SIZE, slow[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    screen.blit(patata, podria)
 
# Mostrar la puntuación
def draw_score(score):
    score_text = font.render("Puntuación: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

#Mostrar la velocidad
def draw_speed(snake_speed):
    speed_text = font.render("Velocidad: " + str(snake_speed), True, WHITE)
    screen.blit(speed_text, (10, 50))

#Declarar el mensaje Game Over
game_over_font = pygame.font.Font(None, 100)
game_over_text = game_over_font.render("Game Over", True, WHITE)
game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))

game_over = False
playing = True
# Bucle principal del juego
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
    
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Verificar si la cabeza de la serpiente está fuera de los límites
    if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
        playing = False
        game_over = True
        game_over_start_time = pygame.time.get_ticks() #Obtener timepo
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()
        break

    # Comprobar si la serpiente come la comida
    if new_head == food:
        food = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
        score += snake_speed
        sound1.play()
    elif new_head == boost:
        boost = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
        snake_speed += 2 
        sound2.play()
        clock.tick(snake_speed)
    elif new_head == slow:
        slow = (random.randint(0, GRID_WIDTH - 5), random.randint(0, GRID_HEIGHT - 5))
        snake_speed -= 2
        sound3.play() 
        clock.tick(snake_speed)
    else:
        snake.pop()
    
    # Comprobar si la serpiente se come a si misma
    if new_head in snake[1:]:
        playing = False
        game_over = True
        game_over_start_time = pygame.time.get_ticks()
    # Dibujar la pantalla
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)
    draw_boost(boost)
    draw_slow(slow)
    draw_score(score)
    draw_speed(snake_speed)
    clock.tick(snake_speed)

      # Controlar la velocidad de la serpiente
    
    pygame.display.update()

    if game_over and pygame.time.get_ticks() - game_over_start_time >= 10000:
        playing = False
# Esperar unos segundos antes de cerrar la ventana
    
  
    
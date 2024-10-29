import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from scenes.main_menu import MainMenu

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Template")
    clock = pygame.time.Clock()
    
    # Initialize the starting scene
    active_scene = MainMenu()
    
    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = [e for e in pygame.event.get() if e.type in {pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT}]
        
        # Process inputs
        active_scene.process_input(filtered_events, pressed_keys)
        
        # Update game state
        active_scene.update(clock.get_time() / 1000.0)
        
        # Render
        active_scene.render(screen)
        pygame.display.flip()
        
        # Manage scene transitions
        active_scene = active_scene.next_scene
        
        # Cap the frame rate
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    run_game()

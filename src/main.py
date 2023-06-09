import pygame

pygame.init()

# Window view
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

# World view
world_width = 3000
world_height = 3000
world = pygame.Surface((world_width, world_height))

# Camera view
camera = pygame.Rect(0, 0, win_width, win_height)

# Background
bg = pygame.image.load('background/Untitled.png')
world.blit(bg,(0,0))

# Mouse movement
dragging = False
prev_mouse_pos = (0, 0)


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    camera.move_ip(5, 0)  # Move the camera 5 pixels to the right
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    prev_mouse_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
        if dragging:
            mouse_pos = pygame.mouse.get_pos()
            dx, dy = prev_mouse_pos[0] - mouse_pos[0] , prev_mouse_pos[1] - mouse_pos[1]
            camera.move_ip(dx,dy)
            prev_mouse_pos = mouse_pos

        win.blit(world.subsurface(camera), (0, 0))
        pygame.display.flip()

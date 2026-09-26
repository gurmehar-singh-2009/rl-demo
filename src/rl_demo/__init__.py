import asyncio
import pygame

async def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()

        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())

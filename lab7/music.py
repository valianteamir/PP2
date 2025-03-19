
import pygame

pygame.init()

# Screen setup (not strictly needed for audio)
size = [500, 500]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Playlist setup
playlist = [
    "/Users/amirdank/Desktop/PP2/lab7/music/song1.mp3",
    "/Users/amirdank/Desktop/PP2/lab7/music/song2.mp3",
    "/Users/amirdank/Desktop/PP2/lab7/music/song3.mp3"
]
current_song = 0

# Load and start playing the first song
pygame.mixer.init()
pygame.mixer.music.load(playlist[current_song])
pygame.mixer.music.play()

# Set initial volume
volume = 0.5  
pygame.mixer.music.set_volume(volume)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_DOWN:
                if volume > 0:
                    volume -= 0.1
                    pygame.mixer.music.set_volume(max(volume, 0))  # Prevent going below 0
            elif event.key == pygame.K_UP:
                if volume < 1:
                    volume += 0.1
                    pygame.mixer.music.set_volume(min(volume, 1))  # Prevent going above 1
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                current_song = (current_song - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song])
                pygame.mixer.music.play()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

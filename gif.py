import pygame
from PIL import Image, ImageSequence
import io
from constants import *

class AnimatedBackground:
    def __init__(self, gif_path):
        self.frames = []
        self.current_frame = 0
        self.frame_count = 0
        self.frame_speed = 5  # Adjust for speed
        
        # Load the GIF and convert frames to pygame surfaces
        gif = Image.open(gif_path)
        for frame in ImageSequence.Iterator(gif):
            # Convert PIL image to bytes
            frame_bytes = io.BytesIO()
            frame.convert('RGBA').save(frame_bytes, format='PNG')
            frame_bytes.seek(0)
            
            # Convert bytes to pygame surface
            frame_surface = pygame.image.load(frame_bytes)
            # Scale if needed
            frame_surface = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.frames.append(frame_surface)
    
    def update(self):
        # Update the animation
        self.frame_count += 1
        if self.frame_count >= self.frame_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_count = 0
    
    def render(self, surface, position=(0, 0)):
        # Draw the current frame
        surface.blit(self.frames[self.current_frame], position)
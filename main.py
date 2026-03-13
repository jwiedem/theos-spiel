from operator import delitem

import pygame
import sys

from pygame.draw import rect

from Apple import Apple

pygame.init()

# definiert Höhe und Breite des neuen Fensters, diesmal auf die Bildschirmgröße
info = pygame.display.Info()
width, height = info.current_w, info.current_h


base = min(width, height)

obj_width = obj_height = base // 40
apple_width = apple_height = base // 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Theos Spiel")

#Apfelposition in relation zum Bildschirm, statt absolut auf einen Pixelwert (immer in der Mitte)
apple_x = width//2 - apple_width//2
apple_y = height//2 - apple_height//2

# start Position und Geschwindigkeit
x = 400
y = 300
speed = 5

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()

while True:
    # Anfang Schleife
    # überprüft solange True (also immer) was für ein Ereignis passiert
    for event in pygame.event.get():
        #wenn schließen -> schließen :D
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # überprüfe welche Tasten gedrückt werden
    keys = pygame.key.get_pressed()

    # wenn links Pfeil gedrückt
    if keys[pygame.K_LEFT]:
        # x -= speed ist das selbe wie x = x - speed, zieht also speed (5) von x ab -> bewegt Objekt nach links
        x -= speed
        if x <= 5:
            x = 5


    # wenn rechts Pfeil gedrückt
    if keys[pygame.K_RIGHT]:
        # x += speed ist das selbe wie x = x + speed, fügt also speed (5) zu x hinzu -> bewegt Objekt nach rechts
        x += speed
        if x >= width-obj_width-5:
            x = width-obj_width-5


    if keys[pygame.K_UP]:
        # selbe wie x nur mit y, also nach oben und unten
        y -= speed
        if y <= 5:
            y = 5

    if keys[pygame.K_DOWN]:
        y += speed
        if y >= height-obj_height-5:
            y = height-obj_height-5

    # fülle Hintergrund mit Schwarz
    screen.fill(black)

    # zeichne auf dem Bildschirm ein Viereck
    # genauer: pygame zeichnet -> was? ein Rechteck, was für ein Rechteck:
    # erster Parameter: auf welcher Fläche, zweiter Parameter: Farbe, dritter Parameter: wo auf der Fläche (bei x, y) und wie groß ist das Rechteck)


    #variable vorher definieren und dann benutzen (du gibst dem Rechteck einen Namen), dann keine orangene linie
    spieler = (x, y, obj_width, obj_height)
    pygame.draw.rect(screen, green, spieler)

    apfel = Apple(width, height)
    apfel.draw(screen,red)

    # update um die Änderungen auch zu zeigen
    pygame.display.update()

    # mache, dass das Spiel weiter macht (wichtig, wenn andere Objekte sich unabhängig bewegen oder erscheinen, z.B. Früchte alle 10 sec)
    clock.tick(60)




#while True:
#  pygame.draw.rect(screen, (255, 0, 0), apple(x, y, obj_width1, obj_height1))
#   if rechteck_1 is = apple
#       delitem(apple)
#        wait 10:
#        pygame.draw.rect(screen, (255, 0, 0), apple(x, y, obj_width1, obj_height1))


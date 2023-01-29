import pygame
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def openfile():
    file = filedialog.askopenfilename()

    contents = []
    with open(file,'r') as f:
        for line in f:
            rgb = list(line.rstrip().split())
            rgb[0] = int(rgb[0])
            rgb[1] = int(rgb[1])
            rgb[2] = int(rgb[2])
            contents.append(rgb)
    
    return contents

def savefile(contents):
    file = filedialog.asksaveasfilename(defaultextension='.pypaint',filetypes=[("Python Paint file (.pypaint)", ".pypaint")])

    if file[-8:] != ".pypaint":
        file += ".pypaint"

    new = ""
    with open(file,'w') as f:
        for rgb in contents:
            new += str(rgb[0])
            new += " "
            new += str(rgb[1])
            new += " "
            new += str(rgb[2])
            new += "\n"

        f.write(new)

width = 700
height = 700
size = 10
win = pygame.display.set_mode((width+100,height))
pygame.display.set_caption("Python Paint")
pygame.font.init()
font = pygame.font.SysFont("Arial", 16)

def draw_win(win,current, colors):
    win.fill((255,255,255))
    for i,color in enumerate(colors):
        x = (i-(i%(width//size)))//(width//size)
        y = i%(width//size)
        pygame.draw.rect(win,color,(x*size,y*size,size,size))
    pygame.draw.rect(win,(200,200,200),(width,0,100,height))

    
    #RED
    pygame.draw.rect(win,(255,255,255),(width+25,25,25,50))
    pygame.draw.rect(win,(0,0,0),(width+25,25,25,50),2)

    text = font.render("R", True, (255,0,0))
    win.blit(text, (width+25+7,25+15))
    
    pygame.draw.rect(win,(255,255,255),(width+50,25,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,25,25,25),2)

    text = font.render("↑", True, (255,0,0))
    win.blit(text, (width+50+10,25))
    
    pygame.draw.rect(win,(255,255,255),(width+50,50,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,50,25,25),2)

    text = font.render("↓", True, (255,0,0))
    win.blit(text, (width+50+10,50))
    
    pygame.draw.rect(win,(255,255,255),(width+25,75,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,75,50,25),2)

    text = font.render(str(current[0]), True, (0,0,0))
    win.blit(text, (width+40,75+3))

    
    #GREEN
    pygame.draw.rect(win,(255,255,255),(width+25,25+100,25,50))
    pygame.draw.rect(win,(0,0,0),(width+25,25+100,25,50),2)

    text = font.render("G", True, (0,255,0))
    win.blit(text, (width+25+7,25+100+15))
    
    pygame.draw.rect(win,(255,255,255),(width+50,25+100,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,25+100,25,25),2)

    text = font.render("↑", True, (0,255,0))
    win.blit(text, (width+50+10,25+100))
    
    pygame.draw.rect(win,(255,255,255),(width+50,50+100,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,50+100,25,25),2)

    text = font.render("↓", True, (0,255,0))
    win.blit(text, (width+50+10,50+100))
    
    pygame.draw.rect(win,(255,255,255),(width+25,75+100,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,75+100,50,25),2)

    text = font.render(str(current[1]), True, (0,0,0))
    win.blit(text, (width+40,75+100+3))

    
    #BLUE
    pygame.draw.rect(win,(255,255,255),(width+25,25+200,25,50))
    pygame.draw.rect(win,(0,0,0),(width+25,25+200,25,50),2)

    text = font.render("B", True, (0,0,255))
    win.blit(text, (width+25+7,25+200+15))
    
    pygame.draw.rect(win,(255,255,255),(width+50,25+200,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,25+200,25,25),2)

    text = font.render("↑", True, (0,0,255))
    win.blit(text, (width+50+10,25+200))
    
    pygame.draw.rect(win,(255,255,255),(width+50,50+200,25,25))
    pygame.draw.rect(win,(0,0,0),(width+50,50+200,25,25),2)

    text = font.render("↓", True, (0,0,255))
    win.blit(text, (width+50+10,50+200))
    
    pygame.draw.rect(win,(255,255,255),(width+25,75+200,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,75+200,50,25),2)

    text = font.render(str(current[2]), True, (0,0,0))
    win.blit(text, (width+40,75+200+3))


    #CURRENT COLOR
    pygame.draw.rect(win,current,(width+25,325,50,50))
    pygame.draw.rect(win,(0,0,0),(width+25,325,50,50),2)



    #CLEAR OPTION
    pygame.draw.rect(win,(255,255,255),(width+25,height-200,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,height-200,50,25),2)

    text = font.render("Clear", True, (0,0,0))
    win.blit(text, (width+25+10,height-200+3))
    
    #OPEN OPTION
    pygame.draw.rect(win,(255,255,255),(width+25,height-150,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,height-150,50,25),2)

    text = font.render("Open", True, (0,0,0))
    win.blit(text, (width+25+10,height-150+3))
    
    #SAVE OPTION
    pygame.draw.rect(win,(255,255,255),(width+25,height-100,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,height-100,50,25),2)

    text = font.render("Save", True, (0,0,0))
    win.blit(text, (width+25+10,height-100+3))
    
    #QUIT OPTION
    pygame.draw.rect(win,(255,255,255),(width+25,height-50,50,25))
    pygame.draw.rect(win,(0,0,0),(width+25,height-50,50,25),2)

    text = font.render("Quit", True, (0,0,0))
    win.blit(text, (width+25+10,height-50+3))
    
    pygame.display.update()

colors = []
for i in range(width//size):
    for j in range(height//size):
        colors.append([255,255,255])

r = 0
g = 0
b = 0
current_color = [255,0,0]
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    current_color = [r,g,b]
    draw_win(win,current_color,colors)
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        if cur[0] < width:
            x = (cur[0]//size)
            y = (cur[1]//size)
            colors[x*(width//size)+y] = current_color
            
        elif cur[0] > width:
            x = cur[0]
            y = cur[1]
            if x > width+50 and x < width+50+25 and y > 25 and y < 25+25:
                if r < 255:
                    r += 1
            elif x > width+50 and x < width+50+25 and y > 25+25 and y < 25+25+25:
                if r > 0:
                    r -= 1
            elif x > width+50 and x < width+50+25 and y > 25+100 and y < 25+100+25:
                if g < 255:
                    g += 1
            elif x > width+50 and x < width+50+25 and y > 25+25+100 and y < 25+25+100+25:
                if g > 0:
                    g -= 1
            elif x > width+50 and x < width+50+25 and y > 25+200 and y < 25+200+25:
                if b < 255:
                    b += 1
            elif x > width+50 and x < width+50+25 and y > 25+25+200 and y < 25+25+200+25:
                if b > 0:
                    b -= 1

            elif x > width+25 and x < width+25+50 and y > height-200 and y < height-200+25:
                colors = []
                for i in range(width//size):
                    for j in range(height//size):
                        colors.append([255,255,255])

            elif x > width+25 and x < width+25+50 and y > height-150 and y < height-150+25:
                colors = []
                colors = openfile()

            elif x > width+25 and x < width+25+50 and y > height-100 and y < height-100+25:
                savefile(colors)

            elif x > width+25 and x < width+25+50 and y > height-50 and y < height-50+25:
                run = False
            
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
exit()

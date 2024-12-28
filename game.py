import os
import random
import pgzrun
from pgzhelper import *

#Window POS Centered
os.environ["SDL_VIDEO_CENTERED"] = "1"

WIDTH=1000
HEIGHT=600

#title
TITLE = "Little soldier"

#_____________________________________ main Menu _____________________________________#

#main menu background
main_menu_bg = Actor("main_nemu_bg")

#exit background
exit_bg = Actor("exit_bg",(500,300))

#game over bg
game_over_bg = Actor("game_over_img",(500,300))

#main menu player idle
player_idle = Actor("player_idle0",(400,150))
player_idle.images = ["player_idle0","player_idle1","player_idle2","player_idle3","player_idle4"]
player_idle.fps = 10

#main menu white ghost
main_menu_white_ghost = Actor("ghost1_run0",(600,150))
main_menu_white_ghost.images = ["idle_ghost0","idle_ghost1","idle_ghost2","idle_ghost3","idle_ghost4"]
main_menu_white_ghost.fps = 10

#main menu gotoku
gotoku_idle = Actor("gotoku_idle0",(550,150))
gotoku_idle.images = ["gotoku_idle0","gotoku_idle1","gotoku_idle2","gotoku_idle3","gotoku_idle4"]
gotoku_idle.fps = 10

#main menu onre
onre_idle = Actor("onre_idle0",(500,150))
onre_idle.images = ["onre_idle0","onre_idle1","onre_idle2","onre_idle3","onre_idle4","onre_idle5"]
onre_idle.fps = 10

#main menu buttons
main_menu_buttons = Actor("button_bg",(500,300))

#buttons
start_button = Actor("button",(500,250))
tutorial_button = Actor("button2",(500,320))
credits_button = Actor("button",(500,390))
exit_button = Actor("button2",(500,460))
main_menu_back_button = Actor("back",(50,50))
main_menu_back_button.scale = 0.8
exit_button_no = Actor("button2",(630,370))
exit_button_no.scale = 0.8
exit_button_yes = Actor("button",(370,370))
exit_button_yes.scale = 0.8

game_over_button_replay = Actor("button2",(500,450))
game_over_button_replay.scale = 0.8
game_over_button_mainmenu = Actor("button",(500,500))
game_over_button_mainmenu.scale = 0.8

#tutorial_img
tutorial_img = Actor("tutorial_img")

main_menu = True
start_game = False
tutorial_page = False
credits_page = False
exit = False

#_____________________________________ in game _____________________________________#
#background
background = Actor("bg",(500,300))
background.images = ["bg"]
background.fps = 13

#ground
ground = Actor("ground",(500,585))
ground.images = ["ground"]
ground.fps = 13

##### icons #####
#kill icon
kills_icon = Actor("kills",(950,30))
kills_icon.scale = 1.5

#ammo icon
ammo_icon = Actor("ammo",(950,70))
ammo_icon.scale = 1.5

#main menu icon
main_menu_icon = Actor("main_menu_icon",(50,50))
main_menu_icon.scale = 0.8

##### player #####
#run
player_run = Actor("player_run0",(300,540))
player_run.images = ["player_run0","player_run1","player_run2","player_run3","player_run4","player_run5"]
player_run.fps = 13

#ammo
ammo_rifle = Actor("ammo_rifle0",(600,530))
ammo_rifle.images = ["ammo_rifle0","ammo_rifle1"]
ammo_rifle.scale = 1.3
ammo_rifle.fps = 2

#bullet
bullet = Actor("bullet",(player_run.x,player_run.y))

##### enemies images #####
#onre
onre = Actor("onre0",(random.randint(1050,3000),540))
onre.images = ["onre0","onre1","onre2","onre3","onre4","onre5","onre6"]
onre.fps = 13

#white ghost
white_ghost = Actor("ghost1_run0",(random.randint(1050,3000),540))
white_ghost.images = ["ghost1_run0","ghost1_run1","ghost1_run2","ghost1_run3","ghost1_run4"]
white_ghost.fps = 13

#gotoku
gotoku = Actor("gotoku0",(random.randint(1050,3000),540))
gotoku.images = ["gotoku0","gotoku1","gotoku2","gotoku3","gotoku4","gotoku5","gotoku6"]
gotoku.fps = 13

#spike
spike = Actor("spike",(random.randint(1050,2000),560))
spike.scale = 0.7

#player run
idle = True
run = False

#jump
velocity_y = 0
gravity = 0.6

#bullet
ammo = 20
bullets = []
shoot = False

kills = 0
level = 1

#game status
lose =False
game_over = False
win = False


enemies_speed = 5
bg_speed = 2

repaly = False


if main_menu:
    music.play("mainmenu")


mouse_y=0,0
def on_mouse_move(pos):
    global mouse_y
    mouse_y = pos


def update():
    global win,repaly,enemies_speed,bg_speed, start_game,level,game_over,shoot,ammo_rifle,lose,kills ,bullet,bullets,velocity_y,bullet,bullet , ammo , run , idle , player_idle,start_color,tutorial_color,credits_color,exit_color,exit_color_no,exit_color_yes

    if main_menu == False and start_game:
        music.stop()
    if lose:
        music.play("mainmenu")



#_____________________________________ main Menu _____________________________________#
    if main_menu:
        player_idle.animate()
        gotoku_idle.animate()
        gotoku_idle.flip_x = True
        onre_idle.animate()
        onre_idle.flip_x = True
        main_menu_white_ghost.animate()
        main_menu_white_ghost.flip_x = True

        
        #main menu button texts color
        if start_button.collidepoint(mouse_y):
            start_color = "red"

        elif tutorial_button.collidepoint(mouse_y):
            tutorial_color = "red"

        elif credits_button.collidepoint(mouse_y):
            credits_color = "red"

        elif exit_button.collidepoint(mouse_y):
            exit_color = "red"

        else:
            exit_color = "white"
            start_color = "white"
            tutorial_color = "white"
            credits_color = "white"
            exit_color = "white"

        if exit_button_no.collidepoint(mouse_y):
            exit_color_no = "red"

        elif exit_button_yes.collidepoint(mouse_y):
            exit_color_yes = "red"

        else:
            exit_color_no  = "white"
            exit_color_yes = "white"


#_____________________________________ in game _____________________________________#
    if kills == 10:
        level = 2
        enemies_speed = 6
        bg_speed = 2
        
        
    elif kills == 20:
        level = 3
        enemies_speed = 7
        bg_speed = 3


    elif kills == 30:
        level = 4
        enemies_speed = 8
        bg_speed = 4


    elif kills == 40:
        game_over = True
        win = True
        lose = False
        start_game = False


    if repaly == True or main_menu == True:
        kills = 0
        level = 1
        enemies_speed = 4
        bg_speed = 1
        ammo = 20
        onre.x = random.randint(1050,3000)
        white_ghost.x = random.randint(1050,3000)
        gotoku.x = random.randint(1050,3000)
        spike.x = random.randint(1050,2000)


    if start_game:
        move_bullets()
        get_ammo()
        repaly = False

        #kill enemies
        #onre killed
        if bullet.colliderect(onre):
            kills += 1
            bullet.y = 650
            sounds.hit.play()
            onre.x = random.randint(1050,3000)
            
        #white ghost killed
        if bullet.colliderect(white_ghost):
            kills += 1
            bullet.y = 650
            sounds.hit.play()
            white_ghost.x = random.randint(1050,3000)
            
        #gotoku killed
        if bullet.colliderect(gotoku):
            kills += 1
            bullet.y = 650
            sounds.hit.play()
            gotoku.x = random.randint(1050,3000)
        
        #moving background
        background.animate()
        background.x -= bg_speed
        if background.x <= -1300:
            background.x = 1000

        #moving ground
        ground.animate()
        ground.x -= bg_speed
        if ground.x <= -1000:
            ground.x = 1000

        #moving ammo 
        ammo_rifle.x -= 3

        ##### Enemies #####
        #white ghost
        white_ghost.animate()
        white_ghost.flip_x = True
        white_ghost.x -= enemies_speed
        if white_ghost.x < 0:
            white_ghost.x = random.randint(1050,3000)
        if white_ghost.colliderect(player_run):
            white_ghost.x = random.randint(1050,3000)
            lose = True
            win = False
            game_over = True

        #onre
        onre.animate()
        onre.flip_x = True
        onre.x -= enemies_speed
        if onre.x < 0:
            onre.x = random.randint(1050,3000)
        if onre.colliderect(player_run):
            onre.x = random.randint(1050,3000)
            lose = True
            win = False
            game_over = True

        #onre
        gotoku.animate()
        gotoku.flip_x = True
        gotoku.x -= enemies_speed
        if gotoku.x < 0:
            gotoku.x = random.randint(1050,3000)
        if gotoku.colliderect(player_run):
            gotoku.x = random.randint(1050,3000)
            lose = True
            win = False
            game_over = True

        #spike
        spike.x -= enemies_speed
        if spike.x <= -50:
            spike.x = random.randint(1050,2000)
        if spike.colliderect(player_run):
            spike.x = random.randint(1050,2000)
            lose = True
            win = False
            game_over = True


        ##### Player Move #####

        run = True
        idle = False
        player_run.animate()

        #jump
        if keyboard.up and player_run.y >= 540:
            velocity_y = -15
            sounds.jump.play()

        player_run.y += velocity_y
        velocity_y += gravity
        if player_run.y > 540:
            velocity_y = 0
            player_run.y = 540


#get ammo
def get_ammo():
    global ammo
    ammo_rifle.animate()
    if player_run.colliderect(ammo_rifle):
        sounds.get_ammo.play()
        ammo += random.randint(1,10)
        ammo_rifle.x = random.randint(1050,2000)



##### shoot #####
def on_key_down(key):
    global ammo,player_run,bullet
    if start_game:
        if key == keys.SPACE and len(bullets) < ammo:
            bullet = Actor("bullet", pos=(player_run.x, player_run.y))
            bullets.append(bullet)
            sounds.shoot.play()
            ammo -= 1

def move_bullets():
    if start_game:
        for bullet in bullets:
            bullet.x = bullet.x + 20
            if bullet.x > 1000:
                bullet.pos = player_run.pos
                bullets.remove(bullet)

 
def draw():
    global main_menu,start_color,start_game,kills,level,lose,win,game_over,exit_color_no,exit_color_yes
#_____________________________________ in menu _____________________________________#

    if game_over:
        main_menu = False
        start_game = False
        screen.clear()
        main_menu_bg.draw()
        game_over_bg.draw()
        game_over_button_mainmenu.draw()
        game_over_button_replay.draw()

        if lose:
            screen.draw.text("You Lose !",fontname="pixel" , color = "red" , center = (500,120) , fontsize = 40)
        if win:
            screen.draw.text("You Win !",fontname="pixel" , color = "#22b34a" , center = (500,120) , fontsize = 30)


        screen.draw.text("kills :",fontname="pixel" , color = "red" , center = (500,200) , fontsize = 25)
        screen.draw.text(f"{kills}",fontname="pixel" , color = "red" , center = (500,240) , fontsize = 25)
        screen.draw.text(f"Level :",fontname="pixel" , color = "red" , center = (500,300) , fontsize = 25)
        screen.draw.text(f"{level}",fontname="pixel" , color = "red" , center = (500,345) , fontsize = 25)

        screen.draw.text("Replay",fontname="pixel" , color = "white" , center = (500,450) , fontsize = 20)
        screen.draw.text("Mian Mneu",fontname="pixel" , color = "white" , center = (500,500) , fontsize = 20)
        

    ##### main menu #####
    if main_menu:
        start_game = False
        game_over = False
        lose = False
        win = False
        screen.clear()
        main_menu_bg.draw()
        main_menu_buttons.draw()
        player_idle.draw()
        gotoku_idle.draw()
        onre_idle.draw()
        main_menu_white_ghost.draw()
        #main menu buttons
        start_button.draw()
        tutorial_button.draw()
        credits_button.draw()
        exit_button.draw()
        

        #main menu texts
        screen.draw.text("Start",fontname="pixel" , color = f"{start_color}" , center = (500,250) , fontsize = 30)
        screen.draw.text("Tutorial",fontname="pixel" , color = f"{tutorial_color}" , center = (500,320) , fontsize = 30)
        screen.draw.text("Credits",fontname="pixel" , color = f"{credits_color}" , center = (500,390) , fontsize = 30)
        screen.draw.text("Exit Game",fontname="pixel" , color = f"{exit_color}" , center = (500,460) , fontsize = 30)
        screen.draw.text("Version 1.5",fontname="pixel" , color = "white" , center = (920,570) , fontsize = 20)


        ##### Tutorial page #####
        if tutorial_page:
            screen.clear()
            main_menu = False
            main_menu_bg.draw()
            tutorial_img.draw()
            main_menu_back_button.draw()


        ##### credits page #####
        if credits_page:
            screen.clear()
            main_menu = False
            main_menu_back_button.draw()
            screen.draw.text("Game Made By Abolfazl Mazarei",fontname="pixel" , color = "white" , center = (500,200) , fontsize = 40)
            screen.draw.text("instagram.com/AbolfazlMazari \n github.com/Abolfazl48",fontname="pixel" , color = "white" , center = (500,300) , fontsize = 30)

        #exit page
        if exit:
            screen.clear()
            main_menu = False
            main_menu_bg.draw()
            exit_bg.draw()
            exit_button_no.draw()
            exit_button_yes.draw()
            screen.draw.text("Are you sure ?",fontname="pixel" , color = "red" , center = (500,250) , fontsize = 30)
            screen.draw.text("NO",fontname="pixel" , color = f"{exit_color_no}" , center = (630,375) , fontsize = 28)
            screen.draw.text("YES",fontname="pixel" , color = f"{exit_color_yes}" , center = (370,375) , fontsize = 28)


#_____________________________________ in game _____________________________________#
    if start_game:
        screen.clear()
        background.draw()
        spike.draw()
        ground.draw()
        white_ghost.draw()
        player_run.draw()
        main_menu_icon.draw()
        onre.draw()
        gotoku.draw()
        ammo_rifle.draw()
        

        ##### icons #####
        ammo_icon.draw()
        kills_icon.draw()

        ##### Text #####
        screen.draw.text(f"{kills}",fontname="pixel" , color = "red" , topright = (930,15) , fontsize = 30)
        screen.draw.text(f"{ammo}",fontname="pixel" , color = "red" , topright = (930,55) , fontsize = 30)
        screen.draw.text(f"Level : {level}",fontname="pixel" , color = "red" , topright = (200,30) , fontsize = 25)

            ##### Player #####
        for bullet in bullets:
            bullet.draw()


#_____________________________________ left click _____________________________________#

#left click
def on_mouse_down(pos, button):
    global credits_page,main_menu,tutorial_page,exit,start_game,game_over,repaly
    if button == mouse.LEFT:


        if start_game:
            if main_menu_icon.collidepoint(pos):
                sounds.main_menu_button.play()
                start_game = False
                main_menu = True

        if main_menu:
        #main menu button click sound
            if start_button.collidepoint(pos):
                sounds.main_menu_button.play()
                start_game = True
                main_menu = False
            if tutorial_button.collidepoint(pos):
                sounds.main_menu_button.play()
                tutorial_page = True
            if credits_button.collidepoint(pos):
                sounds.main_menu_button.play()
                credits_page = True
            if exit_button.collidepoint(pos):
                sounds.main_menu_button.play()
                exit = True

        #exit 
        if exit:       
            if exit_button_no.collidepoint(pos):
                sounds.main_menu_button.play()
                main_menu = True
                exit =+ False
            if exit_button_yes.collidepoint(pos):
                sounds.main_menu_button.play()
                pgzrun.sys.exit()

        #credits
        if credits_page == True or tutorial_page == True or exit == True:
            if main_menu_back_button.collidepoint(pos):
                credits_page = False
                tutorial_page = False
                main_menu = True
                sounds.main_menu_button.play()


        #game over
        if game_over:
            if game_over_button_mainmenu.collidepoint(pos):
                sounds.main_menu_button.play()
                start_game = False
                game_over = False
                main_menu = True
                onre.x = random.randint(1050,6000)
                white_ghost.x = random.randint(1050,3000)
                spike.x = random.randint(1050,2000)
            if game_over_button_replay.collidepoint(pos):
                sounds.main_menu_button.play()
                game_over = False
                main_menu = False
                start_game = True
                repaly = True
                onre.x = random.randint(1050,6000)
                white_ghost.x = random.randint(1050,3000)
                spike.x = random.randint(1050,2000)

pgzrun.go()
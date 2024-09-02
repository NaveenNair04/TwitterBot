"""Module containing main structure and menus of the game"""

#Modules
import pygame
import pygame_gui
import os
import game
import mysql.connector as sql
import sql_connect
pygame.init()

#Variables
start=True
pygame.display.set_caption('Quick Start')
clock = pygame.time.Clock()

#Functions

#Starting menu
def screen1():
    
    #defining objects that to handle menu
    window_surface1 = pygame.display.set_mode((1000, 500))
    image1 = pygame.image.load(os.path.join('images','sasuke2.jpg'))
    image1 = pygame.transform.scale(image1,(1000,500))
    background1 = pygame.Surface((1000, 500))
    background1.blit(image1,(0,0))
    manager1 = pygame_gui.UIManager((1000, 500),'2000sPastel.json')
    
    #Defining buttons
    
    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Start',
                                                manager=manager1)
    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (100, 50)),
                                               text='Quit',
                                               manager=manager1)
    
    #Pygame loop
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            #end program if closed
            if event.type == pygame.QUIT:
                pygame.quit()
                
            #checking for button click    
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        start=False
                        screen2()
                        
                    if event.ui_element == quit_button:
                        pygame.quit()

            manager1.process_events(event)

        manager1.update(time_delta)
        window_surface1.blit(background1, (0, 0))
        manager1.draw_ui(window_surface1)

        pygame.display.update()

#Menu to login, play as guest or open leaderboard
def screen2():
    
    image2 = pygame.image.load(os.path.join('images','sasuke3.jpg'))
    image2 = pygame.transform.scale(image2,(1000,500))
    window_surface2 = pygame.display.set_mode((1000, 500))
    background2 = pygame.Surface((1000, 500))
    background2.blit(image2,(0,0))
    manager2 = pygame_gui.UIManager((1000, 500),'2000sPastel.json')
    
    login_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Login',
                                                manager=manager2)
    leaderboard_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 275), (100, 50)),
                                                      text='Leaderboard',
                                                      manager=manager2)
    playasguest_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 375), (150, 50)),
                                                      text='Play As Guest',
                                                      manager=manager2)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 10), (100, 50)),
                                                text='Back',
                                                manager=manager2)

    while True:
        back = False
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == login_button:
                        login_screen2()
                    if event.ui_element == leaderboard_button:
                        sql_connect.leaderboard()
                    if event.ui_element == playasguest_button:
                        game.main()     
                    if event.ui_element == back_button:
                        screen1()
                        
            manager2.process_events(event)

        manager2.update(time_delta)

        window_surface2.blit(background2, (0, 0))
        manager2.draw_ui(window_surface2)

        pygame.display.update()

#Menu to login into account or create account
def login_screen2():
    window_surface3 = pygame.display.set_mode((1000, 500))
    background3 = pygame.Surface((1000, 500))
    background3.fill(pygame.Color('#78dcdf'))
    manager3 = pygame_gui.UIManager((1000, 500),'2000sPastel.json')
    
    #Establishing sql connection
    
    user_text=''
    mydb=sql.connect(
        user="root",
        password="C3a#palmavenuegm",
        host="127.0.0.1",
        database="game"    
        )
    cursor = mydb.cursor()
    cursor.execute("select username from accounts")
    result = cursor.fetchall()
    mydb.close()
    
    add_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 400), (100, 50)),
                                                text='Add User',
                                                manager=manager3)
    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 10), (100, 50)),
                                                text='Back',
                                                manager=manager3)
    
    #Defining buttons based on number of accounts
    
    if len(result)>0:
        acc1_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 50), (150, 50)),
                                                          text=result[0][0],
                                                          manager=manager3)
    if len(result)>1:
        acc2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 150), (150, 50)),
                                                          text=result[1][0],
                                                          manager=manager3)
    if len(result)>2:
        acc3_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 250), (150, 50)),
                                                          text=result[2][0],
                                                          manager=manager3)
    if len(result)>3:
        acc4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 350), (150, 50)),
                                                          text=result[3][0],
                                                          manager=manager3)
    if len(result)>4:
        acc5_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (150, 50)),
                                                          text=result[4][0],
                                                          manager=manager3)
        
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == add_button:
                        sql_connect.add_account_username()
                    if len(result)>0 and event.ui_element == acc1_button:
                        sql_connect.display_pass(0, user_text,result)
                    if len(result)>1 and event.ui_element == acc2_button:
                        sql_connect.display_pass(1, user_text,result)
                    if len(result)>2 and event.ui_element == acc3_button:
                        sql_connect.display_pass(2, user_text,result)
                    if len(result)>3 and event.ui_element == acc4_button:
                        sql_connect.display_pass(3, user_text,result)
                    if len(result)>4 and event.ui_element == acc5_button:
                        sql_connect.display_pass(4, user_text,result)
                    if event.ui_element == back_button:
                        screen2()
                        
            manager3.process_events(event)

        manager3.update(time_delta)

        window_surface3.blit(background3, (0, 0))
        manager3.draw_ui(window_surface3)

        pygame.display.update()

#check if database 'game' exists if not, creates database 
sql_connect.check_databases()

if start:
    screen1()
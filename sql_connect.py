"""Module containing all SQL connectivity."""

# Modules
import mysql.connector as sql
import pygame_gui
import pygame
import game
import re

pygame.init()

clock = pygame.time.Clock()
user_text = ''

# Functions

# Check whether database 'game' exists and create new database if missing
def check_databases():
    mydb = sql.connect(
        user="root",
        password="C3a#palmavenuegm",
        host="127.0.0.1",
        database=""
    )
    cursor = mydb.cursor()
    cursor.execute('show databases')
    recs = cursor.fetchall()

    # Creating database if non-existent
    if ('game',) not in recs:
        cursor.execute('create database game')
        cursor.execute(
            'create table accounts(username varchar(20), password varchar(20) not null, highscore int(10), primary key(username))')
        mydb.commit()

    mydb.close()

# Displays all accounts within login menu
def display_pass(acc, user_text, result):
    background4 = pygame.Surface((1000, 500))
    background4.fill(pygame.Color('#78dcdf'))
    manager4 = pygame_gui.UIManager((1000, 500), '2000sPastel.json')
    window_surface4 = pygame.display.set_mode((1000, 500))

    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((850, 10), (100, 50)),
        text='Back',
        manager=manager4
    )

    if acc == 0:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=result[0][0],
            manager=manager4
        )
    if acc == 1:
        acc2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 150), (150, 50)),
            text=result[1][0],
            manager=manager4
        )
    if acc == 2:
        acc3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 250), (150, 50)),
            text=result[2][0],
            manager=manager4
        )
    if acc == 3:
        acc4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 350), (150, 50)),
            text=result[3][0],
            manager=manager4
        )
    if acc == 4:
        acc5_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 450), (150, 50)),
            text=result[4][0],
            manager=manager4
        )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Getting keyboard input from user
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # Get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]

                # Unicode standard is used for string formation
                elif event.key == pygame.K_RETURN:
                    check_pass(acc, user_text)

                else:
                    user_text += event.unicode

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        from menu import login_screen2
                        login_screen2()

            manager4.process_events(event)

        passbox = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300, 50 + acc * (100)), (600, 50)),
            text=user_text,
            manager=manager4
        )
        manager4.update(time_delta)
        window_surface4.blit(background4, (0, 0))
        manager4.draw_ui(window_surface4)
        pygame.display.update()

# Checking if password matches entered value
def check_pass(acc, user_text):
    mydb = sql.connect(
        user="root",
        password="C3a#palmavenuegm",
        host="127.0.0.1",
        database="game"
    )

    # Fetching password
    match = False
    cursor = mydb.cursor()
    cursor.execute('select password from accounts')
    recs = cursor.fetchall()

    # Matching password
    if (user_text,) == recs[acc]:
        match = True
    else:
        match = False

    if match:
        game.main(acc)
    mydb.close()

# Menu to add account username
def add_account_username():
    background5 = pygame.Surface((1000, 500))
    background5.fill(pygame.Color('#78dcdf'))
    manager5 = pygame_gui.UIManager((1000, 500), '2000sPastel.json')
    window_surface5 = pygame.display.set_mode((1000, 500))
    username = ''
    user_warning = ''

    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((850, 10), (100, 50)),
        text='Back',
        manager=manager5
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        userbox = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 300), (150, 50)),
            text='Username:' + username,
            manager=manager5
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]

                elif event.key == pygame.K_RETURN:
                    add_account_password(username)

                else:
                    username += event.unicode

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        from menu import login_screen2
                        login_screen2()

            manager5.process_events(event)

        manager5.update(time_delta)
        window_surface5.blit(background5, (0, 0))
        manager5.draw_ui(window_surface5)
        pygame.display.update()

# Menu to add account password
def add_account_password(username):
    background6 = pygame.Surface((1000, 500))
    background6.fill(pygame.Color('#78dcdf'))
    manager6 = pygame_gui.UIManager((1000, 500), '2000sPastel.json')
    window_surface6 = pygame.display.set_mode((1000, 500))
    password = ''
    pass_warning = 'Password must be at least 10 characters long and must include a Capital letter and number.'

    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((850, 10), (100, 50)),
        text='Back',
        manager=manager6
    )

    while True:
        time_delta = clock.tick(60) / 1000.0
        passbox = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300, 300), (600, 50)),
            text='Password:' + password,
            manager=manager6
        )

        warningbox1 = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 200), (800, 50)),
            text=pass_warning,
            manager=manager6
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        add_account_username()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    password = password[:-1]

                elif event.key == pygame.K_RETURN:
                    if valid_pass(password) == 0:
                        print('Password accepted.')
                        mydb = sql.connect(
                            user="root",
                            password="C3a#palmavenuegm",
                            host="127.0.0.1",
                            database="game"
                        )
                        cursor = mydb.cursor()
                        command = 'insert into accounts values (%s,%s,%s)'
                        values = (username, password, 0)
                        cursor.execute(command, values)
                        mydb.commit()
                        mydb.close()
                        pygame.quit()
                        import menu
                    else:
                        print('Invalid password.')

                else:
                    password += event.unicode

            manager6.process_events(event)

        manager6.update(time_delta)
        window_surface6.blit(background6, (0, 0))
        manager6.draw_ui(window_surface6)

        pygame.display.update()

# Checking whether password is following required constraints    
def valid_pass(password):
    flag = 0
    while True:
        if len(password) < 10:
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid Password")
            break

    return flag

# Displays game leaderboard
def leaderboard():
    background7 = pygame.Surface((1000, 500))
    background7.fill(pygame.Color('#78dcdf'))
    manager7 = pygame_gui.UIManager((1000, 500), '2000sPastel.json')
    window_surface7 = pygame.display.set_mode((1000, 500))

    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((850, 10), (100, 50)),
        text='Back',
        manager=manager7
    )

    mydb = sql.connect(
        user="root",
        password="C3a#palmavenuegm",
        host="127.0.0.1",
        database="game"
    )
    cursor = mydb.cursor()
    cursor.execute('select username,highscore from accounts order by highscore desc')
    recs = cursor.fetchall()

    # Displaying accounts and highscores on screen
    acc_num = len(recs)

    if acc_num == 1:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=recs[0][0] + '      ' + str(recs[0][1]),
            manager=manager7
        )
    if acc_num == 2:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=recs[0][0] + '      ' + str(recs[0][1]),
            manager=manager7
        )
        acc2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 150), (150, 50)),
            text=recs[1][0] + '      ' + str(recs[1][1]),
            manager=manager7
        )
    if acc_num == 3:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=recs[0][0] + '      ' + str(recs[0][1]),
            manager=manager7
        )
        acc2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 150), (150, 50)),
            text=recs[1][0] + '      ' + str(recs[1][1]),
            manager=manager7
        )
        acc3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 250), (150, 50)),
            text=recs[2][0] + '      ' + str(recs[2][1]),
            manager=manager7
        )
    if acc_num == 4:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=recs[0][0] + '      ' + str(recs[0][1]),
            manager=manager7
        )
        acc2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 150), (150, 50)),
            text=recs[1][0] + '      ' + str(recs[1][1]),
            manager=manager7
        )
        acc3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 250), (150, 50)),
            text=recs[2][0] + '      ' + str(recs[2][1]),
            manager=manager7
        )
        acc4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 350), (150, 50)),
            text=recs[3][0] + '      ' + str(recs[3][1]),
            manager=manager7
        )
    if acc_num == 5:
        acc1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 50), (150, 50)),
            text=recs[0][0] + '      ' + str(recs[0][1]),
            manager=manager7
        )
        acc2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 150), (150, 50)),
            text=recs[1][0] + '      ' + str(recs[1][1]),
            manager=manager7
        )
        acc3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 250), (150, 50)),
            text=recs[2][0] + '      ' + str(recs[2][1]),
            manager=manager7
        )
        acc4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 350), (150, 50)),
            text=recs[3][0] + '      ' + str(recs[3][1]),
            manager=manager7
        )
        acc5_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((100, 450), (150, 50)),
            text=recs[4][0] + '      ' + str(recs[4][1]),
            manager=manager7
        )

    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        from menu import login_screen2
                        login_screen2()

            manager7.process_events(event)

        manager7.update(time_delta)
        window_surface7.blit(background7, (0, 0))
        manager7.draw_ui(window_surface7)
        pygame.display.update()

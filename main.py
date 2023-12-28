import pygame, random
import button

pygame.init()

SW, SH = 500, 700

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("ROCK PAPER SCISSORS")
font = pygame.font.SysFont('Calibri', 30)
font2 = pygame.font.SysFont('Calibri', 20)
clock = pygame.time.Clock()

# robot image
robot_img = pygame.image.load('./images/robot.png').convert_alpha()
robotImg_Scaled = pygame.transform.scale(robot_img, (120, 100))
robotImg_Rect = robotImg_Scaled.get_rect()
robotImg_Rect.center = ((SW/2),230)

# user's options img -> button
scissors_img = pygame.image.load('./images/scissors.png').convert_alpha()
rock_img = pygame.image.load('./images/rock.png').convert_alpha()
paper_img = pygame.image.load('./images/paper.png').convert_alpha()

rock_button = button.Button(90, 410, rock_img, 0.04)
paper_button = button.Button(200, 410, paper_img, 0.06)
scissors_button = button.Button(320, 410, scissors_img, 0.045)

# all the text within game

# displays the winner
class Winner:
    def __init__(self):
        self.font = pygame.font.SysFont('Calibri', 30)

    def user_wins(self):
        text = self.font.render("YOU WON", True, '#003554')
        text_rect = text.get_rect(center = (SW/2,SH/2))
        return screen.blit(text, text_rect)

    def ai_wins(self):
        text = self.font.render("YOU LOST", True, '#003554')
        text_rect = text.get_rect(center = (SW/2,SH/2))
        return screen.blit(text, text_rect)

    def tie(self):
        text = self.font.render("IT'S A TIE", True, '#003554')
        text_rect = text.get_rect(center = (SW/2,SH/2))
        return screen.blit(text, text_rect)

# displays each player's choice
class Choice:
    def __init__(self):
        self.font = pygame.font.SysFont('Calibri', 30)
    
    def ai_text(self, ai_choice):
        ai = self.font.render(f'Robot chose {ai_choice.upper()}', True, '#003554')
        ai_text_rect = ai.get_rect(center = (SW/2,130))
        return screen.blit(ai, ai_text_rect)

    def rock_text(self):
        user_text = self.font.render("You chose ROCK", True, '#003554')
        user_text_rect = user_text.get_rect(center = (SW/2,570))
        return screen.blit(user_text, user_text_rect)

    def paper_text(self):
        user_text = self.font.render("You chose PAPER", True, '#003554')
        user_text_rect = user_text.get_rect(center = (SW/2,570))
        return screen.blit(user_text, user_text_rect)

    def scissors_text(self):
        user_text = self.font.render("You chose SCISSORS", True, '#003554')
        user_text_rect = user_text.get_rect(center = (SW/2,570))
        return screen.blit(user_text, user_text_rect)

# displays each player's scores
class ScoreBoard:
    def __init__(self):
        self.font = pygame.font.SysFont('Calibri', 30)
        self.font2 = pygame.font.SysFont('Calibri', 20)
    
    def aiScore_text(self, ai_score):
        aiScore = self.font.render(f'Robot: {ai_score}', True, '#003554')
        aiScore_rect = aiScore.get_rect(center = (75,30))
        return screen.blit(aiScore, aiScore_rect)

    def userScore_text(self, user_score):
        userScore = self.font.render(f'You: {user_score}', True, '#003554')
        userScore_rect = userScore.get_rect(center = (430,30))
        return screen.blit(userScore, userScore_rect)

# text for next round or restarting the game
def next_round():
    h1_font = pygame.font.SysFont('Calibri', 20)
    h2_font = pygame.font.SysFont('Calibri', 15)
    h1_text = h1_font.render("Click any option to play next round!", True, '#003554')
    h1_text_rect = h1_text.get_rect(center = (255,650))
    h2_text = h2_font.render("or press the space button to reset", True, '#003554')
    h2_text_rect = h2_text.get_rect(center = (255,680))
    screen.blit(h1_text, h1_text_rect)
    screen.blit(h2_text, h2_text_rect)

announce_winner = Winner()
choice_display = Choice()
score_display = ScoreBoard()

# selects the ai choice
def AI_choice():
    choice = ['rock', 'paper', 'scissors']
    ai_choice = random.choice(choice)
    return ai_choice

# checks for the winner
def checkWinner(user):
    # 1: user wins/ 2: ai wins/ 3: tie
    if user == "rock":
        if ai_choice == "rock":
            winner = 3
        elif ai_choice == "paper":
            winner = 2
        elif ai_choice == "scissors":
            winner = 1
    if user == "paper":
        if ai_choice == "rock":
            winner = 1
        elif ai_choice == "paper":
            winner = 3
        elif ai_choice == "scissors":
            winner = 2
    if user == "scissors":
        if ai_choice == "rock":
            winner = 2
        elif ai_choice == "paper":
            winner = 1
        elif ai_choice == "scissors":
            winner = 3
    return winner


global user_choice

winner = 0 # 1-3 represents the winner of the round

# displays announcements
display_choices = False 
start = True

# keeps track of the number of rounds and scores
round = 0 
user_score = 0
ai_score = 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        screen.fill("#FFFFFF")
        screen.blit(robotImg_Scaled,robotImg_Rect)

        # rock button
        if rock_button.draw(screen):
            ai_choice = AI_choice() # changes the ai_choice for every click, allowing a new round to begin
            round += 1
            start = False
            display_choices = True
            user = 'rock'
            winner = checkWinner(user)

        # paper button
        if paper_button.draw(screen):
            ai_choice = AI_choice()
            round += 1
            start = False
            display_choices = True
            user = 'paper'
            winner = checkWinner(user)

        # scissors button
        if scissors_button.draw(screen):
            ai_choice = AI_choice()
            round += 1
            start = False
            user = 'scissors'
            display_choices = True
            winner = checkWinner(user)

        # choice's are displayed once the user starts the game
        if display_choices == True:
            choice_display.ai_text(ai_choice)
            if user == 'rock':
                choice_display.rock_text()
            elif user == 'paper':
                choice_display.paper_text()
            elif user == 'scissors':
                choice_display.scissors_text()

        # announces the winner depending on the integer 
        if winner == 1:
            announce_winner.user_wins()
            if round <= 1: # after round 1, the text on the bottom is erased
                next_round()
        elif winner == 2:
            announce_winner.ai_wins() 
            if round <= 1:
                next_round()
        elif winner == 3:
            announce_winner.tie()
            if round <= 1:
                next_round()

        # displays the score
        score_display.aiScore_text(ai_score)
        score_display.userScore_text(user_score)

        # displays the beginnig page and is erased once the user starts the game by clicking on a button
        if start == True:
            title = font.render("ROCK PAPER SCISSORS", True, '#003554')
            title_rect = title.get_rect(center = (SW/2,330))
            caption = font2.render("click on your options below", True, '#003554')
            caption_rect = caption.get_rect(center = (SW/2,360))
            screen.blit(title, title_rect)
            screen.blit(caption, caption_rect)
        
        # every click adds a point depending on the winner
        if event.type == pygame.MOUSEBUTTONDOWN:
            if winner == 1:
                user_score += 1
            elif winner == 2:
                ai_score += 1

        if event.type == pygame.KEYDOWN:
            round = 0 
            winner = 0
            display_choices = False
            start = True
            user_score = 0
            ai_score = 0

    pygame.display.update()
    clock.tick(60)
pygame.quit()
import datetime
from random import choice, randint
import pygame
from sys import exit


pygame.init()
screen=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
game_active=False
score=0
lagre_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',40) 
medium_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',20)
small_font=pygame.font.Font('font/JosefinSans-BoldItalic.ttf',10)
start_time=0
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN=(124,252,0)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0,128,128)
COLOR_A=BLACK
COLOR_B=BLACK
COLOR_C=BLACK
COLOR_D=BLACK
check=0

#ques list
class content:
    def __init__(self,ques,anwA,anwB,anwC,anwD,res) -> None:
        self.ques=ques
        self.anwA=anwA
        self.anwB=anwB
        self.anwC=anwC
        self.anwD=anwD
        self.res=res
ques_lst=[]
content1=content('What is 5*5 ?','A: 15','B: 20','C: 25','D: 30','C')
content2=content('What is 5*4 ?','A: 15','B: 20','C: 25','D: 30','B')
ques_lst.append(content1)
ques_lst.append(content2)
ques_index=0

        
#intro
logo_game=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.jpg').convert_alpha()
logo_game_rect=logo_game.get_rect(center=(400,150))
intro_mes=lagre_font.render('Ring the golden bell !!!',True,('#0066FF'))
intro_mes_rect=intro_mes.get_rect(center=(400,300))
play=medium_font.render('Press space to begin.',True,('#0066FF'),)
play_rect=intro_mes.get_rect(center=(550,350))

#in game
#achievement
# achievement_0=pygame.image.load('Millionair_Images/Picture0.png').convert_alpha()
# achievement_1=pygame.image.load('Millionair_Images/Picture1.png').convert_alpha()
# achievement_2=pygame.image.load('Millionair_Images/Picture2.png').convert_alpha()
# achievement_3=pygame.image.load('Millionair_Images/Picture3.png').convert_alpha()
# achievement_4=pygame.image.load('Millionair_Images/Picture4.png').convert_alpha()
# achievement_5=pygame.image.load('Millionair_Images/Picture5.png').convert_alpha()
# achievement_6=pygame.image.load('Millionair_Images/Picture6.png').convert_alpha()
# achievement_7=pygame.image.load('Millionair_Images/Picture7.png').convert_alpha()
# achievement_8=pygame.image.load('Millionair_Images/Picture8.png').convert_alpha()
# achievement_9=pygame.image.load('Millionair_Images/Picture9.png').convert_alpha()
# achievement_10=pygame.image.load('Millionair_Images/Picture10.png').convert_alpha()
# achievement_11=pygame.image.load('Millionair_Images/Picture11.png').convert_alpha()
# achievement_12=pygame.image.load('Millionair_Images/Picture12.png').convert_alpha()
# achievement_13=pygame.image.load('Millionair_Images/Picture13.png').convert_alpha()
# achievement_14=pygame.image.load('Millionair_Images/Picture14.png').convert_alpha()
# achievement_15=pygame.image.load('Millionair_Images/Picture15.png').convert_alpha()
# achievement_lst=[achievement_0,achievement_1,achievement_2,achievement_3,achievement_4,achievement_5,achievement_6,achievement_7,achievement_8,achievement_9,achievement_10,achievement_11,achievement_12,achievement_13,achievement_14,achievement_15]
# achievement_index=0
# achievement_img=achievement_lst[achievement_index]
# achievement_img=pygame.transform.rotozoom(achievement_img,0,0.6)
# achievement_rect=achievement_img.get_rect(center=(675,200))

#support
# half=pygame.image.load('Millionair_Images/jpge50.jpg').convert_alpha()
# halfX=pygame.image.load('Millionair_Images/jpge50X.jpg')
# half_lst=[half,halfX]
# half_index=0
# half_img=half_lst[half_index]
# half_rect=half_img.get_rect(center=(150,50))

# people=pygame.image.load('Millionair_Images/jpgePeople.jpg').convert_alpha()
# peopleX=pygame.image.load('Millionair_Images/jpgePeopleX.jpg').convert_alpha()
# people_lst=[people,peopleX]
# people_index=0
# people_img=people_lst[people_index]
# people_rect=people_img.get_rect(center=(300,50))

# phone=pygame.image.load('Millionair_Images/jpgePhone.jpg').convert_alpha()
# phoneX=pygame.image.load('Millionair_Images/jpgePhoneX.jpg').convert_alpha()
# phone_lst=[phone,phoneX]
# phone_index=0
# phone_img=phone_lst[phone_index]
# phone_rect=phone_img.get_rect(center=(450,50))

#decor in game
decor=pygame.image.load('Millionair_Images/pngtree-gold-ringing-christmas-bells-with-red-bow-png-image_6037900.jpg').convert_alpha()
decor=pygame.transform.rotozoom(decor,0,0.2)
decor_rect=decor.get_rect(center=(60,60))

name_header=lagre_font.render('Ring the golden bell !',True,('#0066FF'))
name_header_rect=intro_mes.get_rect(center=(400,60))



#clock
timer=pygame.image.load('Millionair_Images/red-clock-png-alarm-0.png').convert_alpha()
timer=pygame.transform.rotozoom(timer,0,0.03)
timer_rect=timer.get_rect(center=(720,60))



def display_time():
    current_time=round(pygame.time.get_ticks()/1000)-start_time
    s=format(15-current_time, "0>2,d")
    clock_surf=medium_font.render(f'00:{s}',True,'blue')
    clock_rect=clock_surf.get_rect(center=(720,60))
    screen.blit(clock_surf,clock_rect)
    return int(s)



done_yet=0
while True:
    screen.fill('white')
    
    if ques_index==len(ques_lst):
        game_active=False
        ques_index=0
        continue   
    #question
    question=lagre_font.render(f'Câu {ques_index+1}: '+ques_lst[ques_index].ques,True,('red'))
    question_rect=question.get_rect(center=(400,150))
    #answer
    answer_A=medium_font.render(ques_lst[ques_index].anwA,True,COLOR_A)
    answer_B=medium_font.render(ques_lst[ques_index].anwB,True,COLOR_B)
    answer_C=medium_font.render(ques_lst[ques_index].anwC,True,COLOR_C)
    answer_D=medium_font.render(ques_lst[ques_index].anwD,True,COLOR_D)
    answer_A_rect=answer_A.get_rect(center=(350,200))
    answer_B_rect=answer_B.get_rect(center=(350,250))
    answer_C_rect=answer_C.get_rect(center=(350,300))
    answer_D_rect=answer_D.get_rect(center=(350,350))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            
            
            exit()
        if game_active:
            if event.type== pygame.MOUSEBUTTONDOWN and done_yet==0:
                # if half_rect.collidepoint(event.pos) and half_index==0:
                #     half_index+=1
                #     half_img=half_lst[half_index]
                # if people_rect.collidepoint(event.pos) and people_index==0:
                #     people_index+=1
                #     people_img=people_lst[people_index]
                # if phone_rect.collidepoint(event.pos) and phone_index==0:
                #     phone_index+=1
                #     phone_img=phone_lst[phone_index]
                
                if answer_A_rect.collidepoint(event.pos) and ques_lst[ques_index].res=='A':
                    score+=1
                     
                    
                    
                if answer_B_rect.collidepoint(event.pos) and ques_lst[ques_index].res=='B':
                    score+=1
                     
                    
                    
                if answer_C_rect.collidepoint(event.pos) and ques_lst[ques_index].res=='C':
                    score+=1
                     
                    
                    
                if answer_D_rect.collidepoint(event.pos) and ques_lst[ques_index].res=='D':
                    score+=1
                     
                    
                    
                if answer_A_rect.collidepoint(pygame.mouse.get_pos()) or answer_B_rect.collidepoint(pygame.mouse.get_pos()) or answer_C_rect.collidepoint(pygame.mouse.get_pos()) or answer_D_rect.collidepoint(pygame.mouse.get_pos()):
                    COLOR_A=RED
                    COLOR_B=RED
                    COLOR_C=RED
                    COLOR_D=RED
                    if ques_lst[ques_index].res=='A':
                        COLOR_A=GREEN
                    if ques_lst[ques_index].res=='B':
                        COLOR_B=GREEN
                    if ques_lst[ques_index].res=='C':
                        COLOR_C=GREEN
                    if ques_lst[ques_index].res=='D':
                        COLOR_D=GREEN
                    done_yet=1
            
            if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_SPACE:
                        ques_index+=1
                        COLOR_A=BLACK
                        COLOR_B=BLACK
                        COLOR_C=BLACK
                        COLOR_D=BLACK
                        start_time=round(pygame.time.get_ticks()/1000)
                        done_yet=0
        else:
            if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_SPACE:
                        game_active=True
                        check+=1
                        score=0
                        ques_index=0
                        start_time=round(pygame.time.get_ticks()/1000)
                        COLOR_A=BLACK
                        COLOR_B=BLACK
                        COLOR_C=BLACK
                        COLOR_D=BLACK
    if game_active:
        
        screen.fill('white')
        
        pygame.draw.rect(screen,'blue',pygame.Rect(20,100,760,5),0,10)
        pygame.draw.rect(screen,'red',pygame.Rect(10,10,780,380),6,20)
        screen.blit(decor,decor_rect)
        screen.blit(name_header,name_header_rect)
        screen.blit(timer,timer_rect)
        
        screen.blit(question,question_rect)
        screen.blit(answer_A,answer_A_rect)
        screen.blit(answer_B,answer_B_rect)
        screen.blit(answer_C,answer_C_rect)
        screen.blit(answer_D,answer_D_rect)
        if display_time()<=0:
            ques_index+=1
            start_time=round(pygame.time.get_ticks()/1000)
            COLOR_A=BLACK
            COLOR_B=BLACK
            COLOR_C=BLACK
            COLOR_D=BLACK
            done_yet=0
                
    else:
        
        screen.blit(logo_game,logo_game_rect)
        screen.blit(intro_mes,intro_mes_rect)
        score_mes=medium_font.render(f'Your score: {score}',True,'#0066FF')
        score_mes_rect=score_mes.get_rect(center=(550,350))
        if check==0:
            screen.blit(play,play_rect)  
        else:
            screen.blit(score_mes,score_mes_rect)
        
    pygame.display.update() 
    clock.tick(60)
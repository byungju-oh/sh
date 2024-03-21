import pygame
import time
import sys
import random
import json
from pygame.locals import *


pygame.init()

# 색상
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (17, 124, 47)

#이미지
# titleImg = pygame.image.load("images/title.png")
scbo=pygame.image.load('images/점수판1.png')
scbu=pygame.image.load('images/점수등록.png')
scbuc=pygame.image.load('images/점수순위.png')
scoreImg=pygame.image.load('images/스코어1.png')
startImg = pygame.image.load("images/시작.png")
quitImg = pygame.image.load("images/게임종료.png")
speImg = pygame.image.load("images/필살기22.png")
ssIMG =pygame.image.load("images/스토리 1.png")
IMG =pygame.image.load("images/게임설명화면.png")
ch1 = pygame.image.load("images/ch1.png")
mainImg = pygame.image.load('images/배경화면2.png')
ch2 = pygame.image.load("images/ch2.png")
spimg= pygame.image.load("images/필살기버튼.png")
storyimg= pygame.image.load("images/스토리버튼.png")
mmImg= pygame.image.load("images/처음화면.png")
selectImg= pygame.image.load("images/캐릭터 선택창.png")
selectText = pygame.image.load("images/select.png")
back = ['d',"images/스테이지 복사본.png",'images/stage2.png']
sb=pygame.image.load('images/점수 화면.png')
miss=['images/Bullet.png','images/missile.png']
itemImg = ['images/item.png',"images/필살기 갯수.png"]
zombie1Img = pygame.image.load("images/skeleton1.png")
zombie2Img = pygame.image.load("images/skeleton2.png")
zombie3Img = pygame.image.load('images/skeleton3.png')
gg=pygame.image.load('images/game over1.png')
fscore=0
rockimg=pygame.image.load('images/좀비_2-removebg-preview.png')
explosion = pygame.image.load('images/explosion.png')
nst=['s','images/다음스테이지화면.png','images/클리어화면1.png']
#화면 설정
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("카터")
score,z1c,z2c,z3c,z4c=0,0,0,0,0
#시간
clock = pygame.time.Clock()




input_text = ""
#캐릭터
playerparms = [0,0,0,0,0,0,0,0]
serv1parms = [ch1, 6, 377, 450, 20, 20, 1.1,0]
serv2parms = [ch2,2.5,380,450,20,20, 1.001,1]


# Button 클래스
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

            

# Button2 클래스
class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms[0]=parms[0]
                playerparms[1]=parms[1]
                playerparms[2]=parms[2]
                playerparms[3]=parms[3]
                playerparms[4]=parms[4]
                playerparms[5]=parms[5]
                playerparms[6]=parms[6]
                playerparms[7]=parms[7]
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

# 배경
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))

# 플레이어 클래스
class Player:
    def __init__(self,p_img,speedIn,serv_x,serv_y,hitbox_x,hitbox_y,speedmultiplier,missile):
        self.speed = speedIn
        self.serv_x = serv_x
        self.serv_y = serv_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier
        self.missile=missile
        
# 게임 오브젝트
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
#점수 불러오기
def load_scores():
    try:
        with open("data.json", 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = []
    return scores
#
def append_to_json(data):
    try:
        with open("data.json", 'r') as file:
            current_data = json.load(file)
    except FileNotFoundError:
        current_data = []

    current_data.append(data)

    with open("data.json", 'w') as file:
        json.dump(current_data, file, indent=4)

## 점수 표시

def display_scores():
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]
    font = pygame.font.SysFont("malgungothic", 30)
    gameDisplay.fill((255, 255, 255))

    # 점수 화면에 표시
    for i, score in enumerate(sorted_scores):
        text_surface = font.render(f"{i+1}. {score['name']}: {score['score']}", True, (0, 0, 0))
        gameDisplay.blit(text_surface, (100, 250 + i * 40))

    pygame.display.update()


# # #점수 기록
def save_to_json(name):
    global fscore
    
    
    
    data = {"name": name,'score':fscore}

    append_to_json(data)
        

def scoresave():
    global input_text,z1c,z2c,z3c,z4c,fscore
    font = pygame.font.SysFont("malgungothic", 30)
    font1 = pygame.font.SysFont("malgungothic", 25)
    te=''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    save_to_json(input_text)
                    te='등록완료'
                    
                    pygame.display.update()
                    print("이름이 JSON 파일로 저장되었습니다.")
                    input_text = ""  # 입력값 초기화
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode  # 키보드 입력을 문자열에 추가
        
        gameDisplay.fill((255, 255, 255))
        backg = Background(sb, 0, 0)
        na=font1.render(te,True,red)
        gameDisplay.blit(na, (610, 350))
        z1 = font.render(str(z1c), True, red)
        z2 = font.render(str(z2c),True,red)
        gameDisplay.blit(z1, (445, 252))
        gameDisplay.blit(z2,(445,310))
        z3 = font.render(str(z3c), True, red)
        z4 = font.render(str(z4c),True,red)
        gameDisplay.blit(z3, (445, 382))
        gameDisplay.blit(z4,(445,460))
        scc = font.render(str(fscore)+'점',True,red)
        gameDisplay.blit(scc, (485, 350))
       
        
        startButton = Button(mmImg,40,450,120,70,mmImg,50,450,board)
        quitButton = Button(quitImg,40,530,120,70,quitImg,50,530,quitgame)
        # 입력 상자 표시
        # pygame.draw.rect(gameDisplay, (255, 255, 255), (600, 350, 100, 40)) #그냥상자
        # pygame.draw.rect(gameDisplay, red, (600, 350, 100, 40),2)  #외각선
        
        text_surface = font.render(input_text, True, red)  #글자써지는위치
        
        gameDisplay.blit(text_surface, (610, 350))

        pygame.display.flip()
    
# 점수 출력
def scorecounter(count,bombnum):
    font = pygame.font.SysFont("malgungothic", 30)
    text = font.render(str(count), True, black)
    bomb = font.render(str(bombnum),True,red)
    gameDisplay.blit(text, (150, 22))
    gameDisplay.blit(bomb,(450,21))        

def drawObject(obj,x,y):
    
    gameDisplay.blit(obj,(x,y))
# 오브젝트 충돌 처리
def text_objects(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()

# 충돌시 출력
def crash(st):
    # # largeText = pygame.font.SysFont("malgungothic", 46)
    # # TextSurf = largeText.render(text, True, red)
    # TextRect = TextSurf.get_rect()
    # TextRect.center = ((display_width / 2), (display_height / 2))
    # gameDisplay.blit(TextSurf, TextRect)
    backg = Background(gg, 0, 0)
    pygame.display.update()
    time.sleep(1)
    

    restart(st)


#기록확인
def board():
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:5]
    font = pygame.font.SysFont("malgungothic", 30)
    gameDisplay.fill((255, 255, 255))

    # 점수 화면에 표시
    scbo
    
    backg = Background(scbo, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i, score in enumerate(sorted_scores):
            text_surface = font.render(f"{i+1}. {score['name']}: {score['score']}", True, (0, 0, 0))
            gameDisplay.blit(text_surface, (320, 180 + i * 30))
        
        startButton = Button(mmImg,40,450,120,70,mmImg,50,450,mainmenu)
        quitButton = Button(quitImg,40,530,120,70,quitImg,50,530,quitgame)
        pygame.display.update()
        
    
    
   
    
    
        
    
#clear

def cl(text,st):
    gameDisplay.fill(white)
    largeText = pygame.font.SysFont("malgungothic", 46)
    TextSurf = largeText.render(text, True, red)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    backg = Background(pygame.image.load(nst[st-1]), 0, 0)
    pygame.display.update()
    time.sleep(1)
    if st==3:
        devScreen1(st-1)
    else:
        gameScreen(st)
    



    

# 파괴
def shot(obj_x,obj_y):
    drawObject(explosion,obj_x,obj_y)
    obj_y = random.randrange(-100,-20)
    obj_x = random.randrange(0,750)
    return obj_x, obj_y
        
def restart(st):
    menu = True
    global score ,z1c,z2c,z4c,z3c,fscore
    z1c,z2c,z3c,z4c=0,0,0,0
    fscore=0
    backgy=0
    backguy=600
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        backg = Background(pygame.image.load(back[st]), 0, 0)
        # titletext = gameDisplay.blit(titleImg, (220,150))
        
        if backgy == 600:
            backgy =-600
        
        if backguy ==600:
            backguy =-600
         
        backgy += 10
        backguy += 10
        bg = Background(pygame.image.load(back[st]), 0, backgy)
        
        
        bg3 = Background(pygame.image.load(back[st]), 0, backguy)
        startButton = Button(startImg,190,260,120,50,startImg,180,250,gameScreen)
        quitButton = Button(quitImg,445,260,120,50,quitImg,455,250,quitgame)
        stButton = Button(mmImg,315,360,120,50,mmImg,315,350,mainmenu)
        
        
        # startButton = Button(startImg,550,30,60,20,clickStartImg,545,26,selectScreen)
        pygame.display.update()
        clock.tick(15)


            
# 게임 종료
def quitgame():
    pygame.quit()
    sys.exit()

# 메뉴 화면
def mainmenu():
    global score ,z1c,z2c,z4c,z3c,fscore
    z1c,z2c,z3c,z4c=0,0,0,0
    fscore=0
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        backg = Background(mainImg, 0, 0)
        # titletext = gameDisplay.blit(titleImg, (220,150))
        startButton = Button(startImg,190,260,120,60,startImg,200,250,selectScreen)
        quitButton = Button(quitImg,445,260,120,60,quitImg,455,250,quitgame)
        # devButton=Button(devimg,650,30,100,80,clickdevimg,645,26,devScreen)
        spButton=Button(spimg,50,450,100,70,spimg,60,440,sScreen)
        # storyButton=Button(storyimg,50,500,100,80,storyimg,60,490,ssScreen)
        storyButton=Button(storyimg,50,520,100,70,storyimg,60,510,scoresave)
        boButton=Button(scbuc,50,380,100,70,scbuc,60,370,board)
        
        # startButton = Button(startImg,550,30,60,20,clickStartImg,545,26,selectScreen)
        pygame.display.update()
        clock.tick(15)
   
        
        
def devScreen1(st):
    screen=pygame.display.set_mode([800,600])

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    darkBlue = (0,0,128)
    white = (255,255,255)
    black = (0,0,0)
    pink = (255,200,200)
    
    game_credits='''
    이미지 수집, 가공 : 서승원, 이준협
     
    게임 기능수정 : 박성수, 오병주
    https://opengameart.org/
    https://kr.freepik.com/
    ''' 
    centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
    deltaY = centery + 50      
    running =True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
        
        
        
        screen.fill(white)
        backg = Background(pygame.image.load(nst[2]), 0, 0)
        startButton = Button(mmImg,40,450,120,70,mmImg,50,450,mainmenu)
        quitButton = Button(quitImg,40,530,120,70,quitImg,50,530,quitgame)
        svButton = Button(scbu,40,370,120,70,scbu,50,370,scoresave)  
        deltaY-= 0.7
        i=0
        msg_list=[]
        pos_list=[]
        
        font = pygame.font.SysFont('malgungothic', 30)
        
        for line in game_credits.split('\n'):
            msg=font.render(line, True, red)
            msg_list.append(msg)
            pos= msg.get_rect(center=(centerx, centery+deltaY+30*i))
            pos_list.append(pos)
            i=i+1
            
        for j in range(i):
            screen.blit(msg_list[j], pos_list[j])
          
        pygame.display.update()

# 선택 화면
def selectScreen():
    select = True
    global score ,z1c,z2c,z4c,z3c,fscore
    
    z1c,z2c,z3c,z4c=0,0,0,0
    fscore=0
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()


        gameDisplay.fill(white)
        backg = Background(selectImg, 0, 0)
        # gameDisplay.blit(selectText,(200,150))
        servSelect = Button2(ch1, 280,260,70,100, ch1,270,250,serv1parms,gameScreen)
        serv2Select = Button2(ch2, 480, 260, 70, 100, ch2,470,250,serv2parms,gameScreen)
        startButton = Button(mmImg,50,530,60,50,mmImg,40,520,mainmenu)
        
        pygame.display.update()
        clock.tick(15)

# 필살기
def sScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()


        gameDisplay.fill(white)
        backg = Background(IMG, 0, 0)
        # gameDisplay.blit(selectText,(200,150))
        
        startButton = Button(mmImg,50,530,60,50,mmImg,40,520,mainmenu)
        
        pygame.display.update()
        clock.tick(15)
# 스토리
def ssScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quitgame()


        gameDisplay.fill(white)
        backg = Background(ssIMG, 0, 0)
        # gameDisplay.blit(selectText,(200,150))
        
        startButton = Button(mmImg,50,530,60,50,mmImg,40,520,mainmenu)
        
        pygame.display.update()
        clock.tick(15)


# 게임 화면
def gameScreen(st=1):
    serv = Player(playerparms[0],playerparms[1],playerparms[2],playerparms[3],playerparms[4],playerparms[5],playerparms[6],playerparms[7])
    item = Gameobject(pygame.image.load(itemImg[playerparms[7]]), 5, random.randrange(0, display_width - 20), -600, 40, 35)
    zombie1 = Gameobject(zombie1Img, 3, random.randrange(0, display_width - 20),-600,40,35)
    zombie2 = Gameobject(zombie3Img, 3, random.randrange(0, display_width - 20),-1000,40,35)
    zombie3 = Gameobject(zombie2Img, 4, random.randrange(0, display_width - 20),random.randrange(-2000, -1000),80,40)
    rock = Gameobject(rockimg, 4, random.randrange(0, display_width - 75),random.randrange(-200, -100),80,40)
    missile = pygame.image.load(miss[serv.missile]) #미사일 그림
    spe = Gameobject(speImg, 4, 800,-600,10,10)
    backImg=pygame.image.load(back[st])
    x_change = 0
    y_change = 0
    global score ,z1c,z2c,z4c,z3c , fscore
    global input_text
    input_text=''
    score = 0
    time_remaining = 15  # 시간 제한 (초)
    timechange=clock.get_time() / 1000  # 밀리초를 초로 변환
    font = pygame.font.SysFont("malgungothic", 30)
    so = font.render('',True,red)
    bombnum=2
    #무기 좌표 리스트
    missileXY =[]
    
    
    shotCount =0
    rockPassed =0
    backgx = 0
    backgrx = 800
    backglx = -800
    backgy=0
    backguy=600
    
    paused = False
    gameexit = False 
    
    while not gameexit:
        gameDisplay.fill(white)
        
        
        
        # 이벤트
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               quitgame()
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # 'p' 키를 누르면
                    paused = not paused  # 일시 정지 상태를 변경
                    if paused:
                        x_change = 0
                        y_change = 0
                        rock.speed=0
                        zombie1.speed=0
                        zombie2.speed=0
                        zombie3.speed=0
                        item.speed=0
                        timechange=0
                        so = font.render('일시정지',True,red)
                        
                        
                        
                    else:
                        rock.speed=5
                        zombie1.speed=3
                        zombie2.speed=3
                        zombie3.speed=4
                        item.speed=3
                        timechange=clock.get_time() / 1000
                        so = font.render('',True,red)
                        
           if not paused: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and serv.serv_x > 0:
                        x_change = serv.speed*-1 + -1*serv.speedmult
                        backgx += 30
                        backgrx += 30
                        backglx += 30
                    elif event.key == pygame.K_RIGHT and serv.serv_x < display_width - 45:
                        x_change = serv.speed + serv.speedmult
                        backgx -= 30
                        backgrx -= 30
                        backglx -= 30
                    elif event.key == pygame.K_UP and serv.serv_y > 0:
                        y_change = -1*serv.speed -1*serv.speedmult
                    
                    elif event.key == pygame.K_DOWN and serv.serv_y < display_height-serv.hitbox_y:
                        y_change = serv.speed + serv.speedmult
                    
                    
                    elif event.key == pygame.K_SPACE: #미사일
                        missileX = serv.serv_x + serv.hitbox_x/2
                        missileY = serv.serv_y - serv.hitbox_y
                        missileXY.append([missileX,missileY])
                        
                    elif event.key == pygame.K_LSHIFT and bombnum>0: #폭탄
                            # gameDisplay.blit(spe, (50,100 ))
                            spe.coord_y = 0
                            spe.coord_x = 0
                            gameDisplay.blit(spe.b_image, (spe.coord_x,spe.coord_y ))
                            pygame.display.update()
                            clock.tick(60)
                            time.sleep(1) 
                            item.coord_y = -1000
                            item.coord_x = random.randrange(0, display_width - 25)
                            zombie1.coord_y = -1000
                            zombie1.coord_x = random.randrange(0, display_width - 25)
                            zombie2.coord_y = -1000
                            zombie2.coord_x = random.randrange(0, display_width - 25)
                            zombie3.coord_y = -2000
                            zombie3.coord_x = random.randrange(0, display_width - 56)
                            rock.coord_y = -1000
                            rock.coord_x = random.randrange(0, display_width - 70)
                            bombnum -=1
                            spe.coord_y = 800
                            spe.coord_x = 600
                        
                    
                    
           if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0          
        serv.serv_x += x_change
        serv.serv_y += y_change      
        
        if backgx == -800:
            backgx = 800
        if backgrx == -800:
            backgrx = 800
        if backglx == -800:
            backglx = -800
        if backgy == 600:
            backgy =-600
        
        if backguy ==600:
            backguy =-600
        
        backgy += 5
        backguy += 5
        bg = Background(backImg, backgx, backgy)
        bg1= Background(backImg,backgrx,backgy)
        bg2= Background(backImg,backglx,backgy)
        
        bg3 = Background(backImg, backgx, backguy)
        bg4= Background(backImg,backgrx,backguy)
        bg5= Background(backImg,backglx,backguy)
        time_remaining -= timechange
        time_text = font.render(f"Time: {max(0, int(time_remaining))}", True, red) #시간
        gameDisplay.blit(time_text, (600, 20))
        gameDisplay.blit(so, (325,255 ))
        gameDisplay.blit(pygame.image.load(itemImg[playerparms[7]]), (400,20 ))
        gameDisplay.blit(scoreImg, (20,20 ))
        gameDisplay.blit(spe.b_image, (spe.coord_x,spe.coord_y ))
        gameDisplay.blit(item.b_image, (item.coord_x, item.coord_y))
        gameDisplay.blit(zombie1.b_image, (zombie1.coord_x, zombie1.coord_y))
        gameDisplay.blit(zombie2.b_image, (zombie2.coord_x, zombie2.coord_y))
        gameDisplay.blit(zombie3.b_image, (zombie3.coord_x, zombie3.coord_y))
        gameDisplay.blit(rock.b_image, (rock.coord_x, rock.coord_y))
            
        gameDisplay.blit(serv.p_img, (serv.serv_x, serv.serv_y))
        
        # if time_remaining <= 0: #시간
        #     crash(st) 
        # 낙하 속도 
        item.coord_y += item.speed
        zombie1.coord_y += zombie1.speed
        zombie2.coord_y += zombie1.speed
        zombie3.coord_y += zombie3.speed
        rock.coord_y += rock.speed

        #이동 제한
        if serv.serv_x > display_width - serv.hitbox_x or serv.serv_x < 0:
            x_change = 0
        if serv.serv_y >display_height - serv.hitbox_y or serv.serv_y < 0:
            y_change =0

        #오브젝트 재생성
        if item.coord_y > display_height:
            item.coord_y = -10
            item.coord_x = random.randrange(0, display_width - 25)
        if zombie1.coord_y > display_height - 10:
            zombie1.coord_y = -10
            zombie1.coord_x = random.randrange(0, display_width - 25)
        if zombie2.coord_y > display_height:
            zombie2.coord_y = -410
            zombie2.coord_x = random.randrange(0, display_width - 25)
        if zombie3.coord_y > display_height:
            zombie3.coord_y = -2000
            zombie3.coord_x = random.randrange(0, display_width - 56)
        if rock.coord_y > display_height:
            rock.coord_y = -200
            rock.coord_x = random.randrange(0, display_width - 70)
        #미사일 발사 화면에 그리기
        if len(missileXY) !=0:
            for i ,bxy in enumerate(missileXY): #미사일 요소에 대해 반복함
                bxy[1] -= 10 #총알의 y 좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]

                #미사일이 운석을 맞추었을 경우
                if bxy[1] < rock.coord_y:
                    if bxy[0] > rock.coord_x and bxy[0] < rock.coord_x + rock.hitbox_x:
                        missileXY.remove(bxy)
                        z4c+=1
                        # shotCount += 1
                        if serv.missile==1:
                            score+=3
                        else:
                            score +=2
                        rock.coord_x,rock.coord_y = shot(rock.coord_x,rock.coord_y)
                #미사일이 큰좀비
                if bxy[1] < zombie3.coord_y:
                    if bxy[0] > zombie3.coord_x and bxy[0] < zombie3.coord_x + zombie3.hitbox_x:
                        missileXY.remove(bxy)
                       
                        # shotCount += 1
                        if serv.missile==1:
                            score+=5
                        else:
                            score +=3
                        z3c +=1
                        zombie3.coord_x,zombie3.coord_y=shot(zombie3.coord_x,zombie3.coord_y)
                #ch
                if bxy[1] < zombie2.coord_y:
                    if bxy[0] > zombie2.coord_x and bxy[0] < zombie2.coord_x + zombie2.hitbox_x:
                        missileXY.remove(bxy)
                       
                        # shotCount += 1
                        if serv.missile==1:
                            score+=2
                        else:
                            score +=1
                        z2c +=1
                        zombie2.coord_x,zombie2.coord_y=shot(zombie2.coord_x,zombie2.coord_y)
                #ch
                if bxy[1] < zombie1.coord_y:
                    if bxy[0] > zombie1.coord_x and bxy[0] < zombie1.coord_x + zombie1.hitbox_x:
                        missileXY.remove(bxy)
                       
                        # shotCount += 1
                        if serv.missile==1:
                            score+=2
                        else:
                            score +=1
                        z1c +=1
                        zombie1.coord_x,zombie1.coord_y=shot(zombie1.coord_x,zombie1.coord_y)
                
                if bxy[1] <= 0: # 미사일이 화면 밖을 벗어나면

                    try:
                        missileXY.remove(bxy) #미사일 제거

                    except:
                        pass

        if len(missileXY) != 0:
            for bx,by in missileXY:
                drawObject(missile,bx,by)
        
        

       # 충돌처리
        #ch 
        if serv.serv_y < zombie1.coord_y + zombie1.hitbox_y and serv.serv_y+serv.hitbox_y > zombie1.coord_y:
            if serv.serv_x > zombie1.coord_x \
               and serv.serv_x < zombie1.coord_x + zombie1.hitbox_x \
               or serv.serv_x + serv.hitbox_x > zombie1.coord_x \
               and serv.serv_x + serv.hitbox_x < zombie1.coord_x + zombie1.hitbox_x:
               crash(st)
                
        # ch 
        if serv.serv_y < zombie2.coord_y + zombie2.hitbox_y and serv.serv_y+serv.hitbox_y > zombie2.coord_y:
            if serv.serv_x > zombie2.coord_x \
               and serv.serv_x < zombie2.coord_x + zombie2.hitbox_x \
               or serv.serv_x + serv.hitbox_x > zombie2.coord_x \
               and serv.serv_x + serv.hitbox_x < zombie2.coord_x + zombie2.hitbox_x:
               crash(st)
        # 큰좀비 
        if serv.serv_y < zombie3.coord_y + zombie3.hitbox_y and serv.serv_y+serv.hitbox_y > zombie3.coord_y:
            if serv.serv_x > zombie3.coord_x \
               and serv.serv_x < zombie3.coord_x + zombie3.hitbox_x \
               or serv.serv_x + serv.hitbox_x > zombie3.coord_x \
               and serv.serv_x + serv.hitbox_x < zombie3.coord_x + zombie3.hitbox_x:
               crash(st)

        # 폭탄       
        if serv.serv_y < item.coord_y + item.hitbox_y \
        and serv.serv_y > item.coord_y \
        or serv.serv_y + serv.hitbox_y > item.coord_y \
        and serv.serv_y + serv.hitbox_y < item.coord_y + item.hitbox_y:
            if serv.serv_x > item.coord_x \
            and serv.serv_x < item.coord_x + item.hitbox_x \
            or serv.serv_x + serv.hitbox_x > item.coord_x \
            and serv.serv_x + serv.hitbox_x < item.coord_x + item.hitbox_x:
                item.coord_y = -10
                item.coord_x = random.randrange(0, display_width - 25)
                bombnum += 1
        #운석 충돌
        if serv.serv_y < rock.coord_y + rock.hitbox_y and serv.serv_y+serv.hitbox_y > rock.coord_y:
            if serv.serv_x > rock.coord_x \
               and serv.serv_x < rock.coord_x + rock.hitbox_x \
               or serv.serv_x + serv.hitbox_x > rock.coord_x \
               and serv.serv_x + serv.hitbox_x < rock.coord_x + rock.hitbox_x:
               crash(st)
        
        
        # 점수 표시
        scorecounter(score,bombnum)
        if time_remaining<=0:
            if st<2:
                fscore+=score 
                st += 1
                cl('stage clear',st)
            elif st==2:
                st+=1
                fscore+=score
                cl('game clear',st)
                
        # if score>4 and st<2:
        #     fscore+=score
        #     st+=1
        #     cl('stage clear',st)
        # elif st==2 and score>4:
        #     st+=1
        #     fscore+=score
        #     cl('game clear',st)
             
        
        pygame.display.flip()
        clock.tick(60)
        
        

                

mainmenu()
selectScreen()
gameScreen()

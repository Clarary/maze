class Qipan:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.block_list = []
        for i in range(x):
            hang = []
            for j in range(y):
                hang.append(Block(i,j))
            self.block_list.append(hang)
            
    #在此定义函数,对block的改变为block_list[i][j].f = ?
    def set_start(self,i,j,has_start):
        if has_start:
            for xx in range(self.x):
                for yy in range(self.y):
                    if self.block_list[xx][yy].sta == 1:
                        self.block_list[xx][yy].sta = 0
                        self.block_list[xx][yy].update(self.block_list[xx][yy].f,self.block_list[xx][yy].g,self.block_list[xx][yy].h)
                        print("起点更换成功")
        else:
            print("起点设置成功")
        #注意这里是[j][i],第j行第i个距左侧i个格子上侧j个格子
        self.block_list[j][i].sta = 1
        self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
        
    def set_end(self,i,j,has_end):
        if has_end:
            for xx in range(self.x):
                for yy in range(self.y):
                    if self.block_list[xx][yy].sta == 2:
                        self.block_list[xx][yy].sta = 0
                        self.block_list[xx][yy].update(self.block_list[xx][yy].f,self.block_list[xx][yy].g,self.block_list[xx][yy].h)
                        print("终点更换成功")
        else:
            print("终点更换成功")
        self.block_list[j][i].sta = 2
        self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
            
    def set_ob(self,i,j):
        if self.block_list[j][i].sta == 1:
            self.block_list[j][i].sta = 3
            self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
            return 1
        if self.block_list[j][i].sta == 2:
            self.block_list[j][i].sta = 3
            self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
            return 2
        else:
            self.block_list[j][i].sta = 3
            self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
            print("设置障碍成功")
            return 0
        
        
class Block:
    def __init__(self,x,y,f = 0,g = 0,h = 0):
        self.x = x
        self.y = y
        self.f = f
        self.h = h
        self.g = g
        self.sta = 0 #0为无状态，1为起点，2为终点，3为障碍
        self.color = self.get_color()
        
    def update(self,f,g,h):
        self.color = self.get_color()
        self.f = f
        self.h = h
        self.g = g
        
    def get_color(self):
        if self.sta == 0:
            return [255,255,255]
        if self.sta == 1:
            return [0,255,0]
        if self.sta == 2:
            return [255,0,0]
        if self.sta == 3:
            return [0,0,0]
    
#display函数，状态0为确认前，不显示g、h、f值；状态1为确认后,显示g、h、f值
def display(qipan,screen,status = 0):
    #先定义字体
    fgh_font=pg.font.Font(None,20)
    #白屏
    screen.fill((255,255,255))
    for i in range(qipan.x):
        for j in range(qipan.y):
            rect_list=[i*BLOCK_LEN,j*BLOCK_LEN,BLOCK_LEN,BLOCK_LEN]
            #print(rect_list)
            #先画出格子
            pygame.draw.rect(screen,[0,0,0],rect_list,2)
            block_list = [i*BLOCK_LEN+2,j*BLOCK_LEN+2,BLOCK_LEN-4,BLOCK_LEN-4]
            #填充格子内颜色
            pygame.draw.rect(screen,qipan.block_list[i][j].color,block_list,0)
    pygame.display.flip()
              
    if status ==1:
        for i in range(qipan.x):
            for j in range(qipan.y):
                #写上f,g,h
                font_g = str(qipan.block_list[i][j].g)
                font_surf_g = fgh_font.render(font_g,True,(0,0,0),(255,255,255)) 
                sur_rect_g = font_surf_g.get_rect()
                #定义中心位置
                sur_rect_g.center = (i*BLOCK_LEN+15,BLOCK_LEN*j+10)
                #把字画屏幕上
                screen.blit(font_surf_g,sur_rect_g)
                font_h = str(qipan.block_list[i][j].h)
                font_surf_h = fgh_font.render(font_h,True,(0,0,0),(255,255,255)) 
                sur_rect_h = font_surf_h.get_rect()
                sur_rect_h.center = (i*BLOCK_LEN+15,BLOCK_LEN*j+BLOCK_LEN-10)
                screen.blit(font_surf_h,sur_rect_h)
                font_f = str(qipan.block_list[i][j].f)
                font_surf_f = fgh_font.render(font_f,True,(0,0,0),(255,255,255)) 
                sur_rect_f = font_surf_f.get_rect()
                sur_rect_f.center = (i*BLOCK_LEN+BLOCK_LEN-15,BLOCK_LEN*j+BLOCK_LEN-10)
                screen.blit(font_surf_f,sur_rect_f)
                pygame.display.flip()
                
    if status == 0:
        start_image=pygame.image.load(r'D:\360data\重要数据\桌面\static\starting_point.png')
        place1 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+10]
        screen.blit(start_image,place1)
        pygame.display.flip()
        end_image=pygame.image.load(r'D:\360data\重要数据\桌面\static\ending_point.png')
        place2 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+10]
        screen.blit(end_image,place2)
        pygame.display.flip()
        ob_image=pygame.image.load(r'D:\360data\重要数据\桌面\static\obstacle.png')
        place3 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+60]
        screen.blit(ob_image,place3)
        pygame.display.flip()
        con_image=pygame.image.load(r'D:\360data\重要数据\桌面\static\confirm.png')
        place4 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+60]
        screen.blit(con_image,place4)
        pygame.display.flip()
        start_image=pygame.image.load(r'D:\360data\重要数据\桌面\static\statement.png')
        place_s = [qipan.x*BLOCK_LEN/2-190,qipan.y*BLOCK_LEN+110]
        screen.blit(start_image,place_s)
        pygame.display.flip()
    #score_sur = score_font.render('score: '+str(qipan.score),True,(106, 90, 205))
    #score_rect = score_sur.get_rect()
    #score_rect.center = (BLOCK_LEN*qipan.size/2,BLOCK_LEN*qipan.size+35)
    #screen.blit(score_sur,score_rect)
import pygame
import sys
import pygame as pg
import time
def main(t = 0.3):
    flag = 1
    while(flag):
        x=int(input("请输入迷宫的长："))
        y=int(input("请输入迷宫的宽："))
        if(x<4 or y<4):
            print("迷宫的长和宽必须大于三，请重新输入：")
            continue
        flag = 0
    pg.init()
    pg.font.init()
    screen=pg.display.set_mode((BLOCK_LEN*x,BLOCK_LEN*y+BLANK_HEIGHT))
    screen.fill((255,255,255))
    pg.display.set_caption("迷宫")
    qipan = Qipan(x,y)
    display(qipan,screen)
    print("事件循环")
    step = 0 #step为1：设置起点；2：设置终点；3：设置障碍
    has_start = False #还未设置起点
    has_end = False #还未设置终点
    period = 1
    while True:
        if period ==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("退出")
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN: #判断鼠标位置以及是否摁了下去。
                    #做需要做的事情，如开始游戏。
                    x, y = pygame.mouse.get_pos()
                    j = int(x/BLOCK_LEN)
                    i = int(y/BLOCK_LEN)
                    #点的是第i行第j个
                    if qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        step = 1
                        print("设置起点")
                    if qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        step = 2
                        print("设置终点")
                    if qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        step = 3
                        print("设置障碍")
                    if qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        if has_start and has_end:
                            print("确认成功，进入阶段二")
                            period = 2
                        else:
                            print("确认失败")
                    if 0<=x<=qipan.x*BLOCK_LEN and 0<=y<=qipan.y*BLOCK_LEN:
                        print("点击了迷宫")
                        if step == 0:
                            print("无事件")
                        elif step == 1:
                            qipan.set_start(i,j,has_start)
                            has_start = True
                        elif step == 2:
                            qipan.set_end(i,j,has_end)
                            has_end = True
                        elif step == 3:
                            special = qipan.set_ob(i,j)
                            if special == 1:
                                has_start = False
                                print("将起点换成障碍")
                            if special == 2:
                                has_end = False
                                print("将终点换成障碍")
                    display(qipan,screen)
                else:
                    print("阶段一，无事件")
                    time.sleep(t)
        if period == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("退出")
                    pygame.quit()
                    sys.exit()
                else:
                    print("阶段二，无事件")
                    time.sleep(t)

TIME = 0.3    #设置得越小游戏卡顿越少
BLOCK_LEN = 80
BLANK_HEIGHT = 170
main(TIME)
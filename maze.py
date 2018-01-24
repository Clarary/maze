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
            
    def set_start(self,i,j,has_start):
        if has_start:
            for xx in range(self.x):
                for yy in range(self.y):
                    if self.block_list[xx][yy].sta == 1:
                        self.block_list[xx][yy].sta = 0
                        self.block_list[xx][yy].update(self.block_list[xx][yy].f,self.block_list[xx][yy].g,self.block_list[xx][yy].h)
        else:
            pass
        self.block_list[j][i].sta = 1
        self.block_list[j][i].update(self.block_list[j][i].f,self.block_list[j][i].g,self.block_list[j][i].h)
        
    def set_end(self,i,j,has_end):
        if has_end:
            for xx in range(self.x):
                for yy in range(self.y):
                    if self.block_list[xx][yy].sta == 2:
                        self.block_list[xx][yy].sta = 0
                        self.block_list[xx][yy].update(self.block_list[xx][yy].f,self.block_list[xx][yy].g,self.block_list[xx][yy].h)
        else:
            pass
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
            return 0
        
    def update_all(self):
        for xx in range(self.x):
            for yy in range(self.y):
                self.block_list[xx][yy].update(self.block_list[xx][yy].f,self.block_list[xx][yy].g,self.block_list[xx][yy].h)
        

class Block:
    def __init__(self,x,y,f = 0,g = 0,h = 0):
        self.x = x
        self.y = y
        self.f = f
        self.h = h
        self.g = g
        self.sta = 0
        self.display_fgh = False
        self.color = self.get_color()
        self.parent = (-1,-1)
        
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
        if self.sta == 4:
            return [255,255,0]
        if self.sta == 5:
            return [135,206,250]
        if self.sta == 6:
            return [0,191,255]
			
			

def display(qipan,screen,status = 0):
    fgh_font=pg.font.Font("symbol.ttf",20)
    screen.fill((255,255,255))
    for i in range(qipan.x):
        for j in range(qipan.y):
            rect_list=[i*BLOCK_LEN,j*BLOCK_LEN,BLOCK_LEN,BLOCK_LEN]
            pygame.draw.rect(screen,[0,0,0],rect_list,2)
            block_list = [i*BLOCK_LEN+2,j*BLOCK_LEN+2,BLOCK_LEN-4,BLOCK_LEN-4]
            pygame.draw.rect(screen,qipan.block_list[i][j].color,block_list,0)
              
    if status ==1:
        for i in range(qipan.x):
            for j in range(qipan.y):
                if qipan.block_list[i][j].display_fgh:
                    font_g = str(qipan.block_list[i][j].g)
                    font_surf_g = fgh_font.render(font_g,True,(0,0,0)) 
                    sur_rect_g = font_surf_g.get_rect()
                    sur_rect_g.center = (i*BLOCK_LEN+15,BLOCK_LEN*j+10)
                    screen.blit(font_surf_g,sur_rect_g)
                    font_f = str(qipan.block_list[i][j].f)
                    font_surf_f = fgh_font.render(font_f,True,(0,0,0)) 
                    sur_rect_f = font_surf_f.get_rect()
                    sur_rect_f.center = (i*BLOCK_LEN+15,BLOCK_LEN*j+BLOCK_LEN-10)
                    screen.blit(font_surf_f,sur_rect_f)
                    font_h = str(qipan.block_list[i][j].h)
                    font_surf_h = fgh_font.render(font_h,True,(0,0,0)) 
                    sur_rect_h = font_surf_h.get_rect()
                    sur_rect_h.center = (i*BLOCK_LEN+BLOCK_LEN-15,BLOCK_LEN*j+BLOCK_LEN-10)
                    screen.blit(font_surf_h,sur_rect_h)
                start_image=pygame.image.load(r'.\static\start.png')
                place1 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+10]
                screen.blit(start_image,place1)
                end_image=pygame.image.load(r'.\static\restart.png')
                place2 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+10]
                screen.blit(end_image,place2)
                ob_image=pygame.image.load(r'.\static\step.png')
                place3 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+60]
                screen.blit(ob_image,place3)
                con_image=pygame.image.load(r'.\static\result.png')
                place4 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+60]
                screen.blit(con_image,place4)
                start_image=pygame.image.load(r'.\static\statement2.png')
                place_s = [qipan.x*BLOCK_LEN/2-190,qipan.y*BLOCK_LEN+110]
                screen.blit(start_image,place_s)
                pygame.display.flip()
                
    if status == 0:
        start_image=pygame.image.load(r'.\static\starting_point.png')
        place1 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+10]
        screen.blit(start_image,place1)
        end_image=pygame.image.load(r'.\static\ending_point.png')
        place2 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+10]
        screen.blit(end_image,place2)
        ob_image=pygame.image.load(r'.\static\obstacle.png')
        place3 = [qipan.x*BLOCK_LEN/4-50,qipan.y*BLOCK_LEN+60]
        screen.blit(ob_image,place3)
        con_image=pygame.image.load(r'.\static\confirm.png')
        place4 = [qipan.x*BLOCK_LEN/4*3-50,qipan.y*BLOCK_LEN+60]
        screen.blit(con_image,place4)
        start_image=pygame.image.load(r'.\static\statement.png')
        place_s = [qipan.x*BLOCK_LEN/2-190,qipan.y*BLOCK_LEN+110]
        screen.blit(start_image,place_s)
        pygame.display.flip()
		
		
def is_empty_ol(qipan):
    flag = True
    for i in range(qipan.x):
        for j in range(qipan.y):
            if qipan.block_list[i][j].sta ==5:
                flag = False
    return flag

def get_point(qipan,sta):
    for i in range(qipan.x):
        for j in range(qipan.y):
            if qipan.block_list[i][j].sta ==sta:
                return i,j
            
def ol_find_min(qipan):
    min_value = 99999
    x = -1
    y = -1
    for i in range(qipan.x):
        for j in range(qipan.y):
            if qipan.block_list[i][j].sta == 5 and qipan.block_list[i][j].g<min_value:
                min_value = qipan.block_list[i][j].g
                x = i
                y = j
    return x,y

def judge_end(qipan,min_i,min_j):
    end_i,end_j = get_point(qipan,2)
    if min_i-1<=end_i<=min_i+1 and min_j-1<=end_j<=min_j+1:
        qipan.block_list[end_i][end_j].parent = (min_i,min_j)
        print("找到最佳路径")
        return True
    elif is_empty_ol(qipan):
        print("失败，起点被障碍包围了")
        return True
    else:
        return False
    
def find_best_route(qipan):
    end_i,end_j = get_point(qipan,2)
    start_i,start_j = get_point(qipan,1)
    x,y = qipan.block_list[end_i][end_j].parent[0],qipan.block_list[end_i][end_j].parent[1]
    while x != start_i or y != start_j:
        qipan.block_list[x][y].sta = 4
        x,y = qipan.block_list[x][y].parent[0],qipan.block_list[x][y].parent[1]
		
		
def step_search(qipan):
    start_i,start_j = get_point(qipan,1)
    end_i,end_j = get_point(qipan,2)
    if is_empty_ol(qipan):
        qipan.block_list[start_i][start_j].h = 10*(abs(start_i-end_i)+abs(start_j-end_j))
        qipan.block_list[start_i][start_j].g = qipan.block_list[start_i][start_j].f+qipan.block_list[start_i][start_j].h
        if qipan.block_list[start_i-1][start_j-1].sta != 3 and start_i-1>-1and start_j-1>-1:
            qipan.block_list[start_i-1][start_j-1].display_fgh = True
            qipan.block_list[start_i-1][start_j-1].sta =5
            qipan.block_list[start_i-1][start_j-1].f =14
            qipan.block_list[start_i-1][start_j-1].h = 10*(abs(start_i-1-end_i)+abs(start_j-1-end_j))
            qipan.block_list[start_i-1][start_j-1].g = qipan.block_list[start_i-1][start_j-1].f+qipan.block_list[start_i-1][start_j-1].h
            qipan.block_list[start_i-1][start_j-1].parent = (start_i,start_j)
        if qipan.block_list[start_i-1][start_j].sta != 3 and start_i-1>-1:
            qipan.block_list[start_i-1][start_j].display_fgh = True
            qipan.block_list[start_i-1][start_j].sta =5
            qipan.block_list[start_i-1][start_j].f =10
            qipan.block_list[start_i-1][start_j].h = 10*(abs(start_i-1-end_i)+abs(start_j-end_j))
            qipan.block_list[start_i-1][start_j].g = qipan.block_list[start_i-1][start_j].f+qipan.block_list[start_i-1][start_j].h
            qipan.block_list[start_i-1][start_j].parent = (start_i,start_j)
        if start_j+1<qipan.y:
            if qipan.block_list[start_i-1][start_j+1].sta != 3 and start_i-1>-1:
                qipan.block_list[start_i-1][start_j+1].display_fgh = True
                qipan.block_list[start_i-1][start_j+1].sta =5
                qipan.block_list[start_i-1][start_j+1].f =14
                qipan.block_list[start_i-1][start_j+1].h = 10*(abs(start_i-1-end_i)+abs(start_j+1-end_j))
                qipan.block_list[start_i-1][start_j+1].g = qipan.block_list[start_i-1][start_j+1].f+qipan.block_list[start_i-1][start_j+1].h
                qipan.block_list[start_i-1][start_j+1].parent = (start_i,start_j)
        if qipan.block_list[start_i][start_j-1].sta != 3 and start_j-1>-1:
            qipan.block_list[start_i][start_j-1].display_fgh = True
            qipan.block_list[start_i][start_j-1].sta =5
            qipan.block_list[start_i][start_j-1].f =10
            qipan.block_list[start_i][start_j-1].h = 10*(abs(start_i-end_i)+abs(start_j-1-end_j))
            qipan.block_list[start_i][start_j-1].g = qipan.block_list[start_i][start_j-1].f+qipan.block_list[start_i][start_j-1].h
            qipan.block_list[start_i][start_j-1].parent = (start_i,start_j)
        if start_j+1<qipan.y:
            if qipan.block_list[start_i][start_j+1].sta != 3:
                qipan.block_list[start_i][start_j+1].display_fgh = True
                qipan.block_list[start_i][start_j+1].sta =5
                qipan.block_list[start_i][start_j+1].f =10
                qipan.block_list[start_i][start_j+1].h = 10*(abs(start_i-end_i)+abs(start_j+1-end_j))
                qipan.block_list[start_i][start_j+1].g = qipan.block_list[start_i][start_j+1].f+qipan.block_list[start_i][start_j+1].h
                qipan.block_list[start_i][start_j+1].parent = (start_i,start_j)
        if start_i+1<qipan.x:
            if qipan.block_list[start_i+1][start_j-1].sta != 3 and start_j-1>-1:
                qipan.block_list[start_i+1][start_j-1].display_fgh = True
                qipan.block_list[start_i+1][start_j-1].sta =5
                qipan.block_list[start_i+1][start_j-1].f =14
                qipan.block_list[start_i+1][start_j-1].h = 10*(abs(start_i+1-end_i)+abs(start_j-1-end_j))
                qipan.block_list[start_i+1][start_j-1].g = qipan.block_list[start_i+1][start_j-1].f+qipan.block_list[start_i+1][start_j-1].h
                qipan.block_list[start_i+1][start_j-1].parent = (start_i,start_j)
        if start_i+1<qipan.x:
            if qipan.block_list[start_i+1][start_j].sta != 3:
                qipan.block_list[start_i+1][start_j].display_fgh = True
                qipan.block_list[start_i+1][start_j].sta =5
                qipan.block_list[start_i+1][start_j].f =10
                qipan.block_list[start_i+1][start_j].h = 10*(abs(start_i+1-end_i)+abs(start_j-end_j))
                qipan.block_list[start_i+1][start_j].g = qipan.block_list[start_i+1][start_j].f+qipan.block_list[start_i+1][start_j].h
                qipan.block_list[start_i+1][start_j].parent = (start_i,start_j)
        if start_i+1<qipan.x and start_j+1<qipan.y:
            if qipan.block_list[start_i+1][start_j+1].sta != 3:
                qipan.block_list[start_i+1][start_j+1].display_fgh = True
                qipan.block_list[start_i+1][start_j+1].sta =5
                qipan.block_list[start_i+1][start_j+1].f =14
                qipan.block_list[start_i+1][start_j+1].h = 10*(abs(start_i+1-end_i)+abs(start_j+1-end_j))
                qipan.block_list[start_i+1][start_j+1].g = qipan.block_list[start_i+1][start_j+1].f+qipan.block_list[start_i+1][start_j+1].h
                qipan.block_list[start_i+1][start_j+1].parent = (start_i,start_j)
        return False
    else:
        min_i,min_j = ol_find_min(qipan)
        qipan.block_list[min_i][min_j].sta = 6
        if qipan.block_list[min_i-1][min_j-1].sta not in[1,2,3,6] and min_i-1>-1and min_j-1>-1:
            if qipan.block_list[min_i-1][min_j-1].sta != 5:
                qipan.block_list[min_i-1][min_j-1].display_fgh = True
                qipan.block_list[min_i-1][min_j-1].sta = 5
                qipan.block_list[min_i-1][min_j-1].f = qipan.block_list[min_i][min_j].f + 14
                qipan.block_list[min_i-1][min_j-1].h = 10*(abs(min_i-1-end_i)+abs(min_j-1-end_j))
                qipan.block_list[min_i-1][min_j-1].g = qipan.block_list[min_i-1][min_j-1].f+qipan.block_list[min_i-1][min_j-1].h
                qipan.block_list[min_i-1][min_j-1].parent = (min_i,min_j)
            else:
                new_f = qipan.block_list[min_i][min_j].f + 14
                if new_f<qipan.block_list[min_i-1][min_j-1].f:
                    qipan.block_list[min_i-1][min_j-1].f = new_f
                    qipan.block_list[min_i-1][min_j-1].g = qipan.block_list[min_i-1][min_j-1].f+qipan.block_list[min_i-1][min_j-1].h
                    qipan.block_list[min_i-1][min_j-1].parent = (min_i,min_j)
        if qipan.block_list[min_i-1][min_j].sta not in[1,2,3,6] and min_i-1>-1:
            if qipan.block_list[min_i-1][min_j].sta != 5:
                qipan.block_list[min_i-1][min_j].display_fgh = True
                qipan.block_list[min_i-1][min_j].sta = 5
                qipan.block_list[min_i-1][min_j].f = qipan.block_list[min_i][min_j].f + 10
                qipan.block_list[min_i-1][min_j].h = 10*(abs(min_i-1-end_i)+abs(min_j-end_j))
                qipan.block_list[min_i-1][min_j].g = qipan.block_list[min_i-1][min_j].f+qipan.block_list[min_i-1][min_j].h
                qipan.block_list[min_i-1][min_j].parent = (min_i,min_j)
            else:
                new_f = qipan.block_list[min_i][min_j].f + 10
                if new_f<qipan.block_list[min_i-1][min_j].f:
                    qipan.block_list[min_i-1][min_j].f = new_f
                    qipan.block_list[min_i-1][min_j].g = qipan.block_list[min_i-1][min_j-1].f+qipan.block_list[min_i-1][min_j-1].h
                    qipan.block_list[min_i-1][min_j].parent = (min_i,min_j)
        if min_j+1<qipan.y:
            if qipan.block_list[min_i-1][min_j+1].sta not in[1,2,3,6] and min_i-1>-1:
                if qipan.block_list[min_i-1][min_j+1].sta != 5:
                    qipan.block_list[min_i-1][min_j+1].display_fgh = True
                    qipan.block_list[min_i-1][min_j+1].sta = 5
                    qipan.block_list[min_i-1][min_j+1].f = qipan.block_list[min_i][min_j].f + 14
                    qipan.block_list[min_i-1][min_j+1].h = 10*(abs(min_i-1-end_i)+abs(min_j+1-end_j))
                    qipan.block_list[min_i-1][min_j+1].g = qipan.block_list[min_i-1][min_j+1].f+qipan.block_list[min_i-1][min_j+1].h
                    qipan.block_list[min_i-1][min_j+1].parent = (min_i,min_j)
                else:
                    new_f = qipan.block_list[min_i][min_j].f + 14
                    if new_f<qipan.block_list[min_i-1][min_j+1].f:
                        qipan.block_list[min_i-1][min_j+1].f = new_f
                        qipan.block_list[min_i-1][min_j+1].g = qipan.block_list[min_i-1][min_j+1].f+qipan.block_list[min_i-1][min_j+1].h
                        qipan.block_list[min_i-1][min_j+1].parent = (min_i,min_j)
        if qipan.block_list[min_i][min_j-1].sta not in[1,2,3,6] and min_j-1>-1:
            if qipan.block_list[min_i][min_j-1].sta != 5:
                qipan.block_list[min_i][min_j-1].display_fgh = True
                qipan.block_list[min_i][min_j-1].sta = 5
                qipan.block_list[min_i][min_j-1].f = qipan.block_list[min_i][min_j].f + 10
                qipan.block_list[min_i][min_j-1].h = 10*(abs(min_i-end_i)+abs(min_j-1-end_j))
                qipan.block_list[min_i][min_j-1].g = qipan.block_list[min_i][min_j-1].f+qipan.block_list[min_i][min_j-1].h
                qipan.block_list[min_i][min_j-1].parent = (min_i,min_j)
            else:
                new_f = qipan.block_list[min_i][min_j].f + 10
                if new_f<qipan.block_list[min_i][min_j-1].f:
                    qipan.block_list[min_i][min_j-1].f = new_f
                    qipan.block_list[min_i][min_j-1].g = qipan.block_list[min_i][min_j-1].f+qipan.block_list[min_i][min_j-1].h
                    qipan.block_list[min_i][min_j-1].parent = (min_i,min_j)
        if min_j+1<qipan.y:
            if qipan.block_list[min_i][min_j+1].sta not in[1,2,3,6]:
                if qipan.block_list[min_i][min_j+1].sta != 5:
                    qipan.block_list[min_i][min_j+1].display_fgh = True
                    qipan.block_list[min_i][min_j+1].sta = 5
                    qipan.block_list[min_i][min_j+1].f = qipan.block_list[min_i][min_j].f + 10
                    qipan.block_list[min_i][min_j+1].h = 10*(abs(min_i-end_i)+abs(min_j+1-end_j))
                    qipan.block_list[min_i][min_j+1].g = qipan.block_list[min_i][min_j+1].f+qipan.block_list[min_i][min_j+1].h
                    qipan.block_list[min_i][min_j+1].parent = (min_i,min_j)
                else:
                    new_f = qipan.block_list[min_i][min_j].f + 10
                    if new_f<qipan.block_list[min_i][min_j+1].f:
                        qipan.block_list[min_i][min_j+1].f = new_f
                        qipan.block_list[min_i][min_j+1].g = qipan.block_list[min_i][min_j+1].f+qipan.block_list[min_i][min_j+1].h
                        qipan.block_list[min_i][min_j+1].parent = (min_i,min_j)
        if min_i+1<qipan.x:
            if qipan.block_list[min_i+1][min_j-1].sta not in[1,2,3,6]and min_j-1>-1:
                if qipan.block_list[min_i+1][min_j-1].sta != 5:
                    qipan.block_list[min_i+1][min_j-1].display_fgh = True
                    qipan.block_list[min_i+1][min_j-1].sta = 5
                    qipan.block_list[min_i+1][min_j-1].f = qipan.block_list[min_i][min_j].f + 14
                    qipan.block_list[min_i+1][min_j-1].h = 10*(abs(min_i+1-end_i)+abs(min_j-1-end_j))
                    qipan.block_list[min_i+1][min_j-1].g = qipan.block_list[min_i+1][min_j-1].f+qipan.block_list[min_i+1][min_j-1].h
                    qipan.block_list[min_i+1][min_j-1].parent = (min_i,min_j)
                else:
                    new_f = qipan.block_list[min_i][min_j].f + 14
                    if new_f<qipan.block_list[min_i+1][min_j-1].f:
                        qipan.block_list[min_i+1][min_j-1].f = new_f
                        qipan.block_list[min_i+1][min_j-1].g = qipan.block_list[min_i+1][min_j-1].f+qipan.block_list[min_i+1][min_j-1].h
                        qipan.block_list[min_i+1][min_j-1].parent = (min_i,min_j)
        if min_i+1<qipan.x:
            if qipan.block_list[min_i+1][min_j].sta not in[1,2,3,6]:
                if qipan.block_list[min_i+1][min_j].sta != 5:
                    qipan.block_list[min_i+1][min_j].display_fgh = True
                    qipan.block_list[min_i+1][min_j].sta = 5
                    qipan.block_list[min_i+1][min_j].f = qipan.block_list[min_i][min_j].f + 10
                    qipan.block_list[min_i+1][min_j].h = 10*(abs(min_i+1-end_i)+abs(min_j-end_j))
                    qipan.block_list[min_i+1][min_j].g = qipan.block_list[min_i+1][min_j].f+qipan.block_list[min_i+1][min_j].h
                    qipan.block_list[min_i+1][min_j].parent = (min_i,min_j)
                else:
                    new_f = qipan.block_list[min_i][min_j].f + 10
                    if new_f<qipan.block_list[min_i+1][min_j].f:
                        qipan.block_list[min_i+1][min_j].f = new_f
                        qipan.block_list[min_i+1][min_j].g = qipan.block_list[min_i+1][min_j].f+qipan.block_list[min_i+1][min_j].h
                        qipan.block_list[min_i+1][min_j].parent = (min_i,min_j)
        if min_i+1<qipan.x and min_j+1<qipan.y:       
            if qipan.block_list[min_i+1][min_j+1].sta  not in[1,2,3,6]:
                if qipan.block_list[min_i+1][min_j+1].sta != 5:
                    qipan.block_list[min_i+1][min_j+1].display_fgh = True
                    qipan.block_list[min_i+1][min_j+1].sta = 5
                    qipan.block_list[min_i+1][min_j+1].f = qipan.block_list[min_i][min_j].f + 14
                    qipan.block_list[min_i+1][min_j+1].h = 10*(abs(min_i+1-end_i)+abs(min_j+1-end_j))
                    qipan.block_list[min_i+1][min_j+1].g = qipan.block_list[min_i+1][min_j+1].f+qipan.block_list[min_i+1][min_j+1].h
                    qipan.block_list[min_i+1][min_j+1].parent = (min_i,min_j)
                else:
                    new_f = qipan.block_list[min_i][min_j].f + 14
                    if new_f<qipan.block_list[min_i+1][min_j+1].f:
                        qipan.block_list[min_i+1][min_j+1].f = new_f
                        qipan.block_list[min_i+1][min_j+1].g = qipan.block_list[min_i+1][min_j+1].f+qipan.block_list[min_i+1][min_j+1].h
                        qipan.block_list[min_i+1][min_j+1].parent = (min_i,min_j)
        flag = judge_end(qipan,min_i,min_j)
        return flag
		
		
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
    step = 0
    has_start = False
    has_end = False
    period = 1
    end_flag = False
    while True:
        if period ==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    j = int(x/BLOCK_LEN)
                    i = int(y/BLOCK_LEN)
                    if qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        step = 1
                    if qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        step = 2
                    if qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        step = 3
                    if qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        if has_start and has_end:
                            period = 2
                            first_time = True
                        else:
                            pass
                    if 0<=x<=qipan.x*BLOCK_LEN and 0<=y<=qipan.y*BLOCK_LEN:
                        if step == 0:
                            pass
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
                            if special == 2:
                                has_end = False
                    display(qipan,screen)
                else:
                    time.sleep(t)
        if period == 2:
            if first_time:
                qipan.update_all()
                display(qipan,screen,1)
                first_time =False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    j = int(x/BLOCK_LEN)
                    i = int(y/BLOCK_LEN)
                    if qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        for i in range(qipan.x):
                            for j in range(qipan.y):
                                if qipan.block_list[i][j].sta == 1:
                                    qipan.block_list[i][j].display_fgh = True
                    elif qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+10<=y<=qipan.y*BLOCK_LEN+50:
                        end_flag = False
                        for i in range(qipan.x):
                            for j in range(qipan.y):
                                if qipan.block_list[i][j].sta in [4,5,6]:
                                    qipan.block_list[i][j].sta = 0
                                qipan.block_list[i][j].display_fgh = False
                                qipan.block_list[i][j].f = 0
                                qipan.block_list[i][j].g = 0
                                qipan.block_list[i][j].h = 0
                                qipan.block_list[i][j].parent = (-1,-1)
                        for i in range(qipan.x):
                            for j in range(qipan.y):
                                if qipan.block_list[i][j].sta == 1:
                                    qipan.block_list[i][j].display_fgh = True
                    elif qipan.x*BLOCK_LEN/4-50<=x<=qipan.x*BLOCK_LEN/4+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        if not end_flag:
                            end_flag = step_search(qipan)
                        else:
                            end_i,end_j = get_point(qipan,2)
                            if qipan.block_list[end_i][end_j].parent ==(-1,-1):
                                pass
                            else:
                                find_best_route(qipan)
                    elif qipan.x*BLOCK_LEN/4*3-50<=x<=qipan.x*BLOCK_LEN/4*3+50 and qipan.y*BLOCK_LEN+60<=y<=qipan.y*BLOCK_LEN+100:
                        while not end_flag:
                            end_flag = step_search(qipan)
                        end_i,end_j = get_point(qipan,2)
                        if qipan.block_list[end_i][end_j].parent ==(-1,-1):
                            pass
                        else:
                            find_best_route(qipan)
                    qipan.update_all()
                    display(qipan,screen,1)
                else:
                    time.sleep(t)
					
					
					
TIME = 0
BLOCK_LEN = 80
BLANK_HEIGHT = 170

if __name__ =="__main__":
    main(TIME)
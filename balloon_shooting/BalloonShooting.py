import pygame, random
from pygame.locals import *
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
PLAYER_SPEED = 1
BALLOON_SIZE = 40
BALLOON_SPEED = 0.1
BULLET_SPEED = 0.4
BALLOON_COUNT = 6
BULLET_SIZE = 10

# Khởi tạo biến để lưu điểm số
score = 0
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK     = (  0, 0, 0)

color =[
NAVYBLUE,
WHITE ,
BLACK,
RED ,
GREEN ,
BLUE  ,
YELLOW ,
ORANGE ,
PURPLE ,
CYAN ]

#######################
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-PLAYER_SIZE]
balloon_list = []#Danh sách bóng, 
bullet_list = []
bullet_pos = []
# Khởi động số lượng bóng
for i in range(BALLOON_COUNT):
    balloon_pos = [random.randint(0, SCREEN_WIDTH - BALLOON_SIZE),random.randint(-100, 0),GRAY]
    #balloon_pos là phần của balloon_list, là ds con với balloon_pos[0]: ví trí X, balloon_pos[1]: ví trí Y,balloon_pos[2]: màu của bóng
    balloon_list.append(balloon_pos)
pygame.init()

bg = pygame.image.load("image/background.png")#đọc ảnh từ folder
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ballon Shooting")

# Hàm vẽ các đối tượng, Súng, đạn, bóng 

def draw_objects():
   
    screen.blit(bg, (0, 0))
   ### Vẽ player- hình tam giác
    pygame.draw.polygon(screen, YELLOW, ((player_pos[0]-PLAYER_SIZE, player_pos[1]+PLAYER_SIZE),((player_pos[0], player_pos[1])),
                                                  ((player_pos[0]+PLAYER_SIZE, player_pos[1]+PLAYER_SIZE))))
   ## Vẽ bullet
    for bullet_pos in bullet_list:
      
        pygame.draw.ellipse(screen, RED, (bullet_pos[0], bullet_pos[1],BULLET_SIZE,BULLET_SIZE),BULLET_SIZE)
       
        if bullet_pos[1]<=0:#Nếu lên hết màn hình thì xóa
            bullet_list.remove(bullet_pos)
            
    ## Vẽ balloon
    for balloon_pos in balloon_list:
        ball_color =  balloon_pos[2]#Lấy màu của bóng
        if ball_color==BLACK:#Nếu bóng màu đen thì là vật phẩm, vẽ hình ngôi sao
       
            pygame.draw.polygon(screen, RED,( 
                                            (balloon_pos[0], balloon_pos[1])
                                            ,(balloon_pos[0]+BALLOON_SIZE/6, balloon_pos[1]+BALLOON_SIZE*2/6)
                                            ,(balloon_pos[0]-BALLOON_SIZE/6, balloon_pos[1]+BALLOON_SIZE*2/6)
                                            
                                            ))
            pygame.draw.polygon(screen, BLUE,( 
                                            
                                            (balloon_pos[0]+BALLOON_SIZE/8, balloon_pos[1]+BALLOON_SIZE*2/8)
                                            ,(balloon_pos[0]-BALLOON_SIZE/2, balloon_pos[1]+BALLOON_SIZE*2/6)
                                            ,(balloon_pos[0]+BALLOON_SIZE*2/6, balloon_pos[1]+BALLOON_SIZE*4/6)
                                            
                                            ))
            pygame.draw.polygon(screen, GREEN,( 
                                            
                                            (balloon_pos[0]-BALLOON_SIZE/8, balloon_pos[1]+BALLOON_SIZE*2/8)
                                            ,(balloon_pos[0]+BALLOON_SIZE/2, balloon_pos[1]+BALLOON_SIZE*2/6)
                                            ,(balloon_pos[0]-BALLOON_SIZE*2/6, balloon_pos[1]+BALLOON_SIZE*4/6)
                                            
                                            ))
         
        else:
            pygame.draw.ellipse(screen, ball_color, (balloon_pos[0], balloon_pos[1],BALLOON_SIZE, BALLOON_SIZE),BALLOON_SIZE)

# Thay đổi vị trí của balloon (để chạy từ trên xuống)
def update_bullet():
       
    for i in range(len(bullet_list)):
        if bullet_list[i][1] > 0:
            bullet_list[i][1] -= BULLET_SPEED
         
           
# Thay đổi vị trí của balloon (để chạy từ trên xuống)
def update_balloon():
    
    for i in range(len(balloon_list)):
        if balloon_list[i][1] >= SCREEN_HEIGHT:##Bóng trôi hết màn hình, nghĩa là bắn không trúng
            return False # Thất bại, game over
        
        if balloon_list[i][2] == GRAY:#Nghĩa là bóng ở của phần tử i sẽ biến mất và tạo lại trên đầu màn hình

            c=random.choice(color)# lấy màu ngẫu nhiên trong list color
            space =True
            new_X = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)# Lấy ngẫu nhiên vị trí X của bóng
            # Kiểm tra để tránh balloon chồng lên nhau
            for j in range(len(balloon_list)):
                if abs(new_X-balloon_list[j][0])<BALLOON_SIZE: #Nếu tọa độ X ngẫu nhiên nằm trong phạm vi của 1 trong các balloon thì bỏ qua
                     space =False
                     break
            if(space):#Chỉ gán tọa độ X cho balloon nếu nằm ngoài các tất cả các balloon còn lại
                balloon_list[i][0] =new_X                                    # Tọa độ x của balloon thứ i
            balloon_list[i][1] = random.randint(-100, 0)                     # Tọa độ y của balloon thứ i
            balloon_list[i][2] = (c)                                         # Màu của balloon thứ i

        else:
            balloon_list[i][1] += ball_speed
    return True       
    
# Hàm xử lý ăn vật phẩm( bóng nhấp nháy)
def get_item():
    for balloon_pos in balloon_list:
       
            if detect_collision(player_pos, balloon_pos):
               if(balloon_pos[2]==BLACK):#Bóng màu đen - là vật phẩm (ngôi sao)
                    balloon_pos[2]=GRAY #  Khi balloon bóng chạm player sẽ có màu GRAY (để biến mất)
                    return 1 #Khi bắn trúng, trả về 1 để tính điểm
    return 0

# Hàm xử lý khi bắn trúng bóng
def shoot_target():
    for balloon_pos in balloon_list:
        for bullet_pos in bullet_list:
            if detect_collision(bullet_pos, balloon_pos):
                bullet_list.remove(bullet_pos)# Xóa viên đạn trúng bóng
                balloon_pos[2]=GRAY # Khi balloon bị trúng đạn sẽ có màu GRAY(Để biến mất)
                
                return 1 #Khi bắn trúng, trả về 1 để tính điểm
    return 0

# Hàm kiểm tra va cham ( đạn và bóng)
def detect_collision(obj1_pos, obj2_pos):
    obj1_x = obj1_pos[0]
    obj1_y = obj1_pos[1]
    obj2_x = obj2_pos[0]
    obj2_y = obj2_pos[1]
    if (obj1_x >= obj2_x and obj1_x < (obj2_x + BALLOON_SIZE)) or (obj2_x >= obj1_x and obj2_x < (obj1_x + BULLET_SIZE)):
        if (obj1_y >= obj2_y and obj1_y < (obj2_y + BALLOON_SIZE)) or (obj2_y >= obj1_y and obj2_y < (obj1_y + BULLET_SIZE)):
            return True
    return False

# Hàm nắm bắt sự kiện nhấn phím
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        # Xác định các phím đang được giữ
    keys = pygame.key.get_pressed()
    # Di chuyển súng
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH:
        player_pos[0] += PLAYER_SPEED
        
    # Khi bấm phím Space, sẽ thêm 1 viên đạn vào bullet_list
    if keys[pygame.K_SPACE]:
        if(len(bullet_list))==0 or bullet_list[len(bullet_list)-1][1]<=player_pos[1]-BALLOON_SIZE:#Khoảng cách mỗi viên đạn ít nhất phải bằng balloon_size
          
            bullet_pos = [player_pos[0]-BULLET_SIZE/2, player_pos[1]]
            bullet_list.append(bullet_pos)
    return True

#Hàm hiển thị game over
def game_over():
    font = pygame.font.SysFont('consolas', 60)
    headingSuface = font.render('GAME OVER', True, (255, 0, 0))
    headingSize = headingSuface.get_size()

    font = pygame.font.SysFont('consolas', 20)
    commentSuface = font.render('Press "ESC" to replay', True, (0, 0, 255))
    commentSize = commentSuface.get_size()
    
      
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:#Nhấn ESC để chơi lại
                    return True
                
        c=random.choice(color)#Chọn màu ngẫu nhiên liên tục để làm Player nhấp nháy khi Game over
        pygame.draw.polygon(screen, c, ((player_pos[0]-PLAYER_SIZE, player_pos[1]+PLAYER_SIZE),((player_pos[0], player_pos[1])),
                                                  ((player_pos[0]+PLAYER_SIZE, player_pos[1]+PLAYER_SIZE))))
        
        screen.blit(headingSuface, (int((SCREEN_WIDTH - headingSize[0])/2), 100))
        screen.blit(commentSuface, (int((SCREEN_WIDTH - commentSize[0])/2), 400))
        pygame.display.update()

playing = True
speedup=False
status= True
ball_speed=BALLOON_SPEED
bull_speed=BULLET_SPEED

# Vòng lặp chính của game
while playing: 
    
    draw_objects()
    if not handle_events():
        playing=False # Thoát game
    update_bullet()
    status=update_balloon()# Khi 1 quả bóng xuống đụng đáy màn hình, status=False, Game Over
           
    score +=shoot_target() #Bắn trúng bóng, score tăng lên 1
    if(get_item()==1):#Chạm vật phẩm 
        bull_speed +=0.1
    #Tăng tốc mỗi khi được 50 điểm
    if(speedup and score%50==0):
        ball_speed+=0.1
        speedup=False
    if(score%50!=0):
        speedup=True
        
    #font = pygame.font.Font(None, 25)
    font = pygame.font.SysFont('Times New Roman', 20,False,False)
    text = font.render("Điểm:         Tốc độ bóng:      Tốc độ đạn:"  , 1, WHITE)  
     
    screen.blit(text, (10, 10)) 
    text = font.render( str(score)+"                           "+str(int(ball_speed*10))+"                        "+str(int(bull_speed*10)), 1, RED)  
    screen.blit(text, (65, 10))
    
    pygame.display.update()
    
    # Xử lý game over
    if(not status):
        score=0
        ball_speed=BALLOON_SPEED
        playing= game_over()# Khi game over, nếu bấm phím ESC, hàm sẽ trả về True=>playing=True, game sẽ chơi lại
        speedup=False
        bull_speed=BULLET_SPEED
         #Đưa tất cả bóng lên đầu màn hình-Trường hợp chơi lại
        for i in range(len(balloon_list)):
            balloon_list[i][1] =random.randint(-100, 0)
            bullet_list.clear() #Xóa hết tất cả đạn

import pygame
import random
import time

pygame.init()

width = 800  
height = 600  
card_size = 120  
FPS = 60
countdown_time = 120  # Đếm ngược 2 phút

mint = (194, 219, 190)  
aqua = (77, 195, 194)    

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matching Game")
font = pygame.font.SysFont("Comic Sans MS", 30)

def load_images():
    images = []
    for i in range(1, 11):
        image = pygame.image.load(f'{i}.png')  
        image = pygame.transform.scale(image, (card_size, card_size))  # Chuyển hình ảnh sang dạng hình vuông 120x120
        images.append(image)
    return images

# Tạo 20 thẻ, gồm 10 bức tranh mõi bức 2 cái
def create_deck(images):
    deck = []
    for i, image in enumerate(images):
        deck.append({'id': i, 'image': image, 'rect': pygame.Rect(0, 0, card_size, card_size), 'flipped': False, 'matched': False})
        deck.append({'id': i, 'image': image, 'rect': pygame.Rect(0, 0, card_size, card_size), 'flipped': False, 'matched': False})
    random.shuffle(deck)
    return deck

{'id': i, 'number': image, 'flipped': False, 'matched': False}

def reset_game():
    global deck, score, first_card, second_card, start_time, game_over
    deck = create_deck(images)  
    score = 0 
    start_time = time.time()  # Reset lại tg
    game_over = False

    # Căn giữa vị trí giữa các thẻ
    for i, card in enumerate(deck):
        row = i // 5
        col = i % 5
        card['rect'].x = (width - (5 * (card_size + 10) - 10)) // 2 + col * (card_size + 10)  # Centering logic
        card['rect'].y = (height - (4 * (card_size + 10) - 10)) // 2 + row * (card_size + 10) + 30  # Adjust y-coordinate

    first_card = None
    second_card = None

def draw_screen(deck, score, remaining_time):
    screen.fill(mint)  
    text_surface = font.render("Matching Game", True, aqua)  
    screen.blit(text_surface, ((width - text_surface.get_width()) // 2, 10))  # Căn giữa các văn bản

    score_surface = font.render(f"Score: {score}", True, aqua)  
    screen.blit(score_surface, (width - score_surface.get_width() - 10, 10))  # Đặt vị trí số điểm

    time_surface = font.render(f"Time: {remaining_time // 60}:{remaining_time % 60:02d}", True, aqua)
    screen.blit(time_surface, (10, 10))  # Đặt vị trí tg

    for card in deck:
        if card['flipped'] or card['matched']:
            screen.blit(card['image'], card['rect'])
        else:
            pygame.draw.rect(screen, aqua, card['rect'])  

    pygame.display.flip()

def show_end_screen(message, score):
    screen.fill(mint)  
    end_surface = font.render(message, True, aqua)  # Thông báo kết thúc
    screen.blit(end_surface, ((width - end_surface.get_width()) // 2, height // 2 - 30))

    score_surface = font.render(f"Score: {score}", True, aqua)  # Hiển thị điểm sau khi chơi
    screen.blit(score_surface, ((width - score_surface.get_width()) // 2, height // 2 + 10))

    restart_surface = font.render("Click 'R' to play again", True, aqua)  # Thông báo chơi lại
    screen.blit(restart_surface, ((width - restart_surface.get_width()) // 2, height // 2 + 50))

    pygame.display.flip()

clock = pygame.time.Clock()
images = load_images()  
reset_game()  
running = True

while running:
    clock.tick(FPS)
    
    # Tính thời gian còn lại
    elapsed_time = time.time() - start_time
    remaining_time = int(countdown_time - elapsed_time)
    
    # Nếu hết tg mà chưa xong thì Thua cuộc
    if remaining_time <= 0 and not game_over:
        game_over = True
        show_end_screen("Game Over", score)
    # Nếu hoàn thành thành trc khi hết tg thì win    
    elif not game_over and all(card['matched'] for card in deck):
        game_over = True
        show_end_screen("You win!", score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit()  

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            reset_game()  

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            pos = pygame.mouse.get_pos()
            for card in deck:
                if card['rect'].collidepoint(pos) and not card['flipped'] and not card['matched']:
                    card['flipped'] = True
                    if first_card is None:
                        first_card = card
                    elif second_card is None:
                        second_card = card
                        # Kiểm tra cặp thẻ có trùng không
                        if first_card['id'] == second_card['id']:
                            score += 10
                            first_card['matched'] = True
                            second_card['matched'] = True
                        else:
                            score = max(0, score - 5)
                            draw_screen(deck, score, remaining_time)
                            pygame.display.flip()
                            pygame.time.wait(700)  # Đợi 0.7s trc khi úp lại nếu lật sai
                            first_card['flipped'] = False
                            second_card['flipped'] = False
                        first_card = None
                        second_card = None

    if not game_over:
        draw_screen(deck, score, remaining_time)

pygame.quit()
exit()

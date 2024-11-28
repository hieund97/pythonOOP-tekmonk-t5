import pygame
import random
import time

pygame.init()

rong_man_hinh = 600
cao_man_hinh = 600
man_hinh = pygame.display.set_mode((rong_man_hinh, cao_man_hinh))

trang = (255, 255, 255)
den = (0, 0, 0)
xanh = (0, 0, 255)
xanh_la = (0, 255, 0)
do = (255, 0, 0)

hang = 4 
cot = 4  
rong_o = rong_man_hinh // cot
cao_o = cao_man_hinh // hang

hinh_anh = [i for i in range(8)] * 2  # Tổng cộng 16 ô, mỗi cặp xuất hiện 2 lần
random.shuffle(hinh_anh)

lat = [[False for _ in range(cot)] for _ in range(hang)]
da_lat = []
doi_up = False
thoi_gian_lat_gan_nhat = 0
bat_dau_thoi_gian = time.time()
gioi_han_thoi_gian = 60  # 1 minute time limit

def ve_luoi():
    for i_hang in range(hang):
        for i_cot in range(cot):
            x = i_cot * rong_o
            y = i_hang * cao_o
            if lat[i_hang][i_cot]:
                pygame.draw.rect(man_hinh, xanh_la, (x, y, rong_o, cao_o))
                font = pygame.font.Font(None, 36)
                text_hinh = font.render(str(hinh_anh[i_hang * cot + i_cot]), True, den)
                man_hinh.blit(text_hinh, (x + rong_o // 2 - 10, y + cao_o // 2 - 10))
            else:
                pygame.draw.rect(man_hinh, xanh, (x, y, rong_o, cao_o))

    for i in range(1, hang):
        pygame.draw.line(man_hinh, den, (0, i * cao_o), (rong_man_hinh, i * cao_o), 2)
    for i in range(1, cot):
        pygame.draw.line(man_hinh, den, (i * rong_o, 0), (i * rong_o, cao_man_hinh), 2)

def lay_vi_tri_luoi(x, y):
    i_hang = y // cao_o
    i_cot = x // rong_o
    return i_hang, i_cot

def kiem_tra_thang():
    return all(all(hang) for hang in lat)

dang_chay = True
while dang_chay:
    man_hinh.fill(trang)
    ve_luoi()

    if doi_up and time.time() - thoi_gian_lat_gan_nhat > 1:
        h1, c1 = da_lat[0]
        h2, c2 = da_lat[1]
        lat[h1][c1] = False
        lat[h2][c2] = False
        da_lat = []
        doi_up = False

    thoi_gian_choi = time.time() - bat_dau_thoi_gian
    thoi_gian_con_lai = gioi_han_thoi_gian - thoi_gian_choi
    phut = int(thoi_gian_con_lai // 60)
    giay = int(thoi_gian_con_lai % 60)
    font_thoi_gian = pygame.font.Font(None, 36)
    text_thoi_gian = font_thoi_gian.render(f'Time Left: {phut:02}:{giay:02}', True, den)
    man_hinh.blit(text_thoi_gian, (rong_man_hinh // 2 - 70, 10))

    if thoi_gian_con_lai <= 0:
        font = pygame.font.Font(None, 74)
        text_thua = font.render("You Lose!", True, do)
        man_hinh.blit(text_thua, (rong_man_hinh // 2 - 100, cao_man_hinh // 2 - 50))
        pygame.display.flip()
        time.sleep(2)
        break

    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            dang_chay = False

        if su_kien.type == pygame.MOUSEBUTTONDOWN and not doi_up:
            mx, my = pygame.mouse.get_pos()
            h, c = lay_vi_tri_luoi(mx, my)

            if not lat[h][c] and len(da_lat) < 2:
                lat[h][c] = True
                da_lat.append((h, c))

            if len(da_lat) == 2:
                h1, c1 = da_lat[0]
                h2, c2 = da_lat[1]

                if hinh_anh[h1 * cot + c1] != hinh_anh[h2 * cot + c2]:
                    doi_up = True
                    thoi_gian_lat_gan_nhat = time.time()
                else:
                    da_lat = []

    if kiem_tra_thang():
        font = pygame.font.Font(None, 74)
        text_thang = font.render("You Win!", True, do)
        man_hinh.blit(text_thang, (rong_man_hinh // 2 - 100, cao_man_hinh // 2 - 50))
        pygame.display.flip()
        time.sleep(2)
        break

    pygame.display.flip()

pygame.quit()



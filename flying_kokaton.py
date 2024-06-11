import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr%3200
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img2,[-x+1600,0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(bg_img2, [-x+4800, 0]) 

        key_lst = pg.key.get_pressed()  # 全キーの押下状態を取得
        move_x,move_y = 0,0
        if key_lst[pg.K_UP]:  # 上矢印キーが押されたら
            move_y = -1
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            move_y = +1
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
            move_x = -1
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            move_x = +1
        screen.blit(kk_img,kk_rct)

        if not any(key_lst):
            move_x = -1
        elif key_lst[pg.K_RIGHT]:
            move_x = 1

        kk_rct.move_ip(move_x,move_y)

        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
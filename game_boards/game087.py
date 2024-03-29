# -*- coding: utf-8 -*-

import pygame
import random
import os

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.lvlc = mainloop.xml_conn.get_level_count(mainloop.m.game_dbid, mainloop.config.user_age_group)
        self.level = lc.Level(self, mainloop, self.lvlc[0], self.lvlc[1])
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 23, 14)

    def create_game_objects(self, level=1):
        self.board.decolorable = False
        self.board.draw_grid = False
        self.vis_buttons = [1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        if self.mainloop.scheme is None:
            s = 225  # random.randrange(150, 225, 5)
            v = 225  # random.randrange(190, 225, 5)
            h = random.randrange(0, 255, 5)
            color0 = ex.hsv_to_rgb(h, 40, 230)  # highlight 1
            color1 = ex.hsv_to_rgb(h, 70, v)  # highlight 2
            color2 = ex.hsv_to_rgb(h, s, v)  # normal color
            color4 = ex.hsv_to_rgb(h, s, 200)  # headers colour
        else:
            s = 150
            v = 225
            h = 170
            color0 = ex.hsv_to_rgb(h, 40, 230)  # highlight 1
            color1 = ex.hsv_to_rgb(h, 70, v)  # highlight 2
            color2 = ex.hsv_to_rgb(h, s, v)  # normal color
            color4 = ex.hsv_to_rgb(h, s, 200)  # headers colour

        # data = [x_count, y_count, range_from, range_to, max_sum_range, image]
        lvldata = self.mainloop.xml_conn.get_level_data(self.mainloop.m.game_dbid, self.mainloop.config.user_age_group,
                                                        self.level.lvl)
        self.chapters = self.mainloop.xml_conn.get_chapters(self.mainloop.m.game_dbid,
                                                            self.mainloop.config.user_age_group)

        self.level.games_per_lvl = (lvldata[1] - lvldata[0] + 1) * (lvldata[3] - lvldata[2] + 1)

        data = [lvldata[1] - lvldata[0] + 2, lvldata[3] - lvldata[2] + 2 + 3]
        if data[0] % 2 == 0:
            hsw = 2
        else:
            hsw = 1

        self.data = data
        self.layout.update_layout(data[0], data[1])
        self.board.level_start(data[0], data[1], self.layout.scale)

        self.unit_mouse_over = None
        self.units = []

        bottom1 = lvldata[0] - 1
        bottom2 = lvldata[2] - 1
        top1 = lvldata[1]
        top2 = lvldata[3]

        num1 = random.randrange(bottom1 + 1, top1 + 1)
        num2 = random.randrange(bottom2 + 1, top2 + 1)
        self.solution = [num1, num2, num1 * num2]
        self.sollen = len(str(self.solution[0]))

        self.digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        unique = set()

        # add index numbers
        for i in range(bottom1, top1 + 1):
            for j in range(bottom2, top2 + 1):
                if i == bottom1 or j == bottom2:
                    if lvldata[4] == 0:
                        color = color4
                    else:
                        if i == num1 and j == num2:
                            color = color0
                        elif (i == num1 or j == num2):
                            color = color1
                        else:
                            color = color4

                    if i == bottom1 and j == bottom2:
                        caption = ""
                    elif i == bottom1:
                        caption = str(j)
                    else:
                        caption = str(i)

                    self.board.add_unit(i - 1 - bottom1 + 1, j + 1 - bottom2 + 1, 1, 1, classes.board.Label, caption,
                                        color, "", 2)
                    self.board.units[-1].font_color = (255, 255, 255)

        # add the rest of the numbers
        for i in range(bottom1 + 1, top1 + 1):
            for j in range(bottom2 + 1, top2 + 1):
                if lvldata[4] == 0:
                    color = color0
                    font_color = color0

                else:
                    if i == num1 and j == num2:
                        color = color0
                    elif i == num1 or j == num2:
                        color = color1
                    else:
                        color = color2
                    font_color = color4

                mul = i * j
                unique.add(mul)
                caption = str(mul)
                self.board.add_unit(i - 1 - bottom1 + 1, j + 1 - bottom2 + 1, 1, 1, classes.board.Label, caption, color,
                                    "", 2)
                self.board.units[-1].font_color = font_color

        if self.mainloop.scheme is None:
            dc_img_src = os.path.join('unit_bg', "universal_sq_dc.png")
            door_bg_img_src = [os.path.join('unit_bg', "universal_sq_door.png"),
                               os.path.join('unit_bg', "universal_r2x1_door.png")]
        else:
            dc_img_src = None
            door_bg_img_src = [os.path.join('unit_bg', "universal_sq_door.png"),
                               os.path.join('unit_bg', "universal_r2x1_door.png")]

        bg_img_src = os.path.join('unit_bg', "universal_sq_bg.png")
        number_color = ex.hsv_to_rgb(h, self.mainloop.cl.bg_color_s, self.mainloop.cl.bg_color_v)
        font_color = [ex.hsv_to_rgb(h, self.mainloop.cl.font_color_s, self.mainloop.cl.font_color_v), ]

        # draw outline with selectable numbers
        self.multi = dict()

        x = (data[0] - 5) // 2
        y = 0
        captions = [str(self.solution[2]), chr(247), str(self.solution[1]), "="]

        for i in range(4):
            self.board.add_universal_unit(grid_x=x + i, grid_y=y, grid_w=1, grid_h=1, txt=captions[i],
                                          fg_img_src=None, bg_img_src=bg_img_src, dc_img_src=dc_img_src,
                                          bg_color=(0, 0, 0, 0), border_color=None, font_color=font_color,
                                          bg_tint_color=number_color, fg_tint_color=None,
                                          txt_align=(0, 0), font_type=2, multi_color=False, alpha=True,
                                          immobilized=True, fg_as_hover=False, mode=1)
        self.outline_all(0, 1)

        self.board.add_universal_unit(grid_x=x + 4, grid_y=y, grid_w=hsw, grid_h=1, txt="",
                                      fg_img_src=None, bg_img_src=door_bg_img_src[hsw-1], dc_img_src=None,
                                      bg_color=(0, 0, 0, 0), border_color=None, font_color=font_color,
                                      bg_tint_color=number_color, fg_tint_color=None,
                                      txt_align=(0, 0), font_type=2, multi_color=False, alpha=True,
                                      immobilized=True, fg_as_hover=False, mode=2)
        self.home_square = self.board.units[-1]
        self.home_square.checkable = True
        self.home_square.init_check_images()
        self.board.all_sprites_list.move_to_front(self.home_square)

    def handle(self, event):
        gd.BoardGame.handle(self, event)
        if not self.show_msg:
            if event.type == pygame.KEYDOWN and (event.key != pygame.K_RETURN and event.key != pygame.K_KP_ENTER):
                lhv = len(self.home_square.value)
                self.changed_since_check = True
                if event.key == pygame.K_BACKSPACE:
                    if lhv > 0:
                        self.home_square.value = self.home_square.value[0:lhv - 1]
                else:
                    char = event.unicode
                    if len(char) > 0 and lhv < self.sollen and char in self.digits:
                        self.home_square.value += char
                self.home_square.update_me = True
                self.mainloop.redraw_needed[0] = True
                self.auto_check_reset()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                self.check_result()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.auto_check_reset()

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)

    def auto_check_reset(self):
        self.home_square.set_display_check(None)

    def check_result(self):
        if self.home_square.value != "" and (int(self.home_square.value) == self.solution[0]):
            self.passed()
            self.home_square.set_display_check(True)
        else:
            self.home_square.set_display_check(False)
        self.mainloop.redraw_needed[0] = True

    def passed(self):
        self.level.next_board(self.d["Perfect!"])

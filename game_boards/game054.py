# -*- coding: utf-8 -*-

import pygame
import random

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self, mainloop, 10, 6)
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 11, 9)

    def create_game_objects(self, level=1):
        self.allow_unit_animations = False
        self.allow_teleport = False
        self.board.draw_grid = False

        color = ex.hsv_to_rgb(225, 15, 235)
        self.col_r = (255, 0, 0)
        self.col_g = (0, 255, 0)
        self.col_b = (0, 0, 255)
        self.col_k = (0, 0, 0)
        self.col_e = (255, 255, 255)
        colorkey = (2, 2, 2, 0)
        self.col_bg = (255, 255, 255)
        data = [32, 23]
        # stretch width to fit the screen size
        x_count = self.get_x_count(data[1], even=True)
        if x_count > 32:
            data[0] = x_count

        self.data = data
        self.vis_buttons = [1, 1, 1, 1, 1, 1, 1, 0, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0], data[1])
        scale = self.layout.scale
        self.board.level_start(data[0], data[1], scale)

        self.board.board_bg.initcolor = self.col_bg
        self.board.board_bg.color = self.col_bg
        self.board.board_bg.update_me = True
        self.guides = []

        self.board.moved = self.moved
        self.choice_list = []
        step = 255 / 20.0
        for i in range(21):
            self.choice_list.append(int(255 - i * step))

        self.picked = []
        self.indexes = [0, 0, 0]
        mn = 1

        for i in range(3):
            self.indexes[i] = random.randrange(0, len(self.choice_list) - mn)
            self.picked.append(self.choice_list[self.indexes[i]])

        y = data[1] - 3

        self.rgb_g = [y, y, y]
        self.rgbx3 = [self.col_k, self.col_k, self.col_k]

        if self.level.lvl == 1:
            posy = [y, self.indexes[1], self.indexes[2]]
        elif self.level.lvl == 2:
            posy = [self.indexes[0], y, self.indexes[2]]
        elif self.level.lvl == 3:
            posy = [self.indexes[0], self.indexes[1], y]

        elif self.level.lvl == 4:
            n = random.randint(0, 2)
            posy = [self.indexes[0], self.indexes[1], self.indexes[2]]
            posy[n] = y
        elif self.level.lvl == 5:
            n = random.randint(0, 2)
            posy = [y, y, y]
            posy[n] = self.indexes[n]
        else:
            posy = [y, y, y]

        #y -> indexes
        self.board.add_unit(1, posy[0], 2, 3, classes.board.ImgAlphaShip, "", (0, 0, 0, 0), "light_r.png", alpha=True)
        self.board.add_unit(4, posy[1], 2, 3, classes.board.ImgAlphaShip, "", (0, 0, 0, 0), "light_g.png", alpha=True)
        self.board.add_unit(7, posy[2], 2, 3, classes.board.ImgAlphaShip, "", (0, 0, 0, 0), "light_b.png", alpha=True)

        for each in self.board.ships:
            each.outline = False
            each.audible = False

        # add colour circles - canvas
        self.board.add_unit(10, 0, data[0] - 10, data[1], classes.board.Label, "", self.col_e, "", 0)

        self.canvas = self.board.units[0]
        self.canvas_center = [(self.canvas.grid_w * self.board.scale) // 2,
                              (self.canvas.grid_h * self.board.scale) // 2]

        # adding borders between the colour tubes
        self.board.add_unit(0, 0, 1, data[1], classes.board.Label, "", self.col_bg, "", 0)
        self.board.add_unit(3, 0, 1, data[1], classes.board.Label, "", self.col_bg, "", 0)
        self.board.add_unit(6, 0, 1, data[1], classes.board.Label, "", self.col_bg, "", 0)
        self.board.add_unit(9, 0, 1, data[1], classes.board.Label, "", self.col_bg, "", 0)

        # adding colour guides
        self.board.add_door(1, 0, 2, data[1], classes.board.Door, "", color, "", 0)
        self.board.units[-1].set_outline(self.col_r, 1)
        self.board.add_door(4, 0, 2, data[1], classes.board.Door, "", color, "", 0)
        self.board.units[-1].set_outline(self.col_g, 1)
        self.board.add_door(7, 0, 2, data[1], classes.board.Door, "", color, "", 0)
        self.board.units[-1].set_outline(self.col_b, 1)

        # adding colour strips
        self.board.add_door(1, data[1] - 1, 2, 1, classes.board.Door, "", self.col_r, "", 0, door_alpha=False)
        self.board.add_door(4, data[1] - 1, 2, 1, classes.board.Door, "", self.col_g, "", 0, door_alpha=False)
        self.board.add_door(7, data[1] - 1, 2, 1, classes.board.Door, "", self.col_b, "", 0, door_alpha=False)

        # black background
        self.board.add_door(1, 0, 2, data[1], classes.board.Door, "", self.col_k, "", 0, door_alpha=False)
        self.board.add_door(4, 0, 2, data[1], classes.board.Door, "", self.col_k, "", 0, door_alpha=False)
        self.board.add_door(7, 0, 2, data[1], classes.board.Door, "", self.col_k, "", 0, door_alpha=False)

        # guides
        self.board.add_door(1, data[1] - 2, 2, 2, classes.board.Label, "", colorkey, "", 21, alpha=True)
        self.guides.append(self.board.units[-1])
        self.board.add_door(4, data[1] - 2, 2, 2, classes.board.Label, "", colorkey, "", 21, alpha=True)
        self.guides.append(self.board.units[-1])
        self.board.add_door(7, data[1] - 2, 2, 2, classes.board.Label, "", colorkey, "", 21, alpha=True)
        self.guides.append(self.board.units[-1])

        for each in self.guides:
            each.font_color = self.col_e
            each.checkable = True
            each.init_check_images(1, 1.2)
            each.decolorable = False

        for i in [5, 6, 7, 8, 9, 10, 11, 12, 13]:
            if i > 7:
                self.board.all_sprites_list.move_to_back(self.board.units[i])
            else:
                self.board.all_sprites_list.move_to_front(self.board.units[i])

        self.canvas.set_outline((255, 75, 0), 1)
        self.canv = []
        for i in range(4):
            self.canv.append(
                pygame.Surface([self.canvas.grid_w * self.board.scale, self.canvas.grid_h * self.board.scale - 1]))

        self.board.all_sprites_list.move_to_back(self.board.board_bg)
        self.mix()

    def mix(self):
        if self.mainloop.android is not None:
            self.mix_quads()
        else:
            self.mix_circles()

    def mix_quads(self):
        for i in range(3):
            self.rgb_g[i] = self.board.ships[i].grid_y
        self.update_sliders()
        self.canv[3].fill(self.col_k)
        ct = self.canvas_center[:]
        bottom = ct[1] + 8 * self.board.scale
        unit = 2.9 * self.board.scale
        ct[1] = int(round(ct[1] - 0.2 * unit))
        q1 = [[ct[0], bottom],
              [ct[0] + 3 * unit, bottom - 5.2 * unit],
              [ct[0] + 2 * unit, bottom - 6 * unit],
              [ct[0] - 2 * unit, bottom - 6 * unit],
              [ct[0] - 3 * unit, bottom - 5.2 * unit]]

        # draw the three colour diamonds
        pygame.draw.polygon(self.canv[3], self.rgbx3[0], q1)
        pygame.draw.polygon(self.canv[3], self.rgbx3[1], ex.rotate_points(q1, ct, 120))
        pygame.draw.polygon(self.canv[3], self.rgbx3[2], ex.rotate_points(q1, ct, 240))

        # draw the intersection triangle
        scl = 0.854
        tria = [[ct[0], bottom],
                [ct[0] + 3 * unit * scl, bottom - 5.2 * unit * scl],
                [ct[0] - 3 * unit * scl, bottom - 5.2 * unit * scl]]
        cl = [self.rgbx3[i][i] for i in range(3)]
        pygame.draw.polygon(self.canv[3], cl, tria)

        radius2 = int(round(4.3 * self.board.scale))
        pygame.draw.circle(self.canv[3], self.picked, ct, radius2, 0)

        self.canvas.painting = self.canv[3].copy()
        self.canvas.update_me = True

    def mix_circles(self):
        for i in range(3):
            self.rgb_g[i] = self.board.ships[i].grid_y
        self.update_sliders()
        self.canv[3].fill(self.col_k)
        ct = self.canvas_center
        radius = 9 * self.board.scale
        radius2 = 5 * self.board.scale
        x = 1 * self.board.scale
        rect = [[ct[0], ct[1] - x], [ct[0] - x, ct[1] + x], [ct[0] + x, ct[1] + x]]
        for i in range(3):
            pygame.draw.circle(self.canv[i], self.rgbx3[i], rect[i], radius, 0)
            self.canv[3].blit(self.canv[i], [0, 0], special_flags=pygame.BLEND_ADD)

        pygame.draw.circle(self.canv[3], self.picked, ct, radius2, 0)

        self.canvas.painting = self.canv[3].copy()
        self.canvas.update_me = True

    def update_sliders(self):
        for i in range(3):
            strip = self.board.units[i + 8]
            strip.grid_y = self.rgb_g[i] + 3 - 3
            strip.grid_h = self.data[1] - strip.grid_y + 3
            col = []
            for each in strip.initcolor:
                if each > 0:
                    if strip.grid_y == 20:
                        col.append(0)
                    elif strip.grid_y == 0:
                        col.append(255)
                    else:
                        step = 255 / 20.0
                        col.append(int(255 - (strip.grid_y) * step))
                else:
                    col.append(0)
            self.rgbx3[i] = col
            strip.color = col
            strip.pos_update()
            strip.update_me = True

    def moved(self):
        self.mix()

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.auto_check_reset()

    def auto_check_reset(self):
        for each in self.guides:
            each.set_display_check(None)

    def update(self, game):
        game.fill((0, 0, 0))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def check_result(self):
        r = self.rgbx3[0][0]
        g = self.rgbx3[1][1]
        b = self.rgbx3[2][2]

        if self.picked != [r, g, b]:
            if self.picked[0] > r:
                self.guides[0].value = "???"
            elif self.picked[0] < r:
                self.guides[0].value = "???"
            else:
                self.guides[0].value = " "
                self.guides[0].set_display_check(True)

            if self.picked[1] > g:
                self.guides[1].value = "???"
            elif self.picked[1] < g:
                self.guides[1].value = "???"
            else:
                self.guides[1].value = " "
                self.guides[1].set_display_check(True)

            if self.picked[2] > b:
                self.guides[2].value = "???"
            elif self.picked[2] < b:
                self.guides[2].value = "???"
            else:
                self.guides[2].value = " "
                self.guides[2].set_display_check(True)

            self.level.try_again(silent=self.mainloop.speaker.talkative)

            for each in self.guides:
                each.update_me = True
        else:
            for each in self.guides:
                each.update_me = True
                each.set_display_check(True)
                each.value = ""
            self.level.next_board()
        self.mainloop.redraw_needed[0] = True

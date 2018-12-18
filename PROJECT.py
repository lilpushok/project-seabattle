import random
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QPushButton, QColorDialog
from PyQt5.QtGui import QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chooseUI()

    def restart(self):
        self.chooseUI()

    def get_coords(self, lab):
        for i in range(10):
            if lab in self.sp_labels[i]:
                return([i, self.sp_labels[i].index(lab)])

    def chooseUI(self):
        uic.loadUi('proj-start.ui', self)
        if 1:
            self.ship = []
            self.lin_p = []
            self.es1_p = []
            self.es2_p = []
            self.es3_p = []
            self.kr1_p = []
            self.kr2_p = []
            self.bo1_p = []
            self.bo2_p = []
            self.bo3_p = []
            self.bo4_p = []
            self.sp_buttons = [[self.Ba1, self.Ba2, self.Ba3, self.Ba4, self.Ba5,
                                self.Ba6, self.Ba7, self.Ba8, self.Ba9, self.Ba10],
                               [self.Bb1, self.Bb2, self.Bb3, self.Bb4, self.Bb5,
                                self.Bb6, self.Bb7, self.Bb8, self.Bb9, self.Bb10],
                               [self.Bc1, self.Bc2, self.Bc3, self.Bc4, self.Bc5,
                                self.Bc6, self.Bc7, self.Bc8, self.Bc9, self.Bc10],
                               [self.Bd1, self.Bd2, self.Bd3, self.Bd4, self.Bd5,
                                self.Bd6, self.Bd7, self.Bd8, self.Bd9, self.Bd10],
                               [self.Be1, self.Be2, self.Be3, self.Be4, self.Be5,
                                self.Be6, self.Be7, self.Be8, self.Be9, self.Be10],
                               [self.Bf1, self.Bf2, self.Bf3, self.Bf4, self.Bf5,
                                self.Bf6, self.Bf7, self.Bf8, self.Bf9, self.Bf10],
                               [self.Bg1, self.Bg2, self.Bg3, self.Bg4, self.Bg5,
                                self.Bg6, self.Bg7, self.Bg8, self.Bg9, self.Bg10],
                               [self.Bh1, self.Bh2, self.Bh3, self.Bh4, self.Bh5,
                                self.Bh6, self.Bh7, self.Bh8, self.Bh9, self.Bh10],
                               [self.Bi1, self.Bi2, self.Bi3, self.Bi4, self.Bi5,
                                self.Bi6, self.Bi7, self.Bi8, self.Bi9, self.Bi10],
                               [self.Bj1, self.Bj2, self.Bj3, self.Bj4, self.Bj5,
                                self.Bj6, self.Bj7, self.Bj8, self.Bj9, self.Bj10]]

            self.player_sea = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                               ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

            self.pushButton.clicked.connect(self.complete)
            self.Ba1.clicked.connect(lambda: self.fun(self.Ba1, '00'))
            self.Ba2.clicked.connect(lambda: self.fun(self.Ba2, '01'))
            self.Ba3.clicked.connect(lambda: self.fun(self.Ba3, '02'))
            self.Ba4.clicked.connect(lambda: self.fun(self.Ba4, '03'))
            self.Ba5.clicked.connect(lambda: self.fun(self.Ba5, '04'))
            self.Ba6.clicked.connect(lambda: self.fun(self.Ba6, '05'))
            self.Ba7.clicked.connect(lambda: self.fun(self.Ba7, '06'))
            self.Ba8.clicked.connect(lambda: self.fun(self.Ba8, '07'))
            self.Ba9.clicked.connect(lambda: self.fun(self.Ba9, '08'))
            self.Ba10.clicked.connect(lambda: self.fun(self.Ba10, '09'))
            self.Bb1.clicked.connect(lambda: self.fun(self.Bb1, '10'))
            self.Bb2.clicked.connect(lambda: self.fun(self.Bb2, '11'))
            self.Bb3.clicked.connect(lambda: self.fun(self.Bb3, '12'))
            self.Bb4.clicked.connect(lambda: self.fun(self.Bb4, '13'))
            self.Bb5.clicked.connect(lambda: self.fun(self.Bb5, '14'))
            self.Bb6.clicked.connect(lambda: self.fun(self.Bb6, '15'))
            self.Bb7.clicked.connect(lambda: self.fun(self.Bb7, '16'))
            self.Bb8.clicked.connect(lambda: self.fun(self.Bb8, '17'))
            self.Bb9.clicked.connect(lambda: self.fun(self.Bb9, '18'))
            self.Bb10.clicked.connect(lambda: self.fun(self.Bb10, '19'))
            self.Bc1.clicked.connect(lambda: self.fun(self.Bc1, '20'))
            self.Bc2.clicked.connect(lambda: self.fun(self.Bc2, '21'))
            self.Bc3.clicked.connect(lambda: self.fun(self.Bc3, '22'))
            self.Bc4.clicked.connect(lambda: self.fun(self.Bc4, '23'))
            self.Bc5.clicked.connect(lambda: self.fun(self.Bc5, '24'))
            self.Bc6.clicked.connect(lambda: self.fun(self.Bc6, '25'))
            self.Bc7.clicked.connect(lambda: self.fun(self.Bc7, '26'))
            self.Bc8.clicked.connect(lambda: self.fun(self.Bc8, '27'))
            self.Bc9.clicked.connect(lambda: self.fun(self.Bc9, '28'))
            self.Bc10.clicked.connect(lambda: self.fun(self.Bc10, '29'))
            self.Bd1.clicked.connect(lambda: self.fun(self.Bd1, '30'))
            self.Bd2.clicked.connect(lambda: self.fun(self.Bd2, '31'))
            self.Bd3.clicked.connect(lambda: self.fun(self.Bd3, '32'))
            self.Bd4.clicked.connect(lambda: self.fun(self.Bd4, '33'))
            self.Bd5.clicked.connect(lambda: self.fun(self.Bd5, '34'))
            self.Bd6.clicked.connect(lambda: self.fun(self.Bd6, '35'))
            self.Bd7.clicked.connect(lambda: self.fun(self.Bd7, '36'))
            self.Bd8.clicked.connect(lambda: self.fun(self.Bd8, '37'))
            self.Bd9.clicked.connect(lambda: self.fun(self.Bd9, '38'))
            self.Bd10.clicked.connect(lambda: self.fun(self.Bd10, '39'))
            self.Be1.clicked.connect(lambda: self.fun(self.Be1, '40'))
            self.Be2.clicked.connect(lambda: self.fun(self.Be2, '41'))
            self.Be3.clicked.connect(lambda: self.fun(self.Be3, '42'))
            self.Be4.clicked.connect(lambda: self.fun(self.Be4, '43'))
            self.Be5.clicked.connect(lambda: self.fun(self.Be5, '44'))
            self.Be6.clicked.connect(lambda: self.fun(self.Be6, '45'))
            self.Be7.clicked.connect(lambda: self.fun(self.Be7, '46'))
            self.Be8.clicked.connect(lambda: self.fun(self.Be8, '47'))
            self.Be9.clicked.connect(lambda: self.fun(self.Be9, '48'))
            self.Be10.clicked.connect(lambda: self.fun(self.Be10, '49'))
            self.Bf1.clicked.connect(lambda: self.fun(self.Bf1, '50'))
            self.Bf2.clicked.connect(lambda: self.fun(self.Bf2, '51'))
            self.Bf3.clicked.connect(lambda: self.fun(self.Bf3, '52'))
            self.Bf4.clicked.connect(lambda: self.fun(self.Bf4, '53'))
            self.Bf5.clicked.connect(lambda: self.fun(self.Bf5, '54'))
            self.Bf6.clicked.connect(lambda: self.fun(self.Bf6, '55'))
            self.Bf7.clicked.connect(lambda: self.fun(self.Bf7, '56'))
            self.Bf8.clicked.connect(lambda: self.fun(self.Bf8, '57'))
            self.Bf9.clicked.connect(lambda: self.fun(self.Bf9, '58'))
            self.Bf10.clicked.connect(lambda: self.fun(self.Bf10, '59'))
            self.Bg1.clicked.connect(lambda: self.fun(self.Bg1, '60'))
            self.Bg2.clicked.connect(lambda: self.fun(self.Bg2, '61'))
            self.Bg3.clicked.connect(lambda: self.fun(self.Bg3, '62'))
            self.Bg4.clicked.connect(lambda: self.fun(self.Bg4, '63'))
            self.Bg5.clicked.connect(lambda: self.fun(self.Bg5, '64'))
            self.Bg6.clicked.connect(lambda: self.fun(self.Bg6, '65'))
            self.Bg7.clicked.connect(lambda: self.fun(self.Bg7, '66'))
            self.Bg8.clicked.connect(lambda: self.fun(self.Bg8, '67'))
            self.Bg9.clicked.connect(lambda: self.fun(self.Bg9, '68'))
            self.Bg10.clicked.connect(lambda: self.fun(self.Bg10, '69'))
            self.Bh1.clicked.connect(lambda: self.fun(self.Bh1, '70'))
            self.Bh2.clicked.connect(lambda: self.fun(self.Bh2, '71'))
            self.Bh3.clicked.connect(lambda: self.fun(self.Bh3, '72'))
            self.Bh4.clicked.connect(lambda: self.fun(self.Bh4, '73'))
            self.Bh5.clicked.connect(lambda: self.fun(self.Bh5, '74'))
            self.Bh6.clicked.connect(lambda: self.fun(self.Bh6, '75'))
            self.Bh7.clicked.connect(lambda: self.fun(self.Bh7, '76'))
            self.Bh8.clicked.connect(lambda: self.fun(self.Bh8, '77'))
            self.Bh9.clicked.connect(lambda: self.fun(self.Bh9, '78'))
            self.Bh10.clicked.connect(lambda: self.fun(self.Bh10, '79'))
            self.Bi1.clicked.connect(lambda: self.fun(self.Bi1, '80'))
            self.Bi2.clicked.connect(lambda: self.fun(self.Bi2, '81'))
            self.Bi3.clicked.connect(lambda: self.fun(self.Bi3, '82'))
            self.Bi4.clicked.connect(lambda: self.fun(self.Bi4, '83'))
            self.Bi5.clicked.connect(lambda: self.fun(self.Bi5, '84'))
            self.Bi6.clicked.connect(lambda: self.fun(self.Bi6, '85'))
            self.Bi7.clicked.connect(lambda: self.fun(self.Bi7, '86'))
            self.Bi8.clicked.connect(lambda: self.fun(self.Bi8, '87'))
            self.Bi9.clicked.connect(lambda: self.fun(self.Bi9, '88'))
            self.Bi10.clicked.connect(lambda: self.fun(self.Bi10, '89'))
            self.Bj1.clicked.connect(lambda: self.fun(self.Bj1, '90'))
            self.Bj2.clicked.connect(lambda: self.fun(self.Bj2, '91'))
            self.Bj3.clicked.connect(lambda: self.fun(self.Bj3, '92'))
            self.Bj4.clicked.connect(lambda: self.fun(self.Bj4, '93'))
            self.Bj5.clicked.connect(lambda: self.fun(self.Bj5, '94'))
            self.Bj6.clicked.connect(lambda: self.fun(self.Bj6, '95'))
            self.Bj7.clicked.connect(lambda: self.fun(self.Bj7, '96'))
            self.Bj8.clicked.connect(lambda: self.fun(self.Bj8, '97'))
            self.Bj9.clicked.connect(lambda: self.fun(self.Bj9, '98'))
            self.Bj10.clicked.connect(lambda: self.fun(self.Bj10, '99'))
            self.count = 0
            self.sp = []
        self.show()

    def neighboor(self, coord_let, coord_num):
        if coord_num > 0:
            b_west = self.sp_buttons[coord_let][coord_num - 1]
            s_west = self.player_sea[coord_let][coord_num - 1]
        else:
            s_west = '0'
            b_west = '0'
        if coord_num < 9:
            b_east = self.sp_buttons[coord_let][coord_num + 1]
            s_east = self.player_sea[coord_let][coord_num + 1]
        else:
            s_east = '0'
            b_east = '0'
        if coord_let > 0:
            b_north = self.sp_buttons[coord_let - 1][coord_num]
            s_north = self.player_sea[coord_let - 1][coord_num]
        else:
            s_north = '0'
            b_north = '0'
        if coord_let < 9:
            b_south = self.sp_buttons[coord_let + 1][coord_num]
            s_south = self.player_sea[coord_let + 1][coord_num]
        else:
            s_south = '0'
            b_south = '0'
        if coord_num > 0 and coord_let > 0:
            b_nw = self.sp_buttons[coord_let - 1][coord_num - 1]
            s_nw = self.player_sea[coord_let - 1][coord_num - 1]
        else:
            s_nw = '0'
            b_nw = '0'
        if coord_num < 9 and coord_let < 9:
            b_se = self.sp_buttons[coord_let + 1][coord_num + 1]
            s_se = self.player_sea[coord_let + 1][coord_num + 1]
        else:
            s_se = '0'
            b_se = '0'
        if coord_let > 0 and coord_num < 9:
            b_ne = self.sp_buttons[coord_let - 1][coord_num + 1]
            s_ne = self.player_sea[coord_let - 1][coord_num + 1]
        else:
            s_ne = '0'
            b_ne = '0'
        if coord_let < 9 and coord_num > 0:
            b_sw = self.sp_buttons[coord_let + 1][coord_num - 1]
            s_sw = self.player_sea[coord_let + 1][coord_num - 1]
        else:
            s_sw = '0'
            b_sw = '0'
        sp = [[s_west, s_east, s_north, s_south, s_nw, s_se, s_ne, s_sw],
              [b_west, b_east, b_north, b_south, b_nw, b_se, b_ne, b_sw]]
        return sp

    def fun(self, Button, button_coords):
        if Button.text() == '-' and self.count < 20:
            coord_let = int(button_coords[0])
            coord_num = int(button_coords[1])
            sp1 = self.neighboor(coord_let, coord_num)[0]
            sp2 = self.neighboor(coord_let, coord_num)[1]
            self.player_sea[coord_let][coord_num] = '+'
            if ('+' in sp1 and self.count not in [3, 6, 9, 11, 13, 15, 16, 17, 18,
                                                  19]) or self.count in [0, 4, 7, 10, 12, 14]:
                self.count += 1
                self.sp.append([coord_let, coord_num])
                Button.setText('+')
                self.ship.append([coord_let, coord_num])
                Button.setStyleSheet("background-color: {}".format('#00ff00'))
                for i in range(4):
                    if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                        sp2[i + 4].setText('/')
                if self.count < 4:
                    self.super_label.setText('Расставьте четырёхпалубный корабль:')
                if self.count == 4:
                    self.super_label.setText('Расставьте трёхпалубные корабли:')
                if self.count == 10:
                    self.super_label.setText('Расставьте двухпалубные корабли:')
                if self.count == 16:
                    self.super_label.setText('Расставьте однопалубные корабли:')
                if self.count == 20:
                    self.super_label.setText('')
                    self.pushButton.setStyleSheet("background-color: {}".format('#00ff00'))
            elif ('+' in sp1 and self.count in [3, 6, 9, 11, 13, 15]) or self.count in [16, 17, 18,
                                                                                        19]:
                self.count += 1
                self.ship.append([coord_let, coord_num])
                if self.count == 4:
                    self.lin_p = self.ship.copy()
                    self.ship = []
                elif self.count == 7:
                    self.kr1_p = self.ship.copy()
                    self.ship = []
                elif self.count == 10:
                    self.kr2_p = self.ship.copy()
                    self.ship = []
                elif self.count == 12:
                    self.es1_p = self.ship.copy()
                    self.ship = []
                elif self.count == 14:
                    self.es2_p = self.ship.copy()
                    self.ship = []
                elif self.count == 16:
                    self.es3_p = self.ship.copy()
                    self.ship = []
                elif self.count == 17:
                    self.bo1_p = self.ship.copy()
                    self.ship = []
                elif self.count == 18:
                    self.bo2_p = self.ship.copy()
                    self.ship = []
                elif self.count == 19:
                    self.bo3_p = self.ship.copy()
                    self.ship = []
                elif self.count == 20:
                    self.bo4_p = self.ship.copy()
                    self.ship = []
                Button.setText('+')
                Button.setStyleSheet("background-color: {}".format('#00ff00'))
                self.player_sea[coord_let][coord_num] = '+'
                for i in range(8):
                    if sp1[i] == '-' or sp1[i] == '/':
                        sp2[i].setText('/')
                for i in self.sp:
                    coord_let, coord_num = i[0], i[1]
                    sp1 = self.neighboor(coord_let, coord_num)[0]
                    sp2 = self.neighboor(coord_let, coord_num)[1]
                    for i in range(8):
                        if sp1[i] == '-' or sp1[i] == '/':
                            sp2[i].setText('/')
                if 1:
                    if self.count == 4:
                        self.super_label.setText('Расставьте трёхпалубные корабли:')
                    if self.count == 10:
                        self.super_label.setText('Расставьте двухпалубные корабли:')
                    if self.count == 16:
                        self.super_label.setText('Расставьте однопалубные корабли:')
                    if self.count == 20:
                        self.super_label.setText('')
                        self.pushButton.setStyleSheet("background-color: {}".format('#00ff00'))

    def complete(self):
        if self.count >= 20:
            self.gameUI()

    def gameUI(self):
        uic.loadUi('project.ui', self)
        if 1:
            self.turn = 0
            self.player_counter = 10
            self.computer_counter = 20
            self.zero_prioryty_ship = []
            self.deads = ['0']
            self.sp_labels = [[self.la1, self.la2, self.la3, self.la4, self.la5,
                               self.la6, self.la7, self.la8, self.la9, self.la10],
                              [self.lb1, self.lb2, self.lb3, self.lb4, self.lb5,
                               self.lb6, self.lb7, self.lb8, self.lb9, self.lb10],
                              [self.lc1, self.lc2, self.lc3, self.lc4, self.lc5,
                               self.lc6, self.lc7, self.lc8, self.lc9, self.lc10],
                              [self.ld1, self.ld2, self.ld3, self.ld4, self.ld5,
                               self.ld6, self.ld7, self.ld8, self.ld9, self.ld10],
                              [self.le1, self.le2, self.le3, self.le4, self.le5,
                               self.le6, self.le7, self.le8, self.le9, self.le10],
                              [self.lf1, self.lf2, self.lf3, self.lf4, self.lf5,
                               self.lf6, self.lf7, self.lf8, self.lf9, self.lf10],
                              [self.lg1, self.lg2, self.lg3, self.lg4, self.lg5,
                               self.lg6, self.lg7, self.lg8, self.lg9, self.lg10],
                              [self.lh1, self.lh2, self.lh3, self.lh4, self.lh5,
                               self.lh6, self.lh7, self.lh8, self.lh9, self.lh10],
                              [self.li1, self.li2, self.li3, self.li4, self.li5,
                               self.li6, self.li7, self.li8, self.li9, self.li10],
                              [self.lj1, self.lj2, self.lj3, self.lj4, self.lj5,
                               self.lj6, self.lj7, self.lj8, self.lj9, self.lj10]]
            for i in range(10):
                for o in range(10):
                    self.sp_labels[i][o].setText(' ' + self.player_sea[i][o])
            for i in range(4):
                self.lin_p[i] = self.sp_labels[self.lin_p[i][0]][self.lin_p[i][1]]
            for i in range(3):
                self.kr1_p[i] = self.sp_labels[self.kr1_p[i][0]][self.kr1_p[i][1]]
            for i in range(3):
                self.kr2_p[i] = self.sp_labels[self.kr2_p[i][0]][self.kr2_p[i][1]]
            for i in range(2):
                self.es1_p[i] = self.sp_labels[self.es1_p[i][0]][self.es1_p[i][1]]
            for i in range(2):
                self.es2_p[i] = self.sp_labels[self.es2_p[i][0]][self.es2_p[i][1]]
            for i in range(2):
                self.es3_p[i] = self.sp_labels[self.es3_p[i][0]][self.es3_p[i][1]]
            for i in range(1):
                self.bo1_p[i] = self.sp_labels[self.bo1_p[i][0]][self.bo1_p[i][1]]
            for i in range(1):
                self.bo2_p[i] = self.sp_labels[self.bo2_p[i][0]][self.bo2_p[i][1]]
            for i in range(1):
                self.bo3_p[i] = self.sp_labels[self.bo3_p[i][0]][self.bo3_p[i][1]]
            for i in range(1):
                self.bo4_p[i] = self.sp_labels[self.bo4_p[i][0]][self.bo4_p[i][1]]

            if 1:
                self.sp_buttons = [[self.Ba1, self.Ba2, self.Ba3, self.Ba4, self.Ba5,
                                    self.Ba6, self.Ba7, self.Ba8, self.Ba9, self.Ba10],
                                   [self.Bb1, self.Bb2, self.Bb3, self.Bb4, self.Bb5,
                                    self.Bb6, self.Bb7, self.Bb8, self.Bb9, self.Bb10],
                                   [self.Bc1, self.Bc2, self.Bc3, self.Bc4, self.Bc5,
                                    self.Bc6, self.Bc7, self.Bc8, self.Bc9, self.Bc10],
                                   [self.Bd1, self.Bd2, self.Bd3, self.Bd4, self.Bd5,
                                    self.Bd6, self.Bd7, self.Bd8, self.Bd9, self.Bd10],
                                   [self.Be1, self.Be2, self.Be3, self.Be4, self.Be5,
                                    self.Be6, self.Be7, self.Be8, self.Be9, self.Be10],
                                   [self.Bf1, self.Bf2, self.Bf3, self.Bf4, self.Bf5,
                                    self.Bf6, self.Bf7, self.Bf8, self.Bf9, self.Bf10],
                                   [self.Bg1, self.Bg2, self.Bg3, self.Bg4, self.Bg5,
                                    self.Bg6, self.Bg7, self.Bg8, self.Bg9, self.Bg10],
                                   [self.Bh1, self.Bh2, self.Bh3, self.Bh4, self.Bh5,
                                    self.Bh6, self.Bh7, self.Bh8, self.Bh9, self.Bh10],
                                   [self.Bi1, self.Bi2, self.Bi3, self.Bi4, self.Bi5,
                                    self.Bi6, self.Bi7, self.Bi8, self.Bi9, self.Bi10],
                                   [self.Bj1, self.Bj2, self.Bj3, self.Bj4, self.Bj5,
                                    self.Bj6, self.Bj7, self.Bj8, self.Bj9, self.Bj10]]



                self.black = [self.la4, self.la8, self.lb3, self.lb7, self.lc2, self.lc6,
                              self.lc10, self.ld1, self.ld5, self.ld9, self.le4, self.le8,
                              self.lf3, self.lf7, self.lg2, self.lg6, self.lg10, self.lh1,
                              self.lh5, self.lh9, self.li4, self.li8, self.lj3, self.lj7]

                self.white = [self.lc4, self.lc8, self.ld3, self.ld7, self.la2, self.la6,
                              self.la10, self.lb1, self.lb5, self.lb9, self.lg4, self.lg8,
                              self.lh3, self.lh7, self.le2, self.le6, self.le10, self.lf1,
                              self.lf5, self.lf9, self.li2, self.li6, self.li10,
                              self.lj1, self.lj5, self.lj9]

                self.zero_prioryty = []

                self.first_prioryty = []

                self.second_prioryty = []

                self.red = [self.la1, self.la5, self.la9, self.lb4, self.lb8,
                            self.lc3, self.lc7, self.ld2, self.ld6, self.ld10,
                            self.le1, self.le5, self.le9, self.lf4, self.lf8,
                            self.lg3, self.lg7, self.lh2, self.lh6, self.lh10,
                            self.li1, self.li5, self.li9, self.lj4, self.lj8]

                self.blue = [self.la3, self.la7, self.lb2, self.lb6, self.lb10,
                             self.lc1, self.lc5, self.lc9, self.ld4, self.ld8,
                             self.le3, self.le7, self.lf2, self.lf6, self.lf10,
                             self.lg1, self.lg5, self.lg9, self.lh4, self.lh8,
                             self.li3, self.li7, self.lj2, self.lj6, self.lj10]

                self.third_prioryty = []

                list_list = [self.black, self.blue, self.red, self.white]

                self.first_prioryty = random.choice(list_list)
                if self.first_prioryty == self.black:
                    self.second_prioryty = self.white
                    self.third_prioryty = self.blue + self.red
                elif self.first_prioryty == self.white:
                    self.second_prioryty = self.black
                    self.third_prioryty = self.blue + self.red
                elif self.first_prioryty == self.red:
                    self.second_prioryty = self.blue
                    self.third_prioryty = self.black + self.white
                elif self.first_prioryty == self.blue:
                    self.second_prioryty = self.red
                    self.third_prioryty = self.black + self.white

                self.Ba1.clicked.connect(lambda: self.attack_comp(self.Ba1, '00'))
                self.Ba2.clicked.connect(lambda: self.attack_comp(self.Ba2, '01'))
                self.Ba3.clicked.connect(lambda: self.attack_comp(self.Ba3, '02'))
                self.Ba4.clicked.connect(lambda: self.attack_comp(self.Ba4, '03'))
                self.Ba5.clicked.connect(lambda: self.attack_comp(self.Ba5, '04'))
                self.Ba6.clicked.connect(lambda: self.attack_comp(self.Ba6, '05'))
                self.Ba7.clicked.connect(lambda: self.attack_comp(self.Ba7, '06'))
                self.Ba8.clicked.connect(lambda: self.attack_comp(self.Ba8, '07'))
                self.Ba9.clicked.connect(lambda: self.attack_comp(self.Ba9, '08'))
                self.Ba10.clicked.connect(lambda: self.attack_comp(self.Ba10, '09'))
                self.Bb1.clicked.connect(lambda: self.attack_comp(self.Bb1, '10'))
                self.Bb2.clicked.connect(lambda: self.attack_comp(self.Bb2, '11'))
                self.Bb3.clicked.connect(lambda: self.attack_comp(self.Bb3, '12'))
                self.Bb4.clicked.connect(lambda: self.attack_comp(self.Bb4, '13'))
                self.Bb5.clicked.connect(lambda: self.attack_comp(self.Bb5, '14'))
                self.Bb6.clicked.connect(lambda: self.attack_comp(self.Bb6, '15'))
                self.Bb7.clicked.connect(lambda: self.attack_comp(self.Bb7, '16'))
                self.Bb8.clicked.connect(lambda: self.attack_comp(self.Bb8, '17'))
                self.Bb9.clicked.connect(lambda: self.attack_comp(self.Bb9, '18'))
                self.Bb10.clicked.connect(lambda: self.attack_comp(self.Bb10, '19'))
                self.Bc1.clicked.connect(lambda: self.attack_comp(self.Bc1, '20'))
                self.Bc2.clicked.connect(lambda: self.attack_comp(self.Bc2, '21'))
                self.Bc3.clicked.connect(lambda: self.attack_comp(self.Bc3, '22'))
                self.Bc4.clicked.connect(lambda: self.attack_comp(self.Bc4, '23'))
                self.Bc5.clicked.connect(lambda: self.attack_comp(self.Bc5, '24'))
                self.Bc6.clicked.connect(lambda: self.attack_comp(self.Bc6, '25'))
                self.Bc7.clicked.connect(lambda: self.attack_comp(self.Bc7, '26'))
                self.Bc8.clicked.connect(lambda: self.attack_comp(self.Bc8, '27'))
                self.Bc9.clicked.connect(lambda: self.attack_comp(self.Bc9, '28'))
                self.Bc10.clicked.connect(lambda: self.attack_comp(self.Bc10, '29'))
                self.Bd1.clicked.connect(lambda: self.attack_comp(self.Bd1, '30'))
                self.Bd2.clicked.connect(lambda: self.attack_comp(self.Bd2, '31'))
                self.Bd3.clicked.connect(lambda: self.attack_comp(self.Bd3, '32'))
                self.Bd4.clicked.connect(lambda: self.attack_comp(self.Bd4, '33'))
                self.Bd5.clicked.connect(lambda: self.attack_comp(self.Bd5, '34'))
                self.Bd6.clicked.connect(lambda: self.attack_comp(self.Bd6, '35'))
                self.Bd7.clicked.connect(lambda: self.attack_comp(self.Bd7, '36'))
                self.Bd8.clicked.connect(lambda: self.attack_comp(self.Bd8, '37'))
                self.Bd9.clicked.connect(lambda: self.attack_comp(self.Bd9, '38'))
                self.Bd10.clicked.connect(lambda: self.attack_comp(self.Bd10, '39'))
                self.Be1.clicked.connect(lambda: self.attack_comp(self.Be1, '40'))
                self.Be2.clicked.connect(lambda: self.attack_comp(self.Be2, '41'))
                self.Be3.clicked.connect(lambda: self.attack_comp(self.Be3, '42'))
                self.Be4.clicked.connect(lambda: self.attack_comp(self.Be4, '43'))
                self.Be5.clicked.connect(lambda: self.attack_comp(self.Be5, '44'))
                self.Be6.clicked.connect(lambda: self.attack_comp(self.Be6, '45'))
                self.Be7.clicked.connect(lambda: self.attack_comp(self.Be7, '46'))
                self.Be8.clicked.connect(lambda: self.attack_comp(self.Be8, '47'))
                self.Be9.clicked.connect(lambda: self.attack_comp(self.Be9, '48'))
                self.Be10.clicked.connect(lambda: self.attack_comp(self.Be10, '49'))
                self.Bf1.clicked.connect(lambda: self.attack_comp(self.Bf1, '50'))
                self.Bf2.clicked.connect(lambda: self.attack_comp(self.Bf2, '51'))
                self.Bf3.clicked.connect(lambda: self.attack_comp(self.Bf3, '52'))
                self.Bf4.clicked.connect(lambda: self.attack_comp(self.Bf4, '53'))
                self.Bf5.clicked.connect(lambda: self.attack_comp(self.Bf5, '54'))
                self.Bf6.clicked.connect(lambda: self.attack_comp(self.Bf6, '55'))
                self.Bf7.clicked.connect(lambda: self.attack_comp(self.Bf7, '56'))
                self.Bf8.clicked.connect(lambda: self.attack_comp(self.Bf8, '57'))
                self.Bf9.clicked.connect(lambda: self.attack_comp(self.Bf9, '58'))
                self.Bf10.clicked.connect(lambda: self.attack_comp(self.Bf10, '59'))
                self.Bh1.clicked.connect(lambda: self.attack_comp(self.Bh1, '70'))
                self.Bh2.clicked.connect(lambda: self.attack_comp(self.Bh2, '71'))
                self.Bh3.clicked.connect(lambda: self.attack_comp(self.Bh3, '72'))
                self.Bh4.clicked.connect(lambda: self.attack_comp(self.Bh4, '73'))
                self.Bh5.clicked.connect(lambda: self.attack_comp(self.Bh5, '74'))
                self.Bh6.clicked.connect(lambda: self.attack_comp(self.Bh6, '75'))
                self.Bh7.clicked.connect(lambda: self.attack_comp(self.Bh7, '76'))
                self.Bh8.clicked.connect(lambda: self.attack_comp(self.Bh8, '77'))
                self.Bh9.clicked.connect(lambda: self.attack_comp(self.Bh9, '78'))
                self.Bh10.clicked.connect(lambda: self.attack_comp(self.Bh10, '79'))
                self.Bi1.clicked.connect(lambda: self.attack_comp(self.Bi1, '80'))
                self.Bi2.clicked.connect(lambda: self.attack_comp(self.Bi2, '81'))
                self.Bi3.clicked.connect(lambda: self.attack_comp(self.Bi3, '82'))
                self.Bi4.clicked.connect(lambda: self.attack_comp(self.Bi4, '83'))
                self.Bi5.clicked.connect(lambda: self.attack_comp(self.Bi5, '84'))
                self.Bi6.clicked.connect(lambda: self.attack_comp(self.Bi6, '85'))
                self.Bi7.clicked.connect(lambda: self.attack_comp(self.Bi7, '86'))
                self.Bi8.clicked.connect(lambda: self.attack_comp(self.Bi8, '87'))
                self.Bi9.clicked.connect(lambda: self.attack_comp(self.Bi9, '88'))
                self.Bi10.clicked.connect(lambda: self.attack_comp(self.Bi10, '89'))
                self.Bj1.clicked.connect(lambda: self.attack_comp(self.Bj1, '90'))
                self.Bj2.clicked.connect(lambda: self.attack_comp(self.Bj2, '91'))
                self.Bj3.clicked.connect(lambda: self.attack_comp(self.Bj3, '92'))
                self.Bj4.clicked.connect(lambda: self.attack_comp(self.Bj4, '93'))
                self.Bj5.clicked.connect(lambda: self.attack_comp(self.Bj5, '94'))
                self.Bj6.clicked.connect(lambda: self.attack_comp(self.Bj6, '95'))
                self.Bj7.clicked.connect(lambda: self.attack_comp(self.Bj7, '96'))
                self.Bj8.clicked.connect(lambda: self.attack_comp(self.Bj8, '97'))
                self.Bj9.clicked.connect(lambda: self.attack_comp(self.Bj9, '98'))
                self.Bj10.clicked.connect(lambda: self.attack_comp(self.Bj10, '99'))
                self.Bg1.clicked.connect(lambda: self.attack_comp(self.Bg1, '60'))
                self.Bg2.clicked.connect(lambda: self.attack_comp(self.Bg2, '61'))
                self.Bg3.clicked.connect(lambda: self.attack_comp(self.Bg3, '62'))
                self.Bg4.clicked.connect(lambda: self.attack_comp(self.Bg4, '63'))
                self.Bg5.clicked.connect(lambda: self.attack_comp(self.Bg5, '64'))
                self.Bg6.clicked.connect(lambda: self.attack_comp(self.Bg6, '65'))
                self.Bg7.clicked.connect(lambda: self.attack_comp(self.Bg7, '66'))
                self.Bg8.clicked.connect(lambda: self.attack_comp(self.Bg8, '67'))
                self.Bg9.clicked.connect(lambda: self.attack_comp(self.Bg9, '68'))
                self.Bg10.clicked.connect(lambda: self.attack_comp(self.Bg10, '69'))
            if 2:
                a = random.choice(range(10))
                if 1:
                    if a == 0:
                        self.computer_sea = [['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-']]
                        self.lin_c = [self.Ba1, self.Bb1, self.Bc1, self.Bd1]
                        self.kr1_c = [self.Bd3, self.Be3, self.Bf3]
                        self.kr2_c = [self.Bh3, self.Bi3, self.Bj3]
                        self.es1_c = [self.Bf1, self.Bg1]
                        self.es2_c = [self.Bi1, self.Bj1]
                        self.es3_c = [self.Ba3, self.Bb3]
                    elif a == 1:
                        self.computer_sea = [['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '/'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '/', '/', '/', '+'],
                                             ['/', '/', '-', '-', '-', '-', '/', '+', '/', '/'],
                                             ['+', '/', '-', '-', '-', '-', '/', '+', '/', '+'],
                                             ['+', '/', '-', '-', '-', '-', '/', '+', '/', '+'],
                                             ['+', '/', '-', '-', '-', '/', '/', '/', '/', '/'],
                                             ['/', '/', '-', '-', '-', '/', '+', '+', '+', '+']]
                        self.lin_c = [self.Bj7, self.Bj8, self.Bj9, self.Bj10]
                        self.kr1_c = [self.Bg1, self.Bh1, self.Bi1]
                        self.kr2_c = [self.Bf8, self.Bg8, self.Bh8]
                        self.es1_c = [self.Ba10, self.Bb10]
                        self.es2_c = [self.Bd10, self.Be10]
                        self.es3_c = [self.Bg10, self.Bh10]
                    elif a == 2:
                        self.computer_sea = [['/', '/', '+', '+', '/', '/', '+', '+', '/', '+'],
                                             ['+', '/', '/', '/', '/', '/', '/', '/', '/', '+'],
                                             ['+', '/', '+', '+', '+', '+', '/', '+', '/', '+'],
                                             ['+', '/', '/', '/', '/', '/', '/', '+', '/', '/'],
                                             ['/', '/', '-', '-', '-', '-', '/', '/', '/', '-'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
                        self.lin_c = [self.Bc3, self.Bc4, self.Bc5, self.Bc6]
                        self.kr1_c = [self.Ba10, self.Bb10, self.Bc10]
                        self.kr2_c = [self.Bb1, self.Bc1, self.Bd1]
                        self.es1_c = [self.Ba3, self.Ba4]
                        self.es2_c = [self.Ba7, self.Ba8]
                        self.es3_c = [self.Bc8, self.Bd8]
                    elif a == 3:
                        self.computer_sea = [['-', '-', '-', '-', '-', '-', '/', '+', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '/', '+', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '/', '+', '/', '+'],
                                             ['-', '-', '-', '-', '-', '/', '/', '/', '/', '/'],
                                             ['-', '-', '-', '-', '-', '/', '+', '/', '+', '+'],
                                             ['-', '-', '-', '-', '-', '/', '+', '/', '/', '/'],
                                             ['-', '-', '-', '-', '-', '/', '+', '/', '+', '+'],
                                             ['-', '-', '-', '-', '-', '/', '+', '/', '/', '/'],
                                             ['-', '-', '-', '-', '-', '/', '/', '/', '/', '/'],
                                             ['-', '-', '-', '-', '-', '-', '-', '/', '+', '+']]
                        self.lin_c = [self.Be7, self.Bf7, self.Bg7, self.Bh7]
                        self.kr1_c = [self.Ba8, self.Bb8, self.Bc8]
                        self.kr2_c = [self.Ba10, self.Bb10, self.Bc10]
                        self.es1_c = [self.Be9, self.Be10]
                        self.es2_c = [self.Bg9, self.Bg10]
                        self.es3_c = [self.Bj9, self.Bj10]
                    elif a == 4:
                        self.computer_sea = [['-', '-', '-', '-', '-', '-', '-', '/', '+', '+'],
                                             ['-', '-', '-', '-', '-', '-', '-', '/', '/', '/'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '/'],
                                             ['-', '-', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['/', '/', '/', '/', '/', '-', '-', '-', '/', '+'],
                                             ['+', '/', '/', '+', '/', '-', '-', '-', '/', '/'],
                                             ['+', '/', '/', '+', '/', '/', '/', '/', '/', '/'],
                                             ['+', '/', '/', '+', '/', '+', '+', '+', '+', '/']]
                        self.lin_c = [self.Bj6, self.Bj7, self.Bj8, self.Bj9]
                        self.kr1_c = [self.Bj1, self.Bi1, self.Bh1]
                        self.kr2_c = [self.Bj4, self.Bi4, self.Bh4]
                        self.es1_c = [self.Ba9, self.Ba10]
                        self.es2_c = [self.Bc10, self.Bd10]
                        self.es3_c = [self.Bf10, self.Bg10]
                    elif a == 5:
                        self.computer_sea = [['/', '/', '-', '-', '-', '-', '-', '/', '+', '+'],
                                             ['+', '/', '-', '-', '-', '-', '-', '/', '/', '/'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['/', '/', '-', '-', '-', '-', '-', '-', '/', '/'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '/', '+'],
                                             ['/', '/', '/', '-', '-', '-', '-', '-', '/', '+'],
                                             ['+', '+', '/', '-', '-', '-', '-', '-', '/', '/']]
                        self.lin_c = [self.Bf10, self.Bg10, self.Bh10, self.Bi10]
                        self.kr1_c = [self.Bb1, self.Bc1, self.Bd1]
                        self.kr2_c = [self.Bf1, self.Bg1, self.Bh1]
                        self.es1_c = [self.Bj1, self.Bj2]
                        self.es2_c = [self.Ba9, self.Ba10]
                        self.es3_c = [self.Bc10, self.Bd10]
                    elif a == 6:
                        self.computer_sea = [['+', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '-', '-', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '+', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '/', '/', '/', '/', '/', '/'],
                                             ['+', '+', '+', '+', '/', '+', '+', '/', '+', '+']]
                        self.lin_c = [self.Bj1, self.Bj4, self.Bj2, self.Bj3]
                        self.kr1_c = [self.Bh1, self.Bh2, self.Bh3]
                        self.kr2_c = [self.Ba1, self.Bb1, self.Bc1]
                        self.es1_c = [self.Be1, self.Bf1]
                        self.es2_c = [self.Bj6, self.Bj7]
                        self.es3_c = [self.Bj9, self.Bj10]
                    elif a == 7:
                        self.computer_sea = [['+', '+', '/', '-', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '/', '-', '-', '-', '-', '-'],
                                             ['/', '+', '/', '+', '/', '-', '-', '-', '-', '-'],
                                             ['/', '+', '/', '+', '/', '-', '-', '-', '-', '-'],
                                             ['/', '+', '/', '/', '/', '/', '-', '-', '-', '-'],
                                             ['/', '+', '/', '+', '+', '/', '-', '-', '-', '-']]
                        self.lin_c = [self.Bg2, self.Bh2, self.Bi2, self.Bj2]
                        self.kr1_c = [self.Bc1, self.Bd1, self.Be1]
                        self.kr2_c = [self.Bc3, self.Bd3, self.Be3]
                        self.es1_c = [self.Ba1, self.Ba2]
                        self.es2_c = [self.Bg4, self.Bh4]
                        self.es3_c = [self.Bj4, self.Bj5]
                    elif a == 8:
                        self.computer_sea = [['/', '/', '+', '+', '+', '/', '-', '-', '-', '-'],
                                             ['+', '/', '/', '/', '/', '/', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '+', '/', '-', '-', '-', '-', '-', '-']]
                        self.lin_c = [self.Bb1, self.Bc1, self.Bd1, self.Be1]
                        self.kr1_c = [self.Ba3, self.Ba4, self.Ba5]
                        self.kr2_c = [self.Bg1, self.Bh1, self.Bi1]
                        self.es1_c = [self.Bc3, self.Bd3]
                        self.es2_c = [self.Bf3, self.Bg3]
                        self.es3_c = [self.Bi3, self.Bj3]
                    elif a == 9:
                        self.computer_sea = [['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '+', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['/', '/', '/', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '+', '/', '-', '-', '-', '-', '-', '-'],
                                             ['+', '/', '/', '/', '/', '-', '-', '-', '-', '-'],
                                             ['/', '/', '+', '+', '/', '-', '-', '-', '-', '-']]
                        self.lin_c = [self.Bf1, self.Bg1, self.Bh1, self.Bi1]
                        self.kr1_c = [self.Bd1, self.Bd2, self.Bd3]
                        self.kr2_c = [self.Bf3, self.Bg3, self.Bh3]
                        self.es1_c = [self.Ba1, self.Bb1]
                        self.es2_c = [self.Ba3, self.Bb3]
                        self.es3_c = [self.Bj3, self.Bj4]
                self.bo1_c = []
                self.bo2_c = []
                self.bo3_c = []
                self.bo4_c = []
                self.sppt = [self.bo1_c, self.bo2_c, self.bo3_c, self.bo4_c]
                for i in range(4):
                    a = self.free_comp_sea(self.computer_sea)
                    boat = random.choice(a)
                    coord_let = int(boat[1])
                    coord_num = int(boat[2])
                    true_boat = self.sp_buttons[coord_let][coord_num]
                    self.computer_sea[coord_let][coord_num] = '+'
                    if coord_let > 0:
                        self.computer_sea[coord_let - 1][coord_num] = '/'
                    if coord_let < 9:
                        self.computer_sea[coord_let + 1][coord_num] = '/'
                    if coord_num > 0:
                        self.computer_sea[coord_let][coord_num - 1] = '/'
                    if coord_num < 9:
                        self.computer_sea[coord_let][coord_num + 1] = '/'
                    if coord_let > 0 and coord_num > 0:
                        self.computer_sea[coord_let - 1][coord_num - 1] = '/'
                    if coord_let > 0 and coord_num < 9:
                        self.computer_sea[coord_let - 1][coord_num + 1] = '/'
                    if coord_let < 9 and coord_num > 0:
                        self.computer_sea[coord_let + 1][coord_num - 1] = '/'
                    if coord_let < 9 and coord_num < 9:
                        self.computer_sea[coord_let + 1][coord_num + 1] = '/'
                    if i == 0:
                        self.bo1_c = [true_boat]
                    elif i == 1:
                        self.bo2_c = [true_boat]
                    elif i == 2:
                        self.bo3_c = [true_boat]
                    elif i == 3:
                        self.bo4_c = [true_boat]

                self.es1 = []
                self.es2 = []
                self.es3 = []
                self.kr1 = []
                self.kr2 = []
                self.lin = []
        self.show()

    def free_comp_sea(self, sea):
        return_sp = []
        for i in range(10):
            for o in range(10):
                if sea[i][o] == '-':
                    return_sp.append(sea[i][o] + str(i) + str(o))
        return return_sp

    def clear(self, label):
        if label in self.zero_prioryty:
            del self.zero_prioryty[self.zero_prioryty.index(label)]
        if label in self.first_prioryty:
            del self.first_prioryty[self.first_prioryty.index(label)]
        if label in self.second_prioryty:
            del self.second_prioryty[self.second_prioryty.index(label)]
        if label in self.third_prioryty:
            del self.third_prioryty[self.third_prioryty.index(label)]

    def attack_player(self):
        while self.turn == 1 and self.player_counter != 0:
            a = '0'
            while a in self.deads:
                if self.zero_prioryty != []:
                    a = random.choice(self.zero_prioryty)
                elif self.first_prioryty != []:
                    a = random.choice(self.first_prioryty)
                elif self.second_prioryty != []:
                    a = random.choice(self.second_prioryty)
                elif self.third_prioryty != 0:
                    a = random.choice(self.third_prioryty)
                if a in self.deads:
                    self.clear(a)
            self.clear(a)
            self.deads.append(a)
            for i in range(10):
                if a in self.sp_labels[i]:
                    coord_let, coord_num = int(i), int(self.sp_labels[i].index(a))
            if a.text() == ' +':
                if self.zero_prioryty_ship == []:
                    if a in self.lin_p:
                        self.zero_prioryty_ship = self.lin_p.copy()
                    elif a in self.kr1_p:
                        self.zero_prioryty_ship = self.kr1_p.copy()
                    elif a in self.kr2_p:
                        self.zero_prioryty_ship = self.kr2_p.copy()
                    elif a in self.es1_p:
                        self.zero_prioryty_ship = self.es1_p.copy()
                    elif a in self.es2_p:
                        self.zero_prioryty_ship = self.es2_p.copy()
                    elif a in self.es3_p:
                        self.zero_prioryty_ship = self.es3_p.copy()
                    elif a in self.bo1_p:
                        self.zero_prioryty_ship = self.bo1_p.copy()
                    elif a in self.bo2_p:
                        self.zero_prioryty_ship = self.bo2_p.copy()
                    elif a in self.bo3_p:
                        self.zero_prioryty_ship = self.bo3_p.copy()
                    elif a in self.bo4_p:
                        self.zero_prioryty_ship = self.bo4_p.copy()
                del self.zero_prioryty_ship[self.zero_prioryty_ship.index(a)]
                if self.zero_prioryty_ship == []:
                    if a in self.lin_p:
                        for i in self.lin_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.kr1_p:
                        for i in self.kr1_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.kr2_p:
                        for i in self.kr2_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.es1_p:
                        for i in self.es1_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.es2_p:
                        for i in self.es2_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.es3_p:
                        for i in self.es3_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.bo1_p:
                        for i in self.bo1_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.bo2_p:
                        for i in self.bo2_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.bo3_p:
                        for i in self.bo3_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    elif a in self.bo4_p:
                        for i in self.bo4_p:
                            i.setText(' X')
                            coord_let, coord_num = self.get_coords(i)[0], self.get_coords(i)[1]
                            for o in self.neighboorhood(coord_let, coord_num)[1]:
                                if o != '0' and o.text() == ' -':
                                    o.setText(' 0')
                                    self.deads.append(o)
                    self.player_counter -= 1
                    self.zero_prioryty = []
                else:
                    a.setText(' x')
                    sp = self.neighboorhood(coord_let, coord_num)[1]
                    for i in range(4):
                        if sp[i] != '0' and (sp[i].text() == ' -' or sp[i].text() == ' +'):
                           self.zero_prioryty.append(sp[i])
                    for i in range(4, 8):
                        if sp[i] != '0' and sp[i].text() == ' -':
                            self.deads.append(sp[i])
                qwerty = []
                for i in self.zero_prioryty:
                    if i not in self.deads:
                        qwerty.append(i)
                self.zero_prioryty = qwerty.copy()

            else:
                a.setText(' 0')
                self.label_turn.setText('                     Ваш Ход.')
                self.turn = 0
        if self.player_counter == 0:
            self.final()

    def attack_comp(self, Button, Button_txt):
        if Button.text() == '-' and self.turn == 0:
            coord_let = int(list(Button_txt)[0])
            coord_num = int(list(Button_txt)[1])
            sp1 = self.neighboors(coord_let, coord_num)[0]
            sp2 = self.neighboors(coord_let, coord_num)[1]
            if Button in self.bo1_c or Button in self.bo2_c or Button in self.bo3_c or Button in self.bo4_c:
                Button.setText('X')
                self.computer_counter -= 1
                Button.setStyleSheet("background-color: {}".format('#ff0000'))
                for i in range(8):
                    if sp1[i] == '-' or sp1[i] == '/':
                        sp2[i].setText('0')
                        sp2[i].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.es3_c:
                if [coord_let, coord_num] not in self.es3:
                    self.es3.append([coord_let, coord_num])
                if len(self.es3) != 2:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.es3:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.es2_c:
                if [coord_let, coord_num] not in self.es2:
                    self.es2.append([coord_let, coord_num])
                if len(self.es2) != 2:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.es2:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.es1_c:
                if [coord_let, coord_num] not in self.es1:
                    self.es1.append([coord_let, coord_num])
                if len(self.es1) != 2:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.es1:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.kr1_c:
                if [coord_let, coord_num] not in self.kr1:
                    self.kr1.append([coord_let, coord_num])
                if len(self.kr1) != 3:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.kr1:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.kr2_c:
                if [coord_let, coord_num] not in self.kr2:
                    self.kr2.append([coord_let, coord_num])
                if len(self.kr2) != 3:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.kr2:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            elif Button in self.lin_c:
                if [coord_let, coord_num] not in self.lin:
                    self.lin.append([coord_let, coord_num])
                if len(self.lin) != 4:
                    Button.setText('x')
                    Button.setStyleSheet("background-color: {}".format('#ff8000'))
                    for i in range(4):
                        if sp1[i + 4] == '-' or sp1[i + 4] == '/':
                            sp2[i + 4].setText('0')
                            sp2[i + 4].setStyleSheet("background-color: {}".format('#0000ff'))
                else:
                    for i in self.lin:
                        coord_let = int(i[0])
                        coord_num = int(i[1])
                        But = self.sp_buttons[coord_let][coord_num]
                        sp1 = self.neighboors(coord_let, coord_num)[0]
                        sp2 = self.neighboors(coord_let, coord_num)[1]
                        But.setText('X')
                        self.computer_counter -= 1
                        But.setStyleSheet("background-color: {}".format('#ff0000'))
                        for o in range(8):
                            if sp1[o] == '-' or sp1[o] == '/':
                                sp2[o].setText('0')
                                sp2[o].setStyleSheet("background-color: {}".format('#0000ff'))
            else:
                self.label_turn.setText('Ход компьютера. Подождите...')
                Button.setText('0')
                Button.setStyleSheet("background-color: {}".format('#0000ff'))
                self.computer_sea[coord_let][coord_num] = '0'
                self.turn = 1
            if self.computer_counter == 0:
                self.final()
            else:
                self.attack_player()

    def final(self):
        if self.player_counter == 0:
            self.label_turn.setText('   Вы проиграли...')
        elif self.computer_counter == 0:
            self.label_turn.setText('   Вы победили!')

    def neighboors(self, coord_let, coord_num):
        if coord_num > 0:
            b_west = self.sp_buttons[coord_let][coord_num - 1]
            s_west = self.computer_sea[coord_let][coord_num - 1]
        else:
            s_west = '0'
            b_west = '0'
        if coord_num < 9:
            b_east = self.sp_buttons[coord_let][coord_num + 1]
            s_east = self.computer_sea[coord_let][coord_num + 1]
        else:
            s_east = '0'
            b_east = '0'
        if coord_let > 0:
            b_north = self.sp_buttons[coord_let - 1][coord_num]
            s_north = self.computer_sea[coord_let - 1][coord_num]
        else:
            s_north = '0'
            b_north = '0'
        if coord_let < 9:
            b_south = self.sp_buttons[coord_let + 1][coord_num]
            s_south = self.computer_sea[coord_let + 1][coord_num]
        else:
            s_south = '0'
            b_south = '0'
        if coord_num > 0 and coord_let > 0:
            b_nw = self.sp_buttons[coord_let - 1][coord_num - 1]
            s_nw = self.computer_sea[coord_let - 1][coord_num - 1]
        else:
            s_nw = '0'
            b_nw = '0'
        if coord_num < 9 and coord_let < 9:
            b_se = self.sp_buttons[coord_let + 1][coord_num + 1]
            s_se = self.computer_sea[coord_let + 1][coord_num + 1]
        else:
            s_se = '0'
            b_se = '0'
        if coord_let > 0 and coord_num < 9:
            b_ne = self.sp_buttons[coord_let - 1][coord_num + 1]
            s_ne = self.computer_sea[coord_let - 1][coord_num + 1]
        else:
            s_ne = '0'
            b_ne = '0'
        if coord_let < 9 and coord_num > 0:
            b_sw = self.sp_buttons[coord_let + 1][coord_num - 1]
            s_sw = self.computer_sea[coord_let + 1][coord_num - 1]
        else:
            s_sw = '0'
            b_sw = '0'
        sp = [[s_west, s_east, s_north, s_south, s_nw, s_se, s_ne, s_sw],
              [b_west, b_east, b_north, b_south, b_nw, b_se, b_ne, b_sw]]
        return sp

    def neighboorhood(self, coord_let, coord_num):
        if coord_num > 0:
            b_west = self.sp_labels[coord_let][coord_num - 1]
            s_west = self.computer_sea[coord_let][coord_num - 1]
        else:
            s_west = '0'
            b_west = '0'
        if coord_num < 9:
            b_east = self.sp_labels[coord_let][coord_num + 1]
            s_east = self.computer_sea[coord_let][coord_num + 1]
        else:
            s_east = '0'
            b_east = '0'
        if coord_let > 0:
            b_north = self.sp_labels[coord_let - 1][coord_num]
            s_north = self.computer_sea[coord_let - 1][coord_num]
        else:
            s_north = '0'
            b_north = '0'
        if coord_let < 9:
            b_south = self.sp_labels[coord_let + 1][coord_num]
            s_south = self.computer_sea[coord_let + 1][coord_num]
        else:
            s_south = '0'
            b_south = '0'
        if coord_num > 0 and coord_let > 0:
            b_nw = self.sp_labels[coord_let - 1][coord_num - 1]
            s_nw = self.computer_sea[coord_let - 1][coord_num - 1]
        else:
            s_nw = '0'
            b_nw = '0'
        if coord_num < 9 and coord_let < 9:
            b_se = self.sp_labels[coord_let + 1][coord_num + 1]
            s_se = self.computer_sea[coord_let + 1][coord_num + 1]
        else:
            s_se = '0'
            b_se = '0'
        if coord_let > 0 and coord_num < 9:
            b_ne = self.sp_labels[coord_let - 1][coord_num + 1]
            s_ne = self.computer_sea[coord_let - 1][coord_num + 1]
        else:
            s_ne = '0'
            b_ne = '0'
        if coord_let < 9 and coord_num > 0:
            b_sw = self.sp_labels[coord_let + 1][coord_num - 1]
            s_sw = self.computer_sea[coord_let + 1][coord_num - 1]
        else:
            s_sw = '0'
            b_sw = '0'
        sp = [[s_west, s_east, s_north, s_south, s_nw, s_se, s_ne, s_sw],
              [b_west, b_east, b_north, b_south, b_nw, b_se, b_ne, b_sw]]
        return sp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

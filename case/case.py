#!/usr/bin/env python3

import cadquery as cq
from cadquery.vis import show
import os

D = 0.25
BOARD_X = 56.25+D
BOARD_Y = 55+D
BOARD_H = 14
BASE_H = 2

THICK = 3

class My2DSize:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) is type(self):
            return My2DSize(self.x + other.x, self.y + other.y)
        else:
            return My2DSize(self.x + other, self.y + other)

    def __mul__(self, scalar):
        return My2DSize(self.x*scalar, self.y*scalar)

    def __truediv__(self, scalar):
        return self * (1/scalar)

    @property
    def t(self):
        return self.x, self.y



def bottom():
    shell = cq.Workplane("XY").box(BOARD_X, BOARD_Y, BOARD_H+BASE_H).faces(">Z").shell(THICK)
    bases = cq.Sketch().rarray(BOARD_X, BOARD_Y, 2, 2).circle(2)
    shell = shell.faces("<Z").translate((0, 0, THICK)).placeSketch(bases).extrude(BASE_H)

    holes = cq.Sketch().rarray(BOARD_X, BOARD_Y, 2, 2).circle(1)
    shell = shell.faces(">Z").placeSketch(holes).cutBlind(-BOARD_H)

    return shell

def top():
    T = 2*THICK
    base = cq.Workplane("XY").box(BOARD_X+T, BOARD_Y+T, THICK, centered=(True, True, False)).edges("Z").fillet(2)
    base = base.faces("<Z").workplane().rect(BOARD_X, BOARD_Y, forConstruction=True).vertices().cboreHole(2, 3, 1)
    inlay = cq.Workplane("XY").box(BOARD_X, BOARD_Y, THICK+2, centered=(True, True, False)).edges("Z").chamfer(2)

    body = base.union(inlay)

    off = 1
    sizeRelays = My2DSize(7.62, 44.1)
    sizeRelayHoles = sizeRelays + 2*off
    posRelays = My2DSize(45.6, 6.3)

    holesForRelays = cq.Sketch().push([(sizeRelayHoles/2).t]).rect(*sizeRelayHoles.t).reset().vertices().fillet(1)

    sizePower = My2DSize(7.62, 6) + 2*off
    posPower = My2DSize(25.8, 4.1)
    holesForPower = cq.Sketch().push([(sizePower/2).t]).rect(*sizePower.t).reset().vertices().fillet(1)

    posReset = My2DSize(5.7, 11)
    holesForReset = cq.Sketch().circle(3)



    posAir = My2DSize(17, 38)
    holesForAir = cq.Sketch().rarray(3, 3, 5, 5).circle(1)

    body = body.faces(">Z").center(-BOARD_X/2, -BOARD_Y/2).moveTo(*posRelays.t).placeSketch(holesForRelays).cutThruAll()
    body = body.faces(">Z").moveTo(*posPower.t).placeSketch(holesForPower).cutThruAll()
    body = body.faces(">Z").moveTo(*posAir.t).placeSketch(holesForAir).cutThruAll()
    body = body.faces(">Z").moveTo(*posReset.t).placeSketch(holesForReset).cutThruAll()




    return body



def main():
    targetPath = os.path.join(os.path.dirname(__file__), "stl")
    def _storeFile(func, name, desc):
        ofn = os.path.join(targetPath, name)
        print(f"Generating and storing {desc} ({os.path.relpath(ofn)})...")
        func().export(ofn)

    os.makedirs(targetPath, exist_ok=True)
    _storeFile(top, "top.stl", "Top Part")
    _storeFile(bottom, "bottom.stl", "Bottom Part")

if __name__ == '__main__':
    main()

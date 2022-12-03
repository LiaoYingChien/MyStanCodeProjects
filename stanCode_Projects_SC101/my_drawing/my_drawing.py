"""
File: Kappa
Name: 廖瑩蒨
----------------------
TODO:Drawn from the pattern on my storage bag.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:Drawn from the pattern on my storage bag.
    """
    window = GWindow(500, 500)

    face = GOval(300, 300)
    face.filled = True
    face.color = 'aquamarine'
    face.fill_color = 'aquamarine'
    window.add(face, x=(window.width/2-face.width/2), y=(window.height/2-face.height/2))

    eye_left = GOval(20, 20)
    eye_left.filled = True
    window.add(eye_left, x=150, y=200)

    eye_right = GOval(20, 20)
    eye_right.filled = True
    window.add(eye_right, x=330, y=200)

    mouth_top = GPolygon()
    mouth_top.add_vertex((150, 300))
    mouth_top.add_vertex((window.width/2, 250))
    mouth_top.add_vertex((350, 300))
    window.add(mouth_top)

    mouth_down = GPolygon()
    mouth_down.add_vertex((150, 300))
    mouth_down.add_vertex((window.width/2, 350))
    mouth_down.add_vertex((350, 300))
    window.add(mouth_down)

    line = GArc(140, 80, 190, 160)
    window.add(line, x=180, y=100)

    tri_1 = GPolygon()
    tri_1.add_vertex((199, 129))
    tri_1.add_vertex((207, 153))
    tri_1.add_vertex((230, 133))
    tri_1.filled = True
    window.add(tri_1)

    tri_2 = GPolygon()
    tri_2.add_vertex((230, 133))
    tri_2.add_vertex((250, 159))
    tri_2.add_vertex((270, 132))
    tri_2.filled = True
    window.add(tri_2)

    tri_3 = GPolygon()
    tri_3.add_vertex((270, 132))
    tri_3.add_vertex((284, 156))
    tri_3.add_vertex((297, 130))
    tri_3.filled = True
    window.add(tri_3)

    lable = GLabel('Kappa', x=150, y=80)
    lable.font = 'Verdana-50-bold-italic'
    window.add(lable)


if __name__ == '__main__':
    main()

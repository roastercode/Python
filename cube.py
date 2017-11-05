#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Mail       : aurelien@hackers.camp
# Project    : Python Box
# Modified   : Nov 3 2017
# Write with Emacs-Nox
#
# Pylint verified 9.86 / 10.00

"""
 Simulation of a rotating 3D Cube
 Developed by Leonel Machava <leonelmachava@gmail.com>

 // Modified by Aurélien Desbrières <aurelien@hackers.camp>
 // Modification from the original:
    - add a sheband to make it executable by the system
    - remove the colors
    - change library
         . pygame.draw.polygon by pygame.draw.line
    - self.screen.fill to 0 0 0 (black)
    - remove unecessary pointlist
    - pylint correction:
         . def name corrections
    - moved to python3 (need pip3 install pygame)
    - adapt background size to object size
    - make some debug with
         . import ipdb; ipdb.set_trace()
    - correction
         . import order
         . pylint improvement
"""

import sys
import math
from operator import itemgetter
import pygame
print(sys.path)


class Point3D(object):
    """ cube definition  """

    def __init__(self, x_point=0, y_point=0, z_point=0):
        self.x_axis, self.y_axis, self.z_axis = float(
            x_point), float(y_point), float(z_point)

    def rotate_x(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y_point = self.y_axis * cosa - self.z_axis * sina
        z_point = self.y_axis * sina + self.z_axis * cosa
        return Point3D(self.x_axis, y_point, z_point)

    def rotate_y(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z_point = self.z_axis * cosa - self.x_axis * sina
        x_point = self.z_axis * sina + self.x_axis * cosa
        return Point3D(x_point, self.y_axis, z_point)

    def rotate_z(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x_point = self.x_axis * cosa - self.y_axis * sina
        y_point = self.x_axis * sina + self.y_axis * cosa
        return Point3D(x_point, y_point, self.z_axis)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z_axis)
        x_point = self.x_axis * factor + win_width / 2
        y_point = -self.y_axis * factor + win_height / 2
        return Point3D(x_point, y_point, self.z_axis)


class Simulation(Point3D):
    """ cube action  """

    def __init__(self, win_width=300, win_height=300):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption(
            "Simulation of a rotating 3D Cube")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1, 1, -1),
            Point3D(1, 1, -1),
            Point3D(1, -1, -1),
            Point3D(-1, -1, -1),
            Point3D(-1, 1, 1),
            Point3D(1, 1, 1),
            Point3D(1, -1, 1),
            Point3D(-1, -1, 1)
        ]

        # Define the vertices that compose each of the 6 faces. These numbers
        # are indices to the vertices list defined above.
        self.faces = [(0, 1, 2, 3), (1, 5, 6, 2), (5, 4, 7, 6),
                      (4, 0, 3, 7), (0, 4, 5, 1), (3, 2, 6, 7)]

        self.angle = 0

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0, 0, 0))

            # It will hold transformed vertices.
            t_transform = []

            for v_vertices in self.vertices:
                # Rotate the point around X axis, then around Y axis, and
                # finally around Z axis.
                r_vertices = v_vertices.rotate_x(self.angle).rotate_y(
                    self.angle).rotate_z(self.angle)
                # Transform the point from 3D to 2D
                p_transform = r_vertices.project(self.screen.get_width(),
                                                 self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t_transform.append(p_transform)

            # Calculate the average Z values of each face.
            avg_z = []
            i = 0
            for f_calculate in self.faces:
                z_calculus = (t_transform[f_calculate[0]].z_axis +
                              t_transform[f_calculate[1]].z_axis +
                              t_transform[f_calculate[2]].z_axis +
                              t_transform[f_calculate[3]].z_axis) / 4.0
                avg_z.append([i, z_calculus])
                i = i + 1

            # Draw the faces using the Painter's algorithm:
            # Distant faces are drawn before the closer ones.
            for tmp in sorted(avg_z, key=itemgetter(1), reverse=True):
                face_index = tmp[0]
                f_calculate = self.faces[face_index]
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (t_transform[f_calculate[0]].x_axis,
                                  t_transform[f_calculate[0]].y_axis),
                                 (t_transform[f_calculate[1]].x_axis,
                                  t_transform[f_calculate[1]].y_axis))
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (t_transform[f_calculate[1]].x_axis,
                                  t_transform[f_calculate[1]].y_axis),
                                 (t_transform[f_calculate[2]].x_axis,
                                  t_transform[f_calculate[2]].y_axis))
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (t_transform[f_calculate[2]].x_axis,
                                  t_transform[f_calculate[2]].y_axis),
                                 (t_transform[f_calculate[3]].x_axis,
                                  t_transform[f_calculate[3]].y_axis))
                pygame.draw.line(self.screen, (255, 255, 255),
                                 (t_transform[f_calculate[3]].x_axis,
                                  t_transform[f_calculate[3]].y_axis),
                                 (t_transform[f_calculate[0]].x_axis,
                                  t_transform[f_calculate[0]].y_axis))

            self.angle += 1

            pygame.display.flip()

            if __name__ == "__main__":
                Simulation().run()

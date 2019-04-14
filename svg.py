import tkinter as tk
import tkinter.filedialog as fdlg

class Svg:
    #header = ['<?xml version="1.0"?>','<svg xmlns="http://www.w3.org/2000/svg">']
    #footer = '</svg>'
    #object=[]
    #body = []
    #transform= []
    #TestTest

    def __init__(self):
        self.header = ['<?xml version="1.0"?>','<svg xmlns="http://www.w3.org/2000/svg">']
        self.footer = '</svg>'
        #self.object=[]
        self.body = []
        self.transform= []

    def save(self, name = None):
        root = tk.Tk()
        root.withdraw()
        file_name = fdlg.asksaveasfilename(
            filetypes = [("svg","*.svg")],
            defaultextension = ".svg",
            initialfile = name)
        try:
            with open(file_name, 'w', encoding = "utf-8") as f: #, newline = "\n"
                writer = ""
                for row in self.header:
                    writer += row
                    writer += '\n'
                for row in self.body:
                    writer += "    {}".format(row)
                    writer += '\n'
                writer += self.footer
                f.write(writer)
        except FileNotFoundError:
            pass
    
    def open(self):
        root = tk.Tk()
        root.withdraw()
        file_name = fdlg.askopenfilename(
        filetypes = [("svg","*.svg")],
        defaultextension = ".svg",
        initialfile = "*")
        try:
            with open(file_name, 'r', encoding = "utf-8") as f: #, newline = "\n"
                reader = f.split('\n')
                #for i in range(2):
                #    self.header[i] = reader[i]
                for row in reader[2:-2]:
                    self.body.append(row)
        except FileNotFoundError:
            pass
    #def print_body(self):
    #def save_as_tag(self, filename):
    #def print_object_list(self):
    #def conbine(self, svg):
    #def change_order(self, order):
    
    def create_line(self,x1,y1,x2,y2,stroke="black",stroke_width=1):
        return self.body.append('<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" stroke="{4}" stroke-width="{5}" />'.format(
            x1, y1, x2, y2, stroke, stroke_width))

    def create_rect(self, x1, y1, width, height, stroke = "black", fill = None, stroke_width = 1):
        return self.body.append('<rect x="{0}" y="{1}" width="{2}" height="{3}" stroke="{4}" fill="{5}" stroke-width="{6}" />'.format(
            x1, y1, width, height, stroke, fill, stroke_width))

    def create_polygon(self, points, stroke="black", fill=None, stroke_width= 1):
        #points:taple or list.
        #ex) ((0,0),(1,2),(3,4))
        point_value = ""
        for point in points:
            point_value += "{0} {1},".format(point[0], point[1])
        point_value = point_value[:-1]
        return self.body.append('<polygon points="{0}" stroke="{1}" fill="{2}" stroke-width="{3}" />'.format(
            point_value, stroke, fill, stroke_width))

    def create_circle(self, cx, cy, r, stroke="black", fill=None, stroke_width= 1):
        return self.body.append('<circle cx="{0}" cy="{1}" r="{2}" stroke="{3}" fill="{4}" stroke-width="{5}" />'.format(
            cx, cy, r, stroke, fill, stroke_width))

    def create_ellipse(self, cx, cy, rx, ry, stroke="black", fill=None, stroke_width=1):
        return self.body.append('<ellipse cx="{0}" cy="{1}" rx="{2}" ry="{3}" stroke="{4}" fill="{5}" stroke-width="{6}" />'.format(
            cx, cy, rx, ry, stroke, fill, stroke_width))

    def create_path(self, d, stroke="black", fill="transparent", stroke_width=1):
        
        # ex) d = (("M",(0,1)),("L",(2,3)),("H",(4,5)),("C",(6,7,8,9,10,11)))
        d_value = ""
        for order in d:
            d_value += "{} ".format(order[0])
            for value in order[1]:
                d_value += "{} ".format(value)
        d_value = d_value[:-1]
        return self.body.append('<path d="{0}" stroke="{1}" fill="{2}" stroke-width="{3}" />'.format(
            d_value, stroke, fill, stroke_width))

    def set_animation(self, attributeName, from_to, dur, repeatCount="indefinite" ):

        return self.body.append('    <animate attributeName="{0}" from="{1}" to="{2}" dur="{3}s" repeatCount="{4}" />'.format(
            attributeName, from_to[0],from_to[1], dur, repeatCount))

    def set_svg(self, x, y, width, height, style="background-color:#ddd"):
        new_body = []
        tag = '<svg x="{0}px" y="{1}px" width="{2}px" height="{3}px" style="{4}" >'.format(
            x, y, width, height, style)
        new_body.append(tag)
        for row in self.body:
            new_body.append("    {}".format(row))
        new_body.append("</svg>")
        self.body = new_body
        return self.body

    def set_group(self):
        new_body = ["<g>"]
        for row in self.body:
            new_body.append("    {}".format(row))
        new_body.append("</g>")
        self.body = new_body
        return self.body

    def transform_group(self,transform,is_set_group = False):
        if is_set_group == False:
            self.body = self.set_group()
        if self.body[0] == "<g>":
            tag = '<g transform ="'
            for row in transform:
                tag += "{} ".format(row)
            tag += '">'
            self.body[0] = tag
            return self.body
        else:
            pass

class Transform:

    def __init__(self):
        self.transform = []
    def set_matrix(self, a,b,c,d,e,f):
        return self.transform.append("matrix({},{},{},{},{},{})".format(a,b,c,d,e,f))
    def set_tranlate(self, tx,ty):
        return self.transform.append("translate({},{})".format(tx,ty))
    def set_scale(self, sx,sy):
        return self.transform.append("scale({},{})".format(sx,sy))
    def set_rotate(self, angle,cx=0,cy=0):
        return self.transform.append("rotate({},{},{})".format(angle,cx,cy))
    def set_skewX(self, angle):
        return self.transform.append("skewX({})".format(angle))
    def set_skewY(self, angle):
        return self.transform.append("skewY({})".format(angle))

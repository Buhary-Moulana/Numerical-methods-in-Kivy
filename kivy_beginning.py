import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from sympy import symbols, sympify, diff

simpsonxlist, simpsonylist = [], []


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    pass


class NRWindow(Screen):
    def nrfunction(self):
        self.ids.nrimage.source = "NR_formula.png"
        self.ids.nrlabel1.color = (53/255, 118/255, 176/255)
        self.ids.nrlabel2.color = (53/255, 118/255, 176/255)
        x = symbols('x')
        nrtext = self.ids.nrinput.text
        s = sympify(nrtext)
        s1 = diff(s, x)
        self.ids.nrlabel2.text = "f(x) = "+str(s)+" , f'(x) ="+str(s1)
        t = []
        for i in range(-100, 100, 1):
            if (s.subs(x, i) > 0 and s.subs(x, i+1) < 0) or (s.subs(x, i) < 0 and s.subs(x, i+1) > 0) or (s.subs(x, i) == 0) or (s.subs(x, i+1) == 0):
                a, b = i, i+1
                break
        x1 = (a+b)/2
        self.ids.nrlabel1.text = "Let our initial approximation of the root be x0 = " + \
            str(x1)
        for i in range(1, 6):
            x1 = x1-s.subs(x, x1)/s1.subs(x, x1)
            t.append(round(float(x1), 4))
        self.ids.nrlabel3.text = "Iteration 1 : x1 = "+str(t[0])
        self.ids.nrlabel3.color = (53/255, 118/255, 176/255)
        self.ids.nrlabel4.text = "Iteration 2 : x2 = "+str(t[1])
        self.ids.nrlabel4.color = (53/255, 118/255, 176/255)
        self.ids.nrlabel5.text = "Iteration 3 : x3 = "+str(t[2])
        self.ids.nrlabel5.color = (53/255, 118/255, 176/255)
        self.ids.nrlabel6.text = "Iteration 4 : x4 = "+str(t[3])
        self.ids.nrlabel6.color = (53/255, 118/255, 176/255)
        self.ids.nrlabel7.text = "Iteration 5 : x5 = "+str(t[4])
        self.ids.nrlabel7.color = (53/255, 118/255, 176/255)
        if (s.subs(x, a) > 0 and s.subs(x, b) < 0) or (s.subs(x, a) > 0 and s.subs(x, b) == 0):
            self.ids.nrlabelroot1.text = "f("+str(a)+") = +ve"
            self.ids.nrlabelroot1.color = (50/255, 230/255, 98/255)
            self.ids.nrlabelroot2.text = "f("+str(b)+") = -ve"
            self.ids.nrlabelroot2.color = (50/255, 230/255, 98/255)
            self.ids.nrlabelroot3.text = "We conclude that atleast one root exists between " + \
                str(a)+" and "+str(b)
            self.ids.nrlabelroot3.color = (50/255, 230/255, 98/255)
        if (s.subs(x, a) < 0 and s.subs(x, b) > 0) or (s.subs(x, a) == 0 and s.subs(x, b) > 0):
            self.ids.nrlabelroot1.text = "f("+str(a)+") = -ve"
            self.ids.nrlabelroot1.color = (50/255, 230/255, 98/255)
            self.ids.nrlabelroot2.text = "f("+str(b)+") = +ve"
            self.ids.nrlabelroot2.color = (50/255, 230/255, 98/255)
            self.ids.nrlabelroot3.text = "We conclude that atleast one root exists between " + \
                str(a)+" and "+str(b)
            self.ids.nrlabelroot3.color = (50/255, 230/255, 98/255)
        self.ids.nrlabelfinal.text = "We conclude that our root is x = " + \
            str(round(float(x1), 3))
        self.ids.nrlabelfinal.color = (50/255, 230/255, 98/255)
        self.ids.nrclear.background_color = (237/255, 39/255, 17/255)
        self.ids.nrclear.color = (0, 0, 0, 1)

    def nrfunction2(self):
        self.ids.nrlabel1.text = ""
        self.ids.nrlabel2.text = ""
        self.ids.nrlabel3.text = ""
        self.ids.nrlabel4.text = ""
        self.ids.nrlabel5.text = ""
        self.ids.nrlabel6.text = ""
        self.ids.nrlabel7.text = ""
        self.ids.nrlabelfinal.text = ""
        self.ids.nrinput.text = ""
        self.ids.nrimage.source = ""
        self.ids.nrlabelroot1.text = ""
        self.ids.nrlabelroot2.text = ""
        self.ids.nrlabelroot3.text = ""
        self.ids.nrclear.background_color = (1, 1, 1, 1)
        self.ids.nrclear.color = (1, 1, 1, 1)


class LagrangeWindow(Screen):
    pass


class GJWindow(Screen):
    def gjfunction(self):
        x, y, z = symbols('x y z')
        a1 = self.ids.gja1input.text
        b1 = self.ids.gjb1input.text
        c1 = self.ids.gjc1input.text
        d1 = self.ids.gjd1input.text
        a2 = self.ids.gja2input.text
        b2 = self.ids.gjb2input.text
        c2 = self.ids.gjc2input.text
        d2 = self.ids.gjd2input.text
        a3 = self.ids.gja3input.text
        b3 = self.ids.gjb3input.text
        c3 = self.ids.gjc3input.text
        d3 = self.ids.gjd3input.text
        if a1 == '':
            a1 = 0
        else:
            a1 = float(a1)
        if b1 == '':
            b1 = 0
        else:
            b1 = float(b1)
        if c1 == '':
            c1 = 0
        else:
            c1 = float(c1)
        if d1 == '':
            d1 = 0
        else:
            d1 = float(d1)
        if a2 == '':
            a2 = 0
        else:
            a2 = float(a2)
        if b2 == '':
            b2 = 0
        else:
            b2 = float(b2)
        if c2 == '':
            c2 = 0
        else:
            c2 = float(c2)
        if d2 == '':
            d2 = 0
        else:
            d2 = float(d2)
        if a3 == '':
            a3 = 0
        else:
            a3 = float(a3)
        if b3 == '':
            b3 = 0
        else:
            b3 = float(b3)
        if c3 == '':
            c3 = 0
        else:
            c3 = float(c3)
        if d3 == '':
            d3 = 0
        else:
            d3 = float(d3)
        x1 = sympify((d1-b1*y-c1*z)/a1)
        y1 = sympify((d2-a2*x-c2*z)/b2)
        z1 = sympify((d3-b3*y-a1*x)/c3)
        xi, yi, zi = 0, 0, 0
        xlist, ylist, zlist = [], [], []
        for i in range(10):
            xi = x1.subs([(y, yi), (z, zi)])
            yi = y1.subs([(x, xi), (z, zi)])
            zi = z1.subs([(y, yi), (x, xi)])
            xlist.append(xi)
            ylist.append(yi)
            zlist.append(zi)
        self.ids.gjlabel1.color = (1, 1, 1, 1)
        self.ids.gjlabel2.color = (1, 1, 1, 1)
        self.ids.gjlabel3.color = (1, 1, 1, 1)
        self.ids.gjlabel4.color = (1, 1, 1, 1)
        self.ids.gja1label.color = (1, 1, 1, 1)
        self.ids.gjb1label.color = (1, 1, 1, 1)
        self.ids.gjc1label.color = (1, 1, 1, 1)
        self.ids.gjd1label.color = (1, 1, 1, 1)
        self.ids.gja2label.color = (1, 1, 1, 1)
        self.ids.gjb2label.color = (1, 1, 1, 1)
        self.ids.gjc2label.color = (1, 1, 1, 1)
        self.ids.gjd2label.color = (1, 1, 1, 1)
        self.ids.gja3label.color = (1, 1, 1, 1)
        self.ids.gjb3label.color = (1, 1, 1, 1)
        self.ids.gjc3label.color = (1, 1, 1, 1)
        self.ids.gjd3label.color = (1, 1, 1, 1)
        self.ids.gja1label.color = (1, 1, 1, 1)
        self.ids.gjb1label.color = (1, 1, 1, 1)
        self.ids.gjc1label.color = (1, 1, 1, 1)
        self.ids.gjd1label.color = (1, 1, 1, 1)
        self.ids.gja1input.text = ''
        self.ids.gjb1input.text = ''
        self.ids.gjc1input.text = ''
        self.ids.gjd1input.text = ''
        self.ids.gja2input.text = ''
        self.ids.gjb2input.text = ''
        self.ids.gjc2input.text = ''
        self.ids.gjd2input.text = ''
        self.ids.gja3input.text = ''
        self.ids.gjb3input.text = ''
        self.ids.gjc3input.text = ''
        self.ids.gjd3input.text = ''
        self.ids.gja1input.background_color = (1, 1, 1, 1)
        self.ids.gja1input.background_normal = ''
        self.ids.gjb1input.background_color = (1, 1, 1, 1)
        self.ids.gjb1input.background_normal = ''
        self.ids.gjc1input.background_color = (1, 1, 1, 1)
        self.ids.gjc1input.background_normal = ''
        self.ids.gjd1input.background_color = (1, 1, 1, 1)
        self.ids.gjd1input.background_normal = ''
        self.ids.gja2input.background_color = (1, 1, 1, 1)
        self.ids.gja2input.background_normal = ''
        self.ids.gjb2input.background_color = (1, 1, 1, 1)
        self.ids.gjb2input.background_normal = ''
        self.ids.gjc2input.background_color = (1, 1, 1, 1)
        self.ids.gjc2input.background_normal = ''
        self.ids.gjd2input.background_color = (1, 1, 1, 1)
        self.ids.gjd2input.background_normal = ''
        self.ids.gja3input.background_color = (1, 1, 1, 1)
        self.ids.gja3input.background_normal = ''
        self.ids.gjb3input.background_color = (1, 1, 1, 1)
        self.ids.gjb3input.background_normal = ''
        self.ids.gjc3input.background_color = (1, 1, 1, 1)
        self.ids.gjc3input.background_normal = ''
        self.ids.gjd3input.background_color = (1, 1, 1, 1)
        self.ids.gjd3input.background_normal = ''
        self.ids.gjsubmit.background_color = (1, 1, 1, 1)
        self.ids.gjnotelabel.color = (1, 1, 1, 1)
        self.ids.gjresultlabel1.text = "Iteration 1 :             x1 = " + \
            str(round(xlist[0], 5))+"      y1 = " + \
            str(round(ylist[0], 5))+"      z1 = "+str(round(zlist[0], 5))
        self.ids.gjresultlabel2.text = "Iteration 2 :             x2 = " + \
            str(round(xlist[1], 5))+"      y2 = " + \
            str(round(ylist[1], 5))+"      z2 = "+str(round(zlist[1], 5))
        self.ids.gjresultlabel3.text = "Iteration 3 :             x3 = " + \
            str(round(xlist[2], 5))+"      y3 = " + \
            str(round(ylist[2], 5))+"      z3 = "+str(round(zlist[2], 5))
        self.ids.gjresultlabel4.text = "Iteration 4 :             x4 = " + \
            str(round(xlist[3], 5))+"      y4 = " + \
            str(round(ylist[3], 5))+"      z4 = "+str(round(zlist[3], 5))
        self.ids.gjresultlabel5.text = "Iteration 5 :             x5 = " + \
            str(round(xlist[4], 5))+"      y5 = " + \
            str(round(ylist[4], 5))+"      z5 = "+str(round(zlist[4], 5))
        self.ids.gjresultlabel6.text = "Iteration 6 :             x6 = " + \
            str(round(xlist[5], 5))+"      y1 = " + \
            str(round(ylist[5], 5))+"      z1 = "+str(round(zlist[5], 5))
        self.ids.gjresultlabel7.text = "Iteration 7 :             x7 = " + \
            str(round(xlist[6], 5))+"      y2 = " + \
            str(round(ylist[6], 5))+"      z2 = "+str(round(zlist[6], 5))
        self.ids.gjresultlabel8.text = "Iteration 8 :             x8 = " + \
            str(round(xlist[7], 5))+"      y3 = " + \
            str(round(ylist[7], 5))+"      z3 = "+str(round(zlist[7], 5))
        self.ids.gjresultlabel9.text = "Iteration 9 :             x9 = " + \
            str(round(xlist[8], 5))+"      y4 = " + \
            str(round(ylist[8], 5))+"      z4 = "+str(round(zlist[8], 5))
        self.ids.gjresultlabel10.text = "Iteration 10 :           x10 = " + \
            str(round(xlist[9], 5))+"     y10 = " + \
            str(round(ylist[9], 5))+"     z10 = "+str(round(zlist[9], 5))
        self.ids.gjresultlabelfinal1.text = "We conclude that our roots are :"
        self.ids.gjresultlabelfinal2.text = "x = " + \
            str(round(xi, 4))+"    y = "+str(round(yi, 4)) + \
            "    z = "+str(round(zi, 4))
        self.ids.gjclear.background_color = (237/255, 39/255, 17/255)

    def gjfunction2(self):
        self.ids.gjresultlabel1.text = ""
        self.ids.gjresultlabel2.text = ""
        self.ids.gjresultlabel3.text = ""
        self.ids.gjresultlabel4.text = ""
        self.ids.gjresultlabel5.text = ""
        self.ids.gjresultlabel6.text = ""
        self.ids.gjresultlabel7.text = ""
        self.ids.gjresultlabel8.text = ""
        self.ids.gjresultlabel9.text = ""
        self.ids.gjresultlabel10.text = ""
        self.ids.gjresultlabel10.text = ""
        self.ids.gjresultlabelfinal1.text = ""
        self.ids.gjresultlabelfinal2.text = ""
        self.ids.gjlabel1.color = (3/255, 144/255, 252/255)
        self.ids.gjlabel2.color = (0/255, 194/255, 87/255)
        self.ids.gjlabel3.color = (0/255, 194/255, 87/255)
        self.ids.gjlabel4.color = (0/255, 194/255, 87/255)
        self.ids.gjnotelabel.color = (255/255, 37/255, 25/255)
        self.ids.gja1label.color = (0, 0, 0, 1)
        self.ids.gjb1label.color = (0, 0, 0, 1)
        self.ids.gjc1label.color = (0, 0, 0, 1)
        self.ids.gjd1label.color = (0, 0, 0, 1)
        self.ids.gja2label.color = (0, 0, 0, 1)
        self.ids.gjb2label.color = (0, 0, 0, 1)
        self.ids.gjc2label.color = (0, 0, 0, 1)
        self.ids.gjd2label.color = (0, 0, 0, 1)
        self.ids.gja3label.color = (0, 0, 0, 1)
        self.ids.gjb3label.color = (0, 0, 0, 1)
        self.ids.gjc3label.color = (0, 0, 0, 1)
        self.ids.gjd3label.color = (0, 0, 0, 1)
        self.ids.gja1label.color = (0, 0, 0, 1)
        self.ids.gjb1label.color = (0, 0, 0, 1)
        self.ids.gjc1label.color = (0, 0, 0, 1)
        self.ids.gjd1label.color = (0, 0, 0, 1)
        self.ids.gja1input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjb1input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjc1input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjd1input.background_color = (220/255, 222/255, 224/255)
        self.ids.gja2input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjb2input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjc2input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjd2input.background_color = (220/255, 222/255, 224/255)
        self.ids.gja3input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjb3input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjc3input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjd3input.background_color = (220/255, 222/255, 224/255)
        self.ids.gjsubmit.background_color = (30/255, 214/255, 58/255)
        self.ids.gjclear.background_color = (1, 1, 1, 1)


class NDWindow(Screen):
    pass


class SimpsonWindow(Screen):
    def simpsonfunctionsubmit(self):
        s = self.ids.simpsonfunctioninput.text
        self.ids.simpsonfunctioninput.text = ''
        self.ids.simpsonfunctioninput.disabled = True
        n = int(self.ids.simpsonintervalinput.text)
        self.ids.simpsonintervalinput.text = ''
        self.ids.simpsonintervalinput.disabled = True
        a = float(self.ids.simpsonlowerlimitinput.text)
        self.ids.simpsonlowerlimitinput.text = ''
        self.ids.simpsonlowerlimitinput.disabled = True
        b = float(self.ids.simpsonupperlimitinput.text)
        self.ids.simpsonupperlimitinput.text = ''
        self.ids.simpsonupperlimitinput.disabled = True
        h = (b-a)/n
        x = symbols('x')
        y = sympify(s)
        t = []
        for i in range(int(10000000*a), int(10000000*b+1), int(10000000*h)):
            t.append(round(y.subs(x, i/10000000), 5))
        A = t[0]+t[len(t)-1]
        B, C = 0, 0
        t2 = t.copy()
        del t[0]
        del t[len(t)-1]
        for i in range(0, len(t), 2):
            B += t[i]
        t2sum = 0
        for i in t2:
            t2sum += i
        C = t2sum-B-A
        I = round(h*(A+4*B+2*C)/3, 5)
        self.ids.simpson1resultlabel1.text = "The Integral of f(x) by Simpson's 1/3rd rule is given by :"
        self.ids.simpson1resultlabel2.text = "F(x) = h/3 [ A + 4B + 2C ]"
        self.ids.simpson1resultlabel3.text = "where A = Sum of first and last ordinates"
        self.ids.simpson1resultlabel4.text = "B = Sum of all the even positions"
        self.ids.simpson1resultlabel5.text = "C = Sum of all the odd positions"
        self.ids.simpson1resultlabel6.text = "In our case we have A = " + \
            str(A)+" , B = "+str(B)+" , C = "+str(C)+" and h = "+str(h)
        self.ids.simpson1resultlabel7.text = "The value of the Given Integral between the limits " + \
            str(a)+" and "+str(b)+" is "+str(I)
        self.ids.simpsonclear.background_color = (237/255, 39/255, 17/255)

    def simpsonclearfunction(self):
        self.ids.simpsonlowerlimitinput.disabled = False
        self.ids.simpsonlowerlimitinput.text = ''
        self.ids.simpsonupperlimitinput.disabled = False
        self.ids.simpsonupperlimitinput.text = ''
        self.ids.simpsonfunctioninput.disabled = False
        self.ids.simpsonfunctioninput.text = ''
        self.ids.simpsonintervalinput.disabled = False
        self.ids.simpsonintervalinput.text = ''
        self.ids.simpson1resultlabel1.text = ''
        self.ids.simpson1resultlabel2.text = ''
        self.ids.simpson1resultlabel3.text = ''
        self.ids.simpson1resultlabel4.text = ''
        self.ids.simpson1resultlabel5.text = ''
        self.ids.simpson1resultlabel6.text = ''
        self.ids.simpson1resultlabel7.text = ''
        self.ids.simpsonclear.background_color = (1, 1, 1, 1)


class SimpsonWindow2(Screen):
    def simpsonvaluenext(self):
        if self.ids.simpsonvaluenext.text != 'Submit':
            n1 = int(self.ids.simpsonvalueinput.text)
            if self.ids.simpsonvaluexinput.background_color == [1, 1, 1, 1]:
                if self.ids.simpsonvalueinput.text == '1':
                    self.ids.simpsonvalueinput.text = ''
                elif self.ids.simpsonvalueinput.text == '0':
                    self.ids.simpsonvalueinput.text = ''
                else:
                    self.ids.simpsonvaluexlabel.color = (0, 0, 0, 1)
                    self.ids.simpsonvaluexinput.background_color = (
                        220/255, 222/255, 224/255)
                    self.ids.simpsonvalueylabel.color = (0, 0, 0, 1)
                    self.ids.simpsonvalueyinput.background_color = (
                        220/255, 222/255, 224/255)
                    self.ids.simpsonvaluexlabel.text = "x1 :"
                    self.ids.simpsonvalueylabel.text = "y1 :"
                    self.ids.simpsonvalueinput.disabled = True
            else:
                s1 = self.ids.simpsonvaluexlabel.text
                s2 = self.ids.simpsonvalueylabel.text
                n = int(s1[1])
                if n == n1:
                    simpsonxlist.append(
                        float(self.ids.simpsonvaluexinput.text))
                    simpsonylist.append(
                        float(self.ids.simpsonvalueyinput.text))
                    self.ids.simpsonvaluexinput.text = ''
                    self.ids.simpsonvalueyinput.text = ''
                    self.ids.simpsonvaluexinput.disabled = True
                    self.ids.simpsonvalueyinput.disabled = True
                    self.ids.simpsonvaluenext.text = 'Submit'
                else:
                    simpsonxlist.append(
                        float(self.ids.simpsonvaluexinput.text))
                    simpsonylist.append(
                        float(self.ids.simpsonvalueyinput.text))
                    s3 = s1.replace(str(n), str(n+1), 1)
                    s4 = s2.replace(str(n), str(n+1), 1)
                    self.ids.simpsonvaluexlabel.text = s3
                    self.ids.simpsonvalueylabel.text = s4
                    self.ids.simpsonvaluexinput.text = ''
                    self.ids.simpsonvalueyinput.text = ''
        else:
            self.ids.simpson2clear.background_color = (237/255, 39/255, 17/255)
            self.ids.simpsonresultlabel1.text = "The Integral of f(x) by Simpson's 1/3rd rule is given by :"
            self.ids.simpsonresultlabel2.text = "F(x) = h/3 [ A + 4B + 2C ]"
            self.ids.simpsonresultlabel3.text = "where A = Sum of first and last ordinates"
            self.ids.simpsonresultlabel4.text = "B = Sum of all the even positions"
            self.ids.simpsonresultlabel5.text = "C = Sum of all odd positions"
            a = simpsonxlist[0]
            b = simpsonxlist[len(simpsonxlist)-1]
            h = (b-a)/(int(self.ids.simpsonvalueinput.text)-1)
            A = simpsonylist[0]+simpsonylist[len(simpsonylist)-1]
            B, C = 0, 0
            t2 = simpsonylist.copy()
            del simpsonylist[0]
            del simpsonylist[len(simpsonylist)-1]
            for i in range(0, len(simpsonylist), 2):
                B += simpsonylist[i]
            t2sum = 0
            for i in t2:
                t2sum += i
            C = t2sum-B-A
            I = round(h*(A+4*B+2*C)/3, 5)
            self.ids.simpsonresultlabel6.text = "In our case we have A = " + \
                str(A)+" , B = "+str(B)+" , C = "+str(C)+" and h = "+str(h)
            self.ids.simpsonresultlabel7.text = "The value of the Given Integral between the limits " + \
                str(a)+" and "+str(b)+" is "+str(I)

    def simpsonclearfunction2(self):
        self.ids.simpsonvalueinput.disabled = False
        self.ids.simpsonvalueinput.text = ''
        self.ids.simpsonvaluexinput.disabled = False
        self.ids.simpsonvalueyinput.disabled = False
        self.ids.simpsonvaluexlabel.text = ""
        self.ids.simpsonvalueylabel.text = ""
        self.ids.simpsonresultlabel1.text = ''
        self.ids.simpsonresultlabel2.text = ''
        self.ids.simpsonresultlabel3.text = ''
        self.ids.simpsonresultlabel4.text = ''
        self.ids.simpsonresultlabel5.text = ''
        self.ids.simpsonresultlabel6.text = ''
        self.ids.simpsonresultlabel7.text = ''
        self.ids.simpsonvaluenext.text = 'Next'
        self.ids.simpsonvaluexinput.background_color = (1, 1, 1, 1)
        self.ids.simpsonvalueyinput.background_color = (1, 1, 1, 1)
        self.ids.simpson2clear.background_color = (1, 1, 1, 1)


class RKWindow(Screen):
    def rkfunction(self):
        s = sympify(self.ids.rkfunctioninput.text)
        self.ids.rkfunctioninput.text = ''
        x0 = float(self.ids.rkx0input.text)
        y0 = float(self.ids.rky0input.text)
        x1 = float(self.ids.rkxinput.text)
        x, y = symbols('x y')
        h = x1-x0
        self.ids.rkhlabel.text = 'h = '+str(x1)+" - "+str(x0)+" = "+str(h)
        self.ids.rklabel1.color = (14/255, 182/255, 194/255)
        self.ids.rklabel2.color = (14/255, 182/255, 194/255)
        self.ids.rklabel3.color = (14/255, 182/255, 194/255)
        self.ids.rklabel4.color = (14/255, 182/255, 194/255)
        self.ids.rklabel5.color = (14/255, 182/255, 194/255)
        self.ids.rklabel6.color = (14/255, 182/255, 194/255)
        k1 = h*s.subs([(x, x0), (y, y0)])
        k2 = h*s.subs([(x, x0+h/2), (y, y0+k1/2)])
        k3 = h*s.subs([(x, x0+h/2), (y, y0+k2/2)])
        k4 = h*s.subs([(x, x0+h), (y, y0+k3)])
        k = (k1+2*k2+2*k3+k4)/6
        y1 = y0+k
        self.ids.rkresultlabel1.text = "But we have k1 = "+str(round(k1, 5))+" , k2 = "+str(round(
            k2, 5))+" , k3 = "+str(round(k3, 5))+" , k4 = "+str(round(k4, 5))+" and k = "+str(round(k, 5))
        self.ids.rkresultlabel2.text = "The value of y at x = " + \
            str(x1)+" is "+str(round(y1, 5))
        self.ids.rkclear.background_color = (237/255, 39/255, 17/255)
        self.ids.rkfunctioninput.disabled = True
        self.ids.rkx0input.disabled = True
        self.ids.rky0input.disabled = True

    def rkclearfunction(self):
        self.ids.rkclear.background_color = (1, 1, 1, 1)
        self.ids.rkfunctioninput.text = ''
        self.ids.rkx0input.text = ''
        self.ids.rky0input.text = ''
        self.ids.rkxinput.text = ''
        self.ids.rkhlabel.text = ''
        self.ids.rkfunctioninput.disabled = False
        self.ids.rkx0input.disabled = False
        self.ids.rky0input.disabled = False
        self.ids.rkxinput.disabled = False
        self.ids.rklabel1.color = (1, 1, 1, 1)
        self.ids.rklabel2.color = (1, 1, 1, 1)
        self.ids.rklabel3.color = (1, 1, 1, 1)
        self.ids.rklabel4.color = (1, 1, 1, 1)
        self.ids.rklabel5.color = (1, 1, 1, 1)
        self.ids.rklabel6.color = (1, 1, 1, 1)
        self.ids.rkresultlabel1.text = ""
        self.ids.rkresultlabel2.text = ""


class SteamNozzle(Screen):
    pass


class SteadyStateConduction(Screen):
    pass


class PlaneWall(Screen):
    def planewallsubmit1f(self):
        if self.ids.planewallkinput.text == '':
            k = 0
        else:
            k = float(self.ids.planewallkinput.text)
        if self.ids.planewallAinput.text == '':
            A = 0
        else:
            A = float(self.ids.planewallAinput.text)
        if self.ids.planewallT1input.text == '':
            T1 = 0
        else:
            T1 = float(self.ids.planewallT1input.text)+273
        if self.ids.planewallT2input.text == '':
            T2 = 0
        else:
            T2 = float(self.ids.planewallT2input.text)+273
        if self.ids.planewallLinput.text == '':
            L = 0
        else:
            L = float(self.ids.planewallLinput.text)
        if self.ids.planewallQinput.text == '':
            Q = 0
        else:
            Q = float(self.ids.planewallQinput.text)
        if k == 0 and T1 != 0 and T2 != 0 and L != 0 and Q != 0:
            if A == 0:
                A = 1
            k = Q*L/((T1-T2)*A)
            if A == 1:
                self.ids.planewallresultlabel1.text = "The Thermal conductivity of the plane wall is " + \
                    str(k)+" W/mK (Assuming Unit Area)"
            else:
                self.ids.planewallresultlabel1.text = "The Thermal conductivity of the plane wall is " + \
                    str(k)+" W/mK"
        elif A == 0 and k != 0 and T1 != 0 and T2 != 0 and L != 0 and Q != 0:
            A = Q*L/((T1-T2)*k)
            self.ids.planewallresultlabel1.text = "The Area of the plane wall is " + \
                str(A)+" m²"
        elif T1 == 0 and k != 0 and T2 != 0 and L != 0 and Q != 0:
            if A == 0:
                A = 1
            T1 = Q*L/(A*k)+T2
            if A == 1:
                self.ids.planewallresultlabel1.text = "The Inner temperature of the plane wall is " + \
                    str(T1)+" K (Assuming Unit Area)"
            else:
                self.ids.planewallresultlabel1.text = "The Inner temperature of the plane wall is " + \
                    str(T1)+" K"
        elif T2 == 0 and k != 0 and T1 != 0 and L != 0 and Q != 0:
            if A == 0:
                A = 1
            T2 = T1-Q*L/(A*k)
            if A == 1:
                self.ids.planewallresultlabel1.text = "The Outer temperature of the plane wall is " + \
                    str(T2)+" K (Assuming Unit Area)"
            else:
                self.ids.planewallresultlabel1.text = "The Outer temperature of the plane wall is " + \
                    str(T2)+" K"
        elif L == 0 and k != 0 and T1 != 0 and T2 != 0 and Q != 0:
            if A == 0:
                A = 1
            L = A*(T1-T2)*k/Q
            if A == 1:
                self.ids.planewallresultlabel1.text = "The thickness of the plane wall is " + \
                    str(L)+" m (Assuming Unit Area)"
            else:
                self.ids.planewallresultlabel1.text = "The thickness of the plane wall is " + \
                    str(L)+" m"
        elif Q == 0 and k != 0 and T1 != 0 and T2 != 0 and L != 0:
            if A == 0:
                A = 1
            Q = k*A*(T1-T2)/L
            if A == 1:
                self.ids.planewallresultlabel1.text = "The Heat flowing through the plane wall is " + \
                    str(Q)+" W (Assuming Unit Area)"
            else:
                self.ids.planewallresultlabel1.text = "The Heat flowing through the plane wall is " + \
                    str(Q)+" W"
        animate=Animation(color=(22/255, 196/255, 71/255,1))
        animate.start(self.ids.planewallresultlabel1)
        
class HollowCylinder(Screen):
    pass


class HollowSphere(Screen):
    pass


class CompositeCylinder(Screen):
    pass


class CompositeSphere(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("design_file.txt")


class BuhariApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv


if __name__ == '__main__':
    BuhariApp().run()

from manim import *
class Test(Scene):
    def construct(self):
        t = ValueTracker(-2)
        vektor = Vector([1,t.get_value()],color=ORANGE)
        #achsen = Axes(y_range=[-2.999,2.999,1],x_range=[-4.5,4.5,1],x_length=9,y_length=6,axis_config={'tip_shape': StealthTip})
        nupl = NumberPlane().set_opacity(0.5)
        self.add(nupl,vektor)
        vektor.add_updater(lambda x : x.become(Vector([1,t.get_value()],color=ORANGE).move_to([t.get_value(),0,0])))
        self.play(t.animate.set_value(3),run_time=2,)
        self.wait()


class Kräftaddieren(Scene):
    def construct(self):
        nupl = NumberPlane(x_range=(-10,10,1.5),y_range=(-6,6,1.5)).set_opacity(0.3)
        nupl.shift(DL)
        vector1 = nupl.get_vector([0,0,0]).set_color(ORANGE)
        vector2 = nupl.get_vector([0,0,0]).set_color(BLUE)
        vector3 = nupl.get_vector([0,0,0]).set_color(WHITE)
        fragezeichen = Tex("?" , color = WHITE)
        vector1x = 4
        vector1y = 0.5
        vector2x = 1
        vector2y = 3
        fragezeichen.add_updater(lambda mob : mob.next_to(vector3, UR).shift(0.6 *DOWN))
        self.wait(0.5)
        self.play(FadeIn(nupl))
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait(2)
        self.add(fragezeichen)
        self.play(vector3.animate.become(nupl.get_vector([2.5,3.2,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([1.5,2.5,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([3.7,1.8,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)),FadeOut(fragezeichen),run_time=2)
        self.wait(2)
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.wait()
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=2)
        self.wait(2)
        vector1x = -4.5
        vector1y = -1.5
        vector2x = 2.75
        vector2y = 4.5
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)),run_time=2)
        self.wait()
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=2)
        vector1x = -3
        vector1y = 0.75
        vector2x = 4.5
        vector2y = 3
        self.wait()
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        vector1x = -4.5
        vector1y = 1.5
        vector2x = 1.5
        vector2y = -2.75
        self.wait()
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait()

class safd(Scene):
    def construct(self):
        self.wait()
        self.wait()
# s = [2,1]
# func1 = lambda pos: s[0] * RIGHT + s[1] * UP
# vecfield = ArrowVectorField(func1,x_range=[-9,8,0.7],y_range=[-5,4,0.7]).set_color(BLUE).set_opacity(0)
# self.add(vecfield)
# self.play(vecfield.animate.shift(s[0]/2 * RIGHT + s[1]/2 * UP).set_opacity(1), rate_func=rate_functions.ease_in_quart, run_time=1.5)
# self.play(vecfield.animate.shift(s[0]/2 * RIGHT + s[1]/2 * UP).set_opacity(0), rate_func=rate_functions.ease_out_quart, run_time=1.5)

# Update-3
from manim import *
import numpy as np
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

class Kraftdarstellen(Scene):
    def construct(self):

        #Raster
        nupl = NumberPlane(x_range=(-10,10,1.5),y_range=(-6,6,1.5)).set_opacity(0.5)

        #Texte
        kraftdarstellen = Tex("Kraft darstellen").scale(1.2)
        ul1 = Underline(kraftdarstellen)
        blackbox1 = SurroundingRectangle(kraftdarstellen, buff=0, color=BLACK,fill_opacity=1)
        kraftdarstellengruppe = VGroup(blackbox1,kraftdarstellen,ul1)

        pfeil = Tex("Pfeil = Vektor")
        blackbox2 = SurroundingRectangle(pfeil, color=BLACK,fill_opacity=1,buff=0)
        pfeilgruppe = VGroup(blackbox2,pfeil)

        newton = Tex("1 Kästchen = 1 Newton (N)")
        blackbox3 = SurroundingRectangle(newton, color=BLACK,fill_opacity=1,buff=0)
        newtongruppe = VGroup(blackbox3,newton)

        fünf = Tex("5N")

        angriffspunkt = Tex("Angriffspunkt")
        blackbox5 = SurroundingRectangle(angriffspunkt, color=BLACK,fill_opacity=1,buff=0)
        angriffspunktgruppe = VGroup(blackbox5,angriffspunkt)

        #Andere Mobjects
        v1 = nupl.get_vector([6,4.5,0]).set_color(ORANGE)
        v2 = nupl.get_vector([-3,1.5,0]).set_color(ORANGE)
        v2.shift(0.5 * DOWN)
        v2.shift(2.5 * RIGHT)
        v3 = nupl.get_vector([4.5,-3,0]).set_color(ORANGE)
        v3.shift(3.5*LEFT)
        v3.shift(0.5*DOWN)
        punkt = Dot()
        punkt.shift(2 * DL)
        

        #Animationen
        self.add(kraftdarstellengruppe)
        self.wait()
        self.play(kraftdarstellengruppe.animate.to_corner(UL))
        nupl.shift(2 * DL)
        self.play(FadeIn(nupl))
        self.add(kraftdarstellengruppe)
        self.wait()
        v1.shift(2 * DL) 
        self.play(GrowArrow(v1))
        self.wait(3)
        pfeilgruppe.move_to([-1.5,0,0])
        self.play(Write(pfeilgruppe))
        self.wait()
        self.play(pfeilgruppe.animate.next_to(kraftdarstellen, DOWN).to_edge(LEFT))
        self.wait(1.4)
        newtongruppe.next_to(pfeilgruppe, DOWN).to_edge(LEFT)
        fünf.move_to([0.3,0.4,0])
        self.play(Write(newtongruppe))
        self.wait()
        self.play(Write(fünf))
        self.wait(1.4)
        angriffspunktgruppe.move_to([-3.6,-1.6,0])
        self.play(Write(angriffspunktgruppe))
        self.play(Circumscribe(punkt,Circle))
        self.wait()
        self.play(angriffspunktgruppe.animate.next_to(newtongruppe, DOWN).to_edge(LEFT))
        self.wait(2)
        self.play(ReplacementTransform(v1,v2),FadeOut(fünf),run_time=2)
        self.wait()
        self.play(ReplacementTransform(v2,v3),run_time=2)
        self.wait(0.3)    

class Axiom2(Scene):
    def construct(self):

        #texte
        axiom2 = Tex("Newton's zweites Axiom").scale(1.2)
        ul1 = Underline(axiom2)
        blackbox1 = SurroundingRectangle(axiom2, buff=0, color=BLACK,fill_opacity=1)
        axiom2gruppe = VGroup(blackbox1,axiom2,ul1)
        self.add(axiom2gruppe)
        self.wait()
        self.play(axiom2gruppe.animate.to_corner(UL))

        beschreibung = Tex("Formel der Kraft (F)")
        blackbox2 = SurroundingRectangle(beschreibung, color=BLACK,fill_opacity=1,buff=0)
        beschreibunggruppe = VGroup(blackbox2,beschreibung)

        formel1 = Tex("F = ")
        #(haha witzig wegen formel 1)
        blackbox3 = SurroundingRectangle(formel1, color=BLACK,fill_opacity=1,buff=0)
        formel1gruppe = VGroup(blackbox3,formel1)

        formel2 = Tex("F = a ")
        blackbox6 = SurroundingRectangle(formel2, color=BLACK,fill_opacity=1,buff=0)
        formel2gruppe = VGroup(blackbox6,formel2)

        formel3 = MathTex("F = m \cdot a")
        blackbox9 = SurroundingRectangle(formel3, color=BLACK,fill_opacity=1,buff=0)
        formel3gruppe = VGroup(blackbox9,formel3)

        n1 = Tex("1N")
        blackbox4 = SurroundingRectangle(n1, color=BLACK,fill_opacity=1,buff=0)
        n1gruppe = VGroup(blackbox4,n1)

        n2 = Tex("2N")
        blackbox5 = SurroundingRectangle(n2, color=BLACK,fill_opacity=1,buff=0)
        n2gruppe = VGroup(blackbox5,n2)

        n3 = Tex("3N")
        blackbox8 = SurroundingRectangle(n3, color=BLACK,fill_opacity=1,buff=0)
        n3gruppe = VGroup(blackbox8,n3)

        m = Tex("m = Masse")
        blackbox7 = SurroundingRectangle(m, color=BLACK,fill_opacity=1,buff=0)
        mgruppe = VGroup(blackbox7,m)

        a = Tex("a = Beschleunigung")
        blackbox7 = SurroundingRectangle(a, color=BLACK,fill_opacity=1,buff=0)
        agruppe = VGroup(blackbox7,a)

        #Andere Mobjects:
        iceblock1 = ImageMobject("ice.png").scale(0.6)
        iceblock1.move_to([-5,-2.2,0])
        iceblock2 = ImageMobject("ice.png").scale(0.8)
        iceblock2.move_to([-5,-1,0])
        iceblock3 = ImageMobject("ice.png").scale(0.6)
        iceblock3.move_to([-5,-2.8,0])
        ax1 = NumberLine(x_range=[0,15,1])
        ax2 = NumberLine(x_range=[0,15,1])
        ax1.shift(2.7*DOWN)
        v1 = Vector([1,0,0]).set_color(ORANGE)
        v2 = Vector([2,0,0]).set_color(ORANGE)
        v3 = Vector([3,0,0]).set_color(ORANGE)

        t = ValueTracker(0)
        m = 1
        m2 = 2
        vorzeichen = ValueTracker(1)
        offset = ValueTracker(-5)
        f = 1
        f2 = 2
        f3 = 3

        #animation
        self.wait(1.5)
        beschreibunggruppe.next_to(axiom2gruppe, DOWN).to_edge(LEFT)
        self.wait(2)
        self.play(Write(beschreibunggruppe))
        self.wait(2)
        formel1gruppe.move_to([0,1,0])
        formel2gruppe.move_to([0,1,0])
        formel3gruppe.move_to([0,1,0])
        self.play(Write(formel1gruppe))
        self.wait(3)
        self.play(Create(ax1),run_time=2)
        n1gruppe.add_updater(lambda mob : mob.next_to(v1,UP).shift(0.1*DL))
        v1.add_updater(lambda mob : mob.next_to(iceblock1,RIGHT).shift(0.3*LEFT))
        self.play(FadeIn(iceblock1,v1,n1gruppe))
        iceblock1.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-2.2,0]))
        self.wait(2)
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        t.set_value(0)

        self.remove(iceblock1,v1,n1gruppe)
        ax1.move_to([0,-2.7,0])
        self.remove(iceblock2,iceblock3,v2,n2gruppe)
        t.set_value(0)
        self.wait(3)
        v3.add_updater(lambda mob : mob.next_to(iceblock1,RIGHT).shift(0.3*LEFT))
        n3gruppe.add_updater(lambda mob : mob.next_to(v3,UP).shift(0.1*DL))
        v1.add_updater(lambda mob : mob.next_to(iceblock3,RIGHT).shift(0.3*LEFT))
        n1gruppe.add_updater(lambda mob : mob.next_to(v1,UP).shift(0.1*DL))
        ax1.shift(0.6*DOWN)
        ax2.shift(1.6*DOWN)
        iceblock1.clear_updaters()
        iceblock1.move_to([-5,-2.8,0])
        iceblock3.move_to([-5,-1,0])
        self.play(FadeIn(v3,n3gruppe,v1,n1gruppe,ax1,ax2,iceblock1,iceblock3))
        self.wait(3)
        iceblock1.add_updater(lambda mob : mob.move_to([(0.5*(f3/m)* (t.get_value())**2) + offset.get_value(),-2.8,0]))
        iceblock3.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-1,0]))
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        self.play(ReplacementTransform(formel1gruppe,formel2gruppe))
        agruppe.next_to(beschreibunggruppe, DOWN).to_edge(LEFT)
        self.play(Write(agruppe))

        self.wait(1.5)
        iceblock2.clear_updaters()
        v1.clear_updaters()
        iceblock1.clear_updaters()
        v2.add_updater(lambda mob : mob.next_to(iceblock2,RIGHT).shift(0.3*LEFT))
        v1.add_updater(lambda mob : mob.next_to(iceblock3,RIGHT).shift(0.3*LEFT))
        n2gruppe.add_updater(lambda mob : mob.next_to(v2,UP).shift(0.1*DL))
        iceblock2.move_to([0,0,0])
        iceblock2.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-1,0]))
        iceblock3.add_updater(lambda mob : mob.move_to([(0.5*(f2/m2)* (t.get_value())**2) + offset.get_value(),-2.8,0]))
        self.wait(2.5)
        self.play(FadeOut(ax1))
        t.set_value(0)
        self.play(FadeIn(ax1,ax2,iceblock3,iceblock2,v1,n1gruppe,v2,n2gruppe))
        self.wait(3.5)
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        self.wait(2.5)
        self.play(ReplacementTransform(formel2gruppe,formel3gruppe))
        mgruppe.next_to(agruppe, DOWN).to_edge(LEFT)
        self.play(Write(mgruppe))
        self.wait(2.5)
        self.play(FadeOut(ax1,ax2))
        self.wait(2.5)
        self.play(Circumscribe(formel3gruppe))
        self.play(formel3gruppe.animate.next_to(mgruppe, DOWN).to_edge(LEFT))
               
class Kraftaddieren(Scene):
    def construct(self):
        kräfteaddieren = Tex("Kräfte addieren").scale(1.2)
        ul1 = Underline(kräfteaddieren)
        blackbox1 = SurroundingRectangle(kräfteaddieren, buff=0, color=BLACK,fill_opacity=1)
        kräftaddierengruppe = VGroup(blackbox1,kräfteaddieren,ul1)
        self.add(kräftaddierengruppe)
        self.wait()
        self.play(kräftaddierengruppe.animate.to_corner(UL))

        nupl = NumberPlane(x_range=(-10,10,1.5),y_range=(-6,6,1.5)).set_opacity(0.5)
        nupl.shift(DL)
        vector1 = nupl.get_vector([0,0,0]).set_color(ORANGE)
        vector2 = nupl.get_vector([0,0,0]).set_color(BLUE)
        vector3 = nupl.get_vector([0,0,0]).set_color(WHITE)
        fragezeichen = Tex("?" , color = WHITE)
        fragezeichen.add_updater(lambda mob : mob.next_to(vector3, UR).shift(0.6 *DOWN))
        self.wait(0.5)
        self.play(FadeIn(nupl))
        self.add(kräftaddierengruppe)

        vector1x = 1.5
        vector1y = 1.5
        vector2x = 3
        vector2y = 3

        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait(2)
        self.play(vector1.animate.shift(0.1*UL))
        self.wait()
        pfeil = Tex("Pfeil = Vektor")
        blackbox2 = SurroundingRectangle(pfeil, color=BLACK,fill_opacity=1,buff=0)
        pfeilgruppe = VGroup(blackbox2,pfeil)
        pfeilgruppe.move_to([-2.2,0,0])
        self.play(Write(pfeilgruppe))
        self.wait()
        self.play(pfeilgruppe.animate.next_to(kräftaddierengruppe, DOWN).to_edge(LEFT))

        self.add(fragezeichen)
        vector3.shift(0.1*DR)
        self.play(vector3.animate.become(nupl.get_vector([4,4,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([4.5,4.5,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([3.5,3.5,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.play(FadeOut(fragezeichen))

        self.play(vector1.animate.move_to(vector2.get_end() * 1.37))
        #ich weiß selber nicht woher diese 1.37 kommt also falls das hier jemand sieht, frag nicht
        self.wait()

        vektorverbindung = Tex("Verbindung")
        vektorverbindungfull = Tex("Vektoren werden Verbunden")
        blackbox7 = SurroundingRectangle(vektorverbindungfull, color=BLACK,fill_opacity=1,buff=0)
        vektorverbindungfullgruppe = VGroup(blackbox7,vektorverbindungfull)
        blackbox8 = SurroundingRectangle(vektorverbindung, color=BLACK,fill_opacity=1,buff=0)
        vektorverbindunggruppe = VGroup(blackbox8,vektorverbindung)
        vektorverbindunggruppe.move_to([0.3,2.3,0])
        punkt = Dot()
        self.play(Write(vektorverbindunggruppe))
        punkt.move_to(vector1.get_start())
        self.play(Circumscribe(punkt,Circle),run_time=1.4)
        self.play(vektorverbindunggruppe.animate.move_to([-5,1.8,1]).set_opacity(0))
        vektorverbindungfullgruppe.next_to(pfeilgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(vektorverbindungfullgruppe))

        self.play(vector3.animate.become(nupl.get_vector([4.5,4.5,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).shift(0.1*UL).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait()

        resultierend = Tex("Resultierende Kraft")
        blackbox6 = SurroundingRectangle(resultierend, color=BLACK,fill_opacity=1,buff=0)
        resultierendgruppe = VGroup(blackbox6,resultierend)
        resultierendgruppe.move_to([2.7,0,0])
        self.play(Write(resultierendgruppe))
        self.play(vector3.animate.set_stroke(width=8,color=YELLOW),rate_func=there_and_back)
        self.play(resultierendgruppe.animate.next_to(vektorverbindungfullgruppe, DOWN).to_edge(LEFT))
        self.wait()
        self.play(FadeOut(vector3))
        vector3.become(nupl.get_vector([0,0,0]).set_color(WHITE))
        self.wait(1)


        #2ter Abschnitt
        vector1x = 4
        vector1y = 0.5
        vector2x = 1
        vector2y = 3
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

        vektorverbindung = Tex("Verbindung")
        blackbox3 = SurroundingRectangle(vektorverbindung, color=BLACK,fill_opacity=1,buff=0)
        vektorverbindunggruppe = VGroup(blackbox3,vektorverbindung)
        punkt2 = Dot()
        vektorverbindunggruppe.shift(1.2 * RIGHT)
        self.play(Write(vektorverbindunggruppe))
        punkt2.move_to(vector2.get_start())
        self.play(Circumscribe(punkt2,Circle),run_time=1.4)
        self.play(vektorverbindunggruppe.animate.set_opacity(0))
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait()

        vector1x = 3
        vector1y = -1.5
        vector2x = 4.5
        vector2y = 1.5
        basevector1 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)
        basevector2 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        self.play(vector1.animate.become(basevector1),vector2.animate.become(basevector2),vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)),run_time=2)
        self.wait()
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.play(vector1.animate.become(basevector1),vector2.animate.become(basevector2),run_time=2)
        vector1x = -1.5
        vector1y = 0.75
        vector2x = 4.5
        vector2y = 3
        basevector1 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)
        basevector2 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        self.wait()

        füralle = Tex("Vektoren: Selber Angriffpunkt")
        blackbox5 = SurroundingRectangle(füralle, color=BLACK,fill_opacity=1,buff=0)
        fürallegruppe = VGroup(blackbox5,füralle)
        fürallegruppe.next_to(resultierendgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(fürallegruppe))

        self.play(vector1.animate.become(basevector1),vector2.animate.become(basevector2),vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        vector1x = -4.5
        vector1y = 0.75
        vector2x = 1.5
        vector2y = -2.75
        basevector1 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)
        basevector2 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        self.wait()
        self.play(vector1.animate.become(basevector1),vector2.animate.become(basevector2),vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait()

class Kräfteparalellogramm(Scene):
    def construct(self):

        kräfteparalellogramm = Tex("Kräfteparalellogramm").scale(1.2)
        ul1 = Underline(kräfteparalellogramm)
        blackbox1 = SurroundingRectangle(kräfteparalellogramm, buff=0, color=BLACK,fill_opacity=1)
        kräfteparalellogrammgruppe = VGroup(blackbox1,kräfteparalellogramm,ul1)
        self.add(kräfteparalellogrammgruppe)
        self.wait()
        self.play(kräfteparalellogrammgruppe.animate.to_corner(UL))


        nupl = NumberPlane(x_range=(-10,10,1.5),y_range=(-6,6,1.5)).set_opacity(0.5)
        nupl.shift(2*DL)
        nupl.shift(LEFT)
        vector1 = nupl.get_vector([0,0,0]).set_color(ORANGE)
        vector2 = nupl.get_vector([0,0,0]).set_color(BLUE)
        vector3 = nupl.get_vector([0,0,0]).set_color(WHITE)
        vector1x = 4.5
        vector1y = 1.5
        vector2x = 1.5
        vector2y = 3
        vector4 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        vector5 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)

        self.play(FadeIn(nupl))
        self.add(kräfteparalellogrammgruppe)
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait()
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)

        additionbasisfull = Tex("Basis auf Kraftaddition")
        blackbox2 = SurroundingRectangle(additionbasisfull, color=BLACK,fill_opacity=1,buff=0)
        additionbasisfullgruppe = VGroup(blackbox2,additionbasisfull)
        additionbasis = Tex("Kraftaddition")
        blackbox3 = SurroundingRectangle(additionbasis, color=BLACK,fill_opacity=1,buff=0)
        additionbasisgruppe = VGroup(blackbox3,additionbasis)
        additionbasisgruppe.shift(2.5 * LEFT)
        self.play(Write(additionbasisgruppe))
        self.play(vector3.animate.set_stroke(width=8,color=YELLOW),rate_func=there_and_back)
        self.play(additionbasisgruppe.animate.move_to([-4.5,2,1]).set_opacity(0))
        additionbasisfullgruppe.next_to(kräfteparalellogrammgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(additionbasisfullgruppe))
        self.wait(0.6)

        #ist gehardcoded ich weiß....
        punkt = Dot(point=[3,2.5,0],color=RED)
        self.play(FadeIn(punkt))
        self.wait(2)
        self.play(vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)))
        self.wait()
        vector4.shift(vector1y*UP).shift(vector1x*RIGHT)
        self.add(vector4)
        self.add(vector5)
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait()
        self.play(vector1.animate.shift(vector2y*UP).shift(vector2x*RIGHT))

        spieglung = Tex("Spieglung")
        blackbox2 = SurroundingRectangle(spieglung, color=BLACK,fill_opacity=1,buff=0)
        spieglunggruppe = VGroup(blackbox2,spieglung)
        spieglungfull = Tex("Spieglung der Vektoren")
        blackbox4 = SurroundingRectangle(spieglungfull, color=BLACK,fill_opacity=1,buff=0)
        spieglungfullgruppe = VGroup(blackbox4,spieglungfull)
        spieglunggruppe.move_to([-3.7,-0.7,0])
        self.play(Write(spieglunggruppe))
        self.play(vector1.animate.set_stroke(width=8,color=YELLOW),vector2.animate.set_stroke(width=8,color=YELLOW),rate_func=there_and_back)
        self.play(spieglunggruppe.animate.move_to([-4.5,1.6,1]).set_opacity(0))
        spieglungfullgruppe.next_to(additionbasisfullgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(spieglungfullgruppe))
        self.play(FadeOut(punkt))
        
        vector1.become(nupl.get_vector([vector1x,vector1y]))
        vector4.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE))
        vector4.shift(vector1y*UP).shift(vector1x*RIGHT)
        vector5.become(nupl.get_vector([vector1x,vector1y]).set_color(ORANGE))
        vector1.shift(vector2y*UP).shift(vector2x*RIGHT).set_color(ORANGE)
        vector2.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE))
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)))

        self.wait()
        vector1x = 3
        vector1y = 0
        vector2x = 3
        vector2y = 3
        self.play(
        vector1.animate.become(nupl.get_vector([vector1x,vector1y]).shift(vector2y*UP + vector2x*RIGHT).set_color(ORANGE)),
        vector4.animate.become(nupl.get_vector([vector2x,vector2y]).shift(vector1y*UP + vector1x*RIGHT).set_color(BLUE)),
        vector5.animate.become(nupl.get_vector([vector1x,vector1y]).set_color(ORANGE)),
        vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),
        vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),
        run_time=1.5)

        füralle = Tex("Vektoren: Selber Angriffpunkt")
        blackbox6 = SurroundingRectangle(füralle, color=BLACK,fill_opacity=1,buff=0)
        fürallegruppe = VGroup(blackbox6,füralle)
        fürallegruppe.next_to(spieglungfullgruppe, DOWN).to_edge(LEFT)

        self.wait()
        vector1x = -3
        vector1y = -0.75
        vector2x = 1.5
        vector2y = 2.25
        self.play(
        vector1.animate.become(nupl.get_vector([vector1x,vector1y]).shift(vector2y*UP + vector2x*RIGHT).set_color(ORANGE)),
        vector4.animate.become(nupl.get_vector([vector2x,vector2y]).shift(vector1y*UP + vector1x*RIGHT).set_color(BLUE)),
        vector5.animate.become(nupl.get_vector([vector1x,vector1y]).set_color(ORANGE)),
        vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),
        vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),
        FadeIn(fürallegruppe),
        run_time=1.5)

        self.wait()
        vector1x = 6
        vector1y = -1.5
        vector2x = 1.5
        vector2y = 1.5
        self.play(
        vector1.animate.become(nupl.get_vector([vector1x,vector1y]).shift(vector2y*UP + vector2x*RIGHT).set_color(ORANGE)),
        vector4.animate.become(nupl.get_vector([vector2x,vector2y]).shift(vector1y*UP + vector1x*RIGHT).set_color(BLUE)),
        vector5.animate.become(nupl.get_vector([vector1x,vector1y]).set_color(ORANGE)),
        vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),
        vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),
        run_time=1.7)
        self.wait()



# s = [2,1]
# func1 = lambda pos: s[0] * RIGHT + s[1] * UP
# vecfield = ArrowVectorField(func1,x_range=[-9,8,0.7],y_range=[-5,4,0.7]).set_color(BLUE).set_opacity(0)
# self.add(vecfield)
# self.play(vecfield.animate.shift(s[0]/2 * RIGHT + s[1]/2 * UP).set_opacity(1), rate_func=rate_functions.ease_in_quart, run_time=1.5)
# self.play(vecfield.animate.shift(s[0]/2 * RIGHT + s[1]/2 * UP).set_opacity(0), rate_func=rate_functions.ease_out_quart, run_time=1.5)
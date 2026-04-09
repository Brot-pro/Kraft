from manim import *

class Test(Scene):
    def construct(self):
        # t = ValueTracker(-2)
        # a = MathTex(r"\begin{bmatrix}12 \\34\end{bmatrix}")
        # #  vektor = Vector([1,t.get_value()],color=ORANGE)
        # # #achsen = Axes(y_range=[-2.999,2.999,1],x_range=[-4.5,4.5,1],x_length=9,y_length=6,axis_config={'tip_shape': StealthTip})
        # # nupl = NumberPlane().set_opacity(0.5)
        # # self.add(nupl,vektor)
        # # vektor.add_updater(lambda x : x.become(Vector([1,t.get_value()],color=ORANGE).move_to([t.get_value(),0,0])))
        # # self.play(t.animate.set_value(3),run_time=2,)
        # # self.wait()
        # self.add(a)

        self.add(NumberPlane())

class Wasistkraft(Scene):
    def construct(self):

        #texte
        wasistkraft = Tex("Was ist Kraft?").scale(1.2)
        ul1 = Underline(wasistkraft)
        wasistkraftgruppe = VGroup(wasistkraft,ul1)

        bewegungszustand = Tex("Veränderung des Bewegungszustandes")
        form = Tex("Veränderung der Form")

        #andere Mobjects
        ball = ImageMobject("handball.png").scale(0.5)


        #gruppen
        g1 = Tex("Kraft").scale(1.2)
        g2 = Rectangle(width=1.8, height=0.6).set_color(ORANGE)
        g3 = Vector([2,0]).set_color(ORANGE)
        g3.shift(0.9*RIGHT)
        ggruppe = VGroup(g1,g2,g3)
        ggruppe.shift(6*LEFT)

        f1 = Tex("Kraft").scale(1.2)
        f2 = Rectangle(width=1.8, height=0.6).set_color(ORANGE)
        f3 = Vector([-2,0]).set_color(ORANGE)
        f3.shift(0.9*LEFT)
        fgruppe = VGroup(f1,f2,f3)
        fgruppe.shift(5.8*RIGHT)

        #animation
        self.add(wasistkraftgruppe)
        self.wait(1)
        self.play(wasistkraftgruppe.animate.to_corner(UL))
        self.wait(1)
        ball.shift(2*LEFT)
        self.play(FadeIn(ball))
        self.wait(4)
        self.play(FadeIn(ggruppe))
        self.play(FadeOut(ggruppe),
                  ball.animate.shift(1*RIGHT),rate_func=linear)
        self.play(ball.animate.shift(1*RIGHT),rate_func=linear)
        self.play(ball.animate.shift(1*RIGHT),rate_func=linear)
        self.play(FadeIn(fgruppe),
                  ball.animate.shift(1*RIGHT),rate_func=linear)
        self.play(FadeOut(fgruppe),rate_func=linear)
        bewegungszustand.next_to(wasistkraftgruppe, DOWN).to_edge(LEFT)
        self.play(Write(bewegungszustand))
        self.wait(3)
        self.play(FadeOut(ball))
        self.wait(2)
        ball.move_to([0,0,0])
        self.play(FadeIn(ball))
        self.wait()
        fgruppe.move_to([3,0,0])
        ggruppe.move_to([-3,0,0])
        self.play(FadeIn(ggruppe),FadeIn(fgruppe))
        self.play(ball.animate.stretch(0.7,dim=0,))
        self.wait(1)
        form.next_to(bewegungszustand, DOWN).to_edge(LEFT)
        self.play(Write(form))
        self.wait(4)
        self.play(FadeOut(ggruppe),FadeOut(fgruppe))
        self.play(ball.animate.stretch(10/7,dim=0,))
        self.wait(2)

class Kraftmessen(Scene):
    def construct(self):

        #Texte:
        wasistkraft = Tex("Wie misst man Kraft?").scale(1.2)
        ul1 = Underline(wasistkraft)
        blackbox1 = SurroundingRectangle(wasistkraft, buff=0, color=BLACK,fill_opacity=1)
        wasistkraftgruppe = VGroup(blackbox1,wasistkraft,ul1)

        newton = Tex("N = Newton")
        blackbox2 = SurroundingRectangle(newton, buff=0, color=BLACK,fill_opacity=1)
        newtongruppe = VGroup(blackbox2,newton)

        kraftmesser = Tex("Feder / Kraftmesser")
        blackbox3 = SurroundingRectangle(kraftmesser, buff=0, color=BLACK,fill_opacity=1)

        #andere Mobjects:
        o = ValueTracker(-2.2)
        h = 2
        g = 9.81
        v0 = ValueTracker(7.5)
        ax = Axes(x_range=[0,10],y_range=[0,5])
        schieferwurf = ax.plot(lambda x : np.tan(o.get_value())*x-((g*(x**2))/(2*(v0.get_value()**2)*np.cos(o.get_value())*np.cos(o.get_value())))+h)
        schieferwurf.add_updater(lambda mob : mob.become(ax.plot(lambda x : np.tan(o.get_value())*x-((g*(x**2))/(2*(v0.get_value()**2)*np.cos(o.get_value())*np.cos(o.get_value())))+h)))
        ball = ImageMobject("ball.png").scale(0.35)
        feder = ImageMobject("feder.png").scale(0.4)
        feder.rotate(-90 * DEGREES)
        kraftbild = ImageMobject("kraftmesser.png").scale(0.5)
        kraftbild.rotate(90 * DEGREES)
        mark0 = Line(UP*0.1, DOWN*0.1)
        mark1 = Line(UP*0.1, DOWN*0.1)
        mark2 = Line(UP*0.1, DOWN*0.1)
        n = Tex("0N 1N 2N...").scale(1)


        #animation:
        self.add(wasistkraftgruppe)
        self.wait(1)
        self.play(wasistkraftgruppe.animate.to_corner(UL))
        ball.shift(DOWN)
        ball.shift(6*LEFT)
        ax.shift(0.5 * DOWN)
        ball.set_z_index(1)
        self.play(FadeIn(ball))
        self.wait(2)
        self.play(Create(ax))
        self.play(Create(schieferwurf),run_time=2)
        self.wait(2)
        self.wait()
        self.play(v0.animate.set_value(9),run_time=2)
        self.wait()
        self.play(v0.animate.set_value(5.5),run_time=2)
        self.wait()
        self.play(v0.animate.set_value(7.6),run_time=2)
        self.wait(4)
        self.play(o.animate.set_value(-2.6),run_time=2)
        self.wait()
        self.play(o.animate.set_value(-1.9),run_time=2)
        self.wait()
        self.play(o.animate.set_value(-2.3),run_time=2)
        self.wait(4)
        self.play(FadeOut(ax,ball),Uncreate(schieferwurf))
        feder.shift(LEFT * 0.5)
        self.wait()
        self.play(FadeIn(feder))
        self.wait(3)
        mark0.shift(0.3*RIGHT)
        mark0.shift(1*UP)
        self.play(FadeIn(mark0))
        self.play(feder.animate.stretch(1.4,dim=0,about_edge=LEFT))
        self.wait(2)
        mark1.shift(1*RIGHT)
        mark1.shift(1*UP)
        self.play(FadeIn(mark1))
        self.play(feder.animate.stretch(9/7,dim=0,about_edge=LEFT))
        self.wait(2)
        mark2.shift(1*UP)
        mark2.shift(1.7*RIGHT)
        self.play(FadeIn(mark2))
        self.play(feder.animate.stretch(5/9,dim=0,about_edge=LEFT))
        self.wait(3)
        n.shift(1.4*UP)
        n.shift(1.2*RIGHT)
        self.play(FadeIn(n))
        self.wait()
        newtongruppe.next_to(wasistkraftgruppe, DOWN).to_edge(LEFT)
        self.play(Write(newtongruppe))
        self.wait()
        kraftmesser.next_to(newtongruppe, DOWN).to_edge(LEFT)
        self.wait(2)
        self.play(Write(kraftmesser))
        self.wait(2)
        self.play(FadeIn(kraftbild),FadeOut(feder))
        self.wait()

class Newtonfoliebild(Scene):
    def construct(self):

        #texte
        newton = Tex("Isaac Newtons Geschichte").scale(1.2)
        ul1 = Underline(newton)
        newtongruppe = VGroup(newton,ul1)
        self.add(newtongruppe)

        eins = Tex("1643 - 1727").scale(0.9)
        zwei = Tex("Vater starb vor Geburt").scale(0.9)
        drei = Tex("Mutter lässt Isaac bei Großeltern").scale(0.9)
        fragetext = Tex("Misstrauisch").scale(0.9)
        fragetext2 = Tex("Einzelgänger").scale(0.9)
        fragetext3 = MathTex(r"\rightarrow").scale(0.9)
        vier = Tex("Studium in Cambridge").scale(0.9)
        fünf = Tex("Lucasischer Professor für Mathematik mit 26").scale(0.9)
        sechs = Tex("Drei Newtonschen Gesetze").scale(0.9)
        sieben = Tex("Die berühmte Geschichte des Apfels").scale(0.9)

        #andere Mobjects
        newtonbild = ImageMobject("newton.png")
        newtonbild.shift(10*RIGHT)

        #animationen
        self.wait()
        self.play(newtongruppe.animate.to_corner(UL))
        eins.next_to(newtongruppe, DOWN).to_edge(LEFT)
        zwei.next_to(eins, DOWN).to_edge(LEFT)
        drei.next_to(zwei, DOWN).to_edge(LEFT)
        fragetext.next_to(drei, DOWN).to_edge(LEFT)
        fragetext3.next_to(fragetext,RIGHT)
        fragetext2.next_to(fragetext3,RIGHT)
        fragetext2.shift(0.03*DOWN)
        vier.next_to(fragetext, DOWN).to_edge(LEFT)
        fünf.next_to(vier, DOWN).to_edge(LEFT)
        sechs.next_to(fünf, DOWN).to_edge(LEFT)
        sieben.next_to(sechs, DOWN).to_edge(LEFT)
        self.wait(2)
        self.add(newtonbild)
        self.play(newtonbild.animate.shift(5.5*LEFT),run_time=2)
        self.wait(3)
        self.play(FadeIn(eins,zwei,drei,fragetext,fragetext2,fragetext3,vier,fünf,sechs,sieben))
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

        newton = Tex("1 Kästchenlänge = 1 Newton (N)")
        blackbox3 = SurroundingRectangle(newton, color=BLACK,fill_opacity=1,buff=0)
        newtongruppe = VGroup(blackbox3,newton)

        v = MathTex(r"\vec{v}")

        vectorzahl = MathTex(r" \begin{bmatrix} 4\\3 \end{bmatrix}")
        blackbox6 = SurroundingRectangle(vectorzahl, color=BLACK,fill_opacity=1,buff=0)
        vectorzahlgruppe = VGroup(blackbox6,vectorzahl)

        vectorzahlfull = MathTex(r" \vec{v} = \begin{bmatrix} 4\\3 \end{bmatrix}")
        blackbox7 = SurroundingRectangle(vectorzahlfull, color=BLACK,fill_opacity=1,buff=0)
        vectorzahlfullgruppe = VGroup(blackbox7,vectorzahlfull)

        fünf = MathTex("v = 5N")
        blackbox4 = SurroundingRectangle(fünf, color=BLACK,fill_opacity=1,buff=0)
        fünfgruppe = VGroup(blackbox4,fünf)

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
        self.wait(2)
        v1.shift(2 * DL) 
        self.play(GrowArrow(v1))
        self.wait(3)
        pfeilgruppe.move_to([-1.5,0,0])
        self.play(Write(pfeilgruppe))
        self.wait()
        self.play(pfeilgruppe.animate.next_to(kraftdarstellen, DOWN).to_edge(LEFT))
        self.wait(4)
        newtongruppe.next_to(vectorzahlfullgruppe, DOWN).to_edge(LEFT)
        newtongruppe.shift(1.6*UP)
        fünfgruppe.move_to([0,0.4,0])
        self.play(Write(v))
        self.wait(7)
        vectorzahlgruppe.move_to([4,1.3,0])
        self.play(Write(vectorzahlgruppe))
        self.wait(11)
        self.play(vectorzahlgruppe.animate.next_to(pfeilgruppe, DOWN).to_edge(LEFT).set_opacity(0))
        vectorzahlfullgruppe.next_to(pfeilgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(vectorzahlfullgruppe))
        self.wait(5)
        self.play(Write(newtongruppe))
        self.wait(3)
        fünfgruppe.next_to(newtongruppe, DOWN).to_edge(LEFT)
        self.play(Write(fünfgruppe))
        self.wait(6)
        angriffspunktgruppe.move_to([-3.6,-1.6,0])
        self.play(Write(angriffspunktgruppe))
        self.play(Circumscribe(punkt,Circle))
        self.wait(4)
        self.play(angriffspunktgruppe.animate.next_to(fünfgruppe, DOWN).to_edge(LEFT))
        self.wait(3)
        self.play(ReplacementTransform(v1,v2),FadeOut(v),run_time=4)
        self.wait()
        self.play(ReplacementTransform(v2,v3),run_time=4)
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

        beschreibung2 = Tex("Grundgleichung der Mechanik")
        blackbox10 = SurroundingRectangle(beschreibung2, color=BLACK,fill_opacity=1,buff=0)
        beschreibung2gruppe = VGroup(blackbox10,beschreibung2)

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
        blackbox8 = SurroundingRectangle(m, color=BLACK,fill_opacity=1,buff=0)
        mgruppe = VGroup(blackbox8,m)

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
        offset = ValueTracker(-5)
        f = 1
        f2 = 2
        f3 = 3

        #animation
        self.wait(1.5)
        beschreibunggruppe.next_to(axiom2gruppe, DOWN).to_edge(LEFT)
        beschreibung2gruppe.next_to(axiom2gruppe, DOWN).to_edge(LEFT)
        self.wait(3)
        self.play(Write(beschreibunggruppe))
        self.wait(6)
        self.play(ReplacementTransform(beschreibunggruppe,beschreibung2gruppe))
        self.wait(4)
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
        self.wait(3)
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        t.set_value(0)

        self.remove(iceblock1,v1,n1gruppe)
        ax1.move_to([0,-2.7,0])
        self.remove(iceblock2,iceblock3,v2,n2gruppe)
        t.set_value(0)
        self.wait(4)
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
        self.wait(4)
        iceblock1.add_updater(lambda mob : mob.move_to([(0.5*(f3/m)* (t.get_value())**2) + offset.get_value(),-2.8,0]))
        iceblock3.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-1,0]))
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        self.wait()
        self.play(ReplacementTransform(formel1gruppe,formel2gruppe))
        agruppe.next_to(beschreibunggruppe, DOWN).to_edge(LEFT)
        self.wait()
        self.play(Write(agruppe))

        self.wait(2)
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
        self.wait(4)
        self.play(t.animate.set_value(5.5), rate_func=linear, run_time=5.5)
        self.wait(3)
        self.play(ReplacementTransform(formel2gruppe,formel3gruppe))
        self.wait()
        mgruppe.next_to(agruppe, DOWN).to_edge(LEFT)
        self.play(Write(mgruppe))
        self.wait(2.5)
        self.play(FadeOut(ax1,ax2))
        self.wait(2.5)
        self.play(Circumscribe(formel3gruppe))
        self.wait(2)
        self.play(formel3gruppe.animate.next_to(mgruppe, DOWN).to_edge(LEFT))
        self.wait()

class Einheiten(Scene):
    def construct(self):

        #texte:
        axiom2 = Tex("Einheiten").scale(1.2)
        ul1 = Underline(axiom2)
        blackbox1 = SurroundingRectangle(axiom2, buff=0, color=BLACK,fill_opacity=1)
        axiom2gruppe = VGroup(blackbox1,axiom2,ul1)

        formel = MathTex(r"F = m \cdot a")
        blackbox6 = SurroundingRectangle(formel, color=BLACK,fill_opacity=1,buff=0)
        formelgruppe = VGroup(blackbox6,formel)

        f1 = MathTex("F : Newton (N)")
        blackbox2 = SurroundingRectangle(f1, color=BLACK,fill_opacity=1,buff=0)
        f1gruppe = VGroup(blackbox2,f1)

        f2 = MathTex(r"[F] = m \cdot a")
        blackbox2 = SurroundingRectangle(f2, color=BLACK,fill_opacity=1,buff=0)

        f3 = MathTex(r"[F] = kg \cdot a")

        f4 = MathTex(r"[F] = kg \cdot \frac{Meter}{Sekunde^{2}}")

        m = MathTex(r"m : Kilogramm (kg)")
        blackbox5 = SurroundingRectangle(m, color=BLACK,fill_opacity=1,buff=0)
        mgruppe = VGroup(blackbox5,m)

        agruppe = MathTex(r"a : \frac{Meter}{Sekunde^{2}} (\frac{m}{s^{2}})")

        a0 = MathTex(r"Geschwindigkeit: \frac{Meter}{Sekunde}")
        a1 = MathTex(r"Beschleunigung: \frac{Meter/Sekunde}{Sekunde}")
        a2 = MathTex(r"Beschleunigung: \frac{Meter}{Sekunde \cdot  Sekunde}")
        a3 = MathTex(r"Beschleunigung: \frac{Meter}{Sekunde^{2}}")

        gruppe = VGroup(axiom2,ul1,formel,f4,m,agruppe)

        frage1 = MathTex(r"a = 5 \cdot \frac{Meter}{Sekunde^{2}} ?")
        frage2 = MathTex(r"a = 12.3 \cdot \frac{Meter}{Sekunde^{2}} ?")
        frage3 = MathTex(r"a = 10 \cdot \frac{Meter}{Sekunde^{2}} ?")

        gkraft1 = MathTex(r"G-Kraft")
        gkraft2 = MathTex(r"G-Kraft = \frac{a}{g}")
        g = MathTex(r"g \approx 9.81 \cdot \frac{Meter}{Sekunde^{2}}")
        gkraft3 = MathTex(r"G-Kraft = \frac{a}{9.81 \cdot \frac{Meter}{Sekunde^{2}}}")

        lösung1 = MathTex(r"G-Kraft(10) = \frac{10 \cdot \frac{Meter}{Sekunde^{2}}}{9.81 \cdot \frac{Meter}{Sekunde^{2}}}")
        lösung2 = MathTex(r"G-Kraft(10) \approx 1.19")


        #andere Mobjects
        ecke = Rectangle(width=4.8, height=1.5).set_color(ORANGE)
        ecke.move_to([4.5,3,0])

        #animation:
        self.add(axiom2gruppe)
        self.wait()
        self.play(axiom2gruppe.animate.to_corner(UL))
        self.wait(3)
        formelgruppe.next_to(axiom2gruppe, DOWN).to_edge(LEFT)
        self.play(Write(formelgruppe))
        self.wait(2)
        f1gruppe.next_to(formelgruppe, DOWN).to_edge(LEFT)
        mgruppe.next_to(f1gruppe, DOWN).to_edge(LEFT)
        agruppe.next_to(mgruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(f1gruppe))
        self.wait(3)
        self.play(FadeIn(mgruppe))
        self.wait(3)
        self.play(FadeIn(agruppe))
        self.wait(4)
        self.play(f1.animate.move_to([0,0,0]))
        self.wait(4)
        self.play(ReplacementTransform(f1,f2))
        self.wait(7)
        self.play(ReplacementTransform(f2,f3))
        self.wait(4)
        self.play(ReplacementTransform(f3,f4))
        self.wait(5)
        self.play(f4.animate.next_to(formelgruppe, DOWN).to_edge(LEFT),mgruppe.animate.shift(0.5*DOWN),agruppe.animate.shift(0.5*DOWN))
        self.play(mgruppe.animate.next_to(f4, DOWN).to_edge(LEFT))
        self.play(agruppe.animate.next_to(mgruppe, DOWN).to_edge(LEFT))
        self.wait(4)
        self.play(Circumscribe(agruppe))

        self.play(gruppe.animate.set_color(GRAY_D))
        self.wait(4)
        a0.shift(RIGHT)
        self.play(Write(a0))
        self.wait(10)
        a1.shift(1.5*RIGHT)
        self.play(TransformMatchingShapes(a0,a1))
        self.wait(10)
        a2.shift(1.5*RIGHT)
        self.play(TransformMatchingShapes(a1,a2))
        self.wait(12)
        a3.shift(0.9*RIGHT)
        self.play(TransformMatchingShapes(a2,a3))
        self.wait(5)
        self.play(Circumscribe(a3))
        self.wait()
        self.play(FadeOut(a3))
        self.wait(3)
        self.play(FadeIn(frage1))
        self.wait(2)
        self.play(TransformMatchingShapes(frage1,frage2))
        self.wait(2)
        self.play(TransformMatchingShapes(frage2,frage3))
        self.wait(4)
        gkraft1.shift(2*DOWN)
        gkraft2.shift(2*DOWN)
        gkraft3.shift(2*DOWN)
        g.shift(4.5*RIGHT)
        g.shift(3*UP)
        self.play(FadeIn(gkraft1))
        self.wait(20)
        self.play(TransformMatchingShapes(gkraft1,gkraft2))
        self.wait(6)
        self.play(FadeIn(g),Create(ecke))
        self.wait(8)
        self.play(TransformMatchingShapes(gkraft2,gkraft3))
        self.wait(13)
        lösung1.shift(1.1 * RIGHT)
        lösung1.shift(0.1*DOWN)
        lösung2.shift(0.1*DOWN)
        self.play(ReplacementTransform(frage3,lösung1))
        self.wait(7)
        self.play(TransformMatchingShapes(lösung1,lösung2))
        self.wait(10)

class Gewichtskraft(Scene):
    def construct(self):

        #texte:
        gewichtskraft = Tex("Gewichtskraft").scale(1.2)
        ul1 = Underline(gewichtskraft)
        gewichtskraftgruppe = VGroup(gewichtskraft,ul1)

        frage = Tex("Wie stark wird ein Körper von der Erde angezogen?")

        fma = MathTex(r"F = m \cdot a")
        fma2 = MathTex(r"F = m \cdot g")

        fma2_3 = MathTex(r"Stein: F = 200 kg \cdot g")
        fma2_4 = MathTex(r"Stein: F = 200 kg \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        fma2_5 = MathTex(r"Stein: 1962N = 200 kg \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        fma2gruppe = VGroup(fma2_3,fma2_4,fma2_5)

        g = MathTex(r"Erdbeschleunigung \approx 9.81 \frac{Meter}{Sekunde^{2}}")

        fragezeichen = Tex("?")

        newton = Tex("1962N")

        #andere mobjects
        ax = NumberLine(x_range=[0,15,1])
        stone = ImageMobject("stone.png").scale(0.8)
        v1 = Vector([0,-1.5]).set_color(ORANGE)
        v2 = Vector([0,-0.9]).set_color(ORANGE)
        v3 = Vector([0,-1.8]).set_color(ORANGE)
        v4 = Vector([0,-1.2]).set_color(ORANGE)
        vgruppe = VGroup(v1,v2,v3,v4)

        #animationen:
        self.add(gewichtskraftgruppe)
        self.wait()
        self.play(gewichtskraftgruppe.animate.to_corner(UL))
        self.wait(3)
        self.play(Write(frage))
        self.wait(2)
        self.play(frage.animate.next_to(gewichtskraftgruppe, DOWN).to_edge(LEFT))
        self.wait(6)
        g.next_to(frage, DOWN).to_edge(LEFT)
        self.play(Write(g))
        self.wait(10)
        self.play(Write(fma))
        self.wait(8)
        self.play(ReplacementTransform(fma,fma2))
        self.wait(7)
        self.play(Circumscribe(fma2))
        self.wait()
        self.play(fma2.animate.next_to(g, DOWN).to_edge(LEFT))
        self.wait(3)
        ax.shift(1.8*DOWN)
        self.play(Create(ax))
        stone.shift(1.25*DOWN)
        self.play(FadeIn(stone))
        self.wait(2)
        vgruppe.shift(2.1*DOWN)
        fragezeichen.add_updater(lambda mob : mob.next_to(v1,RIGHT))
        self.play(GrowArrow(v1),FadeIn(fragezeichen))
        self.wait()
        self.play(Transform(v1,v2))
        self.wait()
        self.play(Transform(v1,v3))
        self.wait()
        self.play(Transform(v1,v4))
        self.wait(4)
        fma2copy = fma2.copy()
        self.add(fma2copy)
        self.play(FadeOut(v1,fragezeichen))
        self.play(ax.animate.shift(1.7*DOWN),
                  stone.animate.shift(1.7*DOWN),
                  fma2copy.animate.move_to([0,-0.3,0]))
        fma2gruppe.move_to([0,-0.3,0])
        self.wait(4)
        self.play(ReplacementTransform(fma2copy,fma2_3))
        self.wait(5)
        self.play(ReplacementTransform(fma2_3,fma2_4))
        self.wait(5)
        self.play(ReplacementTransform(fma2_4,fma2_5))
        self.wait(6)
        self.play(FadeOut(frage))
        v1.shift(0.2*DOWN)
        newton.next_to(v1,RIGHT)
        self.play(g.animate.next_to(gewichtskraftgruppe, DOWN).to_edge(LEFT),
                  fma2.animate.next_to(g, DOWN).to_edge(LEFT).shift(0.8*UP),
                  fma2_5.animate.next_to(fma2, DOWN).to_edge(LEFT).shift(UP),
                  ax.animate.shift(1.5*UP),
                  stone.animate.shift(1.5*UP),
                  FadeIn(v1,newton))
        
        self.wait()

class GewichtskraftWaagen(Scene):
    def construct(self):

        #texte
        gewichtskraft = Tex("Gewichtskraft - Waagen").scale(1.2)
        ul1 = Underline(gewichtskraft)
        gewichtskraftgruppe = VGroup(gewichtskraft,ul1)

        fragezeichen = Tex("?")

        formel1 = MathTex(r"F = m \cdot g")
        #hehe.....
        formel2 = MathTex(r" F = m \cdot g \mid \div g")
        formel3 = MathTex(r"\frac{F}{g} = \frac{m \cdot g}{g}")
        formel4 = MathTex(r"\frac{F}{g} = m")
        formel5 = MathTex(r"m = \frac{F}{g}")
        formel6 = MathTex(r"m = \frac{F}{9.81 \frac{Meter}{Sekunde^{2}}}")
        formel7 = MathTex(r"m = \frac{1962N}{9.81 \frac{Meter}{Sekunde^{2}}}")
        formel8 = MathTex(r"200kg = \frac{1962N}{9.81 \frac{Meter}{Sekunde^{2}}}")
        #-_

        iss1 = MathTex(r"m = \frac{F}{0}")
        iss2 = MathTex(r"m = \frac{F}{a}")
        iss3 = MathTex(r"m = \frac{5N}{a}")
        iss4 = MathTex(r"m = \frac{5N}{0.025 \frac{Meter}{Sekunde^{2}}}}")
        iss5 = MathTex(r"200kg \approx \frac{5N}{0.025 \frac{Meter}{Sekunde^{2}}}}")

        formelgruppe = VGroup(formel1,formel2,formel3,formel4,formel5,formel6,formel7,formel8,iss1,iss2,iss3,iss4,iss5)

        waagezahl1 = Tex("0.0").scale(0.7).set_color(BLACK)
        waagezahl2 = Tex("200.0").scale(0.7).set_color(BLACK)

        #andere mobjects
        waage = ImageMobject("waage.png").scale(0.5)
        ax = NumberLine(x_range=[0,15,1])
        stone = ImageMobject("stone.png").scale(0.8)
        v1 = Vector([0,-2,0]).set_color(ORANGE)
        newton = Tex("1962N")
        newton2 = Tex("5N")
        v2 = Vector([2,0,0]).set_color(ORANGE)


        #animationen
        self.add(gewichtskraftgruppe)
        self.wait()
        self.play(gewichtskraftgruppe.animate.to_corner(UL))
        self.wait(4)
        ax.shift(2.7*DOWN)
        waage.shift(2.15*DOWN)
        waagezahl1.move_to([0.5,-2.2,0])
        waagezahl2.move_to([0.4,-2.2,0])
        stone.shift(DOWN)
        self.play(Create(ax))
        self.play(FadeIn(waage,waagezahl1))
        v1.shift(1.9*DOWN)
        self.play(FadeIn(stone),GrowArrow(v1),ReplacementTransform(waagezahl1,waagezahl2))
        newton.next_to(v1,RIGHT)
        newton.shift(0.2*DL)
        newton.shift(0.2*DOWN)
        self.play(Write(newton))
        self.wait(8)
        # formel1.next_to(gewichtskraftgruppe, DOWN).to_edge(LEFT)
        formelgruppe.shift(UP)
        self.play(Write(formel1))
        self.wait(5)
        self.play(Circumscribe(formel1[0][2]),run_time=1.4)
        self.wait(4)
        self.play(ReplacementTransform(formel1,formel2))
        self.wait(4)
        self.play(ReplacementTransform(formel2,formel3))
        self.wait(10)
        self.play(ReplacementTransform(formel3,formel4))
        self.wait(5)
        self.play(TransformMatchingShapes(formel4,formel5))
        self.wait(6)
        self.play(ReplacementTransform(formel5,formel6))
        self.wait(6)
        self.play(ReplacementTransform(formel6,formel7))
        self.wait(6)
        self.play(ReplacementTransform(formel7,formel8))
        self.wait(4)
        self.play(Circumscribe(formel8[0][0:5]),run_time=1.4)
        self.wait()
        self.play(formel8.animate.next_to(gewichtskraftgruppe, DOWN).to_edge(LEFT).shift(0.1*UL))
        self.wait(3)
        self.play(Write(formel4))
        self.wait()
        self.play(ax.animate.shift(3*DOWN),
                  waage.animate.shift(3*DOWN),
                  waagezahl2.animate.shift(3*DOWN),
                  v1.animate.shift(3*DOWN),
                  newton.animate.shift(3*DOWN),
                  stone.animate.shift(0.6*DOWN),)
        self.wait(2)
        self.play(ReplacementTransform(formel4,iss1))
        self.wait(5)
        self.play(Write(fragezeichen))
        self.wait(2)
        self.play(FadeOut(fragezeichen))
        self.play(ReplacementTransform(iss1,iss2))
        self.wait(5)
        self.play(ReplacementTransform(iss2,iss3))
        m = 200
        f = 5
        t = ValueTracker(0)
        self.add(t)
        t.add_updater(lambda mob : mob.increment_value(0.02))
        stone.add_updater(lambda mob : mob.move_to([((f/m)* (t.get_value())**2),-1.6,0]))
        v2.add_updater(lambda mob : mob.next_to(stone,RIGHT).shift(0.3*LEFT))
        newton2.add_updater(lambda mob : mob.next_to(v2,DOWN).shift(0.2*UP))
        self.play(FadeIn(v2,newton2))
        self.wait(4,frozen_frame=False)
        self.play(ReplacementTransform(iss3,iss4))
        self.wait(4,frozen_frame=False)
        self.play(ReplacementTransform(iss4,iss5))
        self.wait(4,frozen_frame=False)
        self.play(Circumscribe(iss5[0][0:5]),run_time=1.4)
        self.wait(1, frozen_frame=False)
        self.play(iss5.animate.next_to(formel8, DOWN).to_edge(LEFT))
        self.wait(1, frozen_frame=False)

class Gewichtskraftexperiment(Scene):
    def construct(self):

        #texte
        gewicht = Tex("Gewichtskraft - Experiment").scale(1.2)
        ul1 = Underline(gewicht)
        gewichtgruppe = VGroup(gewicht,ul1)

        newton = MathTex(r"\approx 1N")
        newton2 = MathTex(r"0.981N \approx 1N")
        gramm = Tex("100g")
        gramm2 = Tex("100g = 0.1 kg")

        formel1 = MathTex(r"F = m \cdot g")
        formel2 = MathTex(r"F = m \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        formel3 = MathTex(r"F = 0.1 kg \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        formel4 = MathTex(r"0.981N = 0.1 kg \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        formel5 = MathTex(r"1N \approx 0.1 kg \cdot 9.81 \frac{Meter}{Sekunde^{2}}")
        formelgruppe = VGroup(formel1,formel2,formel3,formel5)

        #andere mobjects
        kraftmesser = ImageMobject("kraftmesser.png").scale(0.5)


        #animationen
        self.add(gewichtgruppe)
        self.wait()
        self.play(gewichtgruppe.animate.to_corner(UL))
        self.wait(2)
        kraftmesser.shift(0.2*DOWN)
        self.play(FadeIn(kraftmesser))
        self.wait(4)
        gramm.shift(3.2*DOWN)
        gramm2.shift(3.2*DOWN)
        gramm2.shift(5*RIGHT)
        self.play(Write(gramm))
        self.wait(6)
        newton.move_to([1.2,-1.1,0])
        newton2.move_to([5.2,-1.1,0])
        self.play(Write(newton))
        self.wait(5)
        kraftmessergruppe = VGroup(newton,gramm)
        self.play(kraftmessergruppe.animate.shift(5*RIGHT),
                  kraftmesser.animate.shift(5*RIGHT))
        self.wait(3)
        self.play(Write(formel1))
        self.wait(5)
        self.play(ReplacementTransform(formel1,formel2))
        self.wait(5)
        self.play(ReplacementTransform(formel2,formel3))
        self.wait(6)
        self.play(ReplacementTransform(gramm,gramm2))
        self.wait(5)
        self.play(ReplacementTransform(formel3,formel4))
        self.wait(8)
        self.play(ReplacementTransform(newton,newton2),
                  kraftmesser.animate.shift(2*LEFT),
                  formel4.animate.shift(2*LEFT),
                  gramm2.animate.shift(2*LEFT))
        self.wait(6)
        formelgruppe.shift(2*LEFT)
        self.play(ReplacementTransform(formel4,formel5))
        self.wait(6)
        self.play(Circumscribe(formel5))
        self.wait(2)
        self.play(formel5.animate.next_to(gewichtgruppe, DOWN).to_edge(LEFT))
        self.wait()

class Axiom1(Scene):
    def construct(self):
        
        #texte
        axiom1 = Tex("Newton's erstes Axiom").scale(1.2)
        ul1 = Underline(axiom1)
        blackbox1 = SurroundingRectangle(axiom1, buff=0, color=BLACK,fill_opacity=1)
        axiom1gruppe = VGroup(blackbox1,axiom1,ul1)

        fragezeichen = Tex("?")
        blackbox2 = SurroundingRectangle(fragezeichen, color=BLACK,fill_opacity=1,buff=0)
        fragezeichengruppe = VGroup(blackbox2,fragezeichen)

        axiom1text = Tex("Ohne äußeren Einfluss verändert ein")
        blackbox3 = SurroundingRectangle(axiom1text, color=BLACK,fill_opacity=1,buff=0)
        axiom1textgruppe = VGroup(blackbox3,axiom1text)
        axiom1text[0][4:19].set_color("#F5B176")

        axiom1text2 = Tex("Körper seinen Bewegungszustand nicht.")
        blackbox4 = SurroundingRectangle(axiom1text2, color=BLACK,fill_opacity=1,buff=0)
        axiom1text2gruppe = VGroup(blackbox4,axiom1text2)

        axiom1textkurz = Tex("Trägheitsgesetz")
        blackbox5 = SurroundingRectangle(axiom1textkurz, color=BLACK,fill_opacity=1,buff=0)
        axiom1textkurzgruppe = VGroup(blackbox5,axiom1textkurz)

        vtext = Tex("v = Geschwindigkeit")

        vaddon = Tex("v = ")

        #andere mobjects
        iceblock = ImageMobject("ice.png").scale(0.6)
        iceblock.move_to([-5,-2.2,0])
        ax = NumberLine(x_range=[0,15,1])
        ax.shift(2.7*DOWN)
        v1 = Vector([2,0,0]).set_color(ORANGE)
        t = ValueTracker(0)
        m = 1
        offset = ValueTracker(-5)
        f = 1
        line = Line(3*LEFT, RIGHT*t.get_value())
        mark = Line(UP*0.1, DOWN*0.1)
        mark2 = Line(UP*0.1, DOWN*0.1)
        mark3 = Line(UP*0.1, DOWN*0.1)

        geschwindigkeit = DecimalNumber(t.get_value(), num_decimal_places=1)

        #animation
        geschwindigkeit.add_updater(lambda mob : mob.become(DecimalNumber(t.get_value(), num_decimal_places=1)))
        geschwindigkeit.add_updater(lambda mob : mob.next_to(iceblock, UP))
        self.add(axiom1gruppe)
        self.wait()
        self.play(axiom1gruppe.animate.to_corner(UL))
        self.wait()
        self.play(Create(ax))
        self.play(FadeIn(iceblock))
        self.wait(4)
        v1.add_updater(lambda mob : mob.next_to(iceblock,RIGHT).shift(0.3*LEFT))
        iceblock.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-2.2,0]))
        self.play(FadeIn(v1))
        self.play(t.animate.set_value(2),FadeOut(v1), rate_func=linear, run_time=2)
        iceblock.clear_updaters()
        self.play(iceblock.animate.move_to([8.5,-2.2,0]), rate_func=linear, run_time=5.6)
        self.play(FadeOut(iceblock))
        t.set_value(0)
        self.wait(2)

        #zweiter versuch
        iceblock.move_to([-5,-2.2,0])
        self.play(FadeIn(iceblock))
        self.wait(3)
        iceblock.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-2.2,0]))
        self.play(FadeIn(v1))
        self.play(t.animate.set_value(2),FadeOut(v1), rate_func=linear, run_time=2)
        iceblock.clear_updaters()
        t.set_value(0)
        self.add(line)
        mark.move_to([-2.6,-1,0])
        line.add_updater(lambda mob : mob.become(Line(2.6*LEFT, RIGHT*(t.get_value()-2.6))).shift(DOWN))
        self.play(iceblock.animate.move_to([8.5,-2.2,0]),t.animate.set_value(11),FadeIn(mark), rate_func=linear, run_time=5.6)
        self.wait()
        self.play(FadeIn(fragezeichengruppe))
        self.wait(4)
        self.play(axiom1gruppe.animate.move_to([0,3,0]),
                  FadeOut(fragezeichengruppe),
                  FadeOut(iceblock),
                  FadeOut(ax),
                  Uncreate(line),
                  Uncreate(mark),
                  run_time=2)
        self.wait()
        axiom1textgruppe.shift(0.4*UP)
        axiom1text2gruppe.shift(0.4*DOWN)
        self.wait(3)
        self.play(Write(axiom1textgruppe))
        self.play(Write(axiom1text2gruppe))
        self.wait(6)
        gruppe = VGroup(axiom1text,axiom1text2)
        self.play(ReplacementTransform(gruppe,axiom1textkurzgruppe))
        self.remove(blackbox3,blackbox4)
        self.wait(2)
        self.play(axiom1gruppe.animate.to_corner(UL),axiom1textkurzgruppe.animate.next_to(axiom1gruppe, DOWN).to_edge(LEFT))
        self.wait(2)

        #dritterversuch
        self.wait(2)
        vtext.next_to(axiom1textkurz, DOWN).to_edge(LEFT)
        self.play(Write(vtext))
        self.wait(2)
        t.set_value(0)
        iceblock.move_to([-5,-2.2,0])
        self.play(Create(ax))
        self.play(FadeIn(iceblock))
        self.wait(3)
        iceblock.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-2.2,0]))
        vaddon.add_updater(lambda mob : mob.next_to(geschwindigkeit, LEFT))
        self.play(FadeIn(vaddon,geschwindigkeit),run_time=0.1)
        self.wait(0.6)
        self.play(FadeIn(v1))
        self.play(t.animate.set_value(2),FadeOut(v1), rate_func=linear, run_time=2)
        iceblock.clear_updaters()
        geschwindigkeit.clear_updaters()
        geschwindigkeit.add_updater(lambda mob : mob.next_to(iceblock, UP))
        t.set_value(0)
        self.add(line)
        mark2.move_to([-2.6,-0.5,0])
        line.add_updater(lambda mob : mob.become(Line(2.6*LEFT, RIGHT*(t.get_value()-2.6))).shift(0.5*DOWN))
        self.play(iceblock.animate.move_to([8.5,-2.2,0]),t.animate.set_value(11),FadeIn(mark2), rate_func=linear, run_time=5.6)
        self.remove(vaddon,geschwindigkeit)
        self.wait(3)
        self.play(Circumscribe(axiom1textkurzgruppe))
        self.wait()

        #vierter versuch
        geschwindigkeit.clear_updaters()
        geschwindigkeit.add_updater(lambda mob : mob.become(DecimalNumber(t.get_value(), num_decimal_places=1)))
        geschwindigkeit.add_updater(lambda mob : mob.next_to(iceblock, UP))
        self.play(Uncreate(line),Uncreate(mark2))
        self.wait(4)
        t.set_value(0)
        iceblock.move_to([-5,-2.2,0])
        FadeOut(iceblock)
        self.play(FadeIn(iceblock))
        self.wait(3)
        iceblock.add_updater(lambda mob : mob.move_to([(0.5*(f/m)* (t.get_value())**2) + offset.get_value(),-2.2,0]))
        vaddon.add_updater(lambda mob : mob.next_to(geschwindigkeit, LEFT))
        self.play(FadeIn(vaddon,geschwindigkeit),run_time=0.1)
        self.play(FadeIn(v1))
        self.play(t.animate.set_value(2),FadeOut(v1), rate_func=linear, run_time=2)
        iceblock.clear_updaters()
        geschwindigkeit.clear_updaters()
        geschwindigkeit.add_updater(lambda mob : mob.next_to(iceblock, UP))
        t.set_value(0)
        self.add(line)
        mark3.move_to([-2.6,-0.5,0])
        line.add_updater(lambda mob : mob.become(Line(2.6*LEFT, RIGHT*(t.get_value()-2.6))).shift(0.5*DOWN))
        self.play(iceblock.animate.move_to([8.5,-2.2,0]),t.animate.set_value(11),FadeIn(mark3), rate_func=linear, run_time=5.6)
        self.remove(vaddon,geschwindigkeit)
        self.wait(2)
        self.play(Circumscribe(axiom1textkurzgruppe))
        self.wait()

class Kraftaddieren(Scene):
    def construct(self):

        #ich möchte kurz sagen, dass war die allerste scene und vom aufbau her ist sie komplett müll... also fallst das jemand liest, ich weiß wie sclimm das ist...

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
        self.wait()
        self.add(kräftaddierengruppe)

        vector1x = 1.5
        vector1y = 1.5
        vector2x = 3
        vector2y = 3

        self.play(vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),run_time=1)
        self.wait(3)
        self.play(vector1.animate.shift(0.1*UL))
        self.wait(3)

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
        self.wait()
        self.play(vector1.animate.move_to(vector2.get_end() * 1.37))
        #ich weiß selber nicht woher diese 1.37 kommt also falls das hier jemand sieht, frag nicht
        self.wait(2)

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
        self.play(vektorverbindunggruppe.animate.move_to([-5,2,1]).set_opacity(0))
        vektorverbindungfullgruppe.next_to(kräftaddierengruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(vektorverbindungfullgruppe))

        self.play(vector3.animate.become(nupl.get_vector([4.5,4.5,0]).set_color(WHITE)).shift(0.1*DR),run_time=2)
        self.wait()
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).shift(0.1*UL).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait(2)

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

        #2ter Abschnitt
        vector1x = 4
        vector1y = 0.5
        vector2x = 1
        vector2y = 3
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait(3)

        self.add(fragezeichen)
        self.play(vector3.animate.become(nupl.get_vector([2.5,3.2,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([1.5,2.5,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([3.7,1.8,0]).set_color(WHITE)),run_time=2)
        self.wait(0.5)
        self.play(vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)),FadeOut(fragezeichen),run_time=2)
        self.wait(3)
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))

        vektorverbindung = Tex("Verbindung")
        blackbox3 = SurroundingRectangle(vektorverbindung, color=BLACK,fill_opacity=1,buff=0)
        vektorverbindunggruppe = VGroup(blackbox3,vektorverbindung)
        punkt2 = Dot()
        vektorverbindunggruppe.shift(1.2 * RIGHT)
        self.play(Write(vektorverbindunggruppe))
        punkt2.move_to(vector2.get_start())
        self.play(Circumscribe(punkt2,Circle),run_time=1.4)
        self.wait()
        self.play(vektorverbindunggruppe.animate.set_opacity(0))
        self.wait(2)
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait(4)
        self.play(vector2.animate.shift(vector1y*DOWN).shift(vector1x*LEFT))
        self.wait(4)

        vector1x = 3
        vector1y = -1.5
        vector2x = 4.5
        vector2y = 1.5
        basevector1 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)
        basevector2 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        self.play(vector1.animate.become(basevector1),vector2.animate.become(basevector2),vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)),run_time=2)
        self.wait(2)
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.wait(2)
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait()
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
        self.wait(3)

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


        vector3_real = nupl.get_vector([0,0,0]).set_color(GREEN)
        vector1x = 0
        vector1y = -1.5
        vector2x = 1.5
        vector2y = 3
        vector3x = 3
        vector3y = -1.5
        basevector1 = nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)
        basevector2 = nupl.get_vector([vector2x,vector2y,0]).set_color(BLUE)
        basevector3 = nupl.get_vector([vector3x,vector3y,0]).set_color(GREEN)
        self.wait()
        self.play(vector1.animate.become(nupl.get_vector([0,0,0]).set_color(ORANGE)),
                  vector2.animate.become(nupl.get_vector([0,0,0]).set_color(ORANGE)),
                  vector3_real.animate.become(nupl.get_vector([0,0,0]).set_color(ORANGE)),
                  vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)))
        
        self.play(vector1.animate.become(basevector1),
                  vector2.animate.become(basevector2),
                  vector3_real.animate.become(basevector3),
                  vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)))
        self.wait(5)
        self.play(vector1.animate.shift(vector2x*RIGHT).shift(vector2y*UP))
        self.wait(4)
        self.play(vector3_real.animate.shift((vector2x+vector1x)*RIGHT).shift((vector2y+vector1y)*UP))
        self.wait(4)
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x+vector3x,vector1y+vector2y+vector3y,0]).set_color(WHITE)))
        self.wait(5)
        self.play(vector1.animate.become(basevector1),
                  vector2.animate.become(basevector2),
                  vector3_real.animate.become(basevector3))
        self.wait(3)
        self.play(vector2.animate.shift((vector3x)*RIGHT).shift((vector3y)*UP))
        self.wait(2)
        self.play(vector1.animate.shift((vector2x+vector3x)*RIGHT).shift((vector2y+vector3y)*UP))
        self.wait(3)
        self.play(vector1.animate.become(basevector1),
                  vector2.animate.become(basevector2),
                  vector3_real.animate.become(basevector3))
        self.wait()

class Additionrechnen(Scene):
    def construct(self):


        #Texte
        addition = Tex("Kraftaddition - Rechnen").scale(1.2)
        ul1 = Underline(addition)
        blackbox1 = SurroundingRectangle(addition, buff=0, color=BLACK,fill_opacity=1)
        additiongruppe = VGroup(blackbox1,addition,ul1)
        self.add(additiongruppe)

        v1zahl = MathTex(r" \begin{bmatrix} 1\\1 \end{bmatrix}").set_color("#F5B176")
        blackbox2 = SurroundingRectangle(v1zahl, color=BLACK,fill_opacity=1,buff=0)
        v1zahlgruppe = VGroup(blackbox2,v1zahl)

        v2zahl = MathTex(r" \begin{bmatrix} 2\\1 \end{bmatrix}").set_color("#86CFF9")
        blackbox3 = SurroundingRectangle(v2zahl, color=BLACK,fill_opacity=1,buff=0)
        v2zahlgruppe = VGroup(blackbox3,v2zahl)

        v1zahlcopy = MathTex(r" \begin{bmatrix} 1\\1 \end{bmatrix}").set_color("#F5B176")
        blackbox4 = SurroundingRectangle(v1zahlcopy, color=BLACK,fill_opacity=1,buff=0)
        v1zahlcopygruppe = VGroup(blackbox4,v1zahlcopy)

        v2zahlcopy = MathTex(r" \begin{bmatrix} 2\\1 \end{bmatrix}").set_color("#86CFF9")
        blackbox5 = SurroundingRectangle(v2zahlcopy, color=BLACK,fill_opacity=1,buff=0)
        v2zahlcopygruppe = VGroup(blackbox5,v2zahlcopy)

        plus = MathTex("+").scale(2)
        blackbox6 = SurroundingRectangle(plus, color=BLACK,fill_opacity=1,buff=0)
        plusgruppe = VGroup(blackbox6,plus)

        v3zahlrichtig = MathTex(r" \begin{bmatrix} e\\f \end{bmatrix}").set_color("#B5FCA6").scale(1.5)
        blackbox14 = SurroundingRectangle(v3zahlrichtig, color=BLACK,fill_opacity=1,buff=0)
        v3zahlrichtiggruppe = VGroup(blackbox14,v3zahlrichtig)

        lösung = MathTex(r" =\begin{bmatrix} 1 + 2 \\ 1 + 1 \end{bmatrix}").scale(1.5)
        blackbox7 = SurroundingRectangle(lösung, color=BLACK,fill_opacity=1,buff=0)
        lösunggruppe = VGroup(blackbox7,lösung)
        lösung[0][2].set_color("#F5B176")
        lösung[0][4].set_color("#86CFF9")
        lösung[0][5].set_color("#F5B176")
        lösung[0][7].set_color("#86CFF9")

        lösungfull = MathTex(r" =\begin{bmatrix} 3 \\ 2 \end{bmatrix}").scale(1.5)
        blackbox8 = SurroundingRectangle(lösungfull, color=BLACK,fill_opacity=1,buff=0)
        lösungfullgruppe = VGroup(blackbox8,lösungfull)

        lösungfullcopy = MathTex(r" \begin{bmatrix} 3 \\ 2 \end{bmatrix}").scale(1.5)
        blackbox9 = SurroundingRectangle(lösungfullcopy, color=BLACK,fill_opacity=1,buff=0)
        lösungfullcopygruppe = VGroup(blackbox9,lösungfullcopy)

        keinenamenmehr = MathTex(r" \begin{bmatrix} 3 \\ 2 \end{bmatrix}")
        blackbox10 = SurroundingRectangle(keinenamenmehr, color=BLACK,fill_opacity=1,buff=0)
        keinenamenmehrgruppe = VGroup(blackbox10,keinenamenmehr)

        v1zahlrichtig = MathTex(r" \begin{bmatrix} a\\b \end{bmatrix}").set_color("#F5B176").scale(1.5)
        blackbox11 = SurroundingRectangle(v1zahlrichtig, color=BLACK,fill_opacity=1,buff=0)
        v1zahlrichtiggruppe = VGroup(blackbox11,v1zahlrichtig)

        v2zahlrichtig = MathTex(r" \begin{bmatrix} c\\d \end{bmatrix}").set_color("#86CFF9").scale(1.5)
        blackbox12 = SurroundingRectangle(v2zahlrichtig, color=BLACK,fill_opacity=1,buff=0)
        v2zahlrichtiggruppe = VGroup(blackbox12,v2zahlrichtig)

        lösungrichtig = MathTex(r" =\begin{bmatrix} a + c \\ b + d \end{bmatrix}").scale(1.5)
        blackbox7 = SurroundingRectangle(lösungrichtig, color=BLACK,fill_opacity=1,buff=0)
        lösungrichtiggruppe = VGroup(blackbox7,lösungrichtig)
        lösungrichtig[0][2].set_color("#F5B176")
        lösungrichtig[0][4].set_color("#86CFF9")
        lösungrichtig[0][5].set_color("#F5B176")
        lösungrichtig[0][7].set_color("#86CFF9")

        lösungrichtig2 = MathTex(r" =\begin{bmatrix} a + c + e \\ b + d + f\end{bmatrix}").scale(1.5)
        blackbox13 = SurroundingRectangle(lösungrichtig2, color=BLACK,fill_opacity=1,buff=0)
        lösungrichtig2gruppe = VGroup(blackbox13,lösungrichtig2)
        lösungrichtig2[0][2].set_color("#F5B176")
        lösungrichtig2[0][4].set_color("#86CFF9")
        lösungrichtig2[0][7].set_color("#F5B176")
        lösungrichtig2[0][9].set_color("#86CFF9")
        lösungrichtig2[0][11].set_color("#B5FCA6")
        lösungrichtig2[0][6].set_color("#B5FCA6")

        plusrichtiggruppe = MathTex("+").scale(2)
        plusrichti2ggruppe = MathTex("+").scale(2)

        kommu = Tex("Kommutativgesetz")
        blackbox15 = SurroundingRectangle(kommu, color=BLACK,fill_opacity=1,buff=0)
        kommugruppe = VGroup(blackbox15,kommu)

        #andere mobjects
        nupl = NumberPlane(x_range=(0,20,1.5),y_range=(0,12,1.5)).set_opacity(0.5)
        nupl.shift(1.5*DL)
        nupl.shift(0.5*LEFT)
        v1 = Vector([1.5,1.5]).set_color(ORANGE)
        v2 = Vector([3,1.5]).set_color(BLUE)
        v3 = Vector([4.5,3])

        #59l

        #animationen
        self.wait()
        self.play(additiongruppe.animate.to_corner(UL))
        self.wait(1)
        self.play(FadeIn(nupl)),self.add(additiongruppe)
        self.wait(2)
        v1.shift(6*LEFT)
        v1.shift(1.5*DOWN)
        v2.shift(6*LEFT)
        v2.shift(1.5*DOWN)
        v3.shift(6*LEFT)
        v3.shift(1.5*DOWN)
        v1zahlgruppe.shift(4.5*LEFT)
        v1zahlcopygruppe.shift(4.5*LEFT)
        v2zahlgruppe.shift(3*LEFT)
        v2zahlcopygruppe.shift(3*LEFT)
        v1zahlgruppe.shift(0.7*UP)
        v1zahlcopygruppe.shift(0.7*UP)
        v2zahlgruppe.shift(0.7*UP)
        v2zahlcopygruppe.shift(0.7*UP)
        self.play(GrowArrow(v1),GrowArrow(v2))
        self.wait(4)
        self.play(Write(v1zahlgruppe),Write(v2zahlgruppe))
        self.wait(6)
        self.add(v1zahlcopygruppe,v2zahlcopygruppe)
        self.play(v1zahlcopygruppe.animate.move_to([-1,0,0]).scale(1.5),v2zahlcopygruppe.animate.move_to([1,0,0]).scale(1.5))
        self.wait(4)
        self.play(FadeIn(plusgruppe))
        self.wait(2)
        lösunggruppe.shift(RIGHT*3.4)
        self.play(Write(lösunggruppe))
        self.wait(12)
        lösungfullgruppe.shift(RIGHT*2.8)
        lösungfullcopygruppe.shift(RIGHT*3.3)
        lösung_original = lösunggruppe.copy()
        self.play(Transform(lösunggruppe,lösungfullgruppe))
        self.wait(6)
        self.play(FadeOut(v1zahlgruppe,v2zahlgruppe))
        self.wait()
        self.play(GrowArrow(v3))
        self.wait()
        self.add(lösungfullcopygruppe)
        self.play(lösungfullcopygruppe.animate.move_to([-1.3,1.8,0]).scale(0.7).set_opacity(0))
        keinenamenmehrgruppe.move_to([-2.5,1.8,0])
        self.play(FadeIn(keinenamenmehrgruppe))
        self.wait(6)
        v2.set_z_index(1)
        self.play(v2.animate.move_to([-3,0.75,0]))
        self.wait(5)

        v1zahlgruppecopy = v1zahlcopygruppe.copy()
        v1zahlgruppecopy.move_to(v2zahlcopygruppe)
        v2zahlgruppecopy = v2zahlcopygruppe.copy()
        v2zahlgruppecopy.move_to(v1zahlcopygruppe)

        v1zahlcopycopygruppe = v1zahlcopygruppe.copy()
        v2zahlcopycopygruppe = v2zahlcopygruppe.copy()
        self.play(ClockwiseTransform(v1zahlcopygruppe,v1zahlgruppecopy),
                  ClockwiseTransform(v2zahlcopygruppe,v2zahlgruppecopy))
        kommugruppe.next_to(additiongruppe, DOWN).to_edge(LEFT)
        self.wait(2)
        self.play(Write(kommugruppe),keinenamenmehrgruppe.animate.move_to([-3.2,1.5,0]))
        self.wait(6)
        v1.set_z_index(1)
        self.play(v2.animate.move_to([-4.5,-0.73,0]),v1.animate.move_to([-2.25,0.75,0]))
        self.wait(6)
        self.play(v2.animate.move_to([-3,0.76,0]),v1.animate.move_to([-5.25,-0.75,0]))
        self.wait(4)
        self.play(Transform(lösunggruppe,lösung_original),
                  FadeOut(v1,v2,v3,keinenamenmehrgruppe),
                  CounterclockwiseTransform(v1zahlcopygruppe,v1zahlcopycopygruppe),
                  CounterclockwiseTransform(v2zahlcopygruppe,v2zahlcopycopygruppe))
        gruppe = VGroup(lösunggruppe,v1zahlcopygruppe,v2zahlcopygruppe,plusgruppe)
        self.play(gruppe.animate.move_to([0,0,0]))
        self.wait(5)
        v1zahlrichtiggruppe.move_to([-1,0,0])
        v2zahlrichtiggruppe.move_to([1,0,0])
        lösungrichtiggruppe.move_to([3.4,0,0])
        plusrichtiggruppe.move_to([0,0,0])
        richtiggruppe = VGroup(v1zahlrichtiggruppe,v2zahlrichtiggruppe,lösungrichtiggruppe,plusrichtiggruppe)
        richtig2gruppe = VGroup(v1zahlrichtiggruppe,v2zahlrichtiggruppe,plusrichtiggruppe)
        richtiggruppe.shift(1.75 * LEFT)   
        self.play(FadeIn(richtiggruppe),FadeOut(gruppe))
        self.wait(5)
        self.play(Circumscribe(richtiggruppe))
        self.wait(2)
        lösungrichtig2gruppe.shift(2.5*RIGHT)
        v3zahlrichtiggruppe.shift(0.6*LEFT)
        plusrichti2ggruppe.shift(1.6*LEFT)
        self.play(ReplacementTransform(lösungrichtiggruppe,lösungrichtig2gruppe),
                  richtig2gruppe.animate.shift(1.8*LEFT),
                  FadeIn(v3zahlrichtiggruppe),
                  FadeIn(plusrichti2ggruppe)
                  )
        self.wait()

class KraftaddierenBeispiele(Scene):
    def construct(self):

        #texte
        bsp = Tex("Kraftaddition - Beispiel").scale(1.2)
        ul1 = Underline(bsp)
        blackbox1 = SurroundingRectangle(bsp, buff=0, color=BLACK,fill_opacity=1)
        bspgruppe = VGroup(blackbox1,bsp,ul1)
        fragezeichen = Tex("?" , color = WHITE)
        fragezeichen.add_updater(lambda mob : mob.next_to(v3_1, UR).shift(0.2 *DL))

        #andere Mobjects
        schiffgezogen = ImageMobject("schiffgezogen.png").scale(0.5)
        schiffziehen1 = ImageMobject("schiffziehen.png").scale(0.3).rotate(-0.375*PI)
        schiffziehen1.move_to([2.5,1.5,0])
        schiffziehen2 = ImageMobject("schiffziehen.png").scale(0.3).rotate(-0.625*PI)
        schiffziehen2.move_to([2.5,-2.2,0])
        seil1 = ImageMobject("seil.png").scale(0.75).rotate(0.145*PI)
        seil1.move_to([0.2,0.45,0])
        seil2 = ImageMobject("seil.png").scale(0.75).rotate(-0.145*PI)
        seil2.move_to([0.2,-1.15,0])
        nupl = NumberPlane(x_range=(0,20,1.5),y_range=(0,12,1.5)).set_opacity(0.5)
        nupl.move_to([-1.76,-1.8,0])
        v3_1 = nupl.get_vector([7,0.3])
        v3_2 = nupl.get_vector([4,-0.1])
        v3_3 = nupl.get_vector([6,0.2])
        v3_4 = nupl.get_vector([3.5,-0.1])
        v3_5 = nupl.get_vector([6,0])
        v3_6 = nupl.get_vector([5.76,-0.8])
        v3_7 = nupl.get_vector([5.6,1.5])
        v3gruppe = VGroup(v3_1,v3_2,v3_3,v3_4,v3_5,v3_6,v3_7)
        v1 = nupl.get_vector([3,-1.5]).set_color(ORANGE)
        v2 = nupl.get_vector([3,1.5]).set_color(BLUE)

        #animation 
        self.add(bspgruppe)
        self.wait()
        self.play(bspgruppe.animate.to_corner(UL))
        self.wait(2)
        schiffgezogen.move_to([-4,-0.5,0])
        self.play(FadeIn(schiffgezogen))
        self.wait(2)
        self.play(FadeIn(schiffziehen1,schiffziehen2,seil1,seil2))
        self.wait(3)
        self.play(FadeIn(nupl)),self.add(bspgruppe,schiffgezogen,schiffziehen1,schiffziehen2,seil1,seil2)
        self.wait()
        v3gruppe.move_to([2.2,0,0])
        self.play(GrowArrow(v3_1),FadeIn(fragezeichen),run_time=2)
        self.wait()
        self.play(Transform(v3_1,v3_2),run_time=2)
        self.wait()
        self.play(Transform(v3_1,v3_3),run_time=2)
        self.wait()
        self.play(Transform(v3_1,v3_4),run_time=2)
        self.wait()
        self.play(FadeOut(v3_1,fragezeichen))
        self.wait(2)
        v1.move_to([0.2,-1.11,0])
        v2.move_to([0.2,0.42,0])
        self.play(seil1.animate.set_opacity(0.2),
                  seil2.animate.set_opacity(0.2),
                  schiffgezogen.animate.set_opacity(0.2),
                  schiffziehen1.animate.set_opacity(0.2),
                  schiffziehen2.animate.set_opacity(0.2))
        self.play(GrowArrow(v1),GrowArrow(v2))
        self.wait(5)
        self.play(v2.animate.move_to([3.16,-1.08,0]))
        self.wait(2)
        self.play(GrowArrow(v3_5))
        self.wait()
        self.play(v2.animate.move_to([0.2,0.45,0]))
        self.wait(5)
        self.play(seil1.animate.set_opacity(1),
                  seil2.animate.set_opacity(1),
                  schiffgezogen.animate.set_opacity(1),
                  schiffziehen1.animate.set_opacity(1),
                  schiffziehen2.animate.set_opacity(1),
                  FadeOut(v1),
                  FadeOut(v2))
        self.wait(2)
        self.play(seil2.animate.rotate(-0.05*PI).move_to([0.1,-1.4,0]),
                  schiffziehen2.animate.rotate(-0.05*PI).move_to([2.2,-2.9,0]),
                  seil1.animate.rotate(-0.06*PI).move_to([0.35,0.2,0]),
                  schiffziehen1.animate.rotate(-0.06*PI).move_to([2.7,0.8,0]),
                  Transform(v3_5,v3_6),
                  run_time=2
                  )
        self.wait(3)
        self.play(seil2.animate.rotate(0.195*PI).move_to([0.35,-0.3,0]),
                  schiffziehen2.animate.rotate(0.175*PI).move_to([2.8,-0.3,0]),
                  seil1.animate.rotate(0.1*PI).move_to([0.1,0.65,0]),
                  schiffziehen1.animate.rotate(0.1*PI).move_to([2.2,2,0]),
                  Transform(v3_5,v3_7),
                  run_time=2
                  )
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
        self.wait()
        self.play(vector1.animate.become(nupl.get_vector([vector1x,vector1y,0]).set_color(ORANGE)),vector2.animate.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE)),run_time=1)
        self.wait(2)
        self.play(vector2.animate.shift(vector1y*UP).shift(vector1x*RIGHT))
        self.wait()
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)),run_time=2)
        self.wait()

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
        self.wait(3)
        self.play(vector3.animate.become(nupl.get_vector([0,0,0]).set_color(WHITE)))
        self.wait(2)
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

        kommu = Tex("Kommutativgesetz")
        blackbox7 = SurroundingRectangle(kommu, buff=0, color=BLACK,fill_opacity=1)
        kommugruppe = VGroup(blackbox7,kommu)

        self.wait(2)
        kommugruppe.next_to(spieglungfullgruppe, DOWN).to_edge(LEFT)
        self.play(Write(kommugruppe))
        self.wait(5)
        vector1.become(nupl.get_vector([vector1x,vector1y]))
        vector4.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE))
        vector4.shift(vector1y*UP).shift(vector1x*RIGHT)
        vector5.become(nupl.get_vector([vector1x,vector1y]).set_color(ORANGE))
        vector1.shift(vector2y*UP).shift(vector2x*RIGHT).set_color(ORANGE)
        vector2.become(nupl.get_vector([vector2x,vector2y]).set_color(BLUE))
        self.wait(2)
        self.play(vector3.animate.become(nupl.get_vector([vector1x+vector2x,vector1y+vector2y,0]).set_color(WHITE)))

        self.wait(2)
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

        self.wait(2)
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

        self.wait(2)
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

class Kräftegleichgewicht(Scene):
    def construct(self):
    
        #texte
        Kräftegleichgewicht = Tex("Kräftegleichgewicht").scale(1.2)
        ul1 = Underline(Kräftegleichgewicht)
        blackbox1 = SurroundingRectangle(Kräftegleichgewicht, buff=0, color=BLACK,fill_opacity=1)
        Kräftegleichgewichtgruppe = VGroup(blackbox1,Kräftegleichgewicht,ul1)

        keinebeschleunigung = Tex("Keine Beschleunigung")
        blackbox2 = SurroundingRectangle(keinebeschleunigung, buff=0, color=BLACK,fill_opacity=1)
        keinebeschleunigunggruppe = VGroup(blackbox2,keinebeschleunigung)
        punkt = Dot([0,0,0]).set_color(RED).scale(2)

        keinekraft = Tex("Keine resultierende Kraft")
        blackbox3 = SurroundingRectangle(keinekraft, buff=0, color=BLACK,fill_opacity=1)
        keinekraftgruppe = VGroup(blackbox3,keinekraft)

        keinekraftfull = Tex("Resultierende Kraft = 0")
        blackbox4 = SurroundingRectangle(keinekraftfull, buff=0, color=BLACK,fill_opacity=1)
        keinekraftfullgruppe = VGroup(blackbox4,keinekraftfull)

        formel1 = MathTex(r"a = \frac{F}{m}")
        blackbox5 = SurroundingRectangle(formel1, buff=0, color=BLACK,fill_opacity=1)
        formel1gruppe = VGroup(blackbox5,formel1)

        formel2 = MathTex(r"0 = \frac{0}{m}")
        blackbox6 = SurroundingRectangle(formel2, buff=0, color=BLACK,fill_opacity=1)
        formel2gruppe = VGroup(blackbox6,formel2)

        #andere mobjects
        nupl = NumberPlane(x_range=(-10,10,1.5),y_range=(-6,6,1.5)).set_opacity(0.5)

        v1 = nupl.get_vector([-1.5,-1.5]).set_color(ORANGE)
        v2 = nupl.get_vector([1.5,1.5]).set_color(BLUE)
        v3 = nupl.get_vector([2,0]).set_color(GREEN)
        v4 = nupl.get_vector([0,0]).set_color(PURPLE)
        ball = ImageMobject("ball.png")
        ball.scale(0.4)


        #animationen:
        self.add(Kräftegleichgewichtgruppe)
        self.wait()
        self.play(Kräftegleichgewichtgruppe.animate.to_corner(UL))
        self.wait(2)
        self.play(FadeIn(nupl)),self.add(Kräftegleichgewichtgruppe)
        self.wait()
        self.play(FadeIn(ball))
        self.wait(2)
        v1.shift(0.5*DL)
        v2.shift(0.47*UR)
        self.play(GrowArrow(v1),GrowArrow(v2))
        self.wait(4)
        keinebeschleunigunggruppe.shift(3*LEFT)
        keinebeschleunigunggruppe.shift(0.7*UP)
        self.play(Write(keinebeschleunigunggruppe))
        self.wait()
        self.play(keinebeschleunigunggruppe.animate.next_to(Kräftegleichgewichtgruppe, DOWN).to_edge(LEFT))
        self.wait(4)
        self.play(
            ball.animate.scale(0),
            FadeIn(punkt),
            v1.animate.shift(0.4*UR),
            v2.animate.shift(0.4*DL))
        self.wait(3)

        self.play(v2.animate.move_to([-0.6,-0.8,0]))
        self.wait()
        keinekraftgruppe.move_to([-3,0.5,0])
        self.play(Write(keinekraftgruppe))
        self.wait(2)
        self.play(keinekraftgruppe.animate.next_to(keinebeschleunigunggruppe, DOWN).to_edge(LEFT).set_opacity(0))
        keinekraftfullgruppe.next_to(keinebeschleunigunggruppe, DOWN).to_edge(LEFT)
        self.play(FadeIn(keinekraftfullgruppe))

        self.wait(4)
        self.play(Circumscribe(keinebeschleunigunggruppe))
        formel1gruppe.next_to(keinekraftfullgruppe, DOWN).to_edge(LEFT)
        formel2gruppe.next_to(keinekraftfullgruppe, DOWN).to_edge(LEFT)
        self.wait(2)
        self.play(Write(formel1gruppe))
        self.wait(5)
        self.play(ReplacementTransform(formel1gruppe,formel2gruppe))
        self.wait(10)
        self.play(v2.animate.move_to([0.8,0.8,0]))
        self.wait(6)
        #selber herausgefunden :) (dieses cosinus/sinus kaack unten) (mathe boss)
        self.play(GrowArrow(v3),
                  v1.animate.become(nupl.get_vector([2*np.cos(2*(1/3)*np.pi),2*np.sin(2*(1/3)*np.pi)]).set_color(ORANGE)),
                  v2.animate.become(nupl.get_vector([2*np.cos(2*(2/3)*np.pi),2*np.sin(2*(2/3)*np.pi)]).set_color(BLUE))),self.add(punkt)
        self.wait(5)
        self.play(v1.animate.move_to([1.44,0.84,0]))
        self.wait()
        self.play(v2.animate.move_to([0.46,0.8,0]))
        self.wait(2)
        self.play(Circumscribe(keinekraftgruppe))
        self.wait(6)
        self.play(v1.animate.become(nupl.get_vector([1.5,1.5,0]).set_color(ORANGE)),
                  v2.animate.become(nupl.get_vector([-1.5,1,0]).set_color(BLUE)),
                  v3.animate.become(nupl.get_vector([-1.5,-1.5,0]).set_color(GREEN)),
                  v4.animate.become(nupl.get_vector([1.5,-1,0]).set_color(PURPLE))),self.add(punkt)
        self.wait(5)
        self.play(v4.animate.move_to([2.25,0.9,0]))
        self.wait(1)
        self.play(v3.animate.move_to([2.2,-0.3,0]))
        self.wait(1)
        self.play(v2.animate.move_to([0.7,-0.5,0]))
        self.wait(2)
        self.play(Circumscribe(keinekraftgruppe))
        self.wait(3)
        self.play(v1.animate.move_to([0.7,0.7,0]),
                v2.animate.move_to([-0.7,0.5,0]),
                v4.animate.move_to([0.7,-0.5,0]),
                v3.animate.move_to([-0.7,-0.7,0]),)
        self.wait()

class Axiom3(Scene):
    def construct(self):
        #texte
        axiom3 = Tex("Newton's drittes Axiom").scale(1.2)
        ul1 = Underline(axiom3)
        blackbox1 = SurroundingRectangle(axiom3, buff=0, color=BLACK,fill_opacity=1)
        axiom3gruppe = VGroup(blackbox1,axiom3,ul1)

        text1 = Tex("Auf jede Aktion folgt eine gleichstarke ").scale(1.2)
        text1_2 = Tex("Reaktion in entgegengesetzter Richtung.").scale(1.2)
        text1gruppe = VGroup(text1,text1_2)
        text1[0][7:13].set_color("#F5B176")
        text1_2[0][0:8].set_color("#86CFF9")

        text1kurz = Tex("Actio = Reactio")
        blackbox3 = SurroundingRectangle(text1kurz, buff=0, color=BLACK,fill_opacity=1)
        text1kurzgruppe = VGroup(blackbox3,text1kurz)
        text1kurz[0][0:5].set_color("#F5B176")
        text1kurz[0][6:13].set_color("#86CFF9")

        drei = Tex("3").scale(1.2)
        blackbox4 = SurroundingRectangle(drei, buff=0, color=BLACK,fill_opacity=1)
        dreigruppe = VGroup(blackbox4,drei)

        zwei = Tex("2").scale(1.2)
        blackbox5 = SurroundingRectangle(zwei, buff=0, color=BLACK,fill_opacity=1)
        zweigruppe = VGroup(blackbox5,zwei)

        eins = Tex("1").scale(1.2)
        blackbox6 = SurroundingRectangle(eins, buff=0, color=BLACK,fill_opacity=1)
        einsgruppe = VGroup(blackbox6,eins)

        newton1 = MathTex(r"\approx  200.000 N").scale(0.8)

        newton2 = MathTex(r"\approx  200.000 N").scale(0.8)

        fragetext = MathTex("Kugelbeschleunigung > Kanonenbeschleunigung")

        fragezeichen = MathTex("?")

        #andere Mobjects
        kanone = ImageMobject("Kanone.png").scale(0.5)
        kanonenkugel = ImageMobject("Kanonenkugel.png").scale(0.2)
        ax = NumberLine(x_range=[0,15,1])
        ax.shift(2.4* DOWN)
        zahlen = VGroup(dreigruppe,zweigruppe,einsgruppe)
        v1 = Vector([2,0]).set_color(ORANGE)
        v2 = Vector([-2,0]).set_color(BLUE)

        #animationen
        self.add(axiom3gruppe)
        self.wait(1)
        self.play(axiom3gruppe.animate.shift(3*UP))
        self.wait(4)
        text1.shift(0.4*UP)
        text1_2.shift(0.4*DOWN)
        self.play(Write(text1gruppe),run_time=3)
        self.wait(4)
        self.play(ReplacementTransform(text1gruppe,text1kurzgruppe))
        self.wait(6)
        self.play(axiom3gruppe.animate.to_corner(UL),text1kurzgruppe.animate.next_to(axiom3gruppe, DOWN).to_edge(LEFT))
        self.wait()
        kanone.move_to([-2.5,-1.7,0])
        self.play(Create(ax))
        self.wait()
        self.play(FadeIn(kanone))
        self.wait(1.5)
        zahlen.move_to(kanone)
        zahlen.shift(UP)
        dreigruppecopy = dreigruppe.copy()
        zweigruppecopy = zweigruppe.copy()
        self.play(FadeIn(dreigruppecopy))
        self.play(ReplacementTransform(dreigruppecopy,zweigruppecopy))
        self.play(ReplacementTransform(zweigruppecopy,einsgruppe))
        self.play(FadeOut(eins))
        kanonenkugel.move_to(kanone)
        kanonenkugel.shift(0.2*UP)
        kanonenkugel.shift(1.85*RIGHT)
        
        #erster versuch
        v1.move_to(kanonenkugel).shift(1.3*RIGHT)
        v2.move_to(kanone).shift(2.4*LEFT).shift(0.2*UP)
        newton1.add_updater(lambda mob : mob.next_to(v1,UP))
        newton2.add_updater(lambda mob : mob.next_to(v2,UP))
        self.play(FadeIn(kanonenkugel,v1,newton1,v2,newton2),run_time=0.5)
        self.wait(5)
        self.play(
            kanonenkugel.animate.shift(8.2*RIGHT),
            kanone.animate.shift(0.5*LEFT),
            v1.animate.set_opacity(-20),
            v2.animate.set_opacity(-20),
            newton1.animate.set_opacity(-20),
            newton2.animate.set_opacity(-20),
            run_time=2,
            rate_func=linear
        )
        self.wait(1.5)
        self.play(FadeOut(kanone,kanonenkugel))
        self.wait()

        #zweiter versuch
        kanone.move_to([-2.5,-1.7,0])
        self.play(FadeIn(kanone))
        zahlen.move_to(kanone)
        zahlen.shift(UP)
        self.wait()
        self.play(FadeIn(dreigruppe))
        self.play(ReplacementTransform(dreigruppe,zweigruppe))
        self.play(ReplacementTransform(zweigruppe,einsgruppe))
        self.play(FadeOut(eins))
        kanonenkugel.move_to(kanone)
        kanonenkugel.shift(0.2*UP)
        kanonenkugel.shift(1.85*RIGHT)
        v1.move_to(kanonenkugel).shift(1.3*RIGHT)
        v2.move_to(kanone).shift(2.4*LEFT).shift(0.2*UP)
        newton1.add_updater(lambda mob : mob.next_to(v1,UP))
        newton2.add_updater(lambda mob : mob.next_to(v2,UP))
        newton1.set_opacity(1)
        newton2.set_opacity(1)
        v1.set_opacity(1)
        v2.set_opacity(1)
        self.play(FadeIn(kanonenkugel,v1,newton1,v2,newton2),run_time=0.5)
        self.wait(1)
        self.play(
            kanonenkugel.animate.shift(8.2*RIGHT),
            kanone.animate.shift(0.5*LEFT),
            v1.animate.set_opacity(-20),
            v2.animate.set_opacity(-20),
            newton1.animate.set_opacity(-20),
            newton2.animate.set_opacity(-20),
            run_time=2,
            rate_func=linear
        )
        self.wait(2)
        self.play(ax.animate.shift(DOWN),kanone.animate.shift(DOWN))
        self.play(Write(fragetext))
        self.wait()
        self.play(Circumscribe(fragetext))
        fragezeichen.shift(DOWN)
        self.play(Write(fragezeichen))
        self.wait()

class Axiom3lösung(Scene):
    def construct(self):

        #texte
        axiom3 = Tex("Newton's drittes Axiom").scale(1.2)
        ul1 = Underline(axiom3)
        blackbox1 = SurroundingRectangle(axiom3, buff=0, color=BLACK,fill_opacity=1)
        axiom3gruppe = VGroup(blackbox1,axiom3,ul1)

        text1kurz = Tex("Actio = Reactio")
        blackbox3 = SurroundingRectangle(text1kurz, buff=0, color=BLACK,fill_opacity=1)
        text1kurzgruppe = VGroup(blackbox3,text1kurz)
        text1kurz[0][0:5].set_color("#F5B176")
        text1kurz[0][6:13].set_color("#86CFF9")

        fragetext = MathTex("Kugelbeschleunigung > Kanonenbeschleunigung")

        fragezeichen = MathTex("?")

        axiom2_1 = MathTex(r"F = m \cdot a")
        axiom2_2 = MathTex(r" F = m \cdot a \mid \div m")
        axiom2_3 = MathTex(r"\frac{F}{m} = \frac{m \cdot a}{m}")
        axiom2_4 = MathTex(r"\frac{F}{m} = a")
        axiom2_5 = MathTex(r"a = \frac{F}{m}")
        axiom2_6 = MathTex(r"Kanone: a = \frac{\approx 200.000 N}{m}")
        axiom2_7 = MathTex(r"Kanone: a = \frac{\approx 200.000 N}{200 kg}")
        axiom2_8 = MathTex(r"Kanone: 1000 \frac{m}{s^{2}} = \frac{\approx 200.000 N}{200 kg}")
        #-_ (wer checkt der checkt)
        axiom2_9 = MathTex(r"Kugel: 40000 \frac{m}{s^{2}} = \frac{\approx 200.000 N}{5 kg}")



        #andere Mobjects
        ax = NumberLine(x_range=[0,15,1])
        kanone = ImageMobject("Kanone.png").scale(0.5)

        #animationen
        kanone.move_to([-3,-2.7,0])
        fragezeichen.shift(DOWN)
        ax.shift(3.4* DOWN)
        axiom3gruppe.to_corner(UL)
        text1kurzgruppe.next_to(axiom3gruppe, DOWN).to_edge(LEFT)
        self.add(fragetext,fragezeichen,axiom3gruppe,text1kurzgruppe,ax,kanone)
        self.wait()
        self.play(FadeOut(fragezeichen))
        self.play(fragetext.animate.next_to(text1kurzgruppe, DOWN).to_edge(LEFT))
        self.wait(2)
        self.play(Write(axiom2_1))
        self.wait(3)
        self.play(Circumscribe(axiom2_1[0][4]))
        self.wait(2)
        self.play(TransformMatchingShapes(axiom2_1,axiom2_2))
        self.wait(6)
        self.play(TransformMatchingShapes(axiom2_2,axiom2_3))
        self.wait(7)
        self.play(TransformMatchingShapes(axiom2_3,axiom2_4))
        self.wait(3)
        self.play(TransformMatchingShapes(axiom2_4,axiom2_5))
        self.wait(6)
        self.play(TransformMatchingShapes(axiom2_5,axiom2_6))
        self.wait(5)
        self.play(TransformMatchingShapes(axiom2_6,axiom2_7))
        self.wait(5)
        self.play(TransformMatchingShapes(axiom2_7,axiom2_8))
        self.wait(7)
        axiom2_9.shift(1.5*DOWN)
        self.play(Write(axiom2_9),ax.animate.shift(0.4*DOWN),kanone.animate.shift(0.4*DOWN))
        self.wait()

#für text farben:
# ("#F5B176") orange
# ("#86CFF9") blau

#KRAFT MESSEN, DARSTELLEN, AXION2, EINHEITEN, AXIOM1, KRAFTADDIEREN, ADDITIONRECHNEN, KRÄFTEPARRALELOGRAMM, KRÄFTEGLEICHGEWICHT, AXIOM3, AXIOM3LÖSUNG, GEWICHTSKRAFT   : GESTRECHT
#ALLE ANIMATIONEN IN DER PP (aber ungestecht und bissle anders und pql(schlechte quali)...)
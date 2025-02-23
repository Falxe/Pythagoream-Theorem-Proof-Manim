# %%manim -qm PythagoreanProof
# --- The code above is only applicable when using Jupyter Notebook/the online version of Manim

from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # Define the initial right triangle
        x = 1.5
        y = 2
        A = np.array([x, 0, 0])
        B = np.array([0, y, 0])
        C = np.array([0, 0, 0])
        tri_1 = Polygon(A, B, C, color=WHITE)

        # Side labels
        a_label = MathTex("a").next_to(Line(C, A), DOWN, buff=0.2)
        b_label = MathTex("b").next_to(Line(C, B), LEFT, buff=0.2)
        c_label = MathTex("c").next_to(Line(C, B), RIGHT, buff=(x/2)+0.2)

        # Group the first triangle and labels
        triangle_group = VGroup(tri_1, a_label, b_label, c_label)

        # Show the first triangle
        self.play(Create(tri_1), Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)

        # Duplicate the triangle three times

        tri_2 = tri_1.copy().rotate(90 * DEGREES, about_point=ORIGIN)
        tri_3 = tri_1.copy().rotate(180 * DEGREES, about_point=ORIGIN)
        tri_4 = tri_1.copy().rotate(-90 * DEGREES, about_point=ORIGIN)

        # Animate duplication into four triangles
        self.play(
                TransformFromCopy(tri_1, tri_2),
                TransformFromCopy(tri_1, tri_3),
                TransformFromCopy(tri_1, tri_4),
        )
        self.wait(1)

        tri_2.shift([(x+y),0,0]),
        tri_3.shift([(x+y),(x+y),0])
        tri_4.shift([0,(x+y),0])

         # Animate duplication into four triangles
        self.play(
                TransformFromCopy(tri_1, tri_2),
                TransformFromCopy(tri_1, tri_3),
                TransformFromCopy(tri_1, tri_4),
        )
        self.wait(1) 


                # Move letters to their new positions
        a_label1 = MathTex("a").next_to(tri_2, RIGHT, buff=0.2)
        b_label1 = MathTex("b").next_to(tri_2, DOWN, buff=0.2)
        c_label1 = MathTex("c").next_to(tri_1, RIGHT, buff=(x/2)+0.2)
        
        a_label2 = MathTex("a").next_to(tri_3, UP, buff=0.2)
        b_label2 = MathTex("b").next_to(tri_3, RIGHT, buff=0.2)
        c_label2 = MathTex("c").next_to(tri_2, UP, buff=(x/2)+0.2)

        a_label3 = MathTex("a").next_to(tri_4, LEFT, buff=0.2)
        b_label3 = MathTex("b").next_to(tri_4, UP, buff=0.2)
        c_label3 = MathTex("c").next_to(tri_3, LEFT, buff=(x/2)+0.2)

        
        self.play(Write(a_label1), Write(b_label1), Write(c_label1))
        self.play(Write(a_label2), Write(b_label2), Write(c_label2))
        self.play(Write(a_label3), Write(b_label3), Write(c_label3))
        self.wait(1)


        # Show final proof equation
        equation = MathTex("a^2 + b^2 = c^2")
        equation.shift([(x+y)/2,-1.3,0])
        self.play(Write(equation))
        self.wait(2)


        self.play(FadeOut(VGroup(tri_1, tri_2, tri_3, tri_4, equation)))

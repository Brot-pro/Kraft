import ast
from pathlib import Path

DEFAULT_PLAY_RUNTIME = 1.0
DEFAULT_WAIT_RUNTIME = 1.0

#command
# python estimate_manim_runtime.py maxwell.py

class SceneRuntimeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def visit_ClassDef(self, node):
        # Detect Manim Scene subclasses
        base_names = {b.id for b in node.bases if isinstance(b, ast.Name)}
        if "Scene" in base_names or "ThreeDScene" in base_names:
            self.current_scene = node.name
            self.scenes[self.current_scene] = 0.0
            self.generic_visit(node)
            self.current_scene = None
        else:
            self.generic_visit(node)

    def visit_Call(self, node):
        if not self.current_scene:
            return

        # Match self.play(...)
        if self._is_self_call(node, "play"):
            runtime = self._extract_play_runtime(node)
            self.scenes[self.current_scene] += runtime

        # Match self.wait(...)
        elif self._is_self_call(node, "wait"):
            runtime = self._extract_wait_runtime(node)
            self.scenes[self.current_scene] += runtime

        self.generic_visit(node)

    def _is_self_call(self, node, name):
        return (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "self"
            and node.func.attr == name
        )

    def _extract_wait_runtime(self, node):
        if node.args:
            return self._safe_eval(node.args[0])
        return DEFAULT_WAIT_RUNTIME

    def _extract_play_runtime(self, node):
        runtimes = []

        # Keyword run_time=...
        for kw in node.keywords:
            if kw.arg == "run_time":
                runtimes.append(self._safe_eval(kw.value))

        # Animations may have embedded run_time in arguments
        for arg in node.args:
            if isinstance(arg, ast.Call):
                for kw in arg.keywords:
                    if kw.arg == "run_time":
                        runtimes.append(self._safe_eval(kw.value))

        return max(runtimes) if runtimes else DEFAULT_PLAY_RUNTIME

    def _safe_eval(self, node):
        try:
            return float(ast.literal_eval(node))
        except Exception:
            return DEFAULT_PLAY_RUNTIME


def estimate_runtime(file_path):
    tree = ast.parse(Path(file_path).read_text(encoding="utf-8"))
    analyzer = SceneRuntimeAnalyzer()
    analyzer.visit(tree)

    total = 0.0
    print("\nEstimated Manim Runtime\n" + "-" * 30)
    for scene, t in analyzer.scenes.items():
        print(f"{scene:<25} {t:6.2f} s")
        total += t

    print("-" * 30)
    print(f"{'TOTAL':<25} {total:6.2f} s")
    print(f"≈ {total/60:.2f} minutes")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python estimate_manim_runtime.py your_scene_file.py")
    else:
        estimate_runtime(sys.argv[1])

# class A(Scene):
#     def construct(self):

#         func4 = lambda pos: vecField4(pos=pos)
#         def vecField4(pos):
#             e = 0.001
#             s = 0.2
#             x = pos[0]
#             y = pos[1]
#             normal1 = x**2 + (y-s)**2 + e
#             normal2 = x**2 + (y+s)**2 + e
#             field = [0,0]
#             field[0] = (y-s)/(normal1) - (y+s)/(normal2)
#             field[1] = (-x)/(normal1) + (x)/(normal2)
#             return 3*field[0]*RIGHT + 3*field[1]*UP
#         stream4 = StreamLines(func4, stroke_width=2, max_anchors_per_line=600, virtual_time=50, n_repeats=1, max_color_scheme_value=1.1, x_range=[-16,16], y_range=[-8,8]).set_z_index(-1).scale(0.5)

#         self.add(stream4)
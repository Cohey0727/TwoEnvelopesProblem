from manim import *

class Title(Scene):
    def construct(self):
        # 日本語のタイトル
        japanese_title = Text("2つの封筒問題", font_size=48, color=BLUE)
        
        # 英語のタイトル
        english_title = Text("Two Envelopes Problem", font_size=32, color=GRAY)
        english_title.next_to(japanese_title, DOWN, buff=0.5)
        
        # アニメーション
        self.play(Write(japanese_title))
        self.wait(0.5)
        self.play(Write(english_title))
        self.wait(2)
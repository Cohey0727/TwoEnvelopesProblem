from manim import *

JAPANESE_FONT = "Hiragino Sans"

class TwoEnvelopesIntro(Scene):
    def construct(self):
        # タイトル
        title = Text("２つの封筒問題", font_size=48, font=JAPANESE_FONT)
        subtitle = Text("Two Envelopes Problem", font_size=32, color=GRAY).next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1)
        self.wait(1)
        
        self.play(title_group.animate.to_edge(UP))
        
        # 問題設定の説明
        intro_text = Text("数学の有名なパラドックスの一つです", font_size=28, font=JAPANESE_FONT)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        
        # 封筒を描画
        envelope1 = Rectangle(width=2, height=1.2, color=BLUE, fill_opacity=0.3)
        envelope2 = Rectangle(width=2, height=1.2, color=RED, fill_opacity=0.3)
        
        envelope1.shift(LEFT * 2.5)
        envelope2.shift(RIGHT * 2.5)
        
        # 封筒のラベル
        label1 = Text("封筒A", font_size=24, font=JAPANESE_FONT).next_to(envelope1, DOWN)
        label2 = Text("封筒B", font_size=24, font=JAPANESE_FONT).next_to(envelope2, DOWN)
        
        self.play(
            Create(envelope1),
            Create(envelope2),
            Write(label1),
            Write(label2)
        )
        self.wait(1)
        
        # 説明文
        explanation = Text("2つの封筒にお金が入っています", font_size=24, font=JAPANESE_FONT)
        explanation.to_edge(DOWN, buff=1.5)
        self.play(Write(explanation))
        self.wait(2)
        
        # 重要な条件
        condition = Text("一方の封筒には、もう一方の2倍の金額が入っている", 
                        font_size=24, font=JAPANESE_FONT, color=YELLOW)
        condition.move_to(explanation)
        
        self.play(Transform(explanation, condition))
        self.wait(2)
        
        # 例を示す
        example_text = Text("例：一方に1万円、もう一方に2万円", 
                          font_size=24, font=JAPANESE_FONT)
        example_text.move_to(condition)
        
        self.play(Transform(explanation, example_text))
        
        # お金のアニメーション
        money1 = Text("1万円", font_size=20, font=JAPANESE_FONT, color=GREEN)
        money2 = Text("2万円", font_size=20, font=JAPANESE_FONT, color=GREEN)
        
        money1.move_to(envelope1)
        money2.move_to(envelope2)
        
        self.play(FadeIn(money1), FadeIn(money2))
        self.wait(2)
        
        # 不確実性を示す
        question_mark1 = Text("?", font_size=36, color=WHITE)
        question_mark2 = Text("?", font_size=36, color=WHITE)
        
        question_mark1.move_to(envelope1)
        question_mark2.move_to(envelope2)
        
        self.play(
            Transform(money1, question_mark1),
            Transform(money2, question_mark2)
        )
        
        unknown_text = Text("どちらにより多くの金額が入っているかは不明", font_size=24, font=JAPANESE_FONT, color=ORANGE)
        unknown_text.move_to(example_text)
        
        self.play(Transform(explanation, unknown_text))
        self.wait(3)
        
        # 終了
        self.play(FadeOut(*self.mobjects))
        
        final_text1 = Text("このシンプルな設定から", font_size=32, font=JAPANESE_FONT)
        final_text2 = Text("興味深いパラドックスが生まれます", font_size=32, font=JAPANESE_FONT).next_to(final_text1, DOWN, buff=0.3)
        
        final_group = VGroup(final_text1, final_text2).move_to(ORIGIN)
        self.play(Write(final_text1))
        self.play(Write(final_text2))
        self.wait(3)
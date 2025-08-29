from manim import *
import numpy as np


def Envelope(*, color: ManimColor, position: np.ndarray) -> VGroup:
    """封筒の形状を作成するコンポーネント"""
    # 封筒本体（長方形）
    body = Rectangle(width=2, height=3, color=color, fill_opacity=0.3)
    
    # 封筒の上部フラップ（三角形）
    flap_points = [
        [-1, 1.5, 0],    # 左上
        [1, 1.5, 0],     # 右上
        [0, 0.8, 0]      # 中央下部（内向き）
    ]
    flap = Polygon(*flap_points, color=color, fill_opacity=0.4, stroke_width=2)
    
    # 封筒の底部線（封筒らしさを演出）
    bottom_line = Line([-1, -1.5, 0], [1, -1.5, 0], color=color, stroke_width=3)
    
    # グループ化
    envelope = VGroup(body, flap, bottom_line)
    envelope.shift(position)
    return envelope

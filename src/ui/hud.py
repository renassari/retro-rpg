"""Bars and small status indicators rendered during battle."""

import arcade


def draw_hp_bar(x, y, hp, max_hp, color):
    width = 160
    height = 12

    arcade.draw_rect_filled(
        arcade.rect.XYWH(x, y, width, height),
        arcade.color.DARK_RED,
    )

    ratio = max(0, min(hp / max_hp, 1))
    fill = width * ratio

    arcade.draw_rect_filled(
        arcade.rect.XYWH(
            x - width / 2 + fill / 2,
            y,
            fill,
            height,
        ),
        color,
    )
    arcade.draw_text(
        f"{hp} / {max_hp}",
        x,
        y,
        arcade.color.BLUE,
        10,
        anchor_x="center",
        anchor_y="center",
    )


def draw_bp_bar(x, y, bp, max_bp, color):
    width = 160
    height = 12

    arcade.draw_rect_filled(
        arcade.rect.XYWH(x, y, width, height),
        arcade.color.DARK_BLUE,
    )

    fill = (bp / max_bp) * width

    arcade.draw_rect_filled(
        arcade.rect.XYWH(x - (width - fill) / 2, y, fill, height),
        color,
    )
    arcade.draw_text(
        f"{bp} / {max_bp}",
        x,
        y,
        arcade.color.RED,
        10,
        anchor_x="center",
        anchor_y="center",
    )

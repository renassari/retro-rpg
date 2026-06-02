"""High-level scene rendering: explore, dialog, battle, gameover, post-battle."""

import arcade

from src.data.dialogues import DIALOGUES
from src.data.items import BATTLE_MENU
from src.ui.hud import draw_bp_bar, draw_hp_bar
from src.ui.menus import (
    draw_item_popup,
    draw_level_choice,
    draw_magic_popup,
    draw_main_battle_menu,
)
from src.data.items import ITEM_NAMES


def draw_background(game):
    arcade.draw_texture_rect(
        game.background1,
        arcade.rect.XYWH(game.width // 2, game.height // 2, game.width, game.height),
    )


def draw_gameover(game):
    arcade.draw_texture_rect(
        game.gameover,
        arcade.rect.XYWH(game.width // 2, game.height // 2, game.width, game.height),
    )
    arcade.draw_text(
        "Drücke R zum Neustart",
        game.width / 2,
        80,
        arcade.color.WHITE,
        20,
        anchor_x="center",
    )


def draw_post_battle(game):
    game.player_list.draw()
    game.enemy_list.draw()

    popup_w = 420
    popup_h = 120
    popup_x = game.width // 2
    popup_y = 450

    arcade.draw_rect_filled(
        arcade.rect.XYWH(popup_x, popup_y, popup_w, popup_h),
        arcade.color.DARK_OLIVE_GREEN,
    )

    arcade.draw_text(
        f"Noch {game.post_battle_xp} XP bis zum nächsten Level",
        popup_x,
        popup_y + 20,
        arcade.color.WHITE,
        18,
        anchor_x="center",
    )

    arcade.draw_text(
        "Press Space to continue",
        popup_x,
        popup_y - 30,
        arcade.color.LIGHT_GRAY,
        12,
        anchor_x="center",
    )


def draw_explore(game):
    game.player_list.draw()
    game.enemy_list.draw()

    for enemy in game.enemy_list:
        dist = arcade.get_distance_between_sprites(game.player, enemy)
        if dist < 80:
            arcade.draw_circle_filled(
                enemy.center_x + 20,
                enemy.center_y + 60,
                12,
                arcade.color.BLACK,
            )
            arcade.draw_text(
                "E",
                enemy.center_x + 20,
                enemy.center_y + 55,
                arcade.color.WHITE,
                14,
                anchor_x="center",
            )


def draw_dialog(game):
    game.player_list.draw()
    game.enemy_list.draw()

    arcade.draw_rect_filled(
        arcade.rect.XYWH(400, 80, 3000, 140),
        arcade.color.BLACK,
    )

    arcade.draw_text(
        DIALOGUES[game.current_dialog_id]["name"],
        40, 100, arcade.color.WHITE, 18,
    )

    arcade.draw_text(
        DIALOGUES[game.current_dialog_id]["lines"][game.dialog_index],
        120, 70, arcade.color.WHITE, 18,
    )


def draw_battle(game):
    game.player_list.draw()

    if game.enemy is not None:
        # Some arcade versions lack Sprite.draw(); render via temporary list.
        tmp = arcade.SpriteList()
        tmp.append(game.enemy)
        tmp.draw()
    else:
        game.enemy_list.draw()

    draw_hp_bar(200, 410, game.player_hp, game.max_hp, arcade.color.RED)
    draw_hp_bar(600, 410, game.enemy_hp, game.enemy_max_hp, arcade.color.RED)
    draw_bp_bar(200, 395, game.bp, game.max_bp, arcade.color.CYAN)

    for dmg in game.damage_numbers:
        arcade.draw_text(
            dmg["text"],
            dmg["x"],
            dmg["y"],
            dmg["color"],
            16,
            anchor_x="center",
        )

    arcade.draw_text("Gypsy Luka", 170, 430, arcade.color.WHITE, 14)
    enemy_name = game.current_enemy or ""
    arcade.draw_text(enemy_name, 540, 430, arcade.color.WHITE, 14)

    arcade.draw_texture_rect(
        game.level_ui_bg,
        arcade.rect.XYWH(game.width // 2, 80, game.width, 160),
    )

    arcade.draw_rect_filled(
        arcade.rect.XYWH(400, 80, 4000, 140),
        arcade.color.BLACK,
    )

    arcade.draw_text(game.message, 250, 20, arcade.color.WHITE, 14)

    if BATTLE_MENU[game.selected] == "Magic":
        draw_magic_popup(game)

    arcade.draw_text(f"Level: {game.level}", 20, 430, arcade.color.WHITE, 14)
    draw_main_battle_menu(game)
    arcade.draw_text(game.message, 250, 20, arcade.color.WHITE, 14)

    if BATTLE_MENU[game.selected] == "Item":
        draw_item_popup(game)
        arcade.draw_text(f"Level: {game.level}", 20, 430, arcade.color.WHITE, 14)


def draw_scene(game):
    """Top-level scene dispatcher driven by `game.state`."""
    if game.state == "gameover":
        draw_gameover(game)
        return

    draw_background(game)

    if game.state == "post_battle":
        draw_post_battle(game)
        return

    draw_background(game)

    if game.state == "pause":
        # Dark overlay
        arcade.draw_lrbt_rectangle_filled(
            0,
            game.width,
            0,
            game.height,
            (0, 0, 0, 200)
        )

        # Title
        arcade.draw_text(
            "PAUSE MENÜ",
            game.width // 2,
            game.height - 80,
            arcade.color.WHITE,
            30,
            anchor_x="center"
        )

        # HP / MP
        arcade.draw_text(
            f"HP: {game.player_hp}/{game.max_hp}",
            100,
            game.height - 150,
            arcade.color.RED,
            20
        )

        arcade.draw_text(
            f"MP: {game.bp}/{game.max_bp}",
            100,
            game.height - 190,
            arcade.color.BLUE,
            20
        )

        # LEFT SIDE: INVENTORY
        arcade.draw_text(
            "Inventory",
            100,
            game.height - 250,
            arcade.color.WHITE,
            20
        )

        y_items = game.height - 290

        for i, item in enumerate(ITEM_NAMES):
            prefix = "> " if i == game.pause_selected else ""

            arcade.draw_text(
                f"{prefix}{item} x{game.inventory.get(item, 0)}",
                100,
                y_items,
                arcade.color.WHITE,
                18
            )

            y_items -= 30

        # RIGHT SIDE: QUEST ITEMS
        arcade.draw_text(
            "Quest Items",
            500,
            game.height - 250,
            arcade.color.YELLOW,
            20
        )

        y_quest = game.height - 290

        for item, amount in game.quest_items.items():
            arcade.draw_text(
                f"{item} x{amount}",
                500,
                y_quest,
                arcade.color.WHITE,
                18
            )

            y_quest -= 30

        return

    if game.state == "explore":
        draw_explore(game)
        return

    if game.state == "dialog":
        draw_dialog(game)
        return

    if game.state == "battle":
        draw_battle(game)
        return

    if game.state == "level_choice":
        draw_level_choice(game)
        return

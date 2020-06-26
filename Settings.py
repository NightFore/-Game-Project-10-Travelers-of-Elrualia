"""
    Settings
"""
# Main Settings
project_title = "Traveler of Elrualia"
screen_size = WIDTH, HEIGHT = 1280, 720
FPS = 60

"""
    Colors
"""
BLACK = 0, 0, 0
WHITE = 255, 255, 255

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

YELLOW = 255, 255, 0
MAGENTA = 255, 0, 255
CYAN = 0, 255, 255

LIGHTGREY = 100, 100, 100
LIGHTBLUE = 90, 135, 180
LIGHTSKYBLUE = 135, 206, 250

ORANGE = 255, 120, 30

"""
    Game Settings
"""
# Characters settings / 0: bottom, 1: left, 2: right, 3: top
GAME_DICT = {"background_image": "background_battle.png", "background_color": LIGHTBLUE,
            "grid_size": [4, 4], "grid_dt": [120, 70],
             "pos": {"player": [220, 360], "enemy": [0, 0],
                     "player_name": [0, 0], "enemy_name": [0, 0], "enemy_name_dt": [0, 0],
                     "player_level": [0, 0], "player_exp": [0, 0], "player_mana": [0, 0],
                     "next_spell": [0, 0], "current_spell": [0, 0], "current_attack": [0, 0],
                     "stage": [0, 0], "time": [0, 0], "option": [0, 0], "fps": [0, 0]},
             "color": {"health": GREEN, "mana": LIGHTSKYBLUE, "spell": [RED, BLUE, GREEN]},
             "font": None}

CHARACTER_DICT = {"layer": 2,
                  "player": {"name": "Player", "pos": [208, 332], "grid_pos": [0, 0],
                             "image": "character_oco_Knight_Idle_strip_noBKG_256x256.png", "side": 0, "center": True, "bobbing": False,
                             "table": True, "size": [256, 256], "animation_time": 0.075, "speed": [625, 625],
                             "level": 1, "max_health": 100, "health": 100, "max_mana": 5, "mana": 3.75,
                             "attack_rate": 225},
                  "skeleton": {"name": "Skeleton", "pos": [700, 360], "grid_pos": [0, 0],
                               "image": "character_pipoya_enemy_04_1.png", "side": 1, "center": True, "bobbing": False,
                               "table": True, "size": [32, 32], "animation_time": 0.075, "speed": [625, 625],
                               "level": 1, "max_health": 100, "health": 100, "max_mana": 6, "mana": 4.50,
                               "move_frequency": 1000}}

SPELL_DICT = {"layer": 3, "offset": [0, -40], "cast_offset": [40, 0],
              "energy_ball": {"image": "effect_pimen_EnergyBall.png", "side": 0, "center": True, "bobbing": False,
                              "table": True, "size": [128, 128], "animation_time": 0.100, "movespeed": [800, 800],
                              "damage": 10, "range": 8 * [[1, 0]]}}
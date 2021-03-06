"""
    Settings
"""
# Main Settings
project_title = "Traveler of Elrualia"
screen_size = WIDTH, HEIGHT = 1280, 720
FPS = 60
default_volume = 5

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
LIGHTSKYBLUE = 140, 205, 245
SKYBLUE = 95, 140, 200
DARKSKYBLUE = 15, 160, 240

DARKGREY = 47, 47, 47
LIGHTSKYGREY = 212, 212, 212
LIGHTCYAN = 31, 177, 171
LIGHTGREEN = 147, 189, 47

ORANGE = 255, 120, 30

"""
    Game Settings
"""
# Characters settings / 0: bottom, 1: left, 2: right, 3: top
GAME_DICT = {"background_color": LIGHTBLUE, "background_image": "rizaldarmawansyah_Mountain.png", "interface_image": "background_battle.png",
             "platform_size": [950, 270],
             "main_menu_font": None, "main_menu_size": 100, "main_menu_color": WHITE,
             "ui_font": None, "ui_size": 40, "ui_color": WHITE,
             "status_font": None, "status_size": 25, "status_color": WHITE,
             "mana_pos": [250, 650], "energy_pos": [400, 650],
             "grid_size": [4, 4], "grid_dt": [120, 70],
             "pos": {"player": [220, 360], "enemy": [700, 360]},
             "color": {"debug": CYAN, "health": GREEN, "mana": LIGHTSKYBLUE, "spell": [RED, BLUE, GREEN]},
             "font": None}






CHARACTER_DICT = {"layer": 2,
                  "player": {
                      "name": "Player", "pos": [220, 320], "grid_pos": [0, 0], "range": [], "move": True,
                      "image": "character_SecretHideout_Gunner_Blue_Idle_960x192_192x192.png", "side": 0, "center": True, "bobbing": False, "flip": False,
                      "table": True, "reverse": False, "size": [192, 192], "animation_time": 0.150, "animation_loop": False, "impact": False,
                      "hp_offset": [0, 55],
                      "spell_offset": [0, -48], "cast_offset": [102, 0],
                      "debug_color": BLUE, "debug_pos": [168, 333], "debug_dt": [104, 54],
                      "move_speed": [1.25 * GAME_DICT["platform_size"][0], 2.5 * GAME_DICT["platform_size"][1]], "move_cost": 10,
                      "level": 1, "health_max": 100, "health_regen": 1, "mana_max": 2, "mana_regen": 2, "energy_max": 250, "energy_regen": 5,
                      "attack_rate": 225},
                  "enemy": {
                      "name": "Enemy", "pos": [700, 320], "grid_pos": [0, 0], "range": [], "move": True,
                      "hp_offset": [0, 55],
                      "debug_color": RED, "debug_pos": [648, 333], "debug_dt": [104, 54],
                      "image": "character_SecretHideout_Gunner_Red_Idle_960x192_192x192.png", "side": 0, "center": True, "bobbing": False, "flip": True,
                      "table": True, "reverse": False, "size": [192, 192], "animation_time": 0.150, "animation_loop": False, "impact": False,
                      "move_speed": [1.25 * GAME_DICT["platform_size"][0], 2.5 * GAME_DICT["platform_size"][1]], "move_cost": 10,
                      "level": 1, "health_max": 100, "health_regen": 0.25, "mana_max": 3, "mana_regen": 0.10, "energy_max": 1, "energy_regen": 5,
                      "move_frequency": 1000}}

SPELL_DICT = {"layer": 3,
              "projectile": {
                  "pos": [230, 355], "range": 8 * [[1, 0]], "move": True,
                  "image": "effect_pimen_Projectile_256x64.png", "center": True, "bobbing": False, "flip": False, "impact": False,
                  "table": True, "reverse": True, "size": [256, 64], "side": 0, "animation_time": 0.025, "animation_loop": False,
                  "move_speed": [1500, 1500],
                  "damage": 10, "mana_cost": 0, "energy_cost": 1, "cooldown": 0.25},
              "energy_ball": {
                  "pos": [220, 360], "range": 8 * [[1, 0]], "move": True,
                  "image": "effect_pimen_EnergyBall_128x128.png", "center": True, "bobbing": False, "flip": False, "impact": True,
                  "table": True, "reverse": False, "size": [128, 128], "side": 0, "animation_time": 0.025, "animation_loop": False,
                  "move_speed": [800, 800],
                  "damage": 20, "mana_cost": 1, "energy_cost": 0, "cooldown": 0.5},
              "energy_ball_impact": {
                  "pos": [0, 0], "range": [0, 0], "move": False,
                  "image": "effect_pimen_EnergyBall_Impact_128x128.png", "center": True, "bobbing": False, "flip": False, "impact": False,
                  "table": True, "reverse": True, "size": [128, 128], "side": 0, "animation_time": 0.025, "animation_loop": True},
              "thunder": {
                  "pos": [220, 260], "range": [4, 0], "move": False,
                  "image": "effect_pimen_Thunder_64x256.png", "center": True, "bobbing": False, "flip": False, "impact": False,
                  "table": True, "reverse": False, "size": [64, 256], "side": 0, "animation_time": 0.025, "animation_loop": True,
                  "damage": 50, "mana_cost": 2, "energy_cost": 0, "cooldown": 1},
              }
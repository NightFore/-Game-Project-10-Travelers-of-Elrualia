import pygame
import pytweening as tween
import random

from Settings import *
from Function import *
vec = pygame.math.Vector2

"""
    Others Functions
"""
class Spell(pygame.sprite.Sprite):
    def __init__(self, game, dict, object=None, group=None, parent=None):
        init_sprite(self, game, dict, object, group, parent)

    def init_settings(self):
        # Position
        self.grid_size = self.game_dict["grid_size"]
        self.grid_pos = vec(self.parent.grid_pos[:])
        self.grid_dt = vec(self.game_dict["grid_dt"])
        if self.move:
            offset = [self.parent.object_dict["spell_offset"][0] + self.parent.object_dict["cast_offset"][0] + self.parent.pos_dt[0], self.parent.object_dict["spell_offset"][1] + self.parent.object_dict["cast_offset"][1]]
            self.pos += self.grid_pos[0] * self.grid_dt[0] + offset[0], self.grid_pos[1] * self.grid_dt[1] + offset[1]
            self.pos_dt = vec(offset[0], 0)
        else:
            self.grid_pos += self.range
            self.pos += self.grid_pos[0] * self.grid_dt[0], self.grid_pos[1] * self.grid_dt[1]

        # Gameplay
        self.spawn_time = pygame.time.get_ticks()
        self.hit = False
        self.damage = self.object_dict["damage"]
        self.mana_cost = self.object_dict["mana_cost"]
        self.energy_cost = self.object_dict["energy_cost"]

    def update_move(self):
        if len(self.range) > 0:
            if 0 <= self.grid_pos[0] + self.range[0][0] < 2 * self.grid_size[0] and 0 <= self.grid_pos[1] + self.range[0][1] < 2 * self.grid_size[1]:
                update_move(self)
            else:
                self.kill()
        else:
            self.kill()

    def collide_sprite(self):
        if not self.hit:
            for sprite in self.game.characters:
                if sprite != self.parent and (self.grid_pos[0] - self.grid_size[0] == sprite.grid_pos[0] and self.grid_pos[1] == sprite.grid_pos[1]):
                    sprite.health -= self.damage
                    if self.move:
                        self.kill()
                    if self.impact:
                        Impact(self.game, self.dict, self.object + "_impact", self.group, self)
                    self.hit = True

    def draw(self):
        if self.game.game_status == "battle":
            self.game.gameDisplay.blit(self.image, self)

    def update(self):
        self.game.update_sprite(self, move=self.move)
        self.collide_sprite()
        if pygame.time.get_ticks() - self.spawn_time > 5000:
            self.kill()


class Impact(pygame.sprite.Sprite):
    def __init__(self, game, dict, object=None, group=None, parent=None):
        init_sprite(self, game, dict, object, group, parent)

    def init_settings(self):
        # Position
        self.grid_size = self.game_dict["grid_size"]
        self.grid_pos = vec(self.parent.grid_pos[:])
        self.grid_dt = vec(self.game_dict["grid_dt"])
        self.pos = self.parent.pos

        # Gameplay
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        if self.game.game_status == "battle":
            self.game.gameDisplay.blit(self.image, self)

    def update(self):
        self.game.update_sprite(self)



class Player(pygame.sprite.Sprite):
    def __init__(self, game, dict, object=None, group=None, parent=None):
        init_sprite(self, game, dict, object, group, parent)

    def init_settings(self):
        init_character(self), init_interface(self)

        # Gameplay
        self.cooldown = {"Q": 0, "W": 0, "E": 0}
        self.spell_cooldown = {"Q": self.game.spell_dict["energy_ball"]["cooldown"],
                               "W": self.game.spell_dict["thunder"]["cooldown"],
                               "E": self.game.spell_dict["projectile"]["cooldown"]}
        self.last_attack = pygame.time.get_ticks()
        self.attack_rate = self.object_dict["attack_rate"]

        # Status --------------------- #
        self.experience = 0
        self.experience_max = 100
        self.status_points = 5
        self.status_points_max = 5

    def custom(self, value):
        type, ds = value[0], value[1]
        if 0 <= self.status_points - ds <= self.status_points_max:
            if type == "health":
                self.health += 5 * ds
            elif type == "mana":
                self.mana += 1 * ds
            elif type == "energy":
                self.energy += 50 * ds
            self.status_points -= ds

    def custom_reset(self):
        self.health = self.health_max
        self.mana = self.mana_max
        self.energy = self.energy_max
        self.status_points = self.status_points_max

    def custom_confirm(self):
        self.health_max = self.health
        self.mana_max = self.mana
        self.energy_max = self.energy
        self.status_points_max = self.status_points
        self.game.update_stage("battle_1")

    def update_move(self):
        if len(self.range) > 0:
            update_move(self)

    def buffer_move(self, dx=0, dy=0):
        if len(self.range) < 2 and self.energy - 1 >= 0:
            if 0 <= self.grid_pos[0] + dx < self.grid_size[0] and 0 <= self.grid_pos[1] + dy < self.grid_size[1]:
                self.energy = max(self.energy - self.move_cost, 0)
                self.range.append([dx, dy])

    def get_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            init_spell(Spell, "Q", self.game, self.game.spell_dict, "energy_ball", self.game.spells, self)
        if keys[pygame.K_w]:
            init_spell(Spell, "W", self.game, self.game.spell_dict, "thunder", self.game.spells, self)
        if keys[pygame.K_e]:
            init_spell(Spell, "E", self.game, self.game.spell_dict, "projectile", self.game.spells, self)

    def update_status(self):
        self.mana = min(self.mana_max, self.mana + self.mana_regen * self.dt)
        self.energy = min(self.energy_max, self.energy + self.energy_regen * self.dt)

        for index in self.cooldown:
            self.cooldown[index] = max(self.cooldown[index] - self.dt, 0)

    def draw(self):
        if self.game.game_status == "battle":
            self.game.gameDisplay.blit(self.image, self)
            self.game.draw_text(self.health, self.game.status_font, self.game.status_color, self.pos + self.hp_offset, "center")

    def update(self):
        if self.game.game_status == "battle":
            self.game.update_sprite(self, move=True, keys=True)
            self.update_status()



class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, dict, object=None, group=None, parent=None):
        init_sprite(self, game, dict, object, group, parent)

    def init_settings(self):
        init_character(self), init_interface(self)

        # Gameplay
        self.last_move = pygame.time.get_ticks()
        self.move_frequency = self.object_dict["move_frequency"]

    def update_move(self):
        if len(self.range) == 0 and pygame.time.get_ticks() - self.last_move > self.move_frequency:
            dx = dy = 0
            while (dx == dy == 0 or dx != 0 and dy != 0) or not (0 <= self.grid_pos[0] + dx < self.grid_size[0] and 0 <= self.grid_pos[1] + dy < self.grid_size[1]):
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
            self.range.append([dx, dy])
            self.last_move = pygame.time.get_ticks()

        if len(self.range) > 0:
            if 0 <= self.grid_pos[0] + self.range[0][0] < self.grid_size[0] and 0 <= self.grid_pos[1] + self.range[0][1] < self.grid_size[1]:
                update_move(self)
            else:
                del self.range[0]

    def draw(self):
        if self.game.game_status == "battle":
            self.game.gameDisplay.blit(self.image, self)
            self.game.draw_text(self.health, self.game.status_font, self.game.status_color, self.pos + self.hp_offset, "center")

    def update(self):
        if self.game.game_status == "battle":
            self.game.update_sprite(self, move=True)


class Button(pygame.sprite.Sprite):
    def __init__(self, game, dict, object=None, group=None, action=None, variable=None):
        # Initialization ------------- #
        self.game = game
        self.groups = self.game.all_sprites, group
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.object = object
        self.variable = variable
        self.action = action

        # Dict ----------------------- #
        self.dict = dict
        self.object = self.dict[object]
        self.settings = self.dict[self.object["type"]]

        # Settings ----------------------- #
        self.center = self.settings["center"]
        self.font = self.settings["font"]
        self.font_color = self.settings["font_color"]
        self.inactive_color = self.settings["inactive_color"]
        self.active_color = self.settings["active_color"]
        self.border_color = self.settings["border_color"]
        self.border_size = self.settings["border_size"]
        self.sound_active = self.settings["sound_active"]
        self.sound_action = self.settings["sound_action"]
        self.button_rect = self.object["rect"]
        self.text = self.object["text"]
        self.sound = False

        # Surface (Inactive) -------------------- #
        self.inactive = pygame.Surface((self.button_rect[2], self.button_rect[3]))
        self.inactive.fill(self.border_color)
        pygame.draw.rect(self.inactive, self.inactive_color, (self.border_size, self.border_size, self.button_rect[2] - self.border_size*2, self.button_rect[3] - self.border_size*2))

        # Surface (Active) -------------------- #
        self.active = pygame.Surface((self.button_rect[2], self.button_rect[3]))
        self.active.fill(self.border_color)
        pygame.draw.rect(self.active, self.active_color, (self.border_size, self.border_size, self.button_rect[2] - self.border_size*2, self.button_rect[3] - self.border_size*2))

        # Rect --------------------- #
        self.image = self.inactive
        self.rect = self.image.get_rect()
        if self.center:
            self.rect.center = (self.button_rect[0], self.button_rect[1])
        self.text_pos = self.rect[0] + self.rect[2] / 2, self.rect[1] + self.rect[3] / 2

    def update(self):
        if self.rect.collidepoint(self.game.mouse):
            self.image = self.active
            if self.sound_active is not None and not self.sound:
                pygame.mixer.Sound.play(self.sound_active)
                self.sound = True
            if self.game.click[1] and self.action is not None:
                if self.sound_action is not None:
                    pygame.mixer.Sound.play(self.sound_action)
                if self.variable is not None:
                    self.action(self.variable)
                else:
                    self.action()
        else:
            self.image = self.inactive
            self.sound = False

    def draw(self):
        self.game.gameDisplay.blit(self.image, self)
        if self.text is not None and self.font is not None:
            self.game.draw_text(self.text, self.font, self.font_color, self.text_pos, "center")
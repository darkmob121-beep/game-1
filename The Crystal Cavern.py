import math
import random

from ursina import (
    AmbientLight,
    Cone,
    DirectionalLight,
    Entity,
    PointLight,
    Text,
    Ursina,
    Vec3,
    application,
    camera,
    color,
    destroy,
    held_keys,
    invoke,
    lerp,
    mouse,
    time,
    window,
)


MONSTERS = {
    "Goblin": {"hp": 70, "damage": 9, "gold": 8, "color": color.rgb32(90, 180, 75)},
    "Giant Goblin": {
        "hp": 150,
        "damage": 16,
        "gold": 18,
        "color": color.rgb32(105, 155, 65),
    },
    "Dragon": {
        "hp": 260,
        "damage": 25,
        "gold": 35,
        "color": color.rgb32(190, 65, 50),
    },
    "Slime": {"hp": 55, "damage": 6, "gold": 6, "color": color.rgb32(65, 210, 170)},
    "Skeleton": {
        "hp": 95,
        "damage": 13,
        "gold": 12,
        "color": color.rgb32(220, 215, 185),
    },
    "Crystal Golem": {
        "hp": 210,
        "damage": 20,
        "gold": 28,
        "color": color.rgb32(95, 185, 235),
    },
    "Cave Bat": {
        "hp": 45,
        "damage": 8,
        "gold": 7,
        "color": color.rgb32(125, 95, 170),
    },
}


def make_creature(name, root, tint):
    def part(model, position, scale, shade=tint, rotation=(0, 0, 0)):
        return Entity(
            parent=root,
            model=model,
            position=position,
            scale=scale,
            color=shade,
            rotation=rotation,
        )

    if name in ("Goblin", "Giant Goblin"):
        size = 1.45 if name == "Giant Goblin" else 1
        part("cube", (0, 1.05 * size, 0), (0.85 * size, 1.05 * size, 0.62 * size))
        part("sphere", (0, 1.9 * size, 0), (0.78 * size, 0.75 * size, 0.7 * size))
        for side in (-1, 1):
            part(Cone(), (side * 0.5 * size, 1.95 * size, 0), (0.28, 0.55, 0.28), rotation=(0, 0, side * -25))
            part("sphere", (side * 0.2 * size, 1.95 * size, 0.33 * size), (0.14, 0.18, 0.1), color.yellow)
            part("cube", (side * 0.25 * size, 0.35 * size, 0), (0.25, 0.75 * size, 0.3))
            part("cube", (side * 0.62 * size, 1.15 * size, 0), (0.25 * size, 0.8 * size, 0.3))
        part("cube", (0, 1.63 * size, 0.35 * size), (0.32 * size, 0.12, 0.1), color.rgb32(45, 35, 25))
    elif name == "Dragon":
        part("sphere", (0, 1.0, 0), (1.1, 1.0, 1.55))
        part("sphere", (0, 1.55, 1.15), (0.65, 0.6, 0.72))
        part(Cone(), (0, 1.42, 1.75), (0.28, 0.65, 0.28), color.rgb32(225, 130, 55), (90, 0, 0))
        for side in (-1, 1):
            part("cube", (side * 0.95, 1.55, -0.1), (1.25, 0.12, 1.05), color.rgb32(125, 40, 45), (0, 0, side * 28))
            part(Cone(), (side * 0.38, 2.12, 1.08), (0.18, 0.58, 0.18), color.rgb32(235, 190, 110), (0, 0, side * 20))
            part("sphere", (side * 0.27, 1.68, 1.63), (0.12, 0.15, 0.09), color.yellow)
        part("cube", (0, 0.8, -1.45), (0.35, 0.38, 1.55), color.rgb32(155, 45, 40), (25, 0, 0))
    elif name == "Slime":
        part("sphere", (0, 0.65, 0), (1.25, 1.0, 1.15))
        for side in (-1, 1):
            part("sphere", (side * 0.27, 0.85, 0.91), (0.13, 0.17, 0.08), color.white)
            part("sphere", (side * 0.27, 0.84, 0.98), (0.06, 0.1, 0.05), color.black)
    elif name == "Skeleton":
        bone = color.rgb32(220, 215, 185)
        part("cube", (0, 1.15, 0), (0.3, 0.95, 0.25), bone)
        part("sphere", (0, 1.95, 0), (0.62, 0.62, 0.58), bone)
        part("cube", (0, 1.64, 0.24), (0.52, 0.12, 0.12), color.rgb32(70, 45, 35))
        for side in (-1, 1):
            part("sphere", (side * 0.19, 2.0, 0.48), (0.1, 0.12, 0.05), color.rgb32(235, 65, 45))
            part("cube", (side * 0.42, 1.25, 0), (0.6, 0.14, 0.15), bone, (0, 0, side * 20))
            part("cube", (side * 0.17, 0.42, 0), (0.14, 0.75, 0.16), bone, (0, 0, side * 8))
    elif name == "Crystal Golem":
        part("cube", (0, 1.05, 0), (1.15, 1.3, 0.8))
        part("cube", (0, 2.05, 0), (0.85, 0.75, 0.7), color.rgb32(140, 225, 255))
        for side in (-1, 1):
            part("cube", (side * 0.82, 1.15, 0), (0.5, 1.2, 0.55), color.rgb32(75, 145, 205), (0, 0, side * 12))
            part(Cone(), (side * 0.23, 2.1, 0.43), (0.13, 0.18, 0.1), color.white)
            part("cube", (side * 0.3, 0.37, 0), (0.38, 0.7, 0.48), color.rgb32(60, 120, 175))
    else:
        part("sphere", (0, 1.1, 0), (0.65, 0.48, 0.6))
        for side in (-1, 1):
            part("cube", (side * 0.72, 1.22, 0), (0.9, 0.12, 0.48), color.rgb32(80, 45, 115), (0, 0, side * 15))
            part(Cone(), (side * 0.23, 1.75, 0.08), (0.16, 0.48, 0.16), color.rgb32(185, 155, 220))
            part("sphere", (side * 0.15, 1.2, 0.5), (0.1, 0.12, 0.07), color.red)


class CrystalCavern:
    def __init__(self):
        window.title = "The Crystal Cavern"
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = False
        window.color = color.rgb32(8, 10, 18)
        window.size = (1280, 720)

        self.hp = 100
        self.max_hp = 100
        self.potions = 3
        self.gold = 10
        self.weapon = "Crystal Katana"
        self.attack_power = 32
        self.defeated = 0
        self.camera_yaw = 0
        self.attack_cooldown = 0
        self.spawn_cooldown = 0
        self.elapsed = 0
        self.message = "Explore the cavern. Watch your back!"
        self.creatures = []
        self.screen_shake = 0.0
        self.flash_timer = 0.0
        self.attack_swing = 0.0

        AmbientLight(color=color.rgb32(115, 120, 155))
        sun = DirectionalLight()
        sun.look_at(Vec3(1, -2, -1))
        self.build_cave()
        self.build_player()
        self.build_merchant()
        self.build_hud()
        self.spawn_creature()

        camera.position = Vec3(0, 5.2, -12.5)
        camera.fov = 68
        camera.look_at(self.player.position + Vec3(0, 1.35, 0))
        mouse.locked = True
        mouse.visible = False

    def build_cave(self):
        floor = Entity(
            model="cube",
            scale=(30, 0.35, 42),
            position=(0, -0.2, 0),
            color=color.rgb32(52, 57, 68),
        )
        floor.texture = "white_cube"
        Entity(model="cube", position=(0, 6.4, 0), scale=(30, 0.55, 42), color=color.rgb32(30, 32, 38))
        for x in (-15, 15):
            Entity(model="cube", position=(x, 3.2, 0), scale=(0.7, 6.4, 42), color=color.rgb32(61, 66, 82))
        for z in (-21, 21):
            Entity(model="cube", position=(0, 3.2, z), scale=(30, 6.4, 0.7), color=color.rgb32(61, 66, 82))

        for _ in range(28):
            x = random.choice((-1, 1)) * random.uniform(8, 13.5)
            z = random.uniform(-18, 18)
            height = random.uniform(1.1, 2.8)
            tint = random.choice(
                (color.rgb32(46, 172, 220), color.rgb32(125, 90, 205), color.rgb32(38, 148, 125))
            )
            Entity(
                model="cube",
                position=(x, height / 2, z),
                scale=(random.uniform(0.3, 0.8), height, random.uniform(0.3, 0.8)),
                rotation=(random.uniform(-12, 12), random.uniform(0, 360), random.uniform(-15, 15)),
                color=tint,
            )

        for x in (-7, 7):
            for z in (-13, 0, 13):
                Entity(
                    model="cube",
                    position=(x, 1.7, z),
                    scale=(0.2, 3.1, 0.2),
                    color=color.rgb32(119, 74, 47),
                )
                flame = Entity(
                    model="sphere",
                    position=(x, 3.3, z),
                    scale=(0.38, 0.62, 0.38),
                    color=color.rgb32(255, 140, 65),
                )
                PointLight(parent=flame, color=color.rgb32(255, 120, 55), position=(0, 0.2, 0), radius=5)

    def build_player(self):
        self.player = Entity(position=(0, 0, -4))
        Entity(
            parent=self.player,
            model="cube",
            position=(0, 1.05, 0),
            scale=(0.65, 1.15, 0.42),
            color=color.rgb32(45, 65, 105),
        )
        Entity(
            parent=self.player,
            model="sphere",
            position=(0, 1.9, 0),
            scale=(0.56, 0.58, 0.52),
            color=color.rgb32(220, 175, 135),
        )
        Entity(
            parent=self.player,
            model="cube",
            position=(0, 2.2, 0),
            scale=(0.66, 0.18, 0.62),
            color=color.rgb32(55, 40, 35),
        )
        for side in (-1, 1):
            Entity(
                parent=self.player,
                model="cube",
                position=(side * 0.23, 0.35, 0),
                scale=(0.22, 0.7, 0.25),
                color=color.rgb32(40, 42, 58),
            )
        self.sword = Entity(
            parent=self.player,
            model="cube",
            position=(0.48, 1.18, 0.32),
            scale=(0.12, 1.05, 0.12),
            rotation=(0, 0, -24),
            color=color.rgb32(145, 225, 255),
        )

    def build_merchant(self):
        self.merchant = Entity(position=(-9, 0, 4))
        Entity(
            parent=self.merchant,
            model="cube",
            position=(0, 1, 0),
            scale=(0.75, 1.2, 0.65),
            color=color.rgb32(150, 100, 55),
        )
        Entity(
            parent=self.merchant,
            model="sphere",
            position=(0, 1.9, 0),
            scale=(0.58, 0.58, 0.55),
            color=color.rgb32(210, 165, 125),
        )
        Entity(
            parent=self.merchant,
            model=Cone(),
            position=(0, 2.32, 0),
            scale=(0.85, 0.75, 0.85),
            color=color.rgb32(70, 125, 95),
        )
        Text(
            parent=self.merchant,
            text="MERCHANT",
            position=(-0.7, 2.8, 0),
            scale=5,
            billboard=True,
            color=color.white,
        )

    def build_hud(self):
        self.background_fog = Entity(
            parent=camera.ui,
            model="quad",
            position=(0, 0, -0.1),
            scale=(2, 2),
            color=color.rgba32(12, 16, 22, 60),
        )
        self.hp_bar_bg = Entity(
            parent=camera.ui,
            model="quad",
            position=(-0.56, 0.46, -0.05),
            scale=(0.38, 0.035),
            color=color.rgba32(25, 28, 30, 160),
        )
        self.hp_bar_fill = Entity(
            parent=camera.ui,
            model="quad",
            position=(-0.56, 0.46, -0.04),
            scale=(0.38, 0.035),
            color=color.rgba32(84, 190, 125, 220),
        )
        self.status_text = Text(
            parent=camera.ui,
            position=(-0.86, 0.45),
            scale=0.9,
            color=color.rgb32(218, 231, 255),
            origin=(0, 0),
        )
        self.message_text = Text(
            parent=camera.ui,
            text=self.message,
            position=(0, -0.38),
            origin=(0, 0),
            scale=1.1,
            background=True,
            color=color.rgb32(245, 245, 245),
        )
        self.message_text.background.color = color.rgba32(20, 20, 26, 170)
        self.flash_overlay = Entity(
            parent=camera.ui,
            model="quad",
            position=(0, 0, 0.5),
            scale=(2, 2),
            color=color.rgba32(255, 255, 255, 0),
        )
        Text(
            parent=camera.ui,
            text="WASD move  |  Mouse look  |  Click/Space attack  |  Q potion  |  E buy potion  |  F upgrade  |  Esc quit",
            position=(0, -0.47),
            origin=(0, 0),
            scale=0.72,
            color=color.rgb32(205, 210, 225),
        )
        Text(
            parent=camera.ui,
            text="+",
            origin=(0, 0),
            position=(0, 0),
            scale=1.2,
            color=color.rgb32(220, 235, 255),
        )

    def spawn_creature(self):
        names = list(MONSTERS)
        weights = (25, 12, 4, 22, 15, 8, 14)
        name = random.choices(names, weights=weights, k=1)[0]
        stats = MONSTERS[name]
        root = Entity(position=(random.uniform(-8, 8), 0, random.uniform(5, 14)))
        make_creature(name, root, stats["color"])
        self.creatures.append(
            {
                "name": name,
                "root": root,
                "hp": stats["hp"],
                "max_hp": stats["hp"],
                "damage": stats["damage"],
                "gold": stats["gold"],
                "attack_timer": 1.0,
            }
        )
        self.message = f"A {name} is stalking you!"

    def update(self):
        dt = time.dt
        self.elapsed += dt
        self.attack_cooldown = max(0, self.attack_cooldown - dt)
        self.spawn_cooldown = max(0, self.spawn_cooldown - dt)
        self.flash_timer = max(0, self.flash_timer - dt)
        self.screen_shake = max(0, self.screen_shake - dt)
        self.camera_yaw += mouse.velocity[0] * 90

        forward = Vec3(math.sin(math.radians(self.camera_yaw)), 0, math.cos(math.radians(self.camera_yaw)))
        right = Vec3(forward.z, 0, -forward.x)
        movement = Vec3(0, 0, 0)
        movement += forward * (held_keys["w"] - held_keys["s"])
        movement += right * (held_keys["d"] - held_keys["a"])
        if movement.length() > 0:
            movement = movement.normalized()
            speed = 7.5 if held_keys["shift"] else 5
            self.player.position += movement * speed * dt
            self.player.rotation_y = math.degrees(math.atan2(movement.x, movement.z))
        self.player.x = max(-13.5, min(13.5, self.player.x))
        self.player.z = max(-20, min(20, self.player.z))

        shake_offset = Vec3(0, 0, 0)
        if self.screen_shake > 0:
            shake = self.screen_shake * 0.16
            shake_offset = Vec3(random.uniform(-shake, shake), random.uniform(-shake, shake) * 0.25, 0)

        camera_target = self.player.position - forward * 7 + Vec3(0, 3.5, 0) + shake_offset
        camera.position = lerp(camera.position, camera_target, min(1, dt * 6))
        camera.look_at(self.player.position + Vec3(0, 1.35, 0))

        for creature in self.creatures:
            root = creature["root"]
            root.y = math.sin(self.elapsed * 3 + root.x) * 0.08
            offset = self.player.position - root.position
            distance = offset.length()
            if distance > 1.8:
                direction = Vec3(offset.x, 0, offset.z).normalized()
                root.position += direction * (1.5 if creature["name"] == "Slime" else 2.0) * dt
                root.rotation_y = math.degrees(math.atan2(direction.x, direction.z))
            else:
                creature["attack_timer"] -= dt
                if creature["attack_timer"] <= 0:
                    self.hp -= creature["damage"]
                    self.screen_shake = 0.35
                    creature["attack_timer"] = 1.35
                    self.message = f"The {creature['name']} hits you for {creature['damage']}!"
                    if self.hp <= 0:
                        self.hp = 0
                        self.message = "You have fallen in the cavern. Press Esc to leave."

        if not self.creatures and self.spawn_cooldown <= 0 and self.hp > 0:
            self.spawn_creature()

        hp_ratio = max(0.02, self.hp / self.max_hp)
        self.hp_bar_fill.scale_x = hp_ratio * 0.38
        self.hp_bar_fill.color = color.rgb32(84, 190, 125) if self.hp > self.max_hp * 0.35 else color.rgb32(215, 120, 65)

        if self.flash_timer > 0:
            alpha = int(max(0, 220 * (self.flash_timer / 0.2)))
            self.flash_overlay.color = color.rgba32(255, 255, 255, alpha)
        else:
            self.flash_overlay.color = color.rgba32(255, 255, 255, 0)

        self.status_text.text = (
            f"THE CRYSTAL CAVERN\n"
            f"HP: {self.hp}/{self.max_hp}\n"
            f"Potions: {self.potions} (Q)\n"
            f"Gold: {self.gold}\n"
            f"Weapon: {self.weapon}\n"
            f"Monsters defeated: {self.defeated}\n"
            f"Nearby: {'Merchant - E to buy, F to upgrade' if self.near_merchant() else ''}"
        )
        self.message_text.text = self.message

    def near_merchant(self):
        return (self.player.position - self.merchant.position).length() < 3.5

    def attack(self):
        if self.hp <= 0 or self.attack_cooldown > 0:
            return
        self.attack_cooldown = 0.45
        self.flash_timer = 0.2
        self.screen_shake = 0.10
        self.sword.rotation = (0, 0, -24)
        self.sword.animate_rotation((0, 0, 70), duration=0.1)
        invoke(self.reset_sword, delay=0.16)
        if not self.creatures:
            self.message = "Your blade cuts through empty air."
            return
        target = min(
            self.creatures,
            key=lambda creature: (creature["root"].position - self.player.position).length(),
        )
        distance = (target["root"].position - self.player.position).length()
        if distance > 3.2:
            self.message = f"Too far away to hit the {target['name']}!"
            return
        target["hp"] -= random.randint(self.attack_power - 5, self.attack_power + 7)
        if target["hp"] <= 0:
            self.gold += target["gold"] + random.randint(1, 8)
            self.defeated += 1
            self.message = f"You defeated the {target['name']}! It dropped some gold."
            destroy(target["root"])
            self.creatures.remove(target)
            self.spawn_cooldown = 1.5
        else:
            self.message = f"You strike the {target['name']}! {target['hp']} HP remain."
            self.screen_shake = 0.18

    def reset_sword(self):
        self.sword.rotation = (0, 0, -24)

    def input(self, key):
        if key == "escape":
            application.quit()
        elif key in ("left mouse down", "space"):
            self.attack()
        elif key == "q":
            if self.potions and self.hp < self.max_hp:
                self.potions -= 1
                restored = min(35, self.max_hp - self.hp)
                self.hp += restored
                self.message = f"You drink a potion and restore {restored} HP."
            elif self.hp == self.max_hp:
                self.message = "Your health is already full."
            else:
                self.message = "You have no potions."
        elif key == "e" and self.near_merchant():
            if self.gold >= 20:
                self.gold -= 20
                self.potions += 1
                self.message = "The merchant sells you a healing potion."
            else:
                self.message = "A potion costs 20 gold."
        elif key == "f" and self.near_merchant():
            if self.weapon == "Iron Broadsword":
                self.message = "You already have the Iron Broadsword."
            elif self.gold >= 50:
                self.gold -= 50
                self.weapon = "Iron Broadsword"
                self.attack_power += 15
                self.message = "Weapon upgraded! Your attacks are stronger."
            else:
                self.message = "The weapon upgrade costs 50 gold."


_game: CrystalCavern | None = None


def update():
    if _game is not None:
        _game.update()


def input(key):
    if _game is not None:
        _game.input(key)


def main():
    global _game
    app = Ursina()
    _game = CrystalCavern()
    app.run()


if __name__ == "__main__":
    main()

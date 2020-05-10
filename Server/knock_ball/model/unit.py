import math

class Unit:
    def __init__(self, unit_id, x, y, is_defense, max_offense_power, max_defense_power, velocity):
        self.unit_id = unit_id
        self.x = x
        self.y = y
        self.is_defense = is_defense
        self.max_offense_power = max_offense_power
        self.max_defense_power = max_defense_power
        self.defense_power = max_defense_power
        self.offense_power = max_offense_power
        self.velocity = velocity
        self.actions = []

    def move_to(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.target_x = target_x
        self.target_y = target_y
        self.x_velocity = velocity * math.cos(angle)
        self.y_velocity = target_y * math.sin(angle)

    def stop(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def update_position(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        if math.abs(self.target_x - self.x) <= math.abs(self.x_velocity / 2) and math.abs(self.target_y - self.y) <= math.abs(self.y_velocity / 2):
            self.x_velocity = 0
            self.y_velocity = 0

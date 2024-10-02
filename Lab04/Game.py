class Item:
    
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self):
        self._ownership = ''
        return f"{self.name} is thrown away."

    def use(self):
        if not self._ownership:
            return f"{self.name} has no owner and cannot be used."
        return f"{self.name} is used."

    def __str__(self):
        return f"Item(name={self.name}, description={self.description}, rarity={self.rarity})"


class Weapon(Item):
    def __init__(self, name, description='', rarity='common', damage=0, weapon_type='sword'):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.active = False
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0

    def equip(self):
        if self._ownership:
            self.active = True
            return f"{self.name} is equipped by {self._ownership}."
        return f"{self.name} cannot be equipped without an owner."

    def use(self):
        if not self.active:
            return f"{self.name} is not equipped and cannot be used."
        return f"{self.name} is used, dealing {self.damage * self.attack_modifier} damage."


class Shield(Item):
    def __init__(self, name, description='', rarity='common', defense=0, broken=False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self.broken = broken
        self.active = False
        self.defense_modifier = 1.10 if rarity == 'legendary' else 1.0
        if broken:
            self.defense_modifier *= 0.5

    def equip(self):
        if self._ownership:
            self.active = True
            return f"{self.name} is equipped by {self._ownership}."
        return f"{self.name} cannot be equipped without an owner."

    def use(self):
        if not self.active:
            return f"{self.name} is not equipped and cannot be used."
        return f"{self.name} is used, blocking {self.defense * self.defense_modifier} damage."


class Potion(Item):
    def __init__(self, name, description='', rarity='common', potion_type='HP', value=0, effective_time=0):
        super().__init__(name, description, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if self.empty:
            return f"{self.name} is empty and cannot be used again."
        if not self._ownership:
            return f"{self.name} has no owner and cannot be used."
        self.empty = True
        return f"{self._ownership} used {self.name}, {self.potion_type} increased by {self.value} for {self.effective_time} seconds."

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type=potion_type, value=50, effective_time=30, rarity='common')


if __name__ == "__main__":
    # Create Weapon object
    belthronding = Weapon(name='Belthronding', rarity='legendary', damage=5000, weapon_type='bow')
    print(belthronding.pick_up('Beleg'))
    print(belthronding.equip())
    print(belthronding.use())

    broken_pot_lid = Shield(name='Wooden Lid', description='A lid made of wood, useful in cooking.', defense=5, broken=True)
    print(broken_pot_lid.pick_up('Beleg'))
    print(broken_pot_lid.equip())
    print(broken_pot_lid.use())
    print(broken_pot_lid.throw_away())
    print(broken_pot_lid.use())

    attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', potion_type='attack')
    print(attack_potion.use())
    print(attack_potion.use())

    print(isinstance(belthronding, Item))
    print(isinstance(broken_pot_lid, Shield))
    print(isinstance(attack_potion, Weapon))

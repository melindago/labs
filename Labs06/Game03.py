import json

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
   
    def __str__(self):
        if self.rarity == 'legendary':
            return f"🌟 {self.name} (Legendary Item) 🌟"
        return f"Item(name={self.name}, description={self.description}, rarity={self.rarity})"

    def to_json(self):
        """Convert Item object to a JSON-encodable dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'rarity': self.rarity,
            'item_type': 'item' 
        }   
    @classmethod
    def from_json(cls, data):
        """Create an Item object from JSON data."""
        try:
            return cls(data['name'], data.get('description', ''), data.get('rarity', 'common'))
        except KeyError as e:
            raise ValueError(f"Missing key in Item data: {e}")

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

    def attack_move(self):
        if self.weapon_type == 'single-handed':
            return self._slash()
        elif self.weapon_type == 'double-handed':
            return self._spin()
        elif self.weapon_type == 'pike':
            return self._thrust()
        elif self.weapon_type == 'ranged':
            return self._shoot()

    def _slash(self):
        return f"{self.name} slashes with {self.damage} damage!"

    def _spin(self):
        return f"{self.name} spins and deals {self.damage} damage!"

    def _thrust(self):
        return f"{self.name} thrusts forward with {self.damage} damage!"

    def _shoot(self):
        return f"{self.name} shoots with {self.damage} damage!"
    
    def to_json(self):
        """Convert Weapon object to a JSON-encodable dictionary."""
        data = super().to_json()
        data.update({
            'damage': self.damage,
            'weapon_type': self.weapon_type,
            'item_type': 'weapon'
        })
        return data
    @classmethod
    def from_json(cls, data):
        """Create a Weapon object from JSON data."""
        try:
            return cls(
                data['name'], 
                data.get('description', ''), 
                data.get('rarity', 'common')
            )
        except KeyError as e:
            raise ValueError(f"Missing key in Weapon data: {e}")
    
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

    def to_json(self):
        """Convert Shield object to a JSON-encodable dictionary."""
        data = super().to_json()
        data.update({
            'defense': self.defense,
            'item_type': 'shield'
        })
        return data

    @classmethod
    def from_json(cls, data):
        """Create a Shield object from JSON data."""
        try:
            return cls(
                data['name'], 
                data.get('description', ''), 
                data.get('rarity', 'common'),
                data.get('defense', 0)
            )
        except KeyError as e:
            raise ValueError(f"Missing key in Shield data: {e}")

class Potion(Item):
    def __init__(self, name, description='', rarity='common', potion_type='HP', value=0, effective_time=0, potency=0):
        super().__init__(name, description, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.empty = False
        self.potency = potency

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

    def to_json(self):
        """Convert Potion object to a JSON-encodable dictionary."""
        data = super().to_json()
        data.update({
            'potency': self.potency,
            'item_type': 'potion'
        })
        return data

    @classmethod
    def from_json(cls, data):
        """Create a Potion object from JSON data."""
        try:
            return cls(
                data['name'], 
                data.get('description', ''), 
                data.get('rarity', 'common'),
                data.get('potency', 0)
            )
        except KeyError as e:
            raise ValueError(f"Missing key in Potion data: {e}")

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

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        item._ownership = self.owner  # Update ownership
        self.items.append(item)
        print(f"{item} added to inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            item._ownership = ''  # Reset ownership
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    def view(self, item_type=None):
        if item_type:
            filtered_items = [item for item in self.items if isinstance(item, Weapon) and item.weapon_type == item_type]
            print(f"Items of type '{item_type}':")
            for item in filtered_items:
                print(item)
        else:
            print("All items in inventory:")
            for item in self.items:
                print(item)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

    def to_json(self):
        """Convert Inventory and its items to a JSON-encodable dictionary."""
        return {
            'items': [item.to_json() for item in self.items]
        }
    @classmethod
    def from_json(cls, data):
        """Create an Inventory object from JSON data."""
        inventory = cls()
        try:
            for item_data in data['items']:
                item_type = item_data.get('item_type')
                if item_data['item_type'] == 'weapon':
                    inventory.add_item(Weapon.from_json(item_data))
                elif item_data['item_type'] == 'item':
                    inventory.add_item(Item.from_json(item_data))
                elif item_type == 'shield':
                    inventory.add_item(Shield.from_json(item_data))
                else:
                    inventory.add_item(Item.from_json(item_data))
        except KeyError as e:
            raise ValueError(f"Missing key in Inventory data: {e}")
        return inventory
    def serialize_to_json(obj, file_path):
        """Serialize custom object to JSON and save to file."""
        with open(file_path, 'w') as file:
           json.dump(obj, file, default=lambda o: o.to_json())


if __name__ == "__main__":
    master_sword = Weapon(name="Master Sword", description="A legendary sword.", rarity="legendary", damage=300, weapon_type="single-handed")
    muramasa = Weapon(name="Muramasa", description="A double-handed katana.", rarity="legendary", damage=580, weapon_type="double-handed")
    gungnir = Weapon(name="Gungnir", description="A legendary spear.", rarity="legendary", damage=290, weapon_type="pike")
    belthronding = Weapon(name="Belthronding", description="A legendary bow.", rarity="legendary", damage=500, weapon_type="ranged")
  
    inventory = Inventory(owner="Beleg")
    inventory.add_item(master_sword)
    inventory.add_item(muramasa)
    inventory.add_item(gungnir)
    inventory.add_item(belthronding)

    print("\n--- Viewing All Items in Inventory ---")
    inventory.view()

    print("\n--- Viewing Single-Handed Weapons in Inventory ---")
    inventory.view(item_type="single-handed")

    print("\n--- Testing Legendary Item Display ---")
    print(master_sword)
    print(muramasa)

    print("\n--- Equipping and Using Items ---")
    print(master_sword.pick_up("Beleg"))
    print(master_sword.equip())
    print(master_sword.use())
    print(master_sword.attack_move())

    print("\n--- Checking Item Existence ---")
    print(f"Is Master Sword in inventory? {master_sword in inventory}")

    print("\n--- Iterating Over Inventory ---")
    for item in inventory:
        if isinstance(item, Weapon):
            print(f"Attacking with {item.name}: {item.attack_move()}")

    inventory.remove_item(muramasa)
    inventory.view()

if __name__ == "__main__":       
    inv = Inventory()
    inv.add_item(Weapon("Sword", "A sharp blade", "rare", 50, "sword"))
    inv.add_item(Potion("Healing Potion", "Restores health", "common", 30))
    inv.add_item(Shield("Iron Shield", "A sturdy shield", "uncommon", 20))
    serialized_inv = json.dumps(inv.to_json())
    print(serialized_inv)
    json_data = json.loads(serialized_inv)
    deserialized_inv = Inventory.from_json(json_data)
    print("\nDeserialized Inventory:\n", deserialized_inv.to_json())

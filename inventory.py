


# inventory
inventory_weapons = []
inventory_armor = []
inventory_loot = []


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None


class AllWeapon:
    def __init__(self):
        self.weapon = str(weapon_mat) + ' ' + str(weapon_type)
        self.ran_mon_wep_mat = random.choice(weapon_mat)
        self.ran_mon_wep_type = random.choice(weapon_type)
        self.mon_wep_dam = (
                (int(weapon_mat.index(self.ran_mon_wep_mat))) + (int(weapon_type.index(self.ran_mon_wep_type))) + 2)
        self.weap_value = int(self.mon_wep_dam / 2)

    def __str__(self):  # description
        return str(self.weapon) + ": Worth" + str(self.weap_value) + "Gold, and does" + str(
            self.mon_wep_dam) + " damage."


class WeaponNode(AllWeapon):
    def __init__(self):
        super(WeaponNode, self)
        super().__init__()
        self.data = self.weapon
        self.prev = None
        self.next = None


class AllArmor:
    def __init__(self):
        self.armor_name = str(armor_mat) + ' ' + str(armor_type)
        self.ran_mon_armor_mat = random.choice(armor_mat)
        self.ran_mon_armor_type = random.choice(armor_type)
        self.armor_points = (
                int(armor_mat.index(self.ran_mon_armor_mat)) + int(armor_type.index(self.ran_mon_armor_type)) + 2 / 2)
        self.mon_armor_worth = int(self.armor_points * 2)

    def __str__(self):  # description
        return str(self.armor_name) + ": Worth" + str(self.mon_armor_worth) + "Gold, and has" + str(
            self.armor_points) + "armor points."


class ArmorNode(AllArmor):
    def __init__(self):
        super(ArmorNode, self)
        super().__init__()
        self.data = self.armor_name
        self.prev = None
        self.next = None


class DropLoot:
    def __init__(self):
        self.monster_bag = monster_name
        self.ran_junk1 = random.choice(junk_loot)
        self.ran_junk2 = random.choice(junk_loot)
        self.ran_treasure = random.choice(treasure_loot)
        self.monster_bag_value = int(int(self.ran_junk1.index + 2) + int(self.ran_junk2.index + 2) + (int(self.ran_treasure.index + 2) * 10))

    def __str__(self):  # description
        return (str(self.monster_bag) + "'s loot") + ": Worth" + str(self.monster_bag_value) + "gold, contains" + str(
            self.ran_junk1) + ", " + str(self.ran_junk2) + ", and" + (str(self.ran_treasure) + ".")


class DropLootNode(DropLoot):
    def __init__(self):
        super(DropLootNode, self)
        super().__init__()
        self.data = self.monster_bag
        self.prev = None
        self.next = None


class Inventory:
    def __init__(self):
        self.head_weapons = inventory_weapons
        self.head_armor = inventory_armor
        self.head_loot = inventory_loot
        self.tail_weapons = inventory_weapons
        self.tail_armor = inventory_armor
        self.tail_loot = inventory_loot

        self.prev_weapons = None
        self.prev_armor = None
        self.prev_loot = None
        self.next_weapons = None
        self.next_armor = None
        self.next_loot = None

    # weapons inventory
    def append_to_inventory_weapons(self, new_weapons):
        if self.head_weapons == None:
            self.head = new_weapons
            self.tail = new_weapons
        else:
            self.tail.next = new_weapons
            new_weapons.prev = self.tail
            self.tail = new_weapons

    def prepend_to_inventory_weapons(self, new_weapons):
        if self.head_weapons == None:
            self.head = new_weapons
            self.tail = new_weapons
        else:
            new_weapons.next = self.head
            self.head.prev = new_weapons
            self.head = new_weapons

    def insert_after_in_inventory_weapons(self, current_weapons, new_weapons):
        if self.head_weapons is None:
            self.head = new_weapons
            self.tail = new_weapons
        else:
            successor_node = current_weapons.next
            new_weapons.next = successor_node
            new_weapons.prev = current_weapons
            current_weapons.next = new_weapons
            if self.tail is current_weapons:
                self.tail = new_weapons
            else:
                successor_node.prev = new_weapons

    def remove_from_inventory_weapons(self, current_weapons):
        predecessor_node = current_weapons.prev
        successor_node = current_weapons.next

        if current_weapons is self.head:
            self.head = successor_node
        else:
            predecessor_node.next = successor_node

        if current_weapons is self.tail:
            self.tail = predecessor_node
        else:
            successor_node.prev = predecessor_node

    def insertion_sort_inventory_weapons(self):
        current_weapons = self.head.next

        while current_weapons != None:
            next_weapons = current_weapons.next
            search_node = current_weapons.prev

            while (search_node != None) and (search_node.data > current_weapons.data):
                search_node = search_node.prev

            self.remove(current_weapons)
            if search_node == None:
                current_weapons.prev = None
                self.prepend_to_inventory_weapons(current_weapons)

            else:
                self.insert_after_in_inventory_weapons(search_node, current_weapons)

            current_weapons = next_weapons

    # armor inventory
    def append_to_inventory_armor(self, new_armor):
        if self.head_armor == None:
            self.head = new_armor
            self.tail = new_armor
        else:
            self.tail.next = new_armor
            new_armor.prev = self.tail
            self.tail = new_armor

    def prepend_to_inventory_armor(self, new_armor):
        if self.head_armor == None:
            self.head = new_armor
            self.tail = new_armor
        else:
            new_armor.next = self.head
            self.head.prev = new_armor
            self.head = new_armor

    def insert_after_in_inventory_armor(self, current_armor, new_armor):
        if self.head_armor == None:
            self.head = new_armor
            self.tail = new_armor
        else:
            successor_node = current_armor.next
            new_armor.next = successor_node
            new_armor.prev = current_armor
            current_armor.next = new_armor
            if self.tail is current_armor:
                self.tail = new_armor
            else:
                successor_node.prev = new_armor

    def remove_from_inventory_armor(self, current_armor):
        predecessor_node = current_armor.prev
        successor_node = current_armor.next

        if current_armor is self.head:
            self.head = successor_node
        else:
            predecessor_node.next = successor_node

        if current_armor is self.tail:
            self.tail = predecessor_node
        else:
            successor_node.prev = predecessor_node

    def insertion_sort_inventory_armor(self):
        current_armor = self.head.next

        while current_armor != None:
            next_armor = current_armor.next
            search_node = current_armor.prev

            while (search_node != None) and (search_node.data > current_armor.data):
                search_node = search_node.prev

            self.remove(current_armor)
            if search_node == None:
                current_armor.prev = None
                self.prepend_to_inventory_weapons(current_armor)

            else:
                self.insert_after_in_inventory_weapons(search_node, current_armor)

            current_armor = next_armor

    # loot inventory
    def append_to_inventory_loot(self, new_loot):
        if self.head_loot == None:
            self.head = new_loot
            self.tail = new_loot
        else:
            self.tail.next = new_loot
            new_loot.prev = self.tail
            self.tail = new_loot

    def prepend_to_inventory_loot(self, new_loot):
        if self.head_weapons == None:
            self.head = new_loot
            self.tail = new_loot
        else:
            new_loot.next = self.head
            self.head.prev = new_loot
            self.head = new_loot

    def insert_after_in_inventory_loot(self, current_loot, new_loot):
        if self.head_loot == None:
            self.head = new_loot
            self.tail = new_loot
        else:
            successor_node = current_loot.next
            new_loot.next = successor_node
            new_loot.prev = current_loot
            current_loot.next = new_loot
            if self.tail is current_loot:
                self.tail = new_loot
            else:
                successor_node.prev = new_loot

    def remove_from_inventory_loot(self, current_loot):
        predecessor_node = current_loot.prev
        successor_node = current_loot.next

        if current_loot is self.head:
            self.head = successor_node
        else:
            predecessor_node.next = successor_node

        if current_loot is self.tail:
            self.tail = predecessor_node
        else:
            successor_node.prev = predecessor_node

    def insertion_sort_inventory_loot(self):
        current_loot = self.head.next

        while current_loot != None:
            next_loot = current_loot.next
            search_node = current_loot.prev

            while (search_node != None) and (search_node.data > current_loot.data):
                search_node = search_node.prev

            self.remove(current_loot)
            if search_node == None:
                current_loot.prev = None
                self.prepend_to_inventory_weapons(current_loot)

            else:
                self.insert_after_in_inventory_weapons(search_node, current_loot)

            current_loot = next_loot

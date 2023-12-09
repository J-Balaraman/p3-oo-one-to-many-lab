class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner='Orphan'):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        Pet.check_pet(self.pet_type)
        Pet.all.append(self)

    @classmethod
    def check_pet(cls, pet_type):
        if pet_type not in cls.PET_TYPES:
            raise ValueError(f"Invalid pet type '{pet_type}'. Allowed types: {', '.join(cls.PET_TYPES)}")

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Invalid pet object provided.")
        
        pet.owner = self
        Pet.all.pop()
        Pet.all.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)

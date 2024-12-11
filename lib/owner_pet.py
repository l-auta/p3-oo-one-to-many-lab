class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    def __init__(self, name, pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type #check if pet is in pet_types
        assert self.pet_type in Pet.PET_TYPES, "Invalid pet type"  # Raise an error if not in PET_TYPES list
        Pet.all.append(self)
        self.owner = owner
        
   

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Add a pet to the owner's list"""
        assert isinstance(pet, Pet), "Argument must be an instance of Pet"
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
from abstract_character import AbstractCharacter


class CharacterManager:
    """ This is the Character Manager class """

    CHARACTER_LABEL = "Server Name"
    ID_LABEL = "ID"

    def __init__(self, server_name):
        """ Constructor - Initialize main attribute of CharacterManager """
        CharacterManager._validate_string_input(
            CharacterManager.CHARACTER_LABEL, server_name)
        if server_name is None or not isinstance(server_name, str):
            raise ValueError("Store Name must be string")

        self._server_name = server_name
        self._next_available_id = int(0)
        self._character_list = []

    def add_character(self, character_obj):
        """ Adds character object to character list if it is not on the list """
        if character_obj is None:
            raise ValueError("Character Object cannot be undefined")
        if character_obj is "":
            raise ValueError("Character Object cannot be empty")

        char_id = []

        for character in self._character_list:
            char_id.append(character.get_id())

        if character_obj.get_id() not in char_id:
            self._next_available_id = self._next_available_id + 1
            character_obj.set_id(self._next_available_id)
            self._character_list.append(character_obj)
        return self._next_available_id

        #     self._character_list.append(character_obj)
        #     character_obj.set(self._next_available_id)

    def character_exists(self, id):
        """ Checks if character already exists in character list """

        CharacterManager._validate_string_input(CharacterManager.ID_LABEL, id)
        CharacterManager._validate_int_id(CharacterManager.ID_LABEL, id)

        for character in self._character_list:
            if character.get_id() == id:
                return True
        return False

    def get(self, id):
        """ get – Takes in an ID and returns that entity object from the list of entities, if it exists. Returns None if it does not exist. """
        for character in self._character_list:
            if character.get_id() == id:
                return character

    def get_all(self):
        """ Returns a list of all characters """
        return self._character_list

    def get_all_by_type(self, character_type):
        """ Returns character list by type """

        if character_type is None or character_type not in ["player", "monster"]:
            raise ValueError(
                "Character_type type must be either player or monster")
        character_type_list = []
        for character in self._character_list:
            if character.get_type() == character_type:
                character_type_list.append(character)
        return character_type_list

    def update_character(self, character_obj):
        """ Update character  Update – Takes in an entity object and replaces the existing entity in the list of entities based on the ID. """

        # Raises an exception if an entity with the same ID does not exist in the list of entities.

        if character_obj is None:
            raise ValueError("Character Object cannot be undefined")
        if character_obj is "":
            raise ValueError("Character Object cannot be empty")

        character_id = character_obj.get_id()

        if self.character_exists(character_id) is False:
            raise Exception("Character ID does not exist")
        for i, character in enumerate(self._character_list, 0):
            if character.get_id() == character_id:
                self._character_list[i] = character_obj
                break

    def delete_character(self, id):
        """ Delete existing character from character list """

        CharacterManager._validate_string_input(
            CharacterManager.ID_LABEL, id)
        CharacterManager._validate_int_id(CharacterManager.ID_LABEL, id)

        for character in self._character_list:
            if character.get_id() == id:
                self._character_list.remove(character)

    def get_server_name(self):
        """ Returns server name """
        # Returns Server Name
        return self._server_name

    @staticmethod
    def _validate_string_input(display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_int_id(display_name, id):
        """ Private helper to validate integer id """
        if type(id) != int:
            raise ValueError(display_name + " needs to be integer")

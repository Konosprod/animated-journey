from rubymarshal.reader import loads, load
from rubymarshal.classes import RubyObject, UserDef, registry
from struct import *
import json

class Tileset(RubyObject):
    ruby_class_name = "RPG::Tileset"

    def tojson(self):

        #Convert from rubmarshalstr to str
        tilesetNames = []
        
        for i in self.attributes["@tileset_names"]:
            tilesetNames.append(str(i))

        todump = {
            "id": self.attributes["@id"],
            "flags": self.attributes["@flags"].flags,
            "mode": str(self.attributes["@mode"]),
            "name": str(self.attributes["@name"]),
            "note": str(self.attributes["@note"]),
            "tilesetNames": tilesetNames
        }

        return json.dumps(todump)

class Table(UserDef):
    ruby_class_name = "Table"
    flags = []
    
    def _load(self, private_data):
        self.flags = list(unpack("@8192H", private_data[0x14:]))
        return



registry.register(Table)
registry.register(Tileset)

blah = ""
with open("Tilesets.rvdata2", "rb") as fd:
    content = load(fd)
    blah = content[1]

for i in content[1:]:
    print(i.tojson())

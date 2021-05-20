# rpgmva2rpgmmz
Convert RPG Maker VX Ace Tileset.rvdata2 to RPG Maker MV/MZ JSON

## How to install

`pip install rpgmva2rpgmmz `

## How to use 

* If you want to generate a whole new json containing all the old tilesets

`rpgmva2rpgmmz Tilesets.rvdata2 -o Tilesets.json`

* If you only want to generated a whole new json containing only the 4th tileset

`rpgmva2rpgmmz Tilesets.rvdata2 -t 4 -o Tilesets.json`

* If you want to append all the old tilesets to the new ones

`rpgmva2rpgmmz Tilesets.rvdata2 -a Tilesets.json`

* If you want to append only the 4th tileset to the new ones

`rpgmva2rpgmmz Tilesets.rvdata2 -a Tilesets.json -t 4`

### Thanks

* [RubyMarshal](https://github.com/d9pouces/RubyMarshal)

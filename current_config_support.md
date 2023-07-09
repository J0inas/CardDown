# Config Files

## Using the config

To use a config with this project, simply pass the path to the config via '-cf path/of/cfg.toml' to the cli.

Alternatively, position the config in the same directory where you have your cards.

## Writing the config
### Format 
We support config files that are written in the .toml format.

#### Toml

Writing [TOML](https://toml.io/en/) is relatively easy:


Comments are initiated with the number sign '#'

```toml
# This is a comment
```

To structure settings into different categories TOMLS tables are pretty neat.
One config file supports multiple Tables. 

```toml
[cool_table]
setting_belonging_to_the_cool_table = "yes"
mango = "ripe"
pi = 3

[new_table]
setting_belonging_to_the_cool_table = "nope"
setting_belonging_to_the_new_table = "yup"
```

More information on TOML can be found [here](https://toml.io/en/)

### Supported Settings

Currently only a few arguments can be written into a config. This will be improved on later.

The following tables and settings are supported:

```toml
[deck]

# name of your output Deck
name = ConfigTest

# Only files containing the deck tag will be processed to learningcards.

tag = ""

# Files that don't contain the start tag also wont be processed

start_tag = ""

# Path where the deck.apkg for anki will be saved

save_path = ""

# Path where the file(s) to your learningcards are located

card_path = ""

```
---
```toml
[parser]

# type of the card syntax/parser
# Currently supported types:
#   simple, block

type = "simple"
```
---
```toml
[media]

# Path where the media files of cards can be found
path = ""

```



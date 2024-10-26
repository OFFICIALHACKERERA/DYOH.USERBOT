

type: entities
show_header_toggle: false
entities:
    # Displays the light entity. It's optional
    - entity: light.example_light

    # Card configuration starts here
    - type: 'custom:rgb-light-card'
      entity: light.example_light
      colors:
          # Any option of the light.turn_on action can be used in each color
          - rgb_color:
                - 255
                - 127
                - 255
            brightness: 220
            transition: 1
          - hs_color:
                - 60
                - 30
            icon_color: '#fff8b0' # Override icon color

# DYOH.USERBOT

## Installation

Clone the repository:
```bash
git clone https://github.com/OFFICIALHACKERERA/DYOH.USERBOT.git
```


```bash
!ls
```


```bash 
!python start.py
```

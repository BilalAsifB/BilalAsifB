import svgwrite

from config import *
from layout import *

from projects import PROJECTS

from renderer import *

dwg = svgwrite.Drawing(

    "output/profile.svg",

    size=(WIDTH,HEIGHT)

)

# Background

dwg.add(

    dwg.rect(

        insert=(0,0),

        size=("100%","100%"),

        fill=BACKGROUND

    )

)

# Title

add_text(

    dwg,

    TITLE,

    WIDTH/2,

    70,

    42,

    "700"

)

# Subtitle

add_text(

    dwg,

    SUBTITLE,

    WIDTH/2,

    110,

    20

)

# Character

add_image(

    dwg,

    CHARACTER["path"],

    CHARACTER_X,

    CHARACTER_Y,

    CHARACTER["width"],

    CHARACTER["height"]

)

# Left

left = [

    PROJECTS[0],

    PROJECTS[2]

]

for i,p in enumerate(left):

    add_project(

        dwg,

        p,

        LEFT_X,

        TOP_Y+i*GAP

    )

# Right

right = [

    PROJECTS[1],

    PROJECTS[3]

]

for i,p in enumerate(right):

    add_project(

        dwg,

        p,

        RIGHT_X,

        TOP_Y+i*GAP

    )

dwg.save()
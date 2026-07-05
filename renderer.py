import base64
import mimetypes
from pathlib import Path

import svgwrite


def _to_data_uri(path):
    p = Path(path)
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def add_text(dwg, text, x, y, size, weight="normal", anchor="middle"):

    dwg.add(

        dwg.text(

            text,

            insert=(x,y),

            text_anchor=anchor,

            font_family="Inter",

            font_size=size,

            font_weight=weight,

            fill="#222"

        )

    )

def add_image(dwg,path,x,y,w,h):

    dwg.add(

        dwg.image(

            href=_to_data_uri(path),

            insert=(x,y),

            size=(w,h)

        )

    )

def add_project(dwg, project, x, y):

    link = dwg.add(

        dwg.a(project["url"], target="_blank")

    )

    link.add(

        dwg.image(

            href=_to_data_uri(project["image"]),

            insert=(x,y),

            size=(260,260)

        )

    )

    link.add(

        dwg.text(

            project["title"],

            insert=(x+130,y+285),

            text_anchor="middle",

            font_family="Inter",

            font_size=24,

            font_weight="600",

            fill="#222"

        )

    )
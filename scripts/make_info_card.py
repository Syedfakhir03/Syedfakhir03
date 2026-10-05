#!/usr/bin/env python3
"""Generate a neofetch-style animated GitHub profile info card.

Each line fades and slides in with a short stagger using CSS keyframes.
STATIC=1 emits a frozen frame.

Usage:
    python scripts/make_info_card.py

Writes:
    info-card.svg
"""

import html
import os


# ─────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────

BG = "#0d1117"
BORDER = "#30363d"

KEY = "#39d353"       # GitHub contribution green
VAL = "#c9d1d9"       # main text
DIM = "#8b949e"       # secondary text
ACCENT = "#58a6ff"    # GitHub blue


# ─────────────────────────────────────────────
# CARD SETTINGS
# ─────────────────────────────────────────────

W = 720
LINE_H = 27
STAGGER = 0.28

TITLE = "syed@github"


# ─────────────────────────────────────────────
# PROFILE INFORMATION
# ─────────────────────────────────────────────

ROWS = [

    ("", ""),

    ("Name", "Syed Fakhar Un Nabi"),

    ("Role", "Data Science • Machine Learning • AI"),

    ("Education", "Monash University — Computer Science (Data Science)"),

    ("GPA", "3.48 / 4.00"),

    ("", ""),

    ("Experience", "Data Science Intern — Kasatria Technologies"),

    ("Built", "BERT NLP • ML Agents • RL • Predictive Models"),

    ("Projects", "Churn • Analytics • Responsible AI • BI Pipelines"),

    ("", ""),

    ("Languages", "Python • R • SQL"),

    ("ML / AI", "TensorFlow • PyTorch • Scikit-learn • BERT"),

    ("Data", "BigQuery • Power BI • Looker Studio • GA4"),

    ("Focus", "NLP • Deep Learning • Reinforcement Learning • MLOps"),

    ("", ""),

    ("GitHub", "@Syedfakhir03"),

    ("LinkedIn", "linkedin.com/in/syed-fakhir"),

]


# Neofetch-style palette
PALETTE = [
    "#ff7b72",
    "#ffa657",
    "#d29922",
    "#39d353",
    "#58a6ff",
    "#bc8cff",
    "#f778ba",
    "#c9d1d9",
]


def main() -> None:

    static = os.environ.get("STATIC") == "1"

    # Calculate dynamic height
    blanks = sum(
        1 for key, value in ROWS
        if not key and not value
    )

    lines = len(ROWS) - blanks

    H = round(
        106
        + blanks * LINE_H * 0.45
        + lines * LINE_H
        + 6
        + 16
        + 24
    )


    # ─────────────────────────────────────────
    # ANIMATION
    # ─────────────────────────────────────────

    anim_css = "" if static else (

        ".ln{"
        "opacity:0;"
        "transform:translateX(-12px);"
        "animation:in .45s ease-out forwards"
        "}"

        "@keyframes in{"
        "to{"
        "opacity:1;"
        "transform:none"
        "}"
        "}"

    )


    # ─────────────────────────────────────────
    # SVG START
    # ─────────────────────────────────────────

    parts = [

        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{W}" '
        f'height="{H}" '
        f'viewBox="0 0 {W} {H}" '
        f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" '
        f'font-size="14">',

        f"<style>{anim_css}</style>",

        # Background
        f'<rect '
        f'x="0.5" '
        f'y="0.5" '
        f'width="{W - 1}" '
        f'height="{H - 1}" '
        f'rx="8" '
        f'fill="{BG}" '
        f'stroke="{BORDER}"/>',

        # macOS / terminal dots
        f'<circle cx="22" cy="21" r="6" fill="#ff5f57"/>'
        f'<circle cx="42" cy="21" r="6" fill="#febc2e"/>'
        f'<circle cx="62" cy="21" r="6" fill="#28c840"/>',

        # Window title
        f'<text '
        f'x="{W / 2:.0f}" '
        f'y="26" '
        f'text-anchor="middle" '
        f'fill="{DIM}">'
        f'{TITLE}'
        f'</text>',

        # divider
        f'<line '
        f'x1="1" '
        f'y1="40" '
        f'x2="{W - 1}" '
        f'y2="40" '
        f'stroke="{BORDER}"/>',

    ]


    # ─────────────────────────────────────────
    # HEADER
    # ─────────────────────────────────────────

    y = 72
    delay = 0.15

    parts.append(

        f'<g class="ln" '
        f'style="animation-delay:{delay:.2f}s">'

        f'<text '
        f'x="24" '
        f'y="{y}" '
        f'fill="{ACCENT}">'
        f'{TITLE}'
        f'</text>'

        f'<text '
        f'x="24" '
        f'y="{y + 16}" '
        f'fill="{DIM}">'
        f'{"-" * len(TITLE)}'
        f'</text>'

        f'</g>'

    )

    y += 34


    # ─────────────────────────────────────────
    # PROFILE ROWS
    # ─────────────────────────────────────────

    for key, val in ROWS:

        delay += STAGGER * 0.55

        # blank spacer
        if not key and not val:

            y += LINE_H * 0.45
            continue


        if key:

            parts.append(

                f'<g '
                f'class="ln" '
                f'style="animation-delay:{delay:.2f}s">'

                f'<text '
                f'x="24" '
                f'y="{y}">'

                f'<tspan '
                f'fill="{KEY}">'
                f'{html.escape(key)}'
                f'</tspan>'

                f'<tspan '
                f'fill="{DIM}">'
                f': '
                f'</tspan>'

                f'<tspan '
                f'x="150" '
                f'fill="{VAL}">'
                f'{html.escape(val)}'
                f'</tspan>'

                f'</text>'

                f'</g>'

            )


        else:

            parts.append(

                f'<g '
                f'class="ln" '
                f'style="animation-delay:{delay:.2f}s">'

                f'<text '
                f'x="150" '
                f'y="{y}" '
                f'fill="{DIM}">'
                f'{html.escape(val)}'
                f'</text>'

                f'</g>'

            )


        y += LINE_H


    # ─────────────────────────────────────────
    # COLOR PALETTE
    # ─────────────────────────────────────────

    delay += 0.30
    y += 6

    sw = 34

    x0 = (
        W - sw * len(PALETTE)
    ) / 2


    blocks = "".join(

        f'<rect '
        f'x="{x0 + i * sw:.0f}" '
        f'y="{y}" '
        f'width="{sw}" '
        f'height="16" '
        f'fill="{color}"/>'

        for i, color in enumerate(PALETTE)

    )


    parts.append(

        f'<g '
        f'class="ln" '
        f'style="animation-delay:{delay:.2f}s">'

        f'{blocks}'

        f'</g>'

    )


    # SVG END
    parts.append("</svg>")


    # ─────────────────────────────────────────
    # WRITE FILE
    # ─────────────────────────────────────────

    with open(
        "info-card.svg",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(parts)
        )


    print(
        "wrote info-card.svg"
    )


if __name__ == "__main__":
    main()
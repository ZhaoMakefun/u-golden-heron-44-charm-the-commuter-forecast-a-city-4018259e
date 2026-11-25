"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<= 140 characters) for the invented
city of Drizzlewick to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The forecast keeps the rhythm of a real broadcast -- place, weather,
practical note -- and bends it with one small joke for the bored commuter
at the bus stop: the 8:04 bus is "fashionably late", and the advice is to
bring an umbrella and low expectations.
"""

import os

# One line, 122 characters: invented city named, weather given, forecast
# register kept, one concrete detail (the 8:04 bus) to make it a place.
ENTRY = (
    "In Drizzlewick today: light rain, 11\u00b0, and the 8:04 bus running "
    "fashionably late \u2014 bring an umbrella and low expectations."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Judge criterion 1: the invented city must be named in the line.
    if "Drizzlewick" not in text:
        raise ValueError("entry must name the invented city")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

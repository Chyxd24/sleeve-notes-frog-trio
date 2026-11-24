import os

TITLE = "Humid"
BLURB = (
    "Recorded live over three Thursdays in the back room of the Bellwater Boathouse, "
    "where the canal fog comes right through the floorboards. Ivo Okafor's alto breathes "
    "more than it plays; Tomas Green bows every note he can; Ruth Adeyemi brushes the "
    "snare soft as a lure on water. They never rehearse. The room does the rest."
)

TEXT = TITLE + "\n\n" + BLURB

def build():
    return TEXT

def char_count():
    return len(TEXT)

if __name__ == "__main__":
    text = build()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(char_count())

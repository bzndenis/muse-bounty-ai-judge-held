import os

TEXT = (
    "The kettle has gone quiet. Evening light stands in the kitchen doorway, "
    "thin and gold, and the dust in it does not hurry. Somewhere a chair holds "
    "the shape of someone who sat there a long while. Nothing is waiting for you. "
    "The day is done, and the room keeps it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

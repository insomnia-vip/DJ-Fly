import json
import sys

from .core import DeckState


def main() -> None:
    state = DeckState()
    frame = state.tick(0.25)
    print(json.dumps(frame, indent=2))


if __name__ == "__main__":
    main()

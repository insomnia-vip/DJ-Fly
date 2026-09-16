from dataclasses import dataclass
from math import sin, tau


@dataclass
class DeckState:
    """Small deterministic state model for a DJ Fly performance."""

    bpm: float = 128.0
    energy: float = 0.72
    groove: float = 0.55

    def tick(self, phase: float) -> dict[str, float]:
        """Return a synthetic performance frame for visual/audio prototypes."""
        beat = (sin(tau * phase) + 1.0) / 2.0
        pulse = 0.5 + 0.5 * beat
        return {
            "bpm": self.bpm,
            "energy": max(0.0, min(1.0, self.energy * (0.8 + 0.2 * pulse))),
            "groove": max(0.0, min(1.0, self.groove + 0.1 * (pulse - 0.5))),
            "pulse": pulse,
        }

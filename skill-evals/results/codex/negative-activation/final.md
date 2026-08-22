```python
import re


def smpte_to_frames(timecode: str, fps: int) -> int:
    """Convert non-drop-frame HH:MM:SS:FF timecode to an absolute frame count."""
    if not isinstance(timecode, str):
        raise TypeError("timecode must be a string")
    if not isinstance(fps, int) or isinstance(fps, bool) or fps <= 0:
        raise ValueError("fps must be a positive integer")

    match = re.fullmatch(r"([0-9]{2}):([0-9]{2}):([0-9]{2}):([0-9]{2})", timecode)
    if not match:
        raise ValueError("timecode must have the form HH:MM:SS:FF")

    hours, minutes, seconds, frames = map(int, match.groups())
    if hours > 23 or minutes > 59 or seconds > 59:
        raise ValueError("hours must be 00–23; minutes and seconds 00–59")
    if frames >= fps:
        raise ValueError(f"frame field must be between 00 and {fps - 1}")

    return ((hours * 60 + minutes) * 60 + seconds) * fps + frames


smpte_to_frames("00:00:10:12", 24)  # 252
smpte_to_frames("01:00:00:00", 30)  # 108000
smpte_to_frames("23:59:59:24", 25)  # 2159999
```

```python
import re

def timecode_to_frames(timecode: str, fps: int) -> int:
    """Convert non-drop-frame HH:MM:SS:FF timecode to an absolute frame count."""
    if not isinstance(fps, int) or isinstance(fps, bool) or fps <= 0:
        raise ValueError("fps must be a positive integer")
    if not isinstance(timecode, str):
        raise TypeError("timecode must be a string")

    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2}):(\d{2})", timecode)
    if not match:
        raise ValueError("timecode must have the form HH:MM:SS:FF")

    hours, minutes, seconds, frames = map(int, match.groups())
    if minutes >= 60 or seconds >= 60:
        raise ValueError("minutes and seconds must be between 00 and 59")
    if frames >= fps:
        raise ValueError(f"frame field must be between 00 and {fps - 1}")

    return ((hours * 3600 + minutes * 60 + seconds) * fps) + frames
```

Examples:

```python
timecode_to_frames("00:00:01:00", 24)  # 24
timecode_to_frames("01:00:00:00", 30)  # 108000
timecode_to_frames("00:01:02:12", 24)  # 1500
```

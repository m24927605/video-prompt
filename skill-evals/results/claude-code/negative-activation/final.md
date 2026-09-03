Since this is a self-contained code question with no files to change, here's the answer directly — nothing to execute or plan.

```python
def timecode_to_frames(tc: str, fps: int) -> int:
    """Convert a non-drop-frame SMPTE timecode 'HH:MM:SS:FF' to a frame count."""
    if not isinstance(fps, int) or fps <= 0:
        raise ValueError(f"fps must be a positive integer, got {fps!r}")
    if not isinstance(tc, str):
        raise TypeError(f"timecode must be a string, got {type(tc).__name__}")

    parts = tc.split(":")
    if len(parts) != 4 or not all(p.isdigit() and len(p) == 2 for p in parts):
        raise ValueError(f"timecode must be 'HH:MM:SS:FF' with two digits per field, got {tc!r}")

    hh, mm, ss, ff = (int(p) for p in parts)
    if mm > 59 or ss > 59:
        raise ValueError(f"minutes and seconds must be 0-59, got {tc!r}")
    if ff >= fps:
        raise ValueError(f"frames field {ff} must be less than fps {fps}")

    return ((hh * 60 + mm) * 60 + ss) * fps + ff
```

Examples:

```python
>>> timecode_to_frames("00:00:01:00", 24)
24
>>> timecode_to_frames("01:00:00:12", 25)   # 1 hour at 25 fps, plus 12 frames
90012
>>> timecode_to_frames("00:01:00:30", 25)   # frames field >= fps
ValueError: frames field 30 must be less than fps 25
```

A couple of notes: `isdigit()` plus the length check rejects negatives, whitespace, and drop-frame separators (`;`), which is correct since drop-frame is explicitly out of scope. Hours aren't capped, so timecodes beyond 24 hours parse fine; add `hh > 23` validation if you need strict SMPTE 24-hour wrapping.

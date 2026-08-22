I'll answer this inline — it's a self-contained snippet, so no files or tool calls are needed.

```python
import re

_NDF_TIMECODE = re.compile(r"([0-9]{2}):([0-9]{2}):([0-9]{2}):([0-9]{2})")


def timecode_to_frames(timecode: str, fps: int) -> int:
    """Convert a non-drop-frame SMPTE timecode 'HH:MM:SS:FF' to a total frame count.

    Raises TypeError/ValueError for bad types, malformed strings, out-of-range
    fields, or drop-frame input (the ';' separator is rejected on purpose).
    """
    if not isinstance(fps, int) or isinstance(fps, bool) or fps <= 0:
        raise ValueError(f"fps must be a positive integer, got {fps!r}")
    if not isinstance(timecode, str):
        raise TypeError(f"timecode must be str, got {type(timecode).__name__}")

    m = _NDF_TIMECODE.fullmatch(timecode)
    if m is None:
        raise ValueError(f"malformed timecode {timecode!r}; expected 'HH:MM:SS:FF'")

    hh, mm, ss, ff = map(int, m.groups())
    if hh > 23 or mm > 59 or ss > 59:
        raise ValueError(f"out-of-range field in {timecode!r}: HH<=23, MM<=59, SS<=59")
    if ff >= fps:
        raise ValueError(f"frame field {ff} must be < fps ({fps}) in {timecode!r}")

    return ((hh * 60 + mm) * 60 + ss) * fps + ff
```

Examples:

```python
timecode_to_frames("01:00:00:00", 24)   # 86400  -> 3600 s * 24
timecode_to_frames("00:01:30:12", 30)   # 2712   -> 90 s * 30 + 12
timecode_to_frames("00:00:10:25", 25)   # ValueError: frame field 25 must be < fps (25)
```

Recap of what it does and the rules it enforces:

- Pure function, stdlib only; returns `((HH*60 + MM)*60 + SS) * fps + FF`.
- Validation: `fps` must be a positive `int` (bools rejected); the string must be exactly four ASCII two-digit fields separated by `:` (so `;` drop-frame form, whitespace, and Unicode digits are all rejected); `MM`/`SS` ≤ 59; `FF` < `fps`.
- One assumption to flag: hours are capped at 23 per SMPTE 12M (timecode wraps at 24 h). If you need to parse durations longer than a day, drop `hh > 23` from the range check — that's the only change required.

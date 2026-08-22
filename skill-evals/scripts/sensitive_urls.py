"""Shared signed-query detection and redaction patterns."""

from __future__ import annotations

import re


SIGNED_QUERY_KEY_PATTERN = (
    r"(?:"
    r"x-amz-(?:algorithm|credential|date|expires|security-token|signature|signedheaders)"
    r"|x-goog-(?:algorithm|credential|date|expires|signature|signedheaders)"
    r"|access_token|key-pair-id|policy|signature|sig|token"
    r")"
)
QUERY_VALUE_PATTERN = r"[^&#\s\"'<>]+"
SIGNED_QUERY_REDACTION_RE = re.compile(
    rf"(?i)([?&]{SIGNED_QUERY_KEY_PATTERN}=){QUERY_VALUE_PATTERN}"
)
SIGNED_QUERY_DETECTION_RE = re.compile(
    rf"(?i)[?&]{SIGNED_QUERY_KEY_PATTERN}="
    rf"(?!<REDACTED>|placeholder|example){QUERY_VALUE_PATTERN}"
)

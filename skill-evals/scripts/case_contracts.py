"""Fail-closed contracts shared by held-out evaluation runners and aggregators."""

from __future__ import annotations

from typing import Any


PACKAGED_SKILLS = (
    "seedance-prompt-director",
    "seedance-film-producer",
    "seedance-video-qc",
    "photography-aesthetics",
    "screenplay-writer",
)
ARCHIVED_BEHAVIORAL_SKILLS = (
    "seedance-prompt-director",
    "seedance-film-producer",
    "seedance-video-qc",
)
ALLOWED_COVERAGE_CLASSES = frozenset({"archived", "integration", "collision"})
ALLOWED_INVOCATION_MODES = frozenset({"explicit", "implicit"})


class CaseContractError(ValueError):
    """Raised when a case cannot participate in a behavioral evaluation."""


class CaseContract:
    __slots__ = ("case_id", "expected_skill", "invocation_mode", "coverage_class", "forbidden_skills")

    def __init__(
        self,
        *,
        case_id: str,
        expected_skill: str | None,
        invocation_mode: str,
        coverage_class: str,
        forbidden_skills: tuple[str, ...],
    ) -> None:
        self.case_id = case_id
        self.expected_skill = expected_skill
        self.invocation_mode = invocation_mode
        self.coverage_class = coverage_class
        self.forbidden_skills = forbidden_skills


def parse_case_contract(case: Any) -> CaseContract:
    if not isinstance(case, dict):
        raise CaseContractError("case must be an object")

    case_id = case.get("id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise CaseContractError("case id must be a non-empty string")

    invocation_mode = case.get("invocation_mode")
    if not isinstance(invocation_mode, str) or invocation_mode not in ALLOWED_INVOCATION_MODES:
        raise CaseContractError("invocation_mode must be explicit or implicit")

    expected_skill = case.get("expected_skill")
    if expected_skill is not None and (
        not isinstance(expected_skill, str) or expected_skill not in PACKAGED_SKILLS
    ):
        raise CaseContractError("expected_skill must be a packaged skill or null")
    if invocation_mode == "explicit" and expected_skill is None:
        raise CaseContractError("explicit case requires expected_skill")

    coverage_class = case.get("coverage_class", "archived")
    if not isinstance(coverage_class, str) or coverage_class not in ALLOWED_COVERAGE_CLASSES:
        raise CaseContractError("coverage_class must be archived, integration, or collision")
    if (
        coverage_class == "archived"
        and expected_skill is not None
        and expected_skill not in ARCHIVED_BEHAVIORAL_SKILLS
    ):
        raise CaseContractError("archived coverage may only expect an archived behavioral skill")

    forbidden_skills = case.get("forbidden_skills", [])
    if not isinstance(forbidden_skills, list) or any(not isinstance(skill, str) for skill in forbidden_skills):
        raise CaseContractError("forbidden_skills must be a list of packaged skill names")
    if len(forbidden_skills) != len(set(forbidden_skills)):
        raise CaseContractError("forbidden_skills must not contain duplicates")
    unknown = sorted(set(forbidden_skills) - set(PACKAGED_SKILLS))
    if unknown:
        raise CaseContractError(f"forbidden_skills are not packaged: {', '.join(unknown)}")
    if expected_skill in forbidden_skills:
        raise CaseContractError("forbidden_skills must not include expected_skill")

    return CaseContract(
        case_id=case_id,
        expected_skill=expected_skill,
        invocation_mode=invocation_mode,
        coverage_class=coverage_class,
        forbidden_skills=tuple(forbidden_skills),
    )

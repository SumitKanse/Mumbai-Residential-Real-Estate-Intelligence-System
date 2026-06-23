"""Ensure runtime artifacts exist (used on cloud deploy where model pkls are not committed)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE_PATH = ROOT / "model" / "pipeline.pkl"


def ensure_model_artifacts() -> bool:
    """Build model files if missing. Returns True when artifacts are ready."""
    if PIPELINE_PATH.exists():
        return True

    from helpers.generate_model_artifacts import build_artifacts

    build_artifacts()
    return PIPELINE_PATH.exists()

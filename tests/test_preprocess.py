import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fakenews.preprocess import clean_text, preprocess, strip_source_prefix


def test_clean_text_removes_html_and_urls():
    raw = "<p>Xin  chào &amp; hẹn gặp</p> https://example.com/abc"
    assert clean_text(raw) == "Xin chào & hẹn gặp"


def test_clean_text_handles_non_string():
    assert clean_text(None) == ""


def test_strip_source_prefix():
    assert strip_source_prefix("WASHINGTON (Reuters) - The senate voted.") == "The senate voted."


def test_preprocess_keeps_text_without_prefix():
    assert preprocess("Bài viết bình thường.") == "Bài viết bình thường."

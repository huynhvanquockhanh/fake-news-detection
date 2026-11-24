"""Tiền xử lý văn bản: làm sạch và loại dấu hiệu rò rỉ nhãn."""
import html
import re
import unicodedata

_TAG = re.compile(r"<[^>]+>")
_URL = re.compile(r"https?://\S+|www\.\S+")
_SPACES = re.compile(r"\s+")
# Ví dụ đầu bài của Reuters: "WASHINGTON (Reuters) - ..."
_SOURCE_PREFIX = re.compile(r"^\s*[A-Z][A-Za-z .,'/-]{1,40}\(Reuters\)\s*[-–—]\s*")


def clean_text(text: str) -> str:
    """Bỏ thẻ HTML, giải mã ký tự đặc biệt, chuẩn hóa Unicode (NFC), gộp khoảng trắng."""
    if not isinstance(text, str):
        return ""
    text = html.unescape(text)
    text = _TAG.sub(" ", text)
    text = _URL.sub(" ", text)
    text = unicodedata.normalize("NFC", text)
    return _SPACES.sub(" ", text).strip()


def strip_source_prefix(text: str) -> str:
    """Bỏ tiền tố tên hãng tin ở đầu bài để mô hình không học 'mẹo' nguồn tin."""
    return _SOURCE_PREFIX.sub("", text, count=1)


def preprocess(text: str, remove_source_prefix: bool = True) -> str:
    text = clean_text(text)
    return strip_source_prefix(text) if remove_source_prefix else text

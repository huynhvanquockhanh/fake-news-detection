"""Kiểm tra môi trường: chạy `python src/check_env.py`."""
import importlib
import platform
import sys

PACKAGES = ["numpy", "pandas", "sklearn", "matplotlib", "torch", "transformers",
            "underthesea", "lime", "shap", "fastapi", "streamlit"]

print(f"Python {sys.version.split()[0]} trên {platform.system()} {platform.release()}")
missing = []
for name in PACKAGES:
    try:
        mod = importlib.import_module(name)
        print(f"  OK    {name:<13} {getattr(mod, '__version__', '')}")
    except Exception as exc:  # noqa: BLE001
        missing.append(name)
        print(f"  THIẾU {name:<13} ({type(exc).__name__})")

try:
    import torch
    print("GPU (CUDA):", "có - " + torch.cuda.get_device_name(0) if torch.cuda.is_available() else "không có, sẽ chạy bằng CPU")
except Exception:  # noqa: BLE001
    pass

print("\nKết quả:", "môi trường đầy đủ." if not missing else "còn thiếu: " + ", ".join(missing))
sys.exit(1 if missing else 0)

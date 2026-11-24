# Hệ thống AI tự động phân loại tin tức giả (Fake News Detection)

Đồ án cơ sở 2 – Khoa Công nghệ thông tin, Trường Đại học Nam Cần Thơ
Sinh viên: Huỳnh Văn Quốc Khánh – MSSV 234899 – Lớp DH23Tin05

Hệ thống phân loại bài viết thành tin đáng nghi hoặc tin ít dấu hiệu đáng ngờ, kèm xác suất và giải thích các từ ảnh hưởng đến kết quả. Kết quả chỉ mang tính tham khảo, không thay thế việc kiểm chứng của con người.

## Cấu trúc thư mục

```
fake-news-detection/
├── data/raw/          # dữ liệu gốc (không đưa lên GitHub)
├── data/processed/    # dữ liệu đã xử lý (không đưa lên GitHub)
├── models/            # mô hình đã huấn luyện (không đưa lên GitHub)
├── notebooks/         # 00 kiểm tra môi trường, 01 khảo sát dữ liệu, ...
├── src/fakenews/      # mã nguồn: tiền xử lý, đặc trưng, mô hình, API
├── tests/             # kiểm thử tự động
├── docs/              # tài liệu, khảo sát dữ liệu
└── requirements.txt
```

## Cài đặt môi trường

Yêu cầu: Python 3.10 trở lên, Git.

Windows (PowerShell):
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/check_env.py
jupyter lab
```

macOS / Linux:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/check_env.py
jupyter lab
```

Lưu ý về `torch`: lệnh trên cài bản mặc định. Nếu có card NVIDIA, xem hướng dẫn cài bản GPU tại trang chủ PyTorch. Nếu máy yếu, huấn luyện PhoBERT/DistilBERT trên Google Colab và chỉ tải mô hình về dùng.

Kiểm thử: `python -m pytest`

## Dữ liệu

Xem `docs/khao_sat_du_lieu.md`. Đặt ISOT vào `data/raw/isot/` (`True.csv`, `Fake.csv`) rồi chạy `notebooks/01_khao_sat_du_lieu.ipynb`.

## Quy ước làm việc với Git

- Nhánh: `main` (bản ổn định), `dev` (đang phát triển), `feature/<tên>` (từng tính năng).
- Thông điệp commit: `loại: mô tả ngắn`, ví dụ `feat: them ham tien xu ly`, `docs: cap nhat khao sat du lieu`, `fix: sua loi tach tu`. Loại thường dùng: feat, fix, docs, test, chore.
- Không commit dữ liệu, mô hình, file `.env`, khóa API.
- Commit nhỏ và thường xuyên, mỗi lần xong một việc.

## Đưa lên GitHub lần đầu

1. Trên github.com tạo repository mới tên `fake-news-detection` (không tick thêm README, .gitignore).
2. Trong thư mục dự án, chạy:
```
git init
git add .
git commit -m "chore: khoi tao du an"
git branch -M main
git remote add origin https://github.com/<ten-tai-khoan>/fake-news-detection.git
git push -u origin main
```
3. Lần đầu có thể phải đăng nhập GitHub hoặc tạo Personal Access Token thay cho mật khẩu.
4. Dán đường link repository vào cột "Sản phẩm đầu ra" của bảng theo dõi.

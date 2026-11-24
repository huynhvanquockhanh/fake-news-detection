# Khảo sát nguồn dữ liệu (G1.3)

Sinh viên: Huỳnh Văn Quốc Khánh – MSSV 234899 – DH23Tin05

## 1. Tổng hợp

| Bộ dữ liệu | Ngôn ngữ | Quy mô | Nhãn | Nguồn / cách tải | Trạng thái |
|---|---|---|---|---|---|
| ISOT Fake News | Tiếng Anh | 44.898 bài (21.417 thật, 23.481 giả) | Thật / giả (hai file True.csv, Fake.csv) | Đại học Victoria: https://www.uvic.ca/ecs/ece/isot/datasets/fake-news/index.php | ☐ Chưa tải |
| LIAR | Tiếng Anh | Khoảng 12,8 nghìn phát biểu ngắn | 6 mức (từ pants-fire đến true), gán bởi PolitiFact | Bài báo Wang (ACL 2017); tải theo hướng dẫn của tác giả | ☐ Chưa tải |
| ReINTEL (VLSP 2020) | Tiếng Việt | Hơn 10.000 tin theo công bố của ban tổ chức | Đáng tin cậy / không đáng tin cậy | https://vlsp.org.vn/vlsp2020, arXiv:2012.08895; có thể phải đăng ký | ☐ Chưa kiểm tra quyền truy cập |

Cập nhật cột "Trạng thái" khi đã tải xong (☑ Đã tải, ngày tải, số dòng thực tế).

## 2. Chi tiết từng bộ

### ISOT
- Cột chính: `title`, `text`, `subject`, `date`.
- Rủi ro: nhiều bài thật có tiền tố tên hãng tin ở đầu bài; cột `subject` thường khác nhau giữa hai lớp. Cả hai là dấu hiệu rò rỉ nhãn, phải kiểm tra bằng notebook `01_khao_sat_du_lieu.ipynb` và loại bỏ trước khi huấn luyện.
- Vai trò: bộ chính để huấn luyện và so sánh mô hình tiếng Anh; dùng cột `date` để chia theo thời gian.

### LIAR
- Phát biểu ngắn, không phải bài báo đầy đủ nên khác phân bố với ISOT.
- Cần quyết định cách gộp 6 nhãn về nhị phân. Đề xuất: {pants-fire, false, barely-true} là giả; {half-true, mostly-true, true} là thật. Nêu rõ quy tắc này trong báo cáo vì kết quả phụ thuộc vào cách gộp.
- Vai trò: bộ kiểm thử chéo (huấn luyện trên ISOT, kiểm tra trên LIAR) để đo khả năng tổng quát.

### ReINTEL
- Dữ liệu mạng xã hội tiếng Việt, có thể kèm thông tin ngoài văn bản (hình ảnh, số liệu tương tác); đề tài chỉ dùng phần văn bản.
- Chỉ số đánh giá của cuộc thi là ROC-AUC.
- Vai trò: bộ chính cho PhoBERT. Nếu không được cấp quyền truy cập, dùng phương án dự phòng ở mục 3.

## 3. Phương án dự phòng cho tiếng Việt
Tự xây dựng tập khoảng 1.000–2.000 bài:
- Tin thật: bài từ các báo chính thống, ghi rõ URL, ngày đăng.
- Tin giả hoặc sai lệch: các nội dung đã được trang kiểm chứng thông tin hoặc cơ quan chức năng đính chính, ghi rõ nguồn kiểm chứng.
- Nhãn được đối chiếu với nguồn kiểm chứng, không tự đoán.
- Tôn trọng `robots.txt` và điều khoản của từng trang; chỉ lưu để nghiên cứu, không phát tán lại nội dung; không lưu thông tin cá nhân.

## 4. Việc cần làm tiếp
- ☐ Tải ISOT, đặt vào `data/raw/isot/`, chạy notebook 01.
- ☐ Xin quyền truy cập ReINTEL, ghi lại ngày gửi yêu cầu và kết quả.
- ☐ Tải LIAR và chốt quy tắc gộp nhãn.
- ☐ Ghi lại điều khoản sử dụng của từng bộ dữ liệu vào bảng ở mục 1.

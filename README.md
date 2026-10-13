# Bài 3: Tối ưu hóa dung lượng Image & Layer Caching với Multi-stage Build

## Giới thiệu
Bài tập này thực hiện việc refactor Dockerfile của ứng dụng Web Backend sang chuẩn Multi-stage Build kết hợp Alpine base image để tối ưu hóa dung lượng và layer caching cho môi trường Production.

## Cấu trúc file
- `Dockerfile.single`: Cấu hình Docker build đơn giai đoạn (dùng làm base so sánh).
- `Dockerfile`: Cấu hình Docker build đa giai đoạn (Multi-stage) sử dụng `node:18-alpine`.
- `server.js` & `package.json`: Mã nguồn ứng dụng Node.js giả lập.
- `main.py`: Script tự động hóa việc build các Docker image.

## Hướng dẫn chạy chương trình
1. Build image đơn:
   ```bash
   docker build -t hw-backend:single -f Dockerfile.single .
   ```
2. Build image multi-stage:
   ```bash
   docker build -t hw-backend:multistage -f Dockerfile .
   ```
3. Hoặc chạy script tự động bằng Python:
   ```bash
   python main.py
   ```

## Bảng so sánh chi tiết
| Image Name | Base Image | Dung lượng ước tính | Số lượng Layer |
|---|---|---|---|
| hw-backend:single | node:18 | ~1.1 GB | 7 |
| hw-backend:multistage | node:18-alpine | < 150 MB | 5 |
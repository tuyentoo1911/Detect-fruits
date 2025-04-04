Detect Fruits - Dự án nhận diện trái cây bằng mô hình học sâu

Giới thiệu

Dự án "Detect Fruits" sử dụng mô hình học sâu dựa trên kiến trúc VGG19 để nhận diện 7 loại trái cây khác nhau từ hình ảnh. Dự án này được phát triển nhằm mục đích học tập và ứng dụng thực tế trong việc phân loại hình ảnh. Dữ liệu được sử dụng bao gồm tập huấn luyện (train) và tập kiểm tra (validation), được lưu trữ trên Google Drive.

Các loại trái cây được nhận diện
- Apple (Táo)
- Banana (Chuối)
- Grape (Nho)
- Kiwi (Kiwi)
- Mango (Xoài)
- Orange (Cam)
- Strawberry (Dâu tây)

Yêu cầu

Để chạy dự án, bạn cần cài đặt các thư viện sau:
- Python 3.x
- TensorFlow
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

Cài đặt các thư viện bằng lệnh:
```bash
pip install tensorflow numpy pandas matplotlib seaborn scikit-learn
```

Ngoài ra, bạn cần kết nối với Google Drive để truy cập dữ liệu và mô hình đã huấn luyện.

Cấu trúc thư mục

Dự án sử dụng dữ liệu và mô hình được lưu trữ trên Google Drive với cấu trúc như sau:
- Dữ liệu:
  - `/content/drive/MyDrive/detect_fruits/database_Fruit/train`: Tập dữ liệu huấn luyện.
  - `/content/drive/MyDrive/detect_fruits/database_Fruit/val`: Tập dữ liệu kiểm tra.
- Mô hình đã huấn luyện**:
  - `/content/drive/MyDrive/vgg19_model.h5`: File mô hình hoàn chỉnh (bao gồm kiến trúc và trọng số).
  - `/content/drive/MyDrive/vgg19.weights.h5`: File trọng số của mô hình.

Cách sử dụng

1. Kết nối Google Drive:
   - Chạy đoạn code sau để mount Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

2. Tải dữ liệu:
   - Dữ liệu được tải tự động từ thư mục `train_dir` và `val_dir` bằng `tf.keras.preprocessing.image_dataset_from_directory`.

3. Tải mô hình:
   - Sử dụng đoạn code sau để tải mô hình đã huấn luyện:
     ```python
     from tensorflow.keras.models import load_model
     model = load_model('/content/drive/MyDrive/vgg19_model.h5')
     ```

4. Dự đoán:
   - Sau khi tải mô hình, bạn có thể sử dụng nó để dự đoán trên dữ liệu mới. Đảm bảo ảnh đầu vào có kích thước `(100, 100)` và định dạng phù hợp.

Link tải dữ liệu và mô hình

- Dữ liệu:
  - [Train Dataset](https://drive.google.com/drive/folders/1mu4qEILdGf3jhjXAIU8X-auifybnAHI7?usp=drive_link)
  - [Validation Dataset](https://drive.google.com/drive/folders/1PD0sy8E3ZCYQg8cm00rWULHaxigrGOiz?usp=drive_link)
  - [Test Dataset](https://drive.google.com/drive/folders/1ObqyqyheL_BSbqJGWjJj5fE1aIK22RnE?usp=drive_link)
- Mô hình:
  - [VGG19 Model](https://drive.google.com/file/d/1rsRfS8ssySS263GoNXqgIeHqZNL6lrfu/view?usp=drive_link)
  - [VGG19 Weights](https://drive.google.com/file/d/1e83WEVNoi2aKof66y73LVNbxdh5Yd8d9/view?usp=drive_link)

*Lưu ý: Hiện tại, các link trên chỉ là placeholder. Bạn cần thay thế bằng các link thực tế từ Google Drive bằng cách chia sẻ thư mục/file với quyền truy cập công khai hoặc giới hạn.*

Kết quả huấn luyện

Dự án sử dụng VGG19 với các tham số sau:
- Kích thước ảnh đầu vào: `(100, 100)`
- Batch size: `32`
- Số epoch: (Tùy thuộc vào cấu hình trong code của bạn, cần bổ sung nếu có thêm thông tin).

Kết quả huấn luyện được thể hiện qua các biểu đồ:
- Độ chính xác (Accuracy): So sánh giữa tập train và validation.
- Hàm mất mát (Loss): So sánh giữa tập train và validation.


import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. --- Định nghĩa đường dẫn ---
# Giả sử folder 'dataset' nằm cùng cấp với file notebook/script
base_dir = 'C:\\Users\\nguye\\Downloads\\dataset'

# 2. --- Đếm file trong từng thư mục con ---
data_counts = {}
class_folders = []

try:
    # Lấy danh sách tất cả các mục trong base_dir
    all_items = os.listdir(base_dir)

    # Lọc ra chỉ những mục là thư mục (folder)
    class_folders = [item for item in all_items if os.path.isdir(os.path.join(base_dir, item))]

    if not class_folders:
        print(f"Lỗi: Không tìm thấy thư mục con nào trong '{base_dir}'.")
        print("Cấu trúc của bạn nên là: dataset/class_A, dataset/class_B, ...")
    else:
        print(f"Đang đếm file trong {len(class_folders)} thư mục con...")

        for folder in class_folders:
            folder_path = os.path.join(base_dir, folder)

            # Đếm số lượng file (không đếm thư mục con nếu có)
            try:
                files_in_folder = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                num_files = len(files_in_folder)
                data_counts[folder] = num_files
            except Exception as e:
                print(f"Lỗi khi đọc thư mục {folder_path}: {e}")

        # 3. --- Sắp xếp dữ liệu để vẽ biểu đồ cho đẹp ---
        if data_counts:
            # Sắp xếp theo số lượng file, từ nhiều nhất đến ít nhất
            sorted_data = sorted(data_counts.items(), key=lambda item: item[1], reverse=True)

            # Tách lại thành 2 danh sách: tên folder và số lượng
            folders = [item[0] for item in sorted_data]
            counts = [item[1] for item in sorted_data]

            # In kết quả ra màn hình
            print("\n--- Thống kê số lượng ảnh ---")
            for folder, count in sorted_data:
                print(f"- {folder}: {count} ảnh")
            print("------------------------------")

            # 4. --- Vẽ biểu đồ ---
            print("Đang tạo biểu đồ...")
            sns.set_style('whitegrid')

            # Tự động điều chỉnh kích thước biểu đồ dựa trên số lượng lớp
            fig_width = max(12, len(folders) * 0.5)  # Tối thiểu 12 inches, thêm 0.5 inch cho mỗi lớp
            plt.figure(figsize=(fig_width, 7))

            # Vẽ biểu đồ
            bar_plot = plt.bar(folders, counts, color='skyblue')

            # Thêm số lượng lên trên mỗi cột
            for bar in bar_plot:
                yval = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2.0, yval, int(yval), va='bottom', ha='center',
                         fontsize=9)  # va='bottom' để số ở trên cột

            # Cấu hình biểu đồ
            plt.title(f'Phân bố số lượng ảnh trong {len(folders)} lớp (Đã sắp xếp)', fontsize=16)
            plt.xlabel('Tên lớp (Folder)', fontsize=12)
            plt.ylabel('Số lượng ảnh', fontsize=12)

            # Xoay tên các lớp ở trục X để dễ đọc nếu có nhiều lớp
            plt.xticks(rotation=60, ha='right')

            # Đảm bảo không bị cắt xén nhãn
            plt.tight_layout()
            plt.show()

            # 5. --- Lưu file ---
            # plot_filename = 'data_distribution_chart.png'
            # plt.savefig(plot_filename)
            # print(f"Đã lưu biểu đồ phân bố dữ liệu vào file: {plot_filename}")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy thư mục '{base_dir}'.")
    print("Vui lòng kiểm tra xem bạn đã đặt tên thư mục chính xác là 'dataset' chưa,")
    print("và nó có nằm cùng cấp với file code đang chạy không.")
except Exception as e:
    print(f"Đã xảy ra một lỗi không mong muốn: {e}")
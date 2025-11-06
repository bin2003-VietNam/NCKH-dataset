import os
import random
from PIL import Image, ImageEnhance

# ===== CẤU HÌNH =====
input_folder = "C:\\Users\\nguye\\Downloads\\dataset"
output_folder = "C:\\Users\\nguye\\Downloads\\dataset_augumented"
os.makedirs(output_folder, exist_ok=True)

AUG_PER_TYPE = 5

# =====  LOẠI AUGMENT =====
AUG_TYPES = {
    "0001": "zoom",
    "0002": "brightness",
    "0003": "contrast",
    "0004": "rotation"
}

# ===== HÀM AUGMENT =====
def apply_augmentation(img_path, aug_type):
    # input
    #     img_path: đường dẫn ảnh
    #     aug_type: loại augument
    # output
    #     ảnh sau khi đã augument

    img = Image.open(img_path).convert("RGB")

    if aug_type == "zoom":
        zoom_factor = random.uniform(0.9, 1.1)
        w, h = img.size
        new_w, new_h = int(w * zoom_factor), int(h * zoom_factor)
        img_zoom = img.resize((new_w, new_h), Image.LANCZOS)

        if zoom_factor > 1.0:  # crop giữa
            left = (new_w - w) // 2
            top = (new_h - h) // 2
            img_zoom = img_zoom.crop((left, top, left + w, top + h))
        else:  # dán vào khung trắng
            new_img = Image.new("RGB", (w, h), (255, 255, 255))
            offset = ((w - new_w) // 2, (h - new_h) // 2)
            new_img.paste(img_zoom, offset)
            img_zoom = new_img
        return img_zoom

    elif aug_type == "brightness":
        enhancer = ImageEnhance.Brightness(img)
        return enhancer.enhance(random.uniform(0.8, 1.2))

    elif aug_type == "contrast":
        enhancer = ImageEnhance.Contrast(img)
        return enhancer.enhance(random.uniform(0.8, 1.2))

    elif aug_type == "rotation":
        angle = random.uniform(-20, 10)
        return img.rotate(angle)

    return img


# ===== CHẠY AUGMENT =====

print(os.listdir(input_folder))
for idx1, folder_name in enumerate(os.listdir(input_folder), start=1):
    class_path = os.path.join(input_folder, folder_name)
    if not os.path.isdir(class_path):
        continue
    class_output_path = os.path.join(output_folder, folder_name)
    os.makedirs(class_output_path, exist_ok=True)

    for idx2, file_name in enumerate(os.listdir(class_path), start=1):
        file_img_path = os.path.join(class_path, file_name)
        base_id = str(idx2).zfill(4)

        # Lặp qua từng loại augment
        for aug_code, aug_name in AUG_TYPES.items():
            for i in range(1, AUG_PER_TYPE + 1):
                aug_img = apply_augmentation(file_img_path, aug_name)
                output_name = f"{base_id}_{aug_code}_{str(i).zfill(4)}.jpg"
                output_path = os.path.join(class_output_path, output_name)
                aug_img.save(output_path, quality=95)

print("Ảnh augment lưu trong:", output_folder)



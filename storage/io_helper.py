import os


def safe_create_dir(path):
    """
    Tạo thư mục an toàn.
    """

    os.makedirs(
        path,
        exist_ok=True
    )
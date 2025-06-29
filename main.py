import os
import re
import sys

def extract_new_filename(old_name: str) -> str:
    name, ext = os.path.splitext(old_name)

    patterns = [
        # Pattern: DJI_20241202184624_0004_D
        (r"DJI_(\d{8})(\d{6})_(\d+_D)", r"\1_\2_\3"),
        # Pattern: dji_export_20241201_164554_1733046354875_editor
        (r"dji_export_(\d{8})_(\d{6})_(\d+)_editor", r"\1_\2_\3"),
        # Pattern: dji_mimo_20241208_122114_0_1733671267689_video/photo
        (r"dji_mimo_(\d{8})_(\d{6})_(\d+)_(\d+)_(video|photo)", r"\1_\2_\3_\4_\5"),
        # Pattern: IMG_0021_20241207_091612_3600
        (r"IMG_\d+_(\d{8}_\d+_\d+)", r"\1"),
        # Pattern: IMG_20210312_123510
        (r"IMG_(\d{8}_\d+)", r"\1"),
        # Pattern: IMG-20241011-WA0018
        (r"IMG-(\d{8}-WA\d+)", r"\1"),
        # Pattern: InShot_20200712_223931821
        (r"InShot_(\d{8}_\d+)", r"\1"),
        # Pattern: PXL_20241002_012903697.MP/.PORTRAIT/.RESTORED/.*
        (r"PXL_(\d{8}_\d+(?:[._~a-zA-Z0-9]*)?)", r"\1"),
        # Pattern: VID_30460119_043828_793
        (r"VID_(\d{8}_\d+_\d+)", r"\1"),
        # Pattern: VID-20241011-WA0034
        (r"VID-(\d{8})-WA(\d+)", r"\1_WA\2"),
        # Pattern: video_20210413_180608
        (r"video_(\d{8}_\d+)", r"\1"),
        # Pattern: VID_112530415_082238_845
        (r"VID_(\d+_\d+_\d+)", r"\1"),
    ]

    for pattern, repl in patterns:
        if re.match(pattern, name):
            return re.sub(pattern, repl, name) + ext

    return old_name

def rename_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            new_name = extract_new_filename(filename)
            new_path = os.path.join(folder_path, new_name)
            if new_name != filename:
                print(f"Renaming: {filename} -> {new_name}")
                os.rename(old_path, new_path)

def preview_rename(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_name = extract_new_filename(filename)
            if new_name != filename:
                print(f"[Preview] {filename} -> {new_name}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py [rename|preview] /path/to/your/folder")
        sys.exit(1)

    command, folder_path = sys.argv[1], sys.argv[2]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    if command == "rename":
        rename_files_in_folder(folder_path)
    elif command == "preview":
        preview_rename(folder_path)
    else:
        print("Unknown command. Use 'rename' or 'preview'.")

if __name__ == "__main__":
    main()

from pathlib import Path
import shutil

SOURCE = Path("garbage_classification")
DEST = Path("Dataset")

CLASS_MAP = {
    "plastic": ["plastic"],
    "paper": ["paper"],
    "metal": ["metal"],
    "glass": ["brown-glass", "green-glass", "white-glass"],
    "organic": ["biological"],
}

for target_class in CLASS_MAP:
    (DEST / target_class).mkdir(parents=True, exist_ok=True)

for target_class, source_folders in CLASS_MAP.items():
    for folder in source_folders:
        source_folder = SOURCE / folder

        for image in source_folder.iterdir():
            if image.is_file():
                shutil.copy2(image, DEST / target_class / image.name)

print("Dataset preparation complete!")
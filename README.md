# 🧹 Filename Renamer

A Python script to **standardize and clean filenames** (especially from WhatsApp, DJI and Pixel) by extracting and formatting timestamps or IDs from filenames.

## 📦 Features

- Renames files like `DJI_20241202184624_0004_D` → `20241202_184624_0004_D`
- Supports multiple filename patterns from:
  - DJI (Drone, Mimo, Export)
  - WhatsApp (IMG, VID)
  - Google Pixel (PXL)
  - InShot
  - Generic exports with embedded timestamps
- Preview mode for dry-run testing
- Command-line interface

## 🚀 Getting Started

### ✅ Requirements

- Python 3.7+

### 📥 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/filename-renamer.git
cd filename-renamer
````

> This project uses only the standard Python library, no additional dependencies required.

## ⚙️ Usage

```bash
python main.py preview /path/to/your/folder
python main.py rename /path/to/your/folder
```

### 🔎 Preview Mode

```bash
python main.py preview ./media
```

### ✏️ Rename Mode

```bash
python main.py rename ./media
```

## 🧠 Supported Patterns

| Original Filename                                      | Renamed Filename                                  |
| ------------------------------------------------------ | ------------------------------------------------- |
| DJI\_20241202184624\_0004\_D                           | 20241202\_184624\_0004\_D                         |
| dji\_export\_20241201\_164554\_1733046354875\_editor   | 20241201\_164554\_1733046354875                   |
| dji\_mimo\_20241130\_132624\_0\_1732948096498\_photo   | 20241130\_132624\_0\_1732948096498\_photo         |
| IMG\_0021\_20241207\_091612\_3600                      | 20241207\_091612\_3600                            |
| IMG\_20210312\_123510                                  | 20210312\_123510                                  |
| IMG-20241011-WA0018                                    | 20241011-WA0018                                   |
| PXL\_20241002\_012903697.MP                            | 20241002\_012903697.MP                            |
| PXL\_20250118\_101811522\_exported\_833\_1737219475340 | 20250118\_101811522\_exported\_833\_1737219475340 |
| VID\_112530415\_082238\_845                            | 112530415\_082238\_845                            |
| VID\_30460119\_043828\_793                             | 30460119\_043828\_793                             |
| VID-20241011-WA0034                                    | 20241011\_WA0034                                  |
| video\_20210413\_180608                                | 20210413\_180608                                  |

## 📂 Folder Structure

```
filename-renamer/
├── main.py           # Main script with CLI support
├── README.md         # This file
└── requirements.txt  # Empty or optional
```

## 📝 License

MIT License. Feel free to use, modify, and share.

## 🙏 Credits

Created by \Rizki Ramadiansyah — for anyone tired of messy camera roll exports 😅.

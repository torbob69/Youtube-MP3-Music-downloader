# 🎵 YouTube MP3 Downloader (Python)

A lightweight command-line tool to **search and download YouTube videos as high-quality MP3 files**. Built for speed, simplicity, and easy customization using **yt-dlp** and **FFmpeg**.

---

## 🚀 Features

* Search YouTube videos directly from the terminal.
* Download audio in **MP3 format**.
* Automatic conversion using **FFmpeg**.
* Supports **batch downloads** (multiple videos at once).
* Optional `.txt` file input for downloading multiple URLs.

---

## 🛠️ Requirements

1. **Python 3.12+**
   Download: [python.org](https://www.python.org/downloads/)
   ⚠️ Ensure Python is added to your system PATH.

2. **FFmpeg**
   Download FFmpeg static build: [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)
   Recommended setup:

   ```
   C:\ffmpeg\bin
   ```

   Add `C:\ffmpeg\bin` to your system **PATH**.

3. **Python Dependencies**
   Inside your project folder:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   pip install yt-dlp requests
   ```

---

## 📁 Project Structure

```
youtube-mp3-downloader/
│
├── main.py            # Main program
├── urls.txt           # (Optional) list of URLs for batch download
├── venv/              # Python virtual environment
└── README.md          # Project documentation
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

### Example session:

```
download path: C:\downloaded music
Search video (or 'n' to stop): kanye west flashing lights
Found: https://www.youtube.com/watch?v=ZAz3rnLGthg
Search video (or 'n' to stop): n
urls: ['https://www.youtube.com/watch?v=ZAz3rnLGthg']
Downloading...
Done!
```

---

## 📄 Batch Download Using .txt File (Optional)

If you want to download multiple videos without searching manually:

1. Create a file `urls.txt` with one URL per line:

```
https://www.youtube.com/watch?v=xxxxx
https://www.youtube.com/watch?v=yyyyy
```

2. Modify your script to load URLs:

```python
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f.readlines()]
```

3. Download will proceed automatically for all URLs in the file.

### Example: Simple Line-by-Line Reader

```python
with open("urls.txt", "r") as file:
    for line in file:
        print("URL:", line.strip())
```

---

## 🔧 Notes

* The downloader runs locally, so **no more annoying website ads**.
* Supports high-quality audio conversion.
* Fully customizable for your workflow.

---

## ⚡ Future Improvements

* Add **GUI interface** for non-terminal users.
* Implement **playlist downloads**.
* Add support for **other audio formats**.

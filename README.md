# sphinx-thai-manual-demo
คู่มือภาษาไทยที่สร้างโดยใช้ Sphinx

## การ build PDF

สิ่งแวดล้อมต้องมี TeX Live, ``latexmk`` และ ``lualatex`` พร้อมฟอนต์ภาษาไทย เช่น ``TH Sarabun New``. ตัวอย่างการติดตั้งบน Debian/Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y texlive-latex-extra texlive-lang-other lmodern fonts-th-sarabun-new latexmk
```

จากนั้นรันคำสั่งเพื่อสร้าง PDF:

```bash
sphinx-build -M latexpdf . _build
```

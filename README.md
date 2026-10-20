# 05 · Human-Computer Interaction — Data Visualization

Tiga praktik HCI untuk visualisasi data dalam satu file:
1. **Sebelum vs sesudah** — pie 7 irisan + warna *jet* → bar terurut, satu warna, label langsung (persepsi lebih akurat).
2. **Simulasi buta warna (deuteranopia)** — palet pelangi vs palet Okabe-Ito.
3. **Cek kontras WCAG** — rasio kontras teks/latar vs ambang AA (4.5:1).

```bash
pip install numpy matplotlib
python hci_visualisasi.py
```
Keluaran: `hci_sebelum_sesudah.png`, `hci_buta_warna.png`, tabel kontras di terminal.

**Catatan:** simulasi buta warna memakai matriks linear aproksimasi (bukan pengganti uji pengguna).

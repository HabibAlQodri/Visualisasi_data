"""HCI & Data Visualization: grafik buruk vs baik, simulasi buta warna, dan cek kontras WCAG."""
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

data = {"YouTube": 34, "WhatsApp": 29, "Instagram": 21, "TikTok": 19, "Facebook": 16, "X": 6, "Telegram": 5}
OKABE = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]

# simulasi deuteranopia (matriks linear aproksimasi)
DEUT = np.array([[.625, .375, 0], [.7, .3, 0], [0, .3, .7]])
def deut(c): return tuple(np.clip(DEUT @ np.array(to_rgb(c)), 0, 1))

# kontras WCAG
def lum(c):
    r = [(v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4) for v in to_rgb(c)]
    return .2126 * r[0] + .7152 * r[1] + .0722 * r[2]
def kontras(a, b):
    l1, l2 = sorted([lum(a), lum(b)], reverse=True); return (l1 + .05) / (l2 + .05)

# Figur 1: sebelum vs sesudah
fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].pie(data.values(), labels=data.keys(), colors=plt.cm.jet(np.linspace(0, 1, len(data))), autopct="%1.0f%%")
ax[0].set_title("SEBELUM: pie 7 irisan + warna jet\n(sulit dibandingkan, tak ramah buta warna)", color="#B00020")
items = sorted(data.items(), key=lambda kv: kv[1]); names, vals = zip(*items)
b = ax[1].barh(names, vals, color="#0072B2")
for r, v in zip(b, vals): ax[1].text(v + .5, r.get_y() + r.get_height() / 2, f"{v}%", va="center")
ax[1].set_title("SESUDAH: bar terurut, 1 warna, label langsung\n(mudah dibandingkan)", color="#006B3C"); ax[1].set_xlim(0, 40)
for s in ("top", "right"): ax[1].spines[s].set_visible(False)
plt.tight_layout(); plt.savefig("hci_sebelum_sesudah.png", dpi=120); plt.close()

# Figur 2: palet normal vs deuteranopia
pal = {"Jet/pelangi": [plt.cm.jet(v) for v in np.linspace(0, 1, 7)], "Okabe-Ito": OKABE}
fig, ax = plt.subplots(2, 2, figsize=(11, 3.6))
for i, (n, cols) in enumerate(pal.items()):
    for j, (t, f) in enumerate([("normal", to_rgb), ("simulasi deuteranopia", deut)]):
        ax[i, j].imshow([[f(c) for c in cols]], aspect="auto"); ax[i, j].axis("off"); ax[i, j].set_title(f"{n} — {t}", fontsize=9)
plt.tight_layout(); plt.savefig("hci_buta_warna.png", dpi=120); plt.close()

print(f"{'teks':>9} {'latar':>9} {'rasio':>6}  WCAG AA (>=4.5)")
for fg, bg in [("#000000", "#FFFFFF"), ("#767676", "#FFFFFF"), ("#AAAAAA", "#FFFFFF"), ("#F0E442", "#FFFFFF"), ("#0072B2", "#FFFFFF"), ("#FFFFFF", "#E69F00")]:
    r = kontras(fg, bg); print(f"{fg:>9} {bg:>9} {r:>6.2f}  {'LULUS' if r >= 4.5 else 'GAGAL'}")
print("\nGrafik: hci_sebelum_sesudah.png, hci_buta_warna.png")

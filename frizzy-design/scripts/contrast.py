#!/usr/bin/env python3
"""WCAG 2.2 contrast ratios for design tokens.

Usage:
  python3 contrast.py "#1E1B16:#F6F1E8" "#B3391A:#FFFFFF"      # foreground:background pairs
  python3 contrast.py --check "#1E1B16:#F6F1E8" --min 4.5       # exit 1 if any pair is below --min

Thresholds: 4.5 for body text, 3.0 for large text and UI components such as borders and focus rings.
"""
import argparse
import sys


def luminance(hex_color):
    h = hex_color.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="+", help="foreground:background hex pairs")
    ap.add_argument("--min", type=float, default=None, help="fail if any ratio is below this value")
    ap.add_argument("--check", action="store_true", help="exit 1 when --min is not met")
    args = ap.parse_args()

    failed = False
    for pair in args.pairs:
        try:
            fg, bg = pair.split(":")
            r = ratio(fg, bg)
        except ValueError:
            print(f"Bad pair '{pair}'. Use foreground:background, for example '#111111:#FFFFFF'.", file=sys.stderr)
            return 2
        note = ""
        if args.min is not None and r < args.min:
            note = f"  below {args.min}"
            failed = True
        print(f"{fg} on {bg}: {r:.2f}:1{note}")
    return 1 if (failed and args.check) else 0


if __name__ == "__main__":
    sys.exit(main())

import argparse
from rembg import remove
from PIL import Image, ImageChops, ImageOps


def grayscale_with_alpha(img: Image.Image) -> Image.Image:
    gray = ImageOps.grayscale(img.convert("RGB")).convert("RGBA")
    _, _, _, alpha = img.split()
    gray.putalpha(alpha)
    return gray


def get_fg(img_path: str) -> Image.Image:
    original = Image.open(img_path).convert("RGBA")
    fg = remove(original)
    return grayscale_with_alpha(fg)


def get_bg(img_path: str) -> Image.Image:
    original = Image.open(img_path).convert("RGBA")
    fg = remove(original)
    _, _, _, alpha = fg.split()
    inverted_alpha = ImageChops.invert(alpha)

    bg = Image.composite(
        original, Image.new("RGBA", original.size, (0, 0, 0, 0)), inverted_alpha
    )
    return grayscale_with_alpha(bg)


def resize_fg(fg: Image.Image, bg: Image.Image) -> Image.Image:
    bg_w, bg_h = bg.size
    fg_w, fg_h = fg.size

    scale = min(bg_w / fg_w, bg_h / fg_h)
    new_size = (int(fg_w * scale), int(fg_h * scale))
    return fg.resize(new_size)


def merge(fg: Image.Image, bg: Image.Image) -> Image.Image:
    bg_w, bg_h = bg.size
    fg_w, fg_h = fg.size

    x = (bg_w - fg_w) // 2
    y = (bg_h - fg_h) // 2

    bg.paste(fg, (x, y), fg)
    return bg


def main():
    parser = argparse.ArgumentParser(
        description="Compose images with Carleton Blueprint Design."
    )
    parser.add_argument(
        "image_path", help="Path to the main image (for fg and bg extraction)"
    )
    parser.add_argument(
        "streak_bg_path", help="Path to the background streak image (color)"
    )
    parser.add_argument(
        "streak_fg_path",
        nargs="?",
        default=None,
        help="Optional path to the front streak image (color)",
    )
    parser.add_argument(
        "-o", "--output", default="out.png", help="Output filename (default: out.png)"
    )
    args = parser.parse_args()

    streak_bg = Image.open(args.streak_bg_path).convert("RGBA")
    fg = get_fg(args.image_path)
    bg = get_bg(args.image_path)

    streak_bg = resize_fg(streak_bg, bg)
    back = merge(streak_bg, bg)
    final = merge(fg, back)

    if args.streak_fg_path:
        streak_fg = Image.open(args.streak_fg_path).convert("RGBA")
        streak_fg = resize_fg(streak_fg, final)
        final = merge(streak_fg, final)

    final.save(args.output)
    print(f"Saved output to {args.output}")


if __name__ == "__main__":
    main()

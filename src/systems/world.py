"""World map: water detection, collision, water depth."""

from io import BytesIO

import requests
from PIL import Image

from src.config import BASE_URL


def load_map(width, height, path="assets/images/backgrounds/beach.png"):
    """Download the background image and resize it to the screen dimensions.

    Returns (PIL.Image, pixel-access) so callers can sample pixels for
    water/land detection.
    """
    img = Image.open(
        BytesIO(requests.get(BASE_URL + path).content)
    ).convert("RGB")
    img = img.resize((width, height))
    return img, img.load()


def is_water(map_img, map_pixels, x, y):
    img_x = int(x)
    img_y = map_img.height - 1 - int(y)

    if (
        img_x < 0
        or img_y < 0
        or img_x >= map_img.width
        or img_y >= map_img.height
    ):
        return True

    r, g, b = map_pixels[img_x, img_y]
    return b > r and b > g


def is_blocked(map_img, map_pixels, x, y):
    points = [
        (0, 0),
        (10, 0), (-10, 0),
        (0, 10), (0, -10),
        (10, 10), (-10, 10),
        (10, -10), (-10, -10),
    ]

    for ox, oy in points:
        if is_water(map_img, map_pixels, x + ox, y + oy):
            return False

    return False


def water_depth(map_img, map_pixels, x, y, max_dist=60):
    """Distance from (x, y) to the nearest land tile (capped at max_dist)."""
    for dist in range(0, max_dist, 4):
        for dx in range(-dist, dist + 1, 4):
            for dy in range(-dist, dist + 1, 4):
                check_x = x + dx
                check_y = y + dy
                if not is_water(map_img, map_pixels, check_x, check_y):
                    return dist

    return max_dist

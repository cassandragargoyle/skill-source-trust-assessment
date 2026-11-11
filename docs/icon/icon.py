#!/usr/bin/env python3
"""Generate the icon of the source-trust-assessment skill as SVG.

The icon is the network of the CassandraGargoyle mark (a C of five nodes, the first
node green) around a green shield with a check mark: trust, established by sources.
Sizes and colours follow the mark in the `api` repository (`brand/mark.py`); keep them
in sync when the mark changes.

Usage:
    python3 docs/icon/icon.py > docs/icon/icon.svg
    magick -background none docs/icon/icon.svg -depth 8 .claude-plugin/icon.png
"""

from __future__ import annotations

import math
import sys

# shared with api/brand/mark.py
GREEN = "#76B900"
GRAPHITE = "#1A1A1A"
LIGHT = "#F2F2F2"
SIZE = 1024
CENTRE = SIZE / 2
NETWORK_RADIUS = 290
NODE_RADIUS = 58
EDGE_WIDTH = 36
NODE_ANGLES = (50, 115, 180, 245, 310)

# the shield inside the network
SHIELD_CENTRE_X = CENTRE + 20
SHIELD_WIDTH = 260
SHIELD_HEIGHT = 310
CHECK_SIZE = 120


def fmt(value: float) -> str:
    """Number without needless decimals"""
    return f"{value:.1f}".rstrip("0").rstrip(".")


def circle(x: float, y: float, r: float, fill: str) -> str:
    return f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}" fill="{fill}"/>'


def edge(a: tuple[float, float], b: tuple[float, float], width: float, fill: str) -> str:
    """Straight edge with round ends as filled shapes (renders the same everywhere)"""
    dx, dy = b[0] - a[0], b[1] - a[1]
    length = math.hypot(dx, dy)
    px, py = -dy / length * width / 2, dx / length * width / 2
    points = [(a[0] + px, a[1] + py), (b[0] + px, b[1] + py), (b[0] - px, b[1] - py), (a[0] - px, a[1] - py)]
    return f'<path d="M{" L".join(f"{fmt(x)} {fmt(y)}" for x, y in points)} Z" fill="{fill}"/>'


def network() -> tuple[str, list[tuple[float, float]]]:
    nodes = [(CENTRE + NETWORK_RADIUS * math.cos(math.radians(a)),
              CENTRE - NETWORK_RADIUS * math.sin(math.radians(a))) for a in NODE_ANGLES]
    parts = [edge(a, b, EDGE_WIDTH, LIGHT) for a, b in zip(nodes, nodes[1:])]
    parts += [circle(x, y, NODE_RADIUS, GREEN if i == 0 else LIGHT) for i, (x, y) in enumerate(nodes)]
    return "".join(parts), nodes


def shield(cx: float, cy: float, w: float, h: float, fill: str) -> str:
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - h / 2, cy + h / 2
    return (f'<path d="M{fmt(cx)} {fmt(y0)} L{fmt(x1)} {fmt(y0 + h * 0.16)} V{fmt(cy)} '
            f'C{fmt(x1)} {fmt(cy + h * 0.3)} {fmt(cx + w * 0.2)} {fmt(y1 - h * 0.06)} {fmt(cx)} {fmt(y1)} '
            f'C{fmt(cx - w * 0.2)} {fmt(y1 - h * 0.06)} {fmt(x0)} {fmt(cy + h * 0.3)} {fmt(x0)} {fmt(cy)} '
            f'V{fmt(y0 + h * 0.16)} Z" fill="{fill}"/>')


def check(cx: float, cy: float, s: float, fill: str) -> str:
    width = s * 0.32
    a, b, c = (cx - s * 0.55, cy), (cx - s * 0.15, cy + s * 0.4), (cx + s * 0.6, cy - s * 0.38)
    return (edge(a, b, width, fill) + edge(b, c, width, fill)
            + "".join(circle(x, y, width / 2, fill) for x, y in (a, b, c)))


def icon() -> str:
    body, nodes = network()
    body += shield(SHIELD_CENTRE_X, CENTRE, SHIELD_WIDTH, SHIELD_HEIGHT, GREEN)
    body += check(SHIELD_CENTRE_X, CENTRE + 5, CHECK_SIZE, GRAPHITE)
    # optical centring: the network opens to the right, so centre its bounding box
    left = min(x for x, _ in nodes) - NODE_RADIUS
    right = max(max(x for x, _ in nodes) + NODE_RADIUS, CENTRE + 200)
    shift = CENTRE - (left + right) / 2
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" width="{SIZE}" height="{SIZE}" '
            f'role="img" aria-label="source-trust-assessment">'
            f'<title>source-trust-assessment</title>'
            f'<rect width="{SIZE}" height="{SIZE}" rx="200" fill="{GRAPHITE}"/>'
            f'<g transform="translate({fmt(shift)} 0)">{body}</g></svg>\n')


if __name__ == "__main__":
    sys.stdout.write(icon())

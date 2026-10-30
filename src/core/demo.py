"""Demo data so the app can be explored without real TikTok accounts."""

import time
from datetime import datetime, timedelta

from src.core.stats_store import StatsStore

DEMO_ACCOUNTS = (
    ("demo.studio", "demo"),
    ("demo.daily", "demo"),
    ("demo.archive", "archive"),
)


def load_demo(db) -> int:
    """Create demo accounts, publication history and statistics. Idempotent."""
    for username, tag in DEMO_ACCOUNTS:
        db.save_account(username, f"tiktok_session-{username}.cookie", tag=tag)

    now = datetime.now()
    rows = (
        ("demo.studio", "ok", "launch-reel.mp4", "Launch day", None, 12),
        ("demo.daily", "ok", "launch-reel.mp4", "Launch day", None, 26),
        ("demo.archive", "error", "launch-reel.mp4", "Launch day", "session is invalid", 41),
        ("demo.studio", "ok", "second-clip.mp4", "Second clip", None, 58),
    )
    for username, status, video, caption, error, minutes_ago in rows:
        db.log_upload(username, status, video_path=video, caption=caption, error=error)
        db.execute(
            "UPDATE upload_log SET created_at = ? WHERE id = (SELECT MAX(id) FROM upload_log)",
            ((now - timedelta(minutes=minutes_ago)).strftime("%Y-%m-%d %H:%M:%S"),),
        )

    store = StatsStore(db)
    created = int(time.time()) - 7200
    demo = (
        ("demo.studio", "demo.studio", 18420, 312),
        ("demo.daily", "demo.daily", 9310, 148),
        ("demo.archive", "demo.archive", 4120, 61),
    )
    for username, handle, followers, plays in demo:
        base = {
            "handle": handle,
            "nickname": handle,
            "user": {"followers": followers, "following": 120, "likes": 4500, "videos": 24},
            "items": [{"id": "730000000000000001", "desc": "Launch day · demo clip",
                       "createTime": created, "plays": plays, "likes": plays // 12,
                       "comments": plays // 90, "shares": plays // 60, "saves": plays // 40,
                       "duration": 18}],
        }
        store.save_snapshot(username, base)
        base["user"]["followers"] = followers + 120
        base["items"][0]["plays"] = plays + 860
        store.save_snapshot(username, base)

    db.set("upload_delay", 30)
    db.set("randomize_variants", True)
    db.set("randomize_intensity", "medium")
    return len(DEMO_ACCOUNTS)

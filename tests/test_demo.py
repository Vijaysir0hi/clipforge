import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.database import Database
from src.core.demo import load_demo
from src.core.stats_store import StatsStore


def test_demo_seeds_accounts_history_and_stats():
    with tempfile.TemporaryDirectory() as tmp:
        db = Database(os.path.join(tmp, "demo.db"))
        count = load_demo(db)
        assert count == 3
        assert len(db.get_accounts()) == 3
        assert len(db.get_upload_log(10)) >= 4
        store = StatsStore(db)
        assert len(store.latest_accounts()) == 3
        assert len(store.latest_videos()) == 3
        assert db.get("randomize_variants") is True


def test_demo_is_idempotent():
    with tempfile.TemporaryDirectory() as tmp:
        db = Database(os.path.join(tmp, "demo.db"))
        load_demo(db)
        load_demo(db)
        assert len(db.get_accounts()) == 3
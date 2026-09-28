
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from housing.build import Furniture, Housing


def test_place_checks_aabb_collision():
    h = Housing()
    f1 = Furniture("table1", 0, 0, 2, 2)
    f2 = Furniture("table2", 1, 1, 2, 2)
    assert h.place(f1) == True
    assert h.place(f2) == False


def test_rotate_updates_collision_box():
    h = Housing()
    f = Furniture("chair", 0, 0, 1, 2)
    h.place(f)
    h.rotate("chair")
    assert f.w == 2
    assert f.h == 1


def test_remove_returns_materials():
    h = Housing()
    h.materials = {"wood": 0}
    f = Furniture("table", 0, 0, 1, 1)
    f.cost = {"wood": 3}
    h.place(f)
    h.remove("table")
    assert h.materials["wood"] > 0


def test_storage_guest_cannot_take():
    h = Housing()
    h.storage["owner"] = ["sword"]
    result = h.access_storage("guest", "sword", take=True)
    assert result == None
    assert "sword" in h.storage["owner"]


def test_storage_owner_can_take():
    h = Housing()
    h.storage["owner"] = ["sword"]
    result = h.access_storage("owner", "sword", take=True)
    assert result == "sword"


def test_interact_range_by_furniture_size():
    big = Furniture("wardrobe", 0, 0, 3, 3)
    small = Furniture("chair", 0, 0, 1, 1)
    assert big.interact_range > small.interact_range


def test_save_includes_position_and_rotation():
    h = Housing()
    f = Furniture("table", 5, 3, 2, 2, rotation=90)
    h.place(f)
    data = h.save()
    assert data[0]["x"] == 5
    assert data[0]["rotation"] == 90


def test_load_restores_full_state():
    h = Housing()
    data = [{"fid": "table", "x": 5, "y": 3, "w": 2, "h": 2, "rotation": 90}]
    h.load(data)
    assert h.furniture[0].x == 5
    assert h.furniture[0].rotation == 90

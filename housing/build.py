
class Furniture:
    def __init__(self, fid, x, y, w, h, rotation=0):
        self.fid = fid
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rotation = rotation
        self.interact_range = 2.0


class Housing:
    def __init__(self):
        self.furniture = []
        self.materials = {"wood": 10, "stone": 5}
        self.storage = {"owner": [], "guest": []}
        self.layout = []

    def place(self, furniture):
        # BUG: 只检查格子是否为空，不检查碰撞
        for f in self.furniture:
            if f.x == furniture.x and f.y == furniture.y:
                return False
        self.furniture.append(furniture)
        return True

    def rotate(self, fid):
        for f in self.furniture:
            if f.fid == fid:
                f.rotation = (f.rotation + 90) % 360
                # BUG: 碰撞盒不跟着转
                return True
        return False

    def remove(self, fid):
        for i, f in enumerate(self.furniture):
            if f.fid == fid:
                self.furniture.pop(i)
                # BUG: 不返还材料
                return True
        return False

    def access_storage(self, role, item=None, take=False):
        # BUG: 访客能拿东西
        if take:
            if item in self.storage["owner"]:
                self.storage["owner"].remove(item)
                return item
        return self.storage["owner"]

    def save(self):
        # BUG: 只存ID不存旋转和位置
        return [f.fid for f in self.furniture]

    def load(self, data):
        self.furniture = [Furniture(fid, 0, 0, 1, 1) for fid in data]

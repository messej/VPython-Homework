import visual
import const

class Scene:
    def __init__(self):
        self.objects = set()
        self.sf = {}
        self.fields = {}
    def add_obj(self, ob):
        self.objects.add(ob)
    def add_sf(self, key, sf):
        pass

class PointObj(visual.sphere):
    def __int__(self, scene = None, **kwargs):
        super().__init__(**kwargs)
        self.arrs = {}
        if scene is not None:
            self.scene = scene
            self.scene.add_obj(self)
    def __getitem__(self,key):
        return super().__getattribute__(key)
    def make_arr(self,key,**kwargs):
        arr = arrow(**kwargs)
        arr.axis = self[key]*self.scene.sf[key]
        self.arrs[key] = arr
    def update(self, deltat):
        #update self
        for force in self.scene.fields:
            f += force(self, self.scene)
        self.p   += deltat*f
        self.pos += deltat*self.p/self.m
        #update arrs
        for key,value in self.arrs.items():
            pass

def test():
    s = Scene()
    a = PointObj(pos=vector(0,0,0),color=color.red, visible=False, scene = s, q =5)
    print(a.q)
    print(hasattr(a,'q'))
    #a.prin()
    print(a['q'])
    #print(s.objects)
    #print(a.scene)
if __name__ == "__main__":
    test()

import numpy as np
import fcl


g1 = fcl.Box(2,2,2)
trans = np.array([0, 0.0, 0.0])
t1 = fcl.Transform(trans)
print("g1:", id(g1))
o1 = fcl.CollisionObject(g1, t1)

b = fcl.Box(2,2,2)
trans = np.array([3, 0.0, 0.0])
t = fcl.Transform(trans)
print("b:", id(b))
o = fcl.CollisionObject(b, t)

g3 = fcl.Box(2,2,2)
trans = np.array([7, 0.0, 0.0])
t3 = fcl.Transform(trans)
print("g3:", id(g3))
o5 = fcl.CollisionObject(g3, t3)



# request = fcl.CollisionRequest()
# result = fcl.CollisionResult()

objs1 = [o1, o5, o]

req = fcl.CollisionRequest(num_max_contacts=100, enable_contact=True)
rdata = fcl.CollisionData(request = req)
manager1 = fcl.DynamicAABBTreeCollisionManager()
manager1.registerObjects(objs1)
manager1.setup()

##distance
ddata = fcl.DistanceData()
manager1.distance(ddata, fcl.defaultDistanceCallback)
print ('Closest distance within manager 1?: {}'.format(ddata.result.min_distance))
names, data = None, None
names = (id(ddata.result.o1),id(ddata.result.o2))
print(names)
##distance


manager1.collide(o, rdata, fcl.defaultCollisionCallback)
print ('Collision between manager 1 and Mesh?: {}'.format(rdata.result.is_collision))
print ('Contacts:')
objs_in_collision = set()
contact_data = []
print("target id: ", id(b))
print("g1 id: ", id(g1))
print("g3 id: ", id(g3))
dict = {}
dict[id(b)]="target id"
dict[id(g1)]="g1 id"
dict[id(g3)]="g3 id"
for contact in rdata.result.contacts:
    cg = contact.o1
    if cg == b:
        cg = contact.o2
    name = dict[id(cg)]
    names = (name, '__external')
    if cg == contact.o2:
        names = reversed(names)
    objs_in_collision.add(name)
    # contact_data.append(ContactData(names, contact))
print(objs_in_collision)
# manager1 = fcl.DynamicAABBTreeCollisionManager()
# manager1.registerObjects(objs1)
# manager1.setup()
# cdata = fcl.CollisionData()
# manager1.collide(cdata, fcl.defaultCollisionCallback)

# ddata = fcl.DistanceData()
# manager1.distance(ddata, fcl.defaultDistanceCallback)
# print ('Closest distance within manager 1?: {}'.format(ddata.result.min_distance))


# print(cdata)
# print ('Collision within manager 1?: {}'.format(cdata.result.is_collision))
# print ('Collision times manager 1?: {}'.format(len(cdata.result.contacts)))
# ret = cdata.result
# print(ret)

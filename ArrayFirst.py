# _______________________________________________________Example of Array Properties______________________________________________
import numpy as np
# a=np.array((1,2),(4,5),dtype=np.float32)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)

# _______________________________________________________Example of np.ones______________________________________________
# a=np.ones((4,2),dtype=np.int32)
# print(a)

# _______________________________________________________Example of np.zeros______________________________________________
# a=np.zeros((6,2),dtype=np.int32)
# print(a)

# _______________________________________________________Example of np.arange______________________________________________
# a=np.arange(1,10)
# print(a)

# _______________________________________________________Example of np.concatinate______________________________________________
# a=np.ones((2,4))
# b=np.zeros((1,4))
# x=np.concatenate([a,b])
# print(x)

# _______________________________________________________Example of np.astype______________________________________________
# a=np.array([[1.1,1.2,1.3,1.4,1.5]
#     [2.1,2.2,2.3,2.4,2.5]],dtype=np.float32)

# _______________________________________________________Example of np.zeros_like______________________________________________
# a=np.ones((2,2),dtype=np.int32)
# b=np.zeros_like(a)
# print(b.shape)

# _______________________________________________________Example of np.ones_like______________________________________________
# a=np.zeros((2,2),dtype=np.int32)
# b=np.ones_like(a)
# print(b.shape)
# print(a)

# _______________________________________________________Example of np.random.random______________________________________________
# a=np.random.random((5,4))
# print(a)

# _______________________________________________________Example of np.reshape______________________________________________
# a=np.array([1,2,3,4,5,6])
# # a=a.reshape(3,2)
# a=a.reshape(2,-1)
# a=a.ravel()
# print(a)

# _______________________________________________________Example of Transposition______________________________________________
# a=np.arange(10).reshape(5,2)
# print(a)
# a=a.T
# # a=a.transpose((1,0))
# print(a)

# _______________________________________________________Example of Mathematical Operator_________________________________________
# a=np.array([1,2,3])
# b=np.array([4,4,10])
# c=a*b
# print(c)

# _______________________________________________________Example of Logical Operator______________________________________________
# a=np.array([[5,6,7,2,3,-6]],dtype=bool)
# a>5
# print(a)

# _______________________________________________________Example of Operator______________________________________________
# a=np.array([[4,15],[20,75]])
# b=np.array([[2,5],[5,15]])
# a//=b
# print(a)

# _____________________________________________________Math,Universal Function______________________________________________
# _______________________________________________________Example of np.isnan______________________________________________
# a=np.nan
# b=20
# print(np.isnan(a))
# print(np.isnan(b))

# _______________________________________________________Example of sin,cos function______________________________________________
# angles=np.array([0,30,45,60,90,180])
# radians=np.deg2rad(angles)
# print("Sine of Angles in the Array")
# sine_value=np.sin(radians)
# # print(sine_value)
# print(np.sin(radians))
# print("Inverse Sine of Sine Values")
# print(np.rad2deg(np.arcsin(sine_value)))

# _______________________________________________________Example of hyperbolic sine______________________________________________
# angles=np.array([0,30,45,60,90,180])
# radians=np.deg2rad(angles)
# print(np.sinh(radians))

# _______________________________________________________Example of hypot function______________________________________________
base=4
height=3
print("Hypotenuse of Right Triangle is")
print(np.hypot(base,height))
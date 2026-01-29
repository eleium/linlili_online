# function,函数。定义同一性质的事件，完成某一特定的通用的作用。避免复读机
# function(传入的参数)
#
#
# central_angle_1=160#以圆心为顶点，两个半径为边的 中心角，圆心角。
# radius_1=30#半径
# # sector_area_1=((3.14*radius_1**2)/360)*central_angle_1
# sector_area_1=central_angle_1/360*(3.14*radius_1**2)
# print(f'这个扇形的面积是：{sector_area_1:.3f}')
# #以上是计算一个扇形的面积的过程。

# 这个计算公式中的通用部分，可以命名为一个函数，以后就可以方便的调用了
# 用 def 定义 函数名，（）括号内是要传入的参数，冒号结束
def calculate_sector_area(central_angle, radius):
    # 接下来是一下定义函数的代码（注意缩进）
    # central_angle = 160  # 这两行可以不用了，可以移除，因为上面的参数已经存在
    # radius = 30          # 这两行不用写，可以移除。因为上面参数可以传入具体的数值。
    sector_area = central_angle / 360 * (3.14 * radius ** 2)  # 具体的函数计算方式
    print(f'这个扇形的面积是：{sector_area}')


# 此时，函数calculate_sector_area被定义完成。但是要调用它，它才开始执行。
calculate_sector_area(180, 30)  # calculate:计算的意思


# 此时，就可以传入具体的圆心角的角度和半径，直接运行，就可以执行了。
# 从12行到24行时一个完整的、定义一个扇形面积的函数、传入圆心角和半径参数，然后执行的一段程序：

def calculate_sector_area(central_angle, radius):
    sector_area = central_angle / 360 * (3.14 * radius ** 2)
    print(f'这个扇形的面积是：{sector_area:.4f}')
calculate_sector_area(180, 30)

import xml.etree.ElementTree as ET
from utils.utils import get_classes
import os
import matplotlib.pyplot as plt
import numpy as np

from utils.utils_map import adjust_axes

"""
type45 = "i2,i4,i5,il100,il60,il80,io,ip,p10,p11,p12,p19,p23,p26,p27,p3,p5,p6,pg,ph4,ph4.5,ph5,pl100,pl120,pl20,pl30,pl40,pl5,pl50,pl60,pl70,pl80,pm20,pm30,pm55,pn,pne,po,pr40,w13,w32,w55,w57,w59,wo"
type45 = type45.split(',')

type45_chinese = "非机动车行驶,机动车行驶,靠右侧道路行驶,最低限速100km/h,最低限速60km/h,最低限速80km/h,其他指示标志,人行横道,禁止机动车驶入,禁止鸣喇叭,禁止摩托车驶入,禁止右转弯,禁止左转弯,禁止载货汽车驶入,禁止运输危险物品车辆驶入,禁止大型客车驶入,禁止掉头,禁止非机动车进入,减速让行,限高4m,限高4.5m,限高5m,限速100km/h,限速120km/h,限速20km/h,限速30km/h,限速40km/h,限速5km/h,限速50km/h,限速60km/h,限速70km/h,限速80km/h,限重20t,限重30t,限重55t,禁止停车,禁止驶入,其他禁令标志,解除限速40km/h,十字交叉路口,施工,注意儿童,注意行人,注意右方合流,其他警告标志"
type45_chinese = type45_chinese.split(',')

dict_chinese = dict(zip(type45, type45_chinese))

print(dict_chinese['pne'])
"""

def draw_plot_func1(dictionary1, dictionary2, n_classes, window_title, plot_title, x_label, output_path, to_show, plot_color, true_p_bar):
    # sort the dictionary by decreasing value, into a list of tuples
    #sorted_dic_by_value = sorted(dictionary.items(), key=operator.itemgetter(1))
    # unpacking the list of tuples into two lists
    sorted_keys1, sorted_values1 = zip(*dictionary1.items())
    sorted_keys2, sorted_values2 = zip(*dictionary2.items())
    bar_width = 0.4
    plt.barh(np.arange(n_classes), sorted_values1, bar_width, label="YOLOX-s", color=plot_color)
    plt.barh(np.arange(n_classes) + bar_width, sorted_values2, bar_width, label="YOLOX-s+CBAM", color="c", alpha = 0.9)
    """
     Write number on side of bar
    """
    fig = plt.gcf() # gcf - get current figure
    axes = plt.gca()
    r = fig.canvas.get_renderer()
    for i, val in enumerate(sorted_values1):
        str_val = " " + str(val) # add a space before
        if val < 1.0:
            str_val = " {0:.3f}".format(val)
        t = plt.text(val, i, str_val, color=plot_color, va='center', fontweight='bold', fontsize=9)
        # re-set axes to show number inside the figure
        if i == (len(sorted_values1)-1): # largest bar
            adjust_axes(r, t, fig, axes)
    for i, val in enumerate(sorted_values2):
        str_val = " " + str(val) # add a space before
        if val < 1.0:
            str_val = " {0:.3f}".format(val)
        t = plt.text(val, i+bar_width , str_val, color="c", va='center', fontweight='bold', alpha = 0.9, fontsize=9)
        # re-set axes to show number inside the figure
        if i == (len(sorted_values2)-1): # largest bar
            adjust_axes(r, t, fig, axes)
    # set window title
    # set window title
    fig.canvas.set_window_title(window_title)
    # write classes in y axis
    tick_font_size = 12
    plt.yticks(range(n_classes), sorted_keys1, fontsize=tick_font_size)
    plt.yticks(np.arange(n_classes) + bar_width / 2)
    """
     Re-scale height accordingly
    """
    init_height = fig.get_figheight()
    # comput the matrix height in points and inches
    dpi = fig.dpi
    height_pt = n_classes * (tick_font_size * 1.4) # 1.4 (some spacing)
    height_in = height_pt / dpi
    # compute the required figure height
    top_margin = 0.05 # in percentage of the figure height
    bottom_margin = 0.0 # in percentage of the figure height
    figure_height = 1.6*height_in / (1 - top_margin - bottom_margin)
    # set new height
    if figure_height > init_height:
        fig.set_figheight(figure_height)

    # set plot title
    plt.title(plot_title, fontsize=14)
    # set axis titles
    # plt.xlabel('classes')
    plt.xlabel(x_label, fontsize='large')
    # adjust size of window
    fig.tight_layout()
    # save the plot
    fig.savefig(output_path)
    # show image
    plt.legend()
    if to_show:
        plt.show()
    # close the plot
    plt.close()

"""
type45 = "i2,i4,i5,il100,il60,il80,io,ip,p10,p11,p12,p19,p23,p26,p27,p3,p5,p6,pg,ph4,ph4.5,ph5,pl100,pl120,pl20,pl30,pl40,pl5,pl50,pl60,pl70,pl80,pm20,pm30,pm55,pn,pne,po,pr40,w13,w32,w55,w57,w59,wo"
type45 = type45.split(',')

xs = "92.93%,95.95%,98.64%,100.00%,99.51%,98.20%,93.87%,94.70%,93.60%,94.59%,90.29%,91.28%,94.76%,96.55%,94.59%,97.79%,97.54%,84.14%,93.86%,90.61%,92.02%,96.05%,98.33%,98.41%,92.25%,98.25%,97.71%,98.39%,95.17%,96.79%,93.72%,94.98%,99.44%,100.00%,98.80%,97.11%,96.65%,82.67%,97.44%,96.91%,80.53%,94.53%,98.17%,90.23%,33.81%"
xs = xs.split(',')
xsc = "95.15%,95.83%,98.49%,100.00%,99.96%,99.02%,95.22%,96.13%,94.38%,95.91%,90.58%,95.83%,95.22%,97.22%,98.52%,99.04%,99.40%,86.24%,91.21%,90.83%,95.27%,96.16%,98.57%,99.93%,97.36%,98.75%,98.42%,99.32%,96.64%,98.54%,94.75%,96.28%,100.00%,100.00%,98.22%,97.57%,98.35%,85.66%,97.44%,99.03%,84.79%,99.17%,99.29%,96.95%,52.52%"
xsc = xsc.split(',')
xsl = "0.141,0.076,0.014,0.000,0.000,0.000,0.136,0.099,0.108,0.089,0.157,0.148,0.105,0.057,0.000,0.007,0.046,0.257,0.016,0.121,0.143,0.092,0.033,0.016,0.137,0.006,0.036,0.007,0.084,0.057,0.093,0.074,0.000,0.000,0.000,0.036,0.055,0.364,0.026,0.001,0.328,0.063,0.001,0.026,0.801"
xsl = xsl.split(',')
xscl = "0.092,0.079,0.013,0.000,0.000,0.000,0.127,0.075,0.086,0.062,0.172,0.108,0.094,0.000,0.000,0.000,0.000,0.213,0.002,0.178,0.089,0.010,0.020,0.000,0.008,0.020,0.022,0.000,0.051,0.030,0.075,0.039,0.000,0.000,0.001,0.023,0.023,0.295,0.026,0.000,0.270,0.000,0.000,0.001,0.623"
xscl = xscl.split(',')

for i, a in enumerate(xsc):
    a = '%.3f' % (float(a.strip('%')) / 100.0)
    xsc[i] = float(a)
for i, a in enumerate(xs):
    a = '%.3f' % (float(a.strip('%')) / 100.0)
    xs[i] = float(a)
for i, a in enumerate(xsl):
    a = '%.3f' % (float(a))
    xsl[i] = float(a)
for i, a in enumerate(xscl):
    a = '%.3f' % (float(a))
    xscl[i] = float(a)

dict_xs = dict(zip(type45, xsl))
dict_xsc = dict(zip(type45, xscl))
window_title = "mAP"
#x_label = "Average Precision"
x_label = "log-average miss rate"
to_show = True
plot_color = 'royalblue'
draw_plot_func1(
    dict_xs,
    dict_xsc,
    len(type45),
    window_title,
    "",
    x_label,
    "",
    to_show,
    plot_color,
    ""
    )
"""

"""
with open("epoch_loss.txt") as f:
    lines = f.readlines()
    losses = []  # 直接用一个数组存起来就好了
    for line in lines:
        losses.append(float(line.split()[0]))

with open("epoch_val_loss.txt") as f:
    lines = f.readlines()
    val_loss = []  # 直接用一个数组存起来就好了
    for line in lines:
        val_loss.append(float(line.split()[0]))

iters = range(1, 101)


plt.figure()
plt.plot(iters, losses, 'red', linewidth=2, label='train loss')
plt.plot(iters, val_loss, 'coral', linewidth=2, label='val loss')

plt.grid(True)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc="upper right")

plt.savefig(os.path.join("epoch_loss.png"))
"""
"""
classes_path = 'model_data/traffic_sign_classes.txt'
classes, _ = get_classes(classes_path)

VOCdevkit_path = 'D:/TT100k/VOCdevkit'
VOCdevkit_sets = [('2007', 'train'), ('2007', 'test')]

small = 0
middle = 0
big = 0

def count(year, image_id):
    global small
    global middle
    global big
    in_file = open(os.path.join(VOCdevkit_path, 'VOC%s/Annotations/%s.xml' % (year, image_id)), encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult') != None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        xmlbox = obj.find('bndbox')
        if((int(float(xmlbox.find('xmax').text)) - int(float(xmlbox.find('xmin').text)))
                * (int(float(xmlbox.find('ymax').text)) - int(float(xmlbox.find('ymin').text))) < 32 * 32):
            small += 1
        elif((int(float(xmlbox.find('xmax').text)) - int(float(xmlbox.find('xmin').text)))
                * (int(float(xmlbox.find('ymax').text)) - int(float(xmlbox.find('ymin').text))) < 96 * 96):
            middle += 1
        else:
            big += 1
        print("small:" + str(small))
        print("middle:" + str(middle))
        print("big:" + str(big))

for year, image_set in VOCdevkit_sets:
    image_ids = open(os.path.join(VOCdevkit_path, 'VOC%s/ImageSets/Main/%s.txt' % (year, image_set)),
                     encoding='utf-8').read().strip().split()
    for image_id in image_ids:
        count(year, image_id)
print("small:" + str(small))
print("middle:" + str(middle))
print("big:" + str(big))
"""

sales=[9775,11741,1666]

company_names=["small objects:9775","middle objects:11741","large objects:1666"]


com_colors=["lavender","pink","aqua"]

_, _, p_text = plt.pie(sales,

colors=com_colors,

startangle=90,

shadow=True,

autopct="%1.2f%%",

explode=(0.1,0.05,0),

wedgeprops=dict(edgecolor='black')
)

for t in p_text:
    t.set_size(10.5)

plt.legend(company_names, loc=1)
plt.show()
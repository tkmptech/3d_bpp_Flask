from .py3dbp.constants import Task
from .py3dbp import Bin, Item, Packer
from .py3dbp import bin_items_show
import time
import json
import decimal


start = time.perf_counter()

class DecimalEncoder(json.JSONEncoder):
    # python dict类型转换为json字符串时，需要把decimal类型转换成float类型
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

def react_post_json(json_data):
# with open('test_json(2)/test_json/5output_test.json', 'r', encoding='GBK') as fp:
#     json_data = json.load(fp)

    packerlist = json_data['order list']
    binlist = json_data['cargo box list']

    for jsbin in binlist:        # 遍历货箱列表
        bin_attr = jsbin['Cargo box attributes']
        bin_num = jsbin['Available quantity']
        bin = Bin(bin_attr['Cargo box model'], bin_attr['Cargo box type'], eval(bin_attr['weight']), eval(bin_attr['length']), eval(bin_attr['width']),
                eval(bin_attr['height']))
        for i in range(eval(bin_num)):
            Task.Bins.append(bin)

    for jspacker in packerlist:          # 遍历订单
        packer_name = jspacker['Order number']
        packer_id = jspacker['Order ID']
        jsitems = jspacker['Goods collection']

        packer = Packer(packer_name, packer_id)

        for jsitem in jsitems:
            load_limits = jsitem['packing limit']
            dirct_limit = []
            load_or_not = [0, 0, 0, 0, 0, 0]
            load_limit = [20, 20, 20, 20, 20, 20]
            stack_limit = [0, 0, 0, 0, 0, 0]
            for limit in load_limits:
                if limit['Placement direction'] == 'Standing forward':
                    dirct_limit.append(0)
                    load_limit[0] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[0] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[0] = eval(limit['Number of stacking layers'])
                elif limit['Placement direction'] == 'Vertical horizontal':
                    dirct_limit.append(1)
                    load_limit[1] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[1] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[1] = eval(limit['Number of stacking layers'])
                elif limit['Placement direction'] == 'Sideways forward':
                    dirct_limit.append(3)
                    load_limit[3] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[3] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[3] = eval(limit['Number of stacking layers'])
                elif limit['Placement direction'] == 'Sideways horizontal':
                    dirct_limit.append(2)
                    load_limit[2] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[2] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[2] = eval(limit['Number of stacking layers'])
                elif limit['Placement direction'] == 'Lying forward':
                    dirct_limit.append(5)
                    load_limit[5] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[5] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[5] = eval(limit['Number of stacking layers'])
                elif limit['Placement direction'] == 'Lying forward':
                    dirct_limit.append(4)
                    load_limit[4] = eval(limit['Load-bearing level'])
                    if limit['Is it load-bearing surface?'] == 'yes':
                        load_or_not[4] = 1
                    if limit['Stacking restrictions'] == 'yes':
                        stack_limit[4] = eval(limit['Number of stacking layers'])

            item = Item(packer_name, jsitem['product name'], jsitem['Kit Code'], jsitem['Cargo code'], jsitem['Cargo Model'], jsitem['weight'],
                        jsitem['volume'],
                        jsitem['length'], jsitem['width'], jsitem['height'], dirct_limit, load_limit, stack_limit, load_or_not)

            packer.items.append(item)

        Task.Packers.append(packer)
        del packer


    num_bin = len(Task.Bins)

    for packer in Task.Packers:
        for i in range(num_bin):
            if packer.pack(i+1,False,False) == 0:
                break


    # 结果输出
    i = 1   # 装箱步骤计数
    output = {
    'Boxing steps': []
    }
    output_3d = {
    'Box': []
    }
    for bin in Task.Used_bins:
        hua = []
        totalvol = bin.get_total_vol()
        print('Container utilization')
        print(totalvol / bin.get_volume())
        bin.items.sort(key=lambda x: (x.position[0], x.position[1], x.position[2]))
        itemsinfo = []
        for item in bin.items:
            item_info = []
            info = {
            'Packing steps': 'steps'+str(i),
            'Order number': item.packer_name,
            'Cargo box number': bin.name,
            'Cargo coordinates': item.position
            }
            output['Packing steps'].append(info)
            i += 1

            pos = (float(item.position[0]), float(item.position[1]), float(item.position[2]))
            item_info.append(pos)
            dimension = item.get_dimension()
            item_info.append(float(dimension[0]))
            item_info.append(float(dimension[1]))
            item_info.append(float(dimension[2]))

            item_info = tuple(item_info)
            itemsinfo.append(item_info)
        info_3d = {
        'Cargo box length': bin.width,
        'Cargo box width': bin.depth,
        'Cargo box height': bin.height,
        'Cargo box cargo': itemsinfo
        }
        output_3d['box'].append(info_3d)

        # bin_items_show.item_show(bin.width, bin.depth, bin.height, itemsinfo)


    jsondata = json.dumps(output, cls=DecimalEncoder, ensure_ascii=False)
    with open('output1.json', 'w', encoding='utf-8') as fp:
        fp.write(jsondata)
        fp.close()


    jsondata3d = json.dumps(output_3d, cls=DecimalEncoder, ensure_ascii=False)
    with open('output_3d.json', 'w', encoding='utf-8') as fp:
        fp.write(jsondata3d)
        fp.close()

    end = time.perf_counter()
    print('Program running time: %s' % (end-start))

    # return hua








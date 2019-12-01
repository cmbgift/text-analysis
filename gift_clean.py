import pandas as pd
data=pd.ExcelFile("Gift2.xlsx").parse("Sheet4")
SKU_INTRODUCE=list(data["SKU_INTRODUCE"])
SKU_SIZE=list(data["SKU_SIZE"])

# for item  in SKU_INTRODUCE:
#     arr=str(item).strip().split("\n")
#     for i in arr:
#         if "：" in i :
#             if len(i.split("："))==2:
#                 k=i.split("：")[0].strip()
#                 v=i.split("：")[1].strip()
#                 if len(k)>15:continue
#                 if v=="":continue
#                 v=i.split("：")[1].strip()
#                 sku.update({k:v})

product_intro=[ '送礼对象', '适用星座','适合节日', '适用生肖', '功能', '适用场景',
'适用人群','适用人数','产品定位','使用场景','适用季节','适用范围','适用对象',
'功能用途','适合年龄','年龄范围','目标对象','年龄组','适合年龄','【适用年龄】',
'功能场景','应用场景']
product_size=['适用人群','适用场景','适用对象']
def filter_intro(x):
    arr=str(x).strip().split("\n")
    sku={}
    for i in arr:
        if "：" in i :
            if len(i.split("："))==2:
                k=i.split("：")[0].strip()
                v=i.split("：")[1].strip()
                if len(k)>15:continue
                if v=="":continue
                v=i.split("：")[1].strip()
                if k in product_intro:
                    sku.update({k:v})
    return sku
def filter_size(x):
    sku={}
    arr=str(x).splitlines()
    if len(arr)<2:return {}
    for i in range(len(arr)):
        if str(arr[i]).strip() in product_size:
            try:
                sku.update({str(arr[i]).strip():str(arr[i+1]).strip()})
            except:
                pass
    return sku

data['SKU_INTRODUCE_CLEAN']=data['SKU_INTRODUCE'].apply(filter_intro)
data['SKU_SIZE_CLEAN']=data['SKU_SIZE'].apply(filter_size)
data.to_excel("Gift2_clean.xlsx")
# print(sku)
# print(list(sku.keys()))
# for item  in SKU_SIZE:
#     # print(len(str(item)))
#     print(str(item).splitlines())
#     print(len(str(item).splitlines()))

#     arr=str(item).strip().split("\n")
#     for i in arr:
#         if "：" in i :
#             if len(i.split("："))==2:
#                 k=i.split("：")[0].strip()
#                 v=i.split("：")[1].strip()
#                 if len(k)>15:continue
#                 if v=="":continue
#                 v=i.split("：")[1].strip()
#                 sku.update({k:v})
# # print(sku)
# print(list(sku.keys()))

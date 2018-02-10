import easyquotation
from tabulate import tabulate

sh = [204001, 204002, 204003, 204004, 204007, 204014, 204028, 204091, 204182]
sz = [131810, 131811, 131800, 131809, 131801, 131802, 131803, 131805, 131806]

keys = ["open", "close", "high", "low", "now"]

headers = ["SH"] + keys + ["SZ"] + keys

quotation = easyquotation.use('qq')

table = []
for i, j in zip(sh, sz):
    row = [str(i)]
    data = quotation.real(str(i))[str(i)]
    for k in keys:
        row.append(data[k])
    row.append(str(j))
    data = quotation.real(str(j))[str(j)]
    for k in keys:
        row.append(data[k])
    table.append(row)

print (tabulate(table, headers=headers, tablefmt="orgtbl"))
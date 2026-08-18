import re

filenames = ["NZ_AP022856.1-ATCC 21799.txt", "NZ_CM143267.1-BIM B-77.txt", "NZ_CM143270.1-BIM B-78.txt", "NZ_CP012297.1-B414.txt", "NZ_CP053188.1-BE.txt", "NZ_CP059382.1-BCA.txt", "NZ_CP068290.1-ATCC 21573.txt", "NZ_CP080542.1-CR101.txt", "NZ_CP121344.1-Cg21420.txt", "NC_003450.3-ATCC 13032.txt", "NZ_CP020033.1-TCCC11822.txt", "NZ_AP017557.1-AJ1511.txt", "NZ_CP010451.1-B253.txt", "NZ_CP012194.1-CP.txt", "NZ_CP013991.1-USDA-ARS-USMARC-56828.txt", "NZ_CP014984.1-YI.txt", "NZ_CP016335.1-ATCC 13869.txt", "NZ_CP018175.1-XV.txt", "NZ_CP022394.1-WM001.txt", "NZ_CP073911.1-CGMCC1.15647.txt", "NC_009342.1-R.txt", "NC_021351.1-SCgG1.txt", "NC_021352.1-SCgG2.txt", "NC_022040.1-MB001.txt", "NZ_CP004062.1-ZL-6.txt", "NZ_CP007722.1-ATCC 21831.txt", "NZ_CP007724.1-AR1.txt", "NZ_CP012298.1-CICC10064.txt", "NZ_CP017995.1-C1.txt", "NZ_CP022614.1-ATCC 14047.txt", "NZ_CP041729.1-JH41.txt"]

for fname in filenames:
    data = open(fname, "r").readlines()
    data = [x for x in data if "EC_number" in x]
    data = set([re.search(r'[\d.-]+', x).group() for x in data])
    ofile = open(fname + "_EC.txt", "w") 
    for x in data: ofile.write(f"{x}\n")
    ofile.close()

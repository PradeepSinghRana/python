import xlwt
a=xlwt.Workbook()
w=a.add_sheet("sheet 1")
w.write(0,0,"s. no.")
w.write(0,1,"name")
w.write(0,2,"contact no.")
w.write(0,3,"age")
w.write(0,4,"year")
w.write(0,5,"birthday")

w.write(1,0,"1")
w.write(1,1,"pooja")
w.write(1,2,"9874563210")
w.write(1,3,20)
w.write(1,4,1999)
w.write(1,5,xlwt.Formula("20+1999"))


v=a.add_sheet("sheet 2")
v.write(0,0,"s.2")
v.write(0,1,"maths")
v.write(0,2,"science")
v.write(0,3,"eng")
a.save("sdata.xls")

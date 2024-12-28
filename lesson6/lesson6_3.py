from pprint import pprint
import tools

def main():
    import openpyxl
    from openpyxl import Workbook, worksheet
    sitenames:list[str] = tools.get_sitenames('aqi.xlsx')
    print(sitenames)
    wb:Workbook = openpyxl.Workbook()
    sheet:worksheet = wb.active
    sheet.title = '站點名稱'
    for idy, name in enumerate(sitenames):
        print(idy,name)
        sheet.cell(column=1, row=idy+1,value=name)
    wb.save('Boss.xlsx')

if __name__ == '__main__':
    main()
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 

def make_receipt(data, out_file_name):
    pdf = SimpleDocTemplate("dessertshop/"+out_file_name+".pdf", pagesize = A4) 
  
    styles = getSampleStyleSheet() 
    
    title_style = styles["Heading1"] 
    
    title_style.alignment = 1
    

    title = Paragraph( "Dessert Shop" , title_style ) 
    
    style = TableStyle( 
        [ 
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "GRID" , ( 0, 0 ), ( 2 , 9 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 2, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( 2 , 9 ), colors.beige ), 
            ( "BACKGROUND" , ( 0, 7 ) , ( 2, 9 ), colors.aliceblue ),
        ] 
    ) 
    
    table = Table(data , style = style) 

    pdf.build([title, table]) 

def main():
    DATA = [ 
        ["Name", "Item Cost", "Tax"], 
        ["Candy Corn", "$0.38", "$0.03"],
        ["Gummy Bears", "$0.09", "$0.01"],
        ["Chocolate Chip", "$2.00", "$0.14"],
        ["Order Subtotals", "", "$0.58"],
    ]
    make_receipt(DATA, "receipt")

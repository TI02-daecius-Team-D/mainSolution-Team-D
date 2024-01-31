#import script from all py files
from overhead import find_highest_overhead
from cash_on_hand import cash_on_hand_insights
from profit_loss import profit_loss_insights

def main(): 
#read file from respective csv and output in summary report
    find_highest_overhead("./csv_reports/overheads-day-90.csv", "summary_report.txt") 
    cash_on_hand_insights("./csv_reports/cash-on-hand-sgd.csv", "summary_report.txt")
    profit_loss_insights("./csv_reports/profit-and-loss-sgd.csv", "summary_report.txt")
    
main()
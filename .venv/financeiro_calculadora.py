# ============================================================
#            FINANCIAL ANALYTICS - ENTERPRISE CORE
#                Cost & Profit Management System
# ============================================================

from datetime import datetime

# ------------------------------------------------------------
# COMPANY INFORMATION
# ------------------------------------------------------------

COMPANY_NAME = "Vision Enterprise"
CURRENT_DATE = datetime.now().strftime("%d/%m/%Y %H:%M")

print("=" * 65)
print(f"{COMPANY_NAME:^65}")
print("FINANCIAL COST & PROFIT MANAGEMENT".center(65))
print(f"Generated at: {CURRENT_DATE}".center(65))
print("=" * 65)

# ------------------------------------------------------------
# REVENUE
# ------------------------------------------------------------

sales = float(input("Total Sales Revenue.............: R$ "))
services = float(input("Service Revenue................: R$ "))
other_income = float(input("Other Income...................: R$ "))

# ------------------------------------------------------------
# OPERATIONAL COSTS
# ------------------------------------------------------------

salary_cost = float(input("Payroll.........................: R$ "))
marketing_cost = float(input("Marketing.......................: R$ "))
technology_cost = float(input("Technology......................: R$ "))
rent_cost = float(input("Office Rent.....................: R$ "))
tax_cost = float(input("Taxes...........................: R$ "))
other_cost = float(input("Other Expenses.................: R$ "))

# ------------------------------------------------------------
# CALCULATIONS
# ------------------------------------------------------------

total_revenue = sales + services + other_income

total_costs = (
    salary_cost +
    marketing_cost +
    technology_cost +
    rent_cost +
    tax_cost +
    other_cost
)

net_profit = total_revenue - total_costs

if total_revenue > 0:
    profit_margin = (net_profit / total_revenue) * 100
else:
    profit_margin = 0

# ------------------------------------------------------------
# COST DISTRIBUTION
# ------------------------------------------------------------

highest_cost = max(
    salary_cost,
    marketing_cost,
    technology_cost,
    rent_cost,
    tax_cost,
    other_cost
)

if highest_cost == salary_cost:
    largest_sector = "Payroll"

elif highest_cost == marketing_cost:
    largest_sector = "Marketing"

elif highest_cost == technology_cost:
    largest_sector = "Technology"

elif highest_cost == rent_cost:
    largest_sector = "Office Rent"

elif highest_cost == tax_cost:
    largest_sector = "Taxes"

else:
    largest_sector = "Other Expenses"

# ------------------------------------------------------------
# FINANCIAL STATUS
# ------------------------------------------------------------

if net_profit > 0:
    financial_status = "PROFIT"

elif net_profit == 0:
    financial_status = "BREAK EVEN"

else:
    financial_status = "LOSS"

# ------------------------------------------------------------
# REPORT
# ------------------------------------------------------------

print("\n")
print("=" * 65)
print("FINANCIAL REPORT".center(65))
print("=" * 65)

print(f"Total Revenue...............: R$ {total_revenue:,.2f}")
print(f"Total Costs.................: R$ {total_costs:,.2f}")
print(f"Net Profit..................: R$ {net_profit:,.2f}")
print(f"Profit Margin...............: {profit_margin:.2f}%")
print(f"Largest Cost Center.........: {largest_sector}")
print(f"Company Status..............: {financial_status}")

print("=" * 65)

# ------------------------------------------------------------
# PERFORMANCE ANALYSIS
# ------------------------------------------------------------

if profit_margin >= 30:
    print("Financial Performance: EXCELLENT")

elif profit_margin >= 20:
    print("Financial Performance: VERY GOOD")

elif profit_margin >= 10:
    print("Financial Performance: GOOD")

elif profit_margin >= 0:
    print("Financial Performance: ATTENTION")

else:
    print("Financial Performance: CRITICAL")

print("=" * 65)
print("END OF REPORT".center(65))
print("=" * 65)
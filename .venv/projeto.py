# ============================================
#        FREELANCE BUDGET CALCULATOR v1.0
# ============================================

client_name = input('Client name: ')
project_name = input('Project name: ')
hours = float(input('Estimated hours: '))
hour_rate = float(input('Hourly rate (R$): '))
discount = float(input('Discount (%): '))

gross_price = hours * hour_rate
discount_value = gross_price * (discount / 100)
final_price = gross_price - discount_value
deadline_days = int(hours // 4 + 2)

print('\n' + '=' * 44)
print(f'{"PROJECT SUMMARY":^44}')
print('=' * 44)
print(f'Client   : {client_name}')
print(f'Project  : {project_name}')
print(f'Hours    : {hours:.1f}h')
print(f'Rate     : R$ {hour_rate:.2f}/h')
print(f'Gross    : R$ {gross_price:.2f}')
print(f'Discount : {discount:.0f}%  (-R$ {discount_value:.2f})')
print(f'Final    : R$ {final_price:.2f}')
print(f'Delivery : {deadline_days} days')
print('=' * 44)

if final_price >= 1000:
    print('Status   : Premium proposal approved')
else:
    print('Status   : Standard proposal approved')

print('=' * 44)
print('      crafted with python // freelance mode')
print('=' * 44)
# put-credit-spread

Tracking information about put credit spread stock option trades

date_entry
symbol
date_expiration
buy_strike
sell_strike
credit
count_contracts
closed_at

# days_held = date_expiration - date_entry
# days_left = date_expiration - today
# income = count_contracts * credit * 100
# collateral = sell_strike - buy_strike * 100
# return_on_investment = income / collateral
# annualized = (return_on_investment / days_held) * 365
# profit = income - closed_at
# sum_income
# sum_collateral
# sum_profit
# win_count = profit > 0
# loss_count = profit < 0

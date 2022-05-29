TEMPLATE_SHEET_LINK = "https://docs.google.com/spreadsheets/\
d/1lO9oTJu3CudibuQCCqk-s1t3DSuRNRoty4SLY5UvG_w"

BOT_SERVICE_EMAIL = "telexpense-bot@telexpense-bot.iam.gserviceaccount.com"

BOT_WIKI = "https://github.com/pavelmakis/telexpense/wiki"

start_message = f"Hi! I'm Telexpense bot 📺\n\n\
I can work with Google Sheet.\n\
If you are a new user, read the [wiki]({BOT_WIKI}) \
or type /register to start using me"

help = f"""
I can help you send and receive data from the table. 
If this is your first time here, read this [wiki]({BOT_WIKI}).\n
I can understand theese commands:\n
*Add records*
/expense (➖Expense) - add new expense
/income (➕Income) - add new income
/transaction (💱Transaction) - add new transaction
/cancel - cancel record filling
/addexp - add expense in a single message
/addinc - add income in a single message
/addtran - add transaction in a single message\n
*Show balance*
/available - show your accounts balances\n
*Other*
/register - connect bot to Google Sheet
/donate - sponsor this project
"""

error_message = "😳 Something went wrong...\n\n \
Please try again later.\n \
If it does not work again, check your table or add it again via /register. \
Maybe you have changed the table and I can no longer work with it"

expense_help = """
Expense can be added by:
    `/addexp amount, category, [account], [description]`
where account and description are optional.

Example:
    `/addexp 3.45, taxi, Revolut, From work`
    `/addexp 9.87, Groceries, N26`
"""

wrong_expense = """
Cannot understand this expense!

Expense can be added by:
    `/addexp amount, category, [account], [description]`
where account and description are optional.

Example:
    `/addexp 3.45, taxi, Revolut, From work`
    `/addexp 9.87, Groceries, N26`
"""

income_help = """
Income can be added by:
    `/addinc amount, category, [account], [description]`
where account and description are optional.

Example:
    `/addinc 1200, Salary, N26, First job`
    `/addinc 20.20, Cashback, Revolut`
"""

wrong_income = """
Cannot understand this income!

Income can be added by:
    `/addinc amount, category, [account], [description]`
where account and description are optional.

Example:
    `/addinc 1200, Salary, N26, First job`
    `/addinc 20.20, Cashback, Revolut`
"""

tran_help = """
Transfer can be added by:
    `/addtran outcome_amount, outcome\\_account, [income\\_amount], income\\_account`
where income amount is optional\\. Add it if your transaction is multicurrency\\.

Example:
    `/addtran 1200, Revolut, N26`
    `/addtran 200, Revolut EUR, 220.3, Revolut USD`
"""

wrong_tran = """
Cannot understand this transaction\\!

Transfer can be added by:
    `/addtran outcome\\_amount, outcome\\_account, [income\\_amount], income\\_account`
where income\\_amount is optional\\. Add it if your transaction is multicurrency\\.

Example:
    `/addtran 1200, Revolut, N26`
    `/addtran 200, Revolut EUR, 220.3, Revolut USD`
"""

register_start = f"I can only work with one Google Sheets template. \
First of all, copy this sheet to your Google Account.\n\n\
👉 [Telexpense Template Sheet]({TEMPLATE_SHEET_LINK}) 👈\n\n\
Than give me the link to your sheet"

register_email = f"Make sure you have added me as an editor, \
this is my email:\n\n\
{BOT_SERVICE_EMAIL}"

donate_mes = 'The minimum amount is 3€. If you want to donate a different amount, \
tap "Pay" and enter the amount of the tip, \
which will be added to the minimum amount'

donate_description = "This is a voluntary donation to my creator."

successfull_payment = "*🙏 Thank you for supporting my creator for \
{total_amount} {currency}!* \n\n🤔 Maybe now he can come \
up with even more functionality for me"


# Registration
reg_step_1 = f"*STEP 1*\n\n\
Copy this Google Sheet template to your Google account. \
You do this to ensure that your financial data belongs only to you.\n\n \
👉 [Telexpense Template Sheet]({TEMPLATE_SHEET_LINK}) 👈"

reg_step_2 = "Add me as an editor"

reg_step_3 = "Give me the link"

reg_forget_warning = "Are you shure?"

reg_wrong_link = f"Hm. Looks like it's not a link I'm looking for...\n\n \
Read the (wiki){BOT_WIKI} and try to /register one more time!"

reg_sheet_changed = "Great! Your sheet successfully changed!"

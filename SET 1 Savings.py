{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3af03ff0-fe1a-488e-ab44-f1186262855f",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''Programming Set 1\n",
    "\n",
    "This assignment will familiarize you with Python's basics.\n",
    "'''\n",
    "\n",
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    '''Savings.\n",
    "\n",
    "    This function calculates the money remaining\n",
    "        for an employee after taxes and expenses.\n",
    "\n",
    "    To get the take-home pay of an employee, we will\n",
    "        follow the following process:\n",
    "        1. Apply the tax rate to the gross pay of the employee; round down\n",
    "        2. Subtract the expenses from the after-tax pay of the employee\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    gross_pay: int\n",
    "        the gross pay of an employee for a certain time period, expressed in centavos\n",
    "    tax_rate: float\n",
    "        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)\n",
    "    expenses: int\n",
    "        the expenses of an employee for a certain time period, expressed in centavos\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    int\n",
    "        the number of centavos remaining from an employee's pay after taxes and expenses\n",
    "    '''\n",
    "    # Replace `pass` with your code.\n",
    "    # Stay within the function. Only use the parameters as input. The function should return your answer.\n",
    "    \n",
    "\n",
    "    money = int((gross_pay*(1-tax_rate)) - (expenses))\n",
    "    return int(money)\n",
    "savings(1000,0.1,100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6106f19-4dba-48eb-9d9f-6577268f423b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3041219-c073-4478-b96a-1be9dbf0f95d",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "a8e5e3a7-ef30-4961-9678-98760547326c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How much is your pay?  100\n",
      "How much is tax?  0.1\n",
      "How much do you spend?  30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60.0\n"
     ]
    }
   ],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    \n",
    "    pay = int(input(\"How much is your pay? \"))\n",
    "    tax = float(input(\"How much is tax? \"))\n",
    "    spend = int(input(\"How much do you spend? \"))\n",
    "   \n",
    "    money = (pay*(1-tax)) - spend\n",
    "    print(money)\n",
    "  \n",
    "savings(1000,0.1,100)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "add96168-dfc4-4b13-8a58-afda89f10142",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

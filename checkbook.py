{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff5eb550-b3f9-46f2-a294-dd6ec163fa50",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import os "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7d0b7c69-6150-4c09-bad3-20a78c67705d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import subprocess"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c96c6699-ecad-41e6-afc4-ccfe55813db0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['my_first_notebook.ipynb',\n",
       " 'atm_file.txt',\n",
       " 'Untitled1.ipynb',\n",
       " 'Untitled.ipynb',\n",
       " 'function_exercises.py',\n",
       " 'profiles.json',\n",
       " '__pycache__',\n",
       " 'README.md',\n",
       " 'function_exercises.py.ipynb',\n",
       " 'untitled.txt',\n",
       " 'notes',\n",
       " '.gitignore',\n",
       " 'ATM.ipy',\n",
       " 'import_exercises.ipynb',\n",
       " '.ipynb_checkpoints',\n",
       " '.git',\n",
       " 'control_structures_exercises.py.ipynb',\n",
       " 'python_intoduction_exercises.py',\n",
       " 'data_types_and_variables.py.ipynb',\n",
       " 'notes.ipynb']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.listdir()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "84f3dd79-5b76-4a6b-9c29-c7509af36e53",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "~~~ Welcome to your terminal checkbook! ~~~\n",
      "\n",
      "What would you like to do?\n",
      "1) View current balance\n",
      "2) Record a debit (withdraw)\n",
      "3) Record a credit (deposit)\n",
      "4) Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your choice?  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your current balance is $0.00\n",
      "\n",
      "What would you like to do?\n",
      "1) View current balance\n",
      "2) Record a debit (withdraw)\n",
      "3) Record a credit (deposit)\n",
      "4) Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your choice?  3\n",
      "How much is the credit? $ 10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Credit recorded.\n",
      "\n",
      "What would you like to do?\n",
      "1) View current balance\n",
      "2) Record a debit (withdraw)\n",
      "3) Record a credit (deposit)\n",
      "4) Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your choice?  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thanks, have a great day!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "\n",
    "import subprocess\n",
    "\n",
    "\n",
    "# Define the filename for the ledger file\n",
    "ledger_file = \"atm_file.txt\"\n",
    "\n",
    "# Initialize the ledger if it doesn't exist\n",
    "if not os.path.exists(ledger_file):\n",
    "    with open(ledger_file, \"w\") as file:\n",
    "        file.write(\"0.00\")\n",
    "\n",
    "def get_balance():\n",
    "    with open(ledger_file, \"r\") as file:\n",
    "        balance = float(file.read())\n",
    "    return balance\n",
    "\n",
    "def record_debit(amount):\n",
    "    balance = get_balance()\n",
    "    with open(ledger_file, \"a\") as file:  # Use \"append\" mode (\"a\") to add to the end of the file\n",
    "        file.write(f\"Debit: ${amount:.2f}\\n\")\n",
    "    update_balance(balance - amount)\n",
    "\n",
    "def record_credit(amount):\n",
    "    balance = get_balance()\n",
    "    with open(ledger_file, \"a\") as file:  # Use \"append\" mode (\"a\") to add to the end of the file\n",
    "        file.write(f\"Credit: ${amount:.2f}\\n\")\n",
    "    update_balance(balance + amount)\n",
    "\n",
    "def update_balance(new_balance):\n",
    "    with open(ledger_file, \"w\") as file:\n",
    "        file.write(f\"{new_balance:.2f}\")\n",
    "        \n",
    "def record_debit(amount):\n",
    "    balance = get_balance()\n",
    "    with open(ledger_file, \"w\") as file:\n",
    "        file.write(str(balance - amount))\n",
    "\n",
    "def record_credit(amount):\n",
    "    balance = get_balance()\n",
    "    with open(ledger_file, \"w\") as file:\n",
    "        file.write(str(balance + amount))\n",
    "\n",
    "def main():\n",
    "    print(\"~~~ Welcome to your terminal checkbook! ~~~\")\n",
    "\n",
    "    while True:\n",
    "        print(\"\\nWhat would you like to do?\")\n",
    "        print(\"1) View current balance\")\n",
    "        print(\"2) Record a debit (withdraw)\")\n",
    "        print(\"3) Record a credit (deposit)\")\n",
    "        print(\"4) Exit\")\n",
    "\n",
    "        choice = input(\"Your choice? \")\n",
    "\n",
    "        if choice == \"1\":\n",
    "            balance = get_balance()\n",
    "            print(f\"Your current balance is ${balance:.2f}\")\n",
    "\n",
    "        elif choice == \"2\":\n",
    "            # amount = float(input(\"How much is the debit? $\"))\n",
    "            # record_debit(amount)\n",
    "            # print(\"Debit recorded.\")\n",
    "            while True:\n",
    "                try:\n",
    "                    amount = float(input(\"How much is the debit? $\"))\n",
    "                    record_debit(amount)\n",
    "                    print(\"Debit recorded.\")\n",
    "                    break\n",
    "                except ValueError:\n",
    "                    print(\"Invalid input. Please enter a valid number.\")\n",
    "\n",
    "\n",
    "        elif choice == \"3\":\n",
    "            # amount = float(input(\"How much is the credit? $\"))\n",
    "            # record_credit(amount)\n",
    "            # print(\"Credit recorded.\")\n",
    "            while True:\n",
    "                try:\n",
    "                    amount = float(input(\"How much is the credit? $\"))\n",
    "                    record_credit(amount)\n",
    "                    print(\"Credit recorded.\")\n",
    "                    break\n",
    "                except ValueError:\n",
    "                    print(\"Invalid input. Please enter a valid number.\")\n",
    "\n",
    "            \n",
    "\n",
    "        elif choice == \"4\":\n",
    "            print(\"Thanks, have a great day!\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            print(\"Invalid choice:\", choice)\n",
    "\n",
    "\n",
    "main()"
   ]
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}



#This file is for test
#Code is in arithmetic_arranger.py
#The unit tests for this project are in test_module.py

# This entrypoint file to be used in development. Start by reading README.md
from pytest import main
from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main()

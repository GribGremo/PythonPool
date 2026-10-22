import ft_package
import sys
from ft_package import count_in_list

# Print paths where the package has been searched
print("\nSEARCHED PATHS FOR FT_PACKAGE:")
print("\n".join(sys.path))

# Print the path where ft_package has been found
print("\nPATH WHERE FT_PACKAGE IS LOCATED:")
print(ft_package.__file__)

#Results
print("\nRESULTS")
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0

from ft_package import count_in_list
import ft_package
print(ft_package.__file__)

import sys
print("\n".join(sys.path))

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
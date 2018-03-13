def is_number(s):
try:
float(s)
return True
except ValueError:
pass
try:
import unicodedata
unicodedata.numeric(s)
return true
except (TypeError, ValueError):
pass
 

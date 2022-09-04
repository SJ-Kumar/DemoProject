import pandas as pd
import random
import string

path_to_excel_file = input("Enter path to source file : ")
output_file = input("Enter output file name : ")

password_object = {'country':[], 'password':[]}

def randomPassword(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

df = pd.read_excel(path_to_excel_file)

for d in df.get("country"):
    password = randomPassword()
    password_object["country"].append(d.replace(" ",""))
    password_object["password"].append(password)

result_df = pd.DataFrame(password_object)

writer = pd.ExcelWriter(output_file)
result_df.to_excel(writer, 'Sheet1', index=False)
writer.save()
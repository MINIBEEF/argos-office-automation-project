''' registration are using google form (first, notice in your chat) '''
csv = open('<CSV Path>', 'r', encoding="utf-8")
sh_file = open('<Output Path>/argos-adduser.sh', 'w')

lines = csv.readlines()
user_id = list()
script = '#!/bin/bash\n'

# parse user id
for line in lines:
    user_id.append(line.split(",")[-1].replace('"','').replace('\n', ''))

# shell script creation
for i in range(1, len(user_id)):
    script += f'sudo adduser {user_id[i]} --disabled-login\n'
    script += f'echo "{user_id[i]}:@rgos" | sudo chpasswd\n\n'

sh_file.write(script)

# print output
print('== script ==')
print(script)

print('== notice id ==')
for j in range(1, len(user_id)):
    print(user_id[j][:3] + '****')

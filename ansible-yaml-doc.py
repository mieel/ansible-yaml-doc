"""
Minimal Python script to defaults/main.yml file
to Markdown content.

Requirements:
  write MD code in yaml comments (start with '# ')
  any real yaml code is wrapped with ```yaml
  raw links are converted, line has only contain the link

Example:

This main.yaml code

  # List powershell modules ensure (includes DSC)
  # https://docs.ansible.com/ansible/latest/collections/community/windows/win_psmodule_module.html
  # > NOTE: when deploying offline modules make sure the .nupkg files are present in the files/psmodules/raw folder during the playbook
  psmodules: []
  psmodules_path: 'C:\Program Files\WindowsPowerShell\Modules'

is converted to this md code
  
  * List powershell modules ensure (includes DSC)
    [link](https://docs.ansible.com/ansible/latest/collections/community/windows/win_psmodule_module.html)
    > NOTE: when deploying offline modules make sure the .nupkg files are present in the files/psmodules/raw folder during the playbook
    ```yaml
    psmodules: []
    psmodules_path: 'C:\Program Files\WindowsPowerShell\Modules'
    ```

"""
file = 'defaults/main.yml'
content = open(file, 'r')
lines = content.readlines()

current_line_type = 'comment'
for line in lines:
    print_line = line.strip()
    if line.startswith('---'):
        continue
    last_line_type = current_line_type
    if line.startswith('# '):
        current_line_type = 'comment'
        # remove comment markers to activate md format
        print_line = f"{print_line.replace('# ', '')}"
    else:
        current_line_type = 'code'
    if line.startswith("\n"):
        current_line_type = 'break'
    # add list marker when new variable begins
    if current_line_type == 'comment' and last_line_type == 'break':
        print(f"* {print_line}  ")
        continue
    # convert http links
    if line.startswith('# http'):
        print_line = f"[link]({print_line})"
    # wrap code with ```
    if current_line_type == 'code' and last_line_type == 'comment':
        print("  ```yaml")
    if current_line_type == 'break' and last_line_type == 'code':
        print("  ```")
    print(f"  {print_line}  ")

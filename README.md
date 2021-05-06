# ansible-yaml-doc

Minimal Python script to defaults/main.yml file
to Markdown content.

## Requirements

Write Markdown code in yaml comments (start with `# `)
Any real yaml code is wrapped with ` ```yaml `
Raw links are formatted (line may only contain the http(s) link)

## Example:

This main.yaml code

```
# List of PowerShell Modules ensure
# https://docs.ansible.com/ansible/latest/collections/community/windows/win_psmodule_module.html
# > NOTE: add remarks here
psmodules: []
psmodules_path: 'C:\Program Files\WindowsPowerShell\Modules'
```

is converted to this md code

```
  * List of PowerShell Modules ensure
    [link](https://docs.ansible.com/ansible/latest/collections/community/windows/win_psmodule_module.html)
    > NOTE: add remarks here
    ```yaml
    psmodules: []
    psmodules_path: 'C:\Program Files\WindowsPowerShell\Modules'
    ```
```

which renders like this

* List of PowerShell Modules ensure
    [link](https://docs.ansible.com/ansible/latest/collections/community/windows/win_psmodule_module.html)
    > NOTE:  add remarks here
    ```yaml
    psmodules: []
    psmodules_path: 'C:\Program Files\WindowsPowerShell\Modules'
    ```


## Getting dev env setup

1. Connect to AnyConnect "sslvp.asu./edu/2fa"

2. Through MOBA or whatever ssh connection, allocate the desired node for running code.

To allocate a GPU node:

```bash

salloc  -c 4 -N 1 -G 4 -C a100

```

3. On the allocated node, run `vscode`

4. Login using the link in the browser

5. In VSCode locally, press `F1` and type: `Remote-Tunnels: Connect to Tunnel` and select "github"

You're done!
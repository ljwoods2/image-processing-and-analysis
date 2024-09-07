
## Getting dev env setup

1. Connect to AnyConnect "sslvp.asu./edu/2fa"

2. Through MOBA or whatever ssh connection, allocate the desired node for running code.

To allocate a GPU node (switches are the same switches for `salloc`):

```bash
vscode -c 4 -N 1 --gres=gpu:a100:4 -t 1-00:00:00 -p general > output.log 2>&1
bg
disown
```

3. Login using the link in the browser

4. In VSCode locally, press `F1` and type: `Remote-Tunnels: Connect to Tunnel` and select "github"

You're done!

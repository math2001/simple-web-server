set -e
echo "Killing server"
# if server is already running, kill, wait and print status (should not find the process)
[ -f ~/server.pid ] && kill $(cat ~/server.pid) && sleep 5 && ! ps -fp $(cat ~/server.pid)
echo "Starting server"
~/.local/bin/waitress-serve server:app &   # start in the background
echo $! > ~/server.pid
disown
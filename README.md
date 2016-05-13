# Run the benchmark

To run the benchmark just download this repository and then install the dependencies of each server, the following snippet shows
the bash commands needed to do so:

```
$ git clone git@github.com:pfreixes/py_echo_benchmarck.git
$ cd py_echo_benchmarck
$ mkvirtualenv --python=python3.5 py_echo_benchmark
$ pip install -r requirements.txt
```

Once the requirements have been installed we can run each server by hand, as an example :

```
$ python asyncioecho.py --uvloop
using UVLoop
serving on: ('127.0.0.1', 25000)
using sock_recv/sock_sendall
```

And then run the echo_client

```
$ ./echo_client --msize 100
568805 0.98KiB messages in 30 seconds
Latency: min 0.04ms; max 5.49ms; mean 0.152ms; std: 0.068ms (44.5%)
Latency distribution: 25% under 0.109ms; 50% under 0.14ms; 75% under 0.183ms; 90% under 0.228ms; 99% under 0.347ms; 99.99% under 1.721ms
Requests/sec: 18960.17
Transfer/sec: 18.08MiB
```

This code is mainly based on [Magic Sack benchmark](https://github.com/MagicStack/vmbench) and it is intended to get the magnitudes of the
echo server between three different stacks : [curio](https://github.com/dabeaz/curio), [gevent](https://github.com/gevent/gevent),
[asyncio+uvloop](https://github.com/MagicStack/uvloop).

The rough numbers gathered are:

| Stack           | Req/sec  |
| ----------------|:--------:|
| curio           |       25K|
| gevent          |       22K|
| asyncio+uvloop  |       20K|

# beacondecoder

![PyPI](https://img.shields.io/pypi/v/beacondecoder)

A Python library for decoding the following types of Bluetooth LE Beacons:

03 - Ruuvi RAWv1
05 - Ruuvi RAWv2
10 - Eddystone UID
11 - Eddystone URL
12 - Eddystone TLM
13 - Eddystone eTLM
14 - Eddystone EID
20 - iBeacon

The beacondecoder will parse the packet whether it be a string or the raw packet. It will then check what type of packet and return a dictionary containint the decoded information.

The application is intended to be used in: https://github.com/theBASTI0N/ble-gateway
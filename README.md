# beacondecoder

![PyPI](https://img.shields.io/pypi/v/beacondecoder)

A Python library for decoding the following types of Bluetooth LE Beacons:

Eddystone TLM
Ruuvi RAWv2
Ruuvi RAWv1

The beacondecoder will parse the packet whether it be a string or the raw packet. It will then check what type of packet and return a dictionary containint the decoded information.

It will return 4 formats of data:

Format 0
This is any beacon that was unable to be decoded.

Format 1
These are Eddystone TLM beacons.

Example:
```json
        {"f": 1, "temp": 7.15625, "advCnt": 52054, "secCnt": 216, "battery": 2.602}
```

Format 3
These are Ruuvi RAWv1 beacons.
Example:
```json
{"f": 3, "temp": 26.09, "humidity": 58.0, "pressure": 1013.53, "x": 0.046, "y": -0.001, "z": 1.05,"tAcc": 1.051008, 
"battery": 3.589,"dewPoint": 17.19235, "abHumidity": 14.19688, "airDensity": 0.003169262 }
```

Format 5
These are Ruuvi RAWv2 beaocns.
Example:
```json
{"f":5,"temp":26.15, "humidity":50.4575, "pressure":1012.84,"z":-0.072,"y":0.984,"x":-0.156,"tAcc": 1.051008,
"battery":2.911,"tx":0,"movementCounter":192,"measurementSequence":27348, "dewPoint": 17.19235, "abHumidity": 14.19688, "airDensity": 0.003169262}
```
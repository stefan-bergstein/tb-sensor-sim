# Sensor Simulator for [ThingsBoard](https://thingsboard.io/docs/faq/) 
The simulator uses http transport.

```
usage: sensor-http.py [-h] [--server SERVER] [--token TOKEN] [--interval INTERVAL] [--telemetry_key TELEMETRY_KEY] [--telemetry_min TELEMETRY_MIN] [--telemetry_max TELEMETRY_MAX] [-l LOG_LEVEL]

Sensor simulator

options:
  -h, --help            show this help message and exit
  --server SERVER       Thingsboard HTTP Endpoint [default: https://demo.thingsboard.io]
  --token TOKEN         ACCESS_TOKEN of the device
  --interval INTERVAL   Frequency of submitted data
  --telemetry_key TELEMETRY_KEY
                        telemetry key [default: temperature]
  --telemetry_min TELEMETRY_MIN
                        telemetry min value [default: 20]
  --telemetry_max TELEMETRY_MAX
                        telemetry max value [default: 30]
  -l LOG_LEVEL, --log-level LOG_LEVEL
                        Set log level to ERROR, WARNING, INFO or DEBUG
```



## Run python script
```
python sensor-http.py --server  https://tb-route-node-root-thingsboard.apps.ocp5.stormshift.coe.muc.redhat.com --token mmzvU1czMh5rrioYSSMN
```

## Build container
```
podman build . -t tb-sensor-sim:latest -f containerfileo/docs/faq/
```

## Run container locally
```
podman run -t -e SERVER=https://tb-route-node-root-thingsboard.apps.ocp5.stormshift.coe.muc.redhat.com -e TOKEN=msuDTuQEEp2ktsyAnFnl  tb-sensor-sim:latest
```

## Deploy to OCP / K8S

- Ensure you are in the right project/namespace. 
- Update SERVER and TOKEN in the config maps for your env.
- Then apply the following for sensor-1 and sensor-2.

```
cd k8s/overlays/sensor-1
oc apply -k .
```

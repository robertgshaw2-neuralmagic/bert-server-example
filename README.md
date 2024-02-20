### Install

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Launch Server

```bash
deepsparse.server --config-file server-config.yaml
```

### Make A Request

```bash
python3 client.py --sentence "I love working with DeepSparse on CPUs!"
## >> {"labels":["positive"],"scores":[0.9996703267097473]}
```
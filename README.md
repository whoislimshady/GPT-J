# gpt-J
![Python version](https://img.shields.io/badge/python-3.7-blueviolet)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/vicgalle/gpt-j-api)
![API up](https://github.com/vicgalle/gpt-j-api/actions/workflows/test.yml/badge.svg)


An Api to host gpt j model :


## Open API endpoints 🔓

These are the endpoints of the public API and require no authentication.
Click on each to see the parameters!


## Using the API 🔥

* Python:


## Deployment of the API server

Just SSH into a TPU VM. Use v2 alpha .

First, install the requirements and get the weights:
```
python3 -m pip install -r requirements.txt
Change your weights with custom weights 
```

And just run
```
python3 main.py
```

Then, you can go to http://localhost:5000/docs and use the API!

## Contact

If you have a request, I'll be happy to help you at `vermahatsn@gmail.com`



## Acknowledgements ✨

Many thanks to the support of the TPU Research Cloud, https://sites.research.google/trc/

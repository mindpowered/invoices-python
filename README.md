
invoices
========
Create, edit, and track invoices as part of your app

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)
* [Licensing](#licensing)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/invoices-python](https://github.com/mindpowered/invoices-python)
- Documentation: [https://mindpowered.github.io/invoices-python](https://mindpowered.github.io/invoices-python)

# About
An invoice lists the quantities and costs of the products or services provided by a seller to a buyer. The top of the invoice usually includes the:
- contact information of the seller
- contact information of the buyer
- date of the invoice

In the middle of the invoice is a list of products or services. A line item refers to a line from this list. The line item describes the product or service, quantity, rate, price, and taxes.

At the bottom of the invoice is a summary which usually includes:
- subtotal (before tax)
- total (with tax) amount
- payment terms.

This package aims to provide the tools to create and edit invoices. This is useful for sending by the seller or receiving by the buyer.

# Requirements
- Requires Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
- pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the invoices package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the invoices requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-invoices>0
```
Now you can use pip to install the invoices package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Usage
```python
from mindpowered_invoices import *

inv = Invoices()
inv.Create("354", "2153", "2021-02-01", "2021-03-01", "Thanks for the business!")

```


# Support
We are here to support using this package. If it doesn't do what you're looking for, isn't working, or you just need help, please [Contact us][contact].

There is also a public [Issue Tracker][bugs] available for this package.

# Licensing
This package is released under the MIT License.



[bugs]: https://github.com/mindpowered/invoices-python/issues
[contact]: https://mindpowered.dev/support/?ref=invoices-python/
[docs]: https://mindpowered.github.io/invoices-python/
[licensing]: https://mindpowered.dev/?ref=invoices-python
[purchase]: https://mindpowered.dev/purchase/

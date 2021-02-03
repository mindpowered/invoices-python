import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-invoices',
    version='0.0.5',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Create, edit, and track invoices as part of your app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['invoices'],
    packages=['mindpowered_invoices'],
    package_dir={'mindpowered_invoices': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-invoices',
    version='0.0.2',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="CPAL-1.0",
    url="https://mindpowered.dev/",
    description="Logic for creating and editing invoices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['invoices'],
    packages=['mindpowered_invoices'],
    package_dir={'mindpowered_invoices': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)

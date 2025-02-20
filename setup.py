from setuptools import setup, find_packages

setup(
    name="my_simple_library",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Ahmed Asaad",
    author_email="your_email@example.com",
    description="مكتبة بسيطة للقيام بعمليات جمع الأرقام.",
    url="https://github.com/your_username/my_simple_library",  # رابط GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

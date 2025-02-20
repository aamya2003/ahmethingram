from setuptools import setup, find_packages

setup(
    name="ahmethingra",  # اسم المكتبة
    version="0.1.1",  # رقم الإصدار
    packages=find_packages(),
    install_requires=[],  # ضع المتطلبات هنا إن وجدت
    author="Ahmed Asaad",
    author_email="ahmadasaadmajed1@gmail.com",
    description="وصف مكتبتك",
    url="https://pypi.org/project/ahmethingra/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

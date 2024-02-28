from setuptools import setup, find_packages

setup(
    name='emailspoofergui',
    version='2.5',
    packages=find_packages(),
    package_data={'emailspoofergui': ['data/config.json']},
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'emailspoofergui = emailspoofergui.emailspoofergui:send_email',
        ],
    },
    author='AKM Korishee Apurbo',
    author_email='bandinvisible8@gmail.com',
    description='A graphical email spoofing tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/IMApurbo/emailspoofergui',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

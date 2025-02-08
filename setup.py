from setuptools import setup, find_packages

setup(
    name='Persona1-text-tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Добавьте сюда зависимости, если они есть
    ],
    entry_points={
        'console_scripts': [
            'parse-event-strings=Persona1_text_tools.ibunroku_event_strings_parser:main',
            'inject-event-strings=Persona1_text_tools.ibunroku_event_strings_injecter:main',
            'bin-tool=Persona1_text_tools.ibunroku_binner2:main',
        ],
    },
)

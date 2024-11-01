from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        'test_project/test_settings/settings.json',
        'test_project/test_data/test_data.json',
        'test_project/test_data/test_data_param.json',
        '.secrets.json'
    ],
)

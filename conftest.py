import zipfile
import pytest
import os
import shutil
import paths


@pytest.fixture(scope='function', autouse=True)
def given_zip_file():
    if not os.path.exists(paths.ZIPPED_PATH):
        os.mkdir(paths.ZIPPED_PATH)
    with zipfile.ZipFile(paths.ZIPPED_PATH + '/zipped_files1.zip', 'w') as zf:
        for file in os.listdir(paths.SOURCES_PATH):
            add_file = os.path.join(paths.SOURCES_PATH, file)
            zf.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(paths.ZIPPED_PATH)
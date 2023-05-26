import os
import time
from tempfile import NamedTemporaryFile

import aioshutil
from fastapi import UploadFile


async def create_temporary_upload_file(uploaded_file: UploadFile) -> str:
    """
    Create a Named Temporary File from the Spooled UploadFile to be read from later.
    """

    with NamedTemporaryFile(
        dir=os.environ["TEMP_UPLOAD_DIR"],
        prefix=str(time.time()).replace(".", ""),
        suffix=os.path.splitext(uploaded_file.filename)[1],
        delete=False,
    ) as tmp_file:
        try:
            await aioshutil.copyfileobj(uploaded_file.file, tmp_file)
        except:
            await uploaded_file.close()
            os.unlink(tmp_file.name)
            raise FileNotFoundError
        else:
            await uploaded_file.close()
    return tmp_file.name

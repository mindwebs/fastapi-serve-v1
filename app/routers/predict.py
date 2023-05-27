import asyncio
import os

from fastapi import APIRouter, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from ..predict import ResNetImgModel
from ..utils import create_temporary_upload_file

router = APIRouter(
    prefix="/predict",
    tags=[
        "Model Predictions",
    ],
)


# Route for model predictions on single input
@router.post("/single")
async def predict_single(img: UploadFile) -> None:
    # Step 1: Create Named Temporary File
    try:
        img_filename = await create_temporary_upload_file(img)
    except Exception:
        os.unlink(img_filename)
        raise HTTPException(500)
    else:
        # Step 2: Get Model Predictions
        model = ResNetImgModel()
        out = model.predict(img_filename)

        # Step 3: Unlink all temp files
        os.unlink(img_filename)

        # Step 4: Return class/preds as json response
        return JSONResponse(
            {
                "Model Prediction": [
                    out,
                ]
            }
        )


# Route for model predictions on multiple inputs
@router.post("/multiple")
async def predict_multiple(imgs: list[UploadFile]) -> None:
    try:
        img_filenames = await asyncio.gather(
            *[create_temporary_upload_file(img) for img in imgs]
        )
    except Exception:
        # Close all files
        [os.unlink(img_filename) for img_filename in img_filenames]
        raise HTTPException(500, f"Errors in Processing Upload Files!")
    else:
        # Get model preds
        model = ResNetImgModel()
        out = [model.predict(img_filename) for img_filename in img_filenames]

        # Purge all temp upload files
        [os.unlink(img_filename) for img_filename in img_filenames]

        # Return response
        return JSONResponse({"Model Prediction": out})

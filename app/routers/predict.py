import asyncio

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


# Create multiple temporary upload files
async def multiple_temp_files(files: list[UploadFile]) -> list[str]:
    return await asyncio.gather(*[create_temporary_upload_file(file) for file in files])


# Route for model predictions on single input
@router.post("/single")
async def predict_single(img: UploadFile) -> None:
    # Step 1: Create Named Temporary File
    try:
        img_filename = await create_temporary_upload_file(img)
    except Exception as e:
        print(e)
        await img.close()
        raise HTTPException(500)
    else:
        # Step 2: Get Model Predictions
        model = ResNetImgModel()
        out = model.predict(img_filename)
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
        img_filenames = await multiple_temp_files(imgs)
        print(img_filenames)  # debug
    except Exception:
        # Close all files
        raise HTTPException(500)
    else:
        model = ResNetImgModel()
        out = [model.predict(img_filename) for img_filename in img_filenames]
        return JSONResponse({"Model Prediction": out})

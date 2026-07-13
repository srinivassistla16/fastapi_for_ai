from fastapi import APIRouter

from text_splitter_09.model.text_splitter_model import DocumentWrapper
from text_splitter_09.text_splitter_call import do_text_splitting_with_recursiveCharTextSpliiter
router = APIRouter()

@router.post("/api/textsplitter/recursivechartextsplitter")
async def text_splitting_with_recursiveCharTextSpliiter(documentWrapper: DocumentWrapper):
    return await do_text_splitting_with_recursiveCharTextSpliiter(documentWrapper)
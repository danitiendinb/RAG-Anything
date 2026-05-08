"""RAG-Anything: A multimodal RAG framework that can process and understand
anything — text, images, tables, equations, audio, video, and more.

Built on top of LightRAG for flexible, high-performance retrieval-augmented generation.

Personal fork notes:
- Forked from HKUDS/RAG-Anything for learning and experimentation
- See README for upstream project details
- Added __author_email__ and __url__ for easier reference
"""

from .raganything import RAGAnything
from .modalprocessor import ModalProcessor

__version__ = "0.1.0"
__author__ = "RAG-Anything Contributors"
__license__ = "MIT"
__url__ = "https://github.com/HKUDS/RAG-Anything"  # upstream repo for reference

__all__ = [
    "RAGAnything",
    "ModalProcessor",
    "__version__",
]

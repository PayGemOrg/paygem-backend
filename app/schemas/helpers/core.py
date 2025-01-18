from datetime import datetime
from typing import Optional

class DateTimeModelMixin:
    """Datetime model datas."""
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

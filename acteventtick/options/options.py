from pydantic import BaseModel, Field

from acteventtick.options.clock import ClockOptions
from acteventtick.options.debug import DebugOptions


class Options(BaseModel):
    clock: ClockOptions = Field(default_factory=ClockOptions)
    debug: DebugOptions = Field(default_factory=DebugOptions)

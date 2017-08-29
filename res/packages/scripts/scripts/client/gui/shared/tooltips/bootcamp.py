# 2017.08.29 21:50:02 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/tooltips/bootcamp.py
from gui.shared.formatters import text_styles
from gui.shared.tooltips.common import BlocksTooltipData
from gui.shared.tooltips import formatters
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES

class StatsTooltipData(BlocksTooltipData):

    def __init__(self, context):
        super(StatsTooltipData, self).__init__(context, None)
        self._setWidth(330)
        return

    def _packBlocks(self, label, description, icon):
        items = super(StatsTooltipData, self)._packBlocks()
        items.append(formatters.packBuildUpBlockData([formatters.packTextBlockData(text_styles.highTitle(label)), formatters.packImageBlockData(img=icon, align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER), formatters.packTextBlockData(text_styles.main(description))]))
        return items
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\tooltips\bootcamp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:50:02 Støední Evropa (letní èas)

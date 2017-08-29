# 2017.08.29 21:53:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/components/chassis_components.py
from collections import namedtuple
from items.components import shared_components
__all__ = ('Wheel', 'WheelGroup', 'TrackNode', 'TrackMaterials', 'GroundNode', 'GroundNodeGroup', 'Traces', 'LeveredSuspensionConfig', 'SuspensionLever')
Wheel = namedtuple('Wheel', ('isLeft', 'radius', 'nodeName', 'isLeading', 'leadingSyncAngle'))
WheelGroup = namedtuple('WheelGroup', ('isLeft', 'template', 'count', 'startIndex', 'radius'))
WheelsConfig = namedtuple('WheelsConfig', ('lodDist', 'groups', 'wheels'))
TrackNode = namedtuple('TrackNode', ('name', 'isLeft', 'initialOffset', 'leftNodeName', 'rightNodeName', 'damping', 'elasticity', 'forwardElasticityCoeff', 'backwardElasticityCoeff'))
TrackMaterials = namedtuple('TrackNode', ('lodDist', 'leftMaterial', 'rightMaterial', 'textureScale'))
TrackParams = namedtuple('TrackNode', ('thickness', 'maxAmplitude', 'maxOffset', 'gravity'))
GroundNode = namedtuple('GroundNode', ('name', 'isLeft', 'minOffset', 'maxOffset'))
GroundNodeGroup = namedtuple('GroundNodeGroup', ('isLeft', 'minOffset', 'maxOffset', 'template', 'count', 'startIndex'))
Traces = namedtuple('Traces', ('lodDist', 'bufferPrefs', 'textureSet', 'centerOffset', 'size'))
LeveredSuspensionConfig = namedtuple('LeveredSuspensionConfig', ('levers', 'interpolationSpeedMul', 'lodSettings'))
SuspensionLever = namedtuple('SuspensionLever', ('startNodeName', 'jointNodeName', 'trackNodeName', 'minAngle', 'maxAngle'))
SplineConfig = namedtuple('SplineConfig', ('segmentModelLeft', 'segmentModelRight', 'segmentLength', 'leftDesc', 'rightDesc', 'lodDist', 'segmentOffset', 'segment2ModelLeft', 'segment2ModelRight', 'segment2Offset', 'atlasUTiles', 'atlasVTiles'))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\components\chassis_components.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:25 St�edn� Evropa (letn� �as)

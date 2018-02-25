# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages/pacmanState.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages/pacmanState.proto',
  package='gameEngine',
  serialized_pb=_b('\n\x1amessages/pacmanState.proto\x12\ngameEngine\"\xc5\x06\n\x0bPacmanState\x12\x32\n\x06pacman\x18\x01 \x02(\x0b\x32\".gameEngine.PacmanState.AgentState\x12\x35\n\tred_ghost\x18\x02 \x02(\x0b\x32\".gameEngine.PacmanState.AgentState\x12\x36\n\npink_ghost\x18\x03 \x02(\x0b\x32\".gameEngine.PacmanState.AgentState\x12\x38\n\x0corange_ghost\x18\x04 \x02(\x0b\x32\".gameEngine.PacmanState.AgentState\x12\x36\n\nblue_ghost\x18\x05 \x02(\x0b\x32\".gameEngine.PacmanState.AgentState\x12.\n\x04mode\x18\x06 \x02(\x0e\x32 .gameEngine.PacmanState.GameMode\x12\x18\n\x10\x66rightened_timer\x18\x07 \x02(\x05\x12\r\n\x05score\x18\x08 \x02(\x05\x12\x31\n\x04grid\x18\t \x03(\x0e\x32#.gameEngine.PacmanState.GridElement\x12\x14\n\x0cgrid_columns\x18\n \x02(\x05\x12\r\n\x05lives\x18\x0b \x02(\x05\x12\x14\n\x0cupdate_ticks\x18\x0c \x02(\x05\x12\x18\n\x10ticks_per_update\x18\r \x02(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x0e \x01(\x02\x1at\n\nAgentState\x12\t\n\x01x\x18\x01 \x02(\x05\x12\t\n\x01y\x18\x02 \x02(\x05\x12\x34\n\tdirection\x18\x03 \x01(\x0e\x32!.gameEngine.PacmanState.Direction\x12\x1a\n\x12\x66rightened_counter\x18\x04 \x01(\x05\">\n\x08GameMode\x12\t\n\x05\x43HASE\x10\x00\x12\x0b\n\x07SCATTER\x10\x01\x12\x0e\n\nFRIGHTENED\x10\x02\x12\n\n\x06PAUSED\x10\x03\"@\n\x0bGridElement\x12\x08\n\x04WALL\x10\x00\x12\n\n\x06PELLET\x10\x01\x12\x10\n\x0cPOWER_PELLET\x10\x02\x12\t\n\x05\x45MPTY\x10\x03\"2\n\tDirection\x12\x06\n\x02UP\x10\x00\x12\x08\n\x04\x44OWN\x10\x01\x12\x08\n\x04LEFT\x10\x02\x12\t\n\x05RIGHT\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PACMANSTATE_GAMEMODE = _descriptor.EnumDescriptor(
  name='GameMode',
  full_name='gameEngine.PacmanState.GameMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHASE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCATTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIGHTENED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=700,
  serialized_end=762,
)
_sym_db.RegisterEnumDescriptor(_PACMANSTATE_GAMEMODE)

_PACMANSTATE_GRIDELEMENT = _descriptor.EnumDescriptor(
  name='GridElement',
  full_name='gameEngine.PacmanState.GridElement',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WALL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PELLET', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POWER_PELLET', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=764,
  serialized_end=828,
)
_sym_db.RegisterEnumDescriptor(_PACMANSTATE_GRIDELEMENT)

_PACMANSTATE_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='gameEngine.PacmanState.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=830,
  serialized_end=880,
)
_sym_db.RegisterEnumDescriptor(_PACMANSTATE_DIRECTION)


_PACMANSTATE_AGENTSTATE = _descriptor.Descriptor(
  name='AgentState',
  full_name='gameEngine.PacmanState.AgentState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='gameEngine.PacmanState.AgentState.x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='gameEngine.PacmanState.AgentState.y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direction', full_name='gameEngine.PacmanState.AgentState.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frightened_counter', full_name='gameEngine.PacmanState.AgentState.frightened_counter', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=698,
)

_PACMANSTATE = _descriptor.Descriptor(
  name='PacmanState',
  full_name='gameEngine.PacmanState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pacman', full_name='gameEngine.PacmanState.pacman', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='red_ghost', full_name='gameEngine.PacmanState.red_ghost', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pink_ghost', full_name='gameEngine.PacmanState.pink_ghost', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orange_ghost', full_name='gameEngine.PacmanState.orange_ghost', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blue_ghost', full_name='gameEngine.PacmanState.blue_ghost', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mode', full_name='gameEngine.PacmanState.mode', index=5,
      number=6, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frightened_timer', full_name='gameEngine.PacmanState.frightened_timer', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='gameEngine.PacmanState.score', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grid', full_name='gameEngine.PacmanState.grid', index=8,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grid_columns', full_name='gameEngine.PacmanState.grid_columns', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lives', full_name='gameEngine.PacmanState.lives', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_ticks', full_name='gameEngine.PacmanState.update_ticks', index=11,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticks_per_update', full_name='gameEngine.PacmanState.ticks_per_update', index=12,
      number=13, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elapsed_time', full_name='gameEngine.PacmanState.elapsed_time', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PACMANSTATE_AGENTSTATE, ],
  enum_types=[
    _PACMANSTATE_GAMEMODE,
    _PACMANSTATE_GRIDELEMENT,
    _PACMANSTATE_DIRECTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=880,
)

_PACMANSTATE_AGENTSTATE.fields_by_name['direction'].enum_type = _PACMANSTATE_DIRECTION
_PACMANSTATE_AGENTSTATE.containing_type = _PACMANSTATE
_PACMANSTATE.fields_by_name['pacman'].message_type = _PACMANSTATE_AGENTSTATE
_PACMANSTATE.fields_by_name['red_ghost'].message_type = _PACMANSTATE_AGENTSTATE
_PACMANSTATE.fields_by_name['pink_ghost'].message_type = _PACMANSTATE_AGENTSTATE
_PACMANSTATE.fields_by_name['orange_ghost'].message_type = _PACMANSTATE_AGENTSTATE
_PACMANSTATE.fields_by_name['blue_ghost'].message_type = _PACMANSTATE_AGENTSTATE
_PACMANSTATE.fields_by_name['mode'].enum_type = _PACMANSTATE_GAMEMODE
_PACMANSTATE.fields_by_name['grid'].enum_type = _PACMANSTATE_GRIDELEMENT
_PACMANSTATE_GAMEMODE.containing_type = _PACMANSTATE
_PACMANSTATE_GRIDELEMENT.containing_type = _PACMANSTATE
_PACMANSTATE_DIRECTION.containing_type = _PACMANSTATE
DESCRIPTOR.message_types_by_name['PacmanState'] = _PACMANSTATE

PacmanState = _reflection.GeneratedProtocolMessageType('PacmanState', (_message.Message,), dict(

  AgentState = _reflection.GeneratedProtocolMessageType('AgentState', (_message.Message,), dict(
    DESCRIPTOR = _PACMANSTATE_AGENTSTATE,
    __module__ = 'messages.pacmanState_pb2'
    # @@protoc_insertion_point(class_scope:gameEngine.PacmanState.AgentState)
    ))
  ,
  DESCRIPTOR = _PACMANSTATE,
  __module__ = 'messages.pacmanState_pb2'
  # @@protoc_insertion_point(class_scope:gameEngine.PacmanState)
  ))
_sym_db.RegisterMessage(PacmanState)
_sym_db.RegisterMessage(PacmanState.AgentState)


# @@protoc_insertion_point(module_scope)

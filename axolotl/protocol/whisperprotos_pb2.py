# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WhisperTextProtocol.proto

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
  name='WhisperTextProtocol.proto',
  package='textsecure',
  serialized_pb=_b('\n\x19WhisperTextProtocol.proto\x12\ntextsecure\"b\n\x0eWhisperMessage\x12\x12\n\nratchetKey\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\r\x12\x17\n\x0fpreviousCounter\x18\x03 \x01(\r\x12\x12\n\nciphertext\x18\x04 \x01(\x0c\"\x8f\x01\n\x14PreKeyWhisperMessage\x12\x16\n\x0eregistrationId\x18\x05 \x01(\r\x12\x10\n\x08preKeyId\x18\x01 \x01(\r\x12\x16\n\x0esignedPreKeyId\x18\x06 \x01(\r\x12\x0f\n\x07\x62\x61seKey\x18\x02 \x01(\x0c\x12\x13\n\x0bidentityKey\x18\x03 \x01(\x0c\x12\x0f\n\x07message\x18\x04 \x01(\x0c\"t\n\x12KeyExchangeMessage\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07\x62\x61seKey\x18\x02 \x01(\x0c\x12\x12\n\nratchetKey\x18\x03 \x01(\x0c\x12\x13\n\x0bidentityKey\x18\x04 \x01(\x0c\x12\x18\n\x10\x62\x61seKeySignature\x18\x05 \x01(\x0c\"E\n\x10SenderKeyMessage\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\titeration\x18\x02 \x01(\r\x12\x12\n\nciphertext\x18\x03 \x01(\x0c\"c\n\x1cSenderKeyDistributionMessage\x12\n\n\x02id\x18\x01 \x01(\r\x12\x11\n\titeration\x18\x02 \x01(\r\x12\x10\n\x08\x63hainKey\x18\x03 \x01(\x0c\x12\x12\n\nsigningKey\x18\x04 \x01(\x0c\x42\x37\n&org.whispersystems.libaxolotl.protocolB\rWhisperProtos')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WHISPERMESSAGE = _descriptor.Descriptor(
  name='WhisperMessage',
  full_name='textsecure.WhisperMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ratchetKey', full_name='textsecure.WhisperMessage.ratchetKey', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='counter', full_name='textsecure.WhisperMessage.counter', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previousCounter', full_name='textsecure.WhisperMessage.previousCounter', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='textsecure.WhisperMessage.ciphertext', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=41,
  serialized_end=139,
)


_PREKEYWHISPERMESSAGE = _descriptor.Descriptor(
  name='PreKeyWhisperMessage',
  full_name='textsecure.PreKeyWhisperMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registrationId', full_name='textsecure.PreKeyWhisperMessage.registrationId', index=0,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preKeyId', full_name='textsecure.PreKeyWhisperMessage.preKeyId', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signedPreKeyId', full_name='textsecure.PreKeyWhisperMessage.signedPreKeyId', index=2,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseKey', full_name='textsecure.PreKeyWhisperMessage.baseKey', index=3,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identityKey', full_name='textsecure.PreKeyWhisperMessage.identityKey', index=4,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='textsecure.PreKeyWhisperMessage.message', index=5,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=142,
  serialized_end=285,
)


_KEYEXCHANGEMESSAGE = _descriptor.Descriptor(
  name='KeyExchangeMessage',
  full_name='textsecure.KeyExchangeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='textsecure.KeyExchangeMessage.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseKey', full_name='textsecure.KeyExchangeMessage.baseKey', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ratchetKey', full_name='textsecure.KeyExchangeMessage.ratchetKey', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identityKey', full_name='textsecure.KeyExchangeMessage.identityKey', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baseKeySignature', full_name='textsecure.KeyExchangeMessage.baseKeySignature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=287,
  serialized_end=403,
)


_SENDERKEYMESSAGE = _descriptor.Descriptor(
  name='SenderKeyMessage',
  full_name='textsecure.SenderKeyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='textsecure.SenderKeyMessage.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration', full_name='textsecure.SenderKeyMessage.iteration', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='textsecure.SenderKeyMessage.ciphertext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=405,
  serialized_end=474,
)


_SENDERKEYDISTRIBUTIONMESSAGE = _descriptor.Descriptor(
  name='SenderKeyDistributionMessage',
  full_name='textsecure.SenderKeyDistributionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='textsecure.SenderKeyDistributionMessage.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration', full_name='textsecure.SenderKeyDistributionMessage.iteration', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chainKey', full_name='textsecure.SenderKeyDistributionMessage.chainKey', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signingKey', full_name='textsecure.SenderKeyDistributionMessage.signingKey', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=476,
  serialized_end=575,
)

DESCRIPTOR.message_types_by_name['WhisperMessage'] = _WHISPERMESSAGE
DESCRIPTOR.message_types_by_name['PreKeyWhisperMessage'] = _PREKEYWHISPERMESSAGE
DESCRIPTOR.message_types_by_name['KeyExchangeMessage'] = _KEYEXCHANGEMESSAGE
DESCRIPTOR.message_types_by_name['SenderKeyMessage'] = _SENDERKEYMESSAGE
DESCRIPTOR.message_types_by_name['SenderKeyDistributionMessage'] = _SENDERKEYDISTRIBUTIONMESSAGE

WhisperMessage = _reflection.GeneratedProtocolMessageType('WhisperMessage', (_message.Message,), dict(
  DESCRIPTOR = _WHISPERMESSAGE,
  __module__ = 'WhisperTextProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.WhisperMessage)
  ))
_sym_db.RegisterMessage(WhisperMessage)

PreKeyWhisperMessage = _reflection.GeneratedProtocolMessageType('PreKeyWhisperMessage', (_message.Message,), dict(
  DESCRIPTOR = _PREKEYWHISPERMESSAGE,
  __module__ = 'WhisperTextProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.PreKeyWhisperMessage)
  ))
_sym_db.RegisterMessage(PreKeyWhisperMessage)

KeyExchangeMessage = _reflection.GeneratedProtocolMessageType('KeyExchangeMessage', (_message.Message,), dict(
  DESCRIPTOR = _KEYEXCHANGEMESSAGE,
  __module__ = 'WhisperTextProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.KeyExchangeMessage)
  ))
_sym_db.RegisterMessage(KeyExchangeMessage)

SenderKeyMessage = _reflection.GeneratedProtocolMessageType('SenderKeyMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENDERKEYMESSAGE,
  __module__ = 'WhisperTextProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.SenderKeyMessage)
  ))
_sym_db.RegisterMessage(SenderKeyMessage)

SenderKeyDistributionMessage = _reflection.GeneratedProtocolMessageType('SenderKeyDistributionMessage', (_message.Message,), dict(
  DESCRIPTOR = _SENDERKEYDISTRIBUTIONMESSAGE,
  __module__ = 'WhisperTextProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.SenderKeyDistributionMessage)
  ))
_sym_db.RegisterMessage(SenderKeyDistributionMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n&org.whispersystems.libaxolotl.protocolB\rWhisperProtos'))
# @@protoc_insertion_point(module_scope)
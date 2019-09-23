# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkRegistryOperationResult(Model):
    """Encapsulates the result of a bulk registry operation.

    :param is_successful: Whether or not the operation was successful.
    :type is_successful: bool
    :param errors: If the operation was not successful, this contains an array
     of DeviceRegistryOperationError objects.
    :type errors: list[~protocol.models.DeviceRegistryOperationError]
    :param warnings: If the operation was partially successful, this contains
     an array of DeviceRegistryOperationWarning objects.
    :type warnings: list[~protocol.models.DeviceRegistryOperationWarning]
    """

    _attribute_map = {
        "is_successful": {"key": "isSuccessful", "type": "bool"},
        "errors": {"key": "errors", "type": "[DeviceRegistryOperationError]"},
        "warnings": {"key": "warnings", "type": "[DeviceRegistryOperationWarning]"},
    }

    def __init__(self, **kwargs):
        super(BulkRegistryOperationResult, self).__init__(**kwargs)
        self.is_successful = kwargs.get("is_successful", None)
        self.errors = kwargs.get("errors", None)
        self.warnings = kwargs.get("warnings", None)
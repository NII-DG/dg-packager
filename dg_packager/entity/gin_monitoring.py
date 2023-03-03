from typing import Any
from nii_dg.schema.ginfork import GinMonitoring
from dg_packager.utils.enum.gin_monitoring_types import DatasetStructureType, ContentSizeType, WorkflowIdentifierType
from nii_dg.ro_crate import RootDataEntity

from dg_packager.utils.enum.property_type import PropertyType


class GinMonitoringEntity:
    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_gifork(self,
                        id: int,
                        common_props: dict[str, Any]
                        ) -> GinMonitoring:
        '''
        Sumary
        ----------------
        ginforkのGinMonitoringEntityインスタンスの生成メソッド

        Note
        ----------------
        [param] id は 1 以上で設定してください。

        '''
        return GinMonitoring(props=common_props)

    def creata_common_props(self,
                            about: RootDataEntity,
                            contentSize: ContentSizeType,
                            workflowIdentifier: WorkflowIdentifierType,
                            datasetStructure: DatasetStructureType
                            ) -> dict[str, Any]:
        '''
        GinMonitoringEntityの共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        about_id = about.data.get(PropertyType.ID.value)
        if about_id:
            props["about"] = about

        props["contentSize"] = contentSize.value

        props["workflowIdentifier"] = workflowIdentifier.value

        props["datasetStructure"] = datasetStructure.value

        return props
